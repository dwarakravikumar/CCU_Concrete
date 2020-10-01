import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FormatStrFormatter
import CCU_Concrete_Constants
import CCU_Concrete_Functions
from CCU_Concrete_Functions import f_get_input_array
from scipy.stats.kde import gaussian_kde
from datetime import datetime



excel_file = CCU_Concrete_Constants.excel_file
df = pd.read_excel(excel_file, sheet_name=CCU_Concrete_Constants.sheet_name)
plot_rows=CCU_Concrete_Constants.plot_rows
plot_columns=CCU_Concrete_Constants.plot_columns
number_of_studies=CCU_Concrete_Constants.number_of_studies
number_of_samples=CCU_Concrete_Constants.number_of_samples
number_of_parameters=CCU_Concrete_Constants.number_of_parameters
Allocation_Type = CCU_Concrete_Constants.Allocation_Type

if(Allocation_Type == CCU_Concrete_Constants.System_Boundary_Expansion):
    output_file_name = CCU_Concrete_Constants.output_file_name_deltaplot_SE

if(Allocation_Type == CCU_Concrete_Constants.Economic_Allocation):
    output_file_name = CCU_Concrete_Constants.output_file_name_deltaplot_EA

if(Allocation_Type == CCU_Concrete_Constants.Mass_Allocation): 
    output_file_name = CCU_Concrete_Constants.output_file_name_deltaplot_MA


ticks_font = font_manager.FontProperties(family=CCU_Concrete_Constants.font_family, \
                                         style=CCU_Concrete_Constants.font_style,\
                                         size=CCU_Concrete_Constants.xaxis_tick_fontsize,\
                                         weight=CCU_Concrete_Constants.font_weight)

fig, ax = plt.subplots(plot_rows, plot_columns, sharex=True, sharey=True,\
                       figsize=(CCU_Concrete_Constants.figsize_width_deltaplot,\
                                CCU_Concrete_Constants.figsize_height_deltaplot), edgecolor=None)

fig.add_subplot(111, frameon=False)

plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)

for a in range(plot_rows):
    for b in range(plot_columns):
        ax[a,b].spines['top'].set_visible(False)
        ax[a,b].spines['right'].set_visible(False)
        ax[a,b].spines['bottom'].set_visible(False)
        ax[a,b].spines['left'].set_visible(False)

ax[0,0].set_xticklabels([])
ax[0,0].set_xticks([])
ax[0,0].set_yticks([])


ticks_font = font_manager.FontProperties(family=CCU_Concrete_Constants.font_family, \
                                         style=CCU_Concrete_Constants.font_style,\
                                         size=CCU_Concrete_Constants.xaxis_tick_fontsize,\
                                         weight=CCU_Concrete_Constants.font_weight)

par_array=[CCU_Concrete_Constants.parameter1,\
           CCU_Concrete_Constants.parameter2,\
           CCU_Concrete_Constants.parameter3,\
           CCU_Concrete_Constants.parameter4,\
           CCU_Concrete_Constants.parameter5,\
           CCU_Concrete_Constants.parameter6, \
           CCU_Concrete_Constants.parameter7,\
           CCU_Concrete_Constants.parameter8,\
           CCU_Concrete_Constants.parameter9,\
           CCU_Concrete_Constants.parameter10,\
           CCU_Concrete_Constants.parameter11,\
           CCU_Concrete_Constants.parameter12,\
           CCU_Concrete_Constants.parameter13]

color_array=[CCU_Concrete_Constants.parameter1_color,\
           CCU_Concrete_Constants.parameter2_color,\
           CCU_Concrete_Constants.parameter3_color,\
           CCU_Concrete_Constants.parameter4_color,\
           CCU_Concrete_Constants.parameter5_color,\
           CCU_Concrete_Constants.parameter6_color, \
           CCU_Concrete_Constants.parameter7_color,\
           CCU_Concrete_Constants.parameter8_color,\
           CCU_Concrete_Constants.parameter9_color,\
           CCU_Concrete_Constants.parameter10_color,\
           CCU_Concrete_Constants.parameter11_color,\
           CCU_Concrete_Constants.parameter12_color,\
           CCU_Concrete_Constants.parameter13_color]

flag=0

for i in range(number_of_studies):
    
    print('i             :',i)
    
    Delta_process_emissions_array_array_A,Baseline_process_emissions_array_array, CCU_process_emissions_array_array = f_get_input_array(i)
    Delta_process_emissions_array_array_B, Baseline_process_emissions_array_array_B, CCU_process_emissions_array_array_B = f_get_input_array(i)

    rows,columns=np.shape(Delta_process_emissions_array_array_A)
    Y_A=np.zeros((columns,rows))
    Y_B=np.zeros((columns,rows))
    Y_C=np.zeros((1,rows))
    s_array=np.zeros((columns,rows))
    delta_array=np.zeros((1))

    Y_A=np.sum(Delta_process_emissions_array_array_A,axis=1)
    

    Y_B=np.sum(Delta_process_emissions_array_array_B,axis=1)
    gkde_Y_B = gaussian_kde(Y_B)
    

    
    for c in range(columns):
        
        now = datetime.now()
        print(now.strftime("%H:%M:%S"))
        
        
        for r in range(rows):
            
            Delta_process_emissions_array_array_C = Delta_process_emissions_array_array_B.copy()
            
            Delta_process_emissions_array_array_C[:,c]=Delta_process_emissions_array_array_A[r,c]
            

            Y_C[0]=np.sum(Delta_process_emissions_array_array_C,axis=1)
            

            
            gkde_Y_C = gaussian_kde(Y_C[0])  
#                
            xx=0
            
            for c1 in range(rows):
                
                if(gkde_Y_C.evaluate(Y_C[0][c1])!=0):

                   xx=xx+abs((gkde_Y_B.evaluate(Y_C[0][c1])/gkde_Y_C.evaluate(Y_C[0][c1]))-1)
                 
                    

                s_array[c][c1]=xx/rows
  
    delta_array=np.sum(s_array,axis=1)/(2*rows)
  
    delta_array = delta_array/np.sum(delta_array)
    
   
    CCU_total_lower_than_Baseline = 0
    
  
    Baseline_CO2_Total=np.sum(Baseline_process_emissions_array_array,axis=1)
    CCU_CO2_Total=np.sum(CCU_process_emissions_array_array,axis=1)
    

    for p,q in zip(CCU_CO2_Total,Baseline_CO2_Total):
        
        if (p<q):
            CCU_total_lower_than_Baseline = CCU_total_lower_than_Baseline+1
    
 
    y_pos = np.arange(len(par_array))
 
    ax1 = fig.add_subplot(plot_rows, plot_columns,i+1)

    
    for j in range(number_of_parameters):
        
        CCU_process_higher_than_Baseline=0

        for p,q in zip(CCU_process_emissions_array_array[:,j],Baseline_process_emissions_array_array[:,j]):
            
            if (p>=q):
                CCU_process_higher_than_Baseline = CCU_process_higher_than_Baseline+1   
              
        if((CCU_process_higher_than_Baseline/number_of_samples)>CCU_Concrete_Constants.Probability_Preference):
            delta_array[j]=-delta_array[j]

           
        l1=ax1.barh(y_pos[j], delta_array[j], height=.6,color=color_array[j],label=par_array[j])
        
    if ((CCU_total_lower_than_Baseline/number_of_samples)<CCU_Concrete_Constants.Probability_Preference):
        spine_color='red'

        flag=flag+1

    else:
        spine_color='green'
        
    ax1.invert_yaxis() 
    
    text_font = {'family': CCU_Concrete_Constants.font_family,
        'color':  spine_color,
        'weight': CCU_Concrete_Constants.font_weight,
        'size': CCU_Concrete_Constants.xaxis_tick_fontsize,
        }
   
    ax1.text(-1,number_of_parameters,"("+str(i+1)+")",fontdict=text_font, color=spine_color, verticalalignment='bottom')
        

    if(i+1<=CCU_Concrete_Constants.Number_of_Category1_Studies):
        linewidth=CCU_Concrete_Constants.Category1_Plot_Linewidth
        linestyle_array=CCU_Concrete_Constants.Category1_Plot_Linestyle
        
    if(i+1>CCU_Concrete_Constants.Number_of_Category1_Studies and \
       i+1<=CCU_Concrete_Constants.Number_of_Category1_Studies\
       +CCU_Concrete_Constants.Number_of_Category2_Studies):
        linewidth=CCU_Concrete_Constants.Category2_Plot_Linewidth
        linestyle_array=CCU_Concrete_Constants.Category2_Plot_Linestyle
        
    if(i+1>CCU_Concrete_Constants.Number_of_Category1_Studies\
       +CCU_Concrete_Constants.Number_of_Category2_Studies\
       and i<=CCU_Concrete_Constants.Number_of_Category1_Studies\
       +CCU_Concrete_Constants.Number_of_Category2_Studies\
       +CCU_Concrete_Constants.Number_of_Category3_Studies):
        linewidth=CCU_Concrete_Constants.Category3_Plot_Linewidth
        linestyle_array=CCU_Concrete_Constants.Category3_Plot_Linestyle
        
    if(i+1>CCU_Concrete_Constants.Number_of_Category1_Studies\
       +CCU_Concrete_Constants.Number_of_Category2_Studies\
       +CCU_Concrete_Constants.Number_of_Category3_Studies):
        linewidth=CCU_Concrete_Constants.Category4_Plot_Linewidth
        linestyle_array=CCU_Concrete_Constants.Category4_Plot_Linestyle
        
    
    ax1.spines['left'].set_linewidth(linewidth)
    ax1.spines['right'].set_linewidth(linewidth)
    ax1.spines['top'].set_linewidth(linewidth)
    ax1.spines['bottom'].set_linewidth(linewidth)        

    ax1.spines['left'].set_color(spine_color)
    ax1.spines['right'].set_color(spine_color)
    ax1.spines['top'].set_color(spine_color)
    ax1.spines['bottom'].set_color(spine_color)
    
    ax1.spines['left'].set_linestyle(linestyle_array)
    ax1.spines['right'].set_linestyle(linestyle_array)
    ax1.spines['top'].set_linestyle(linestyle_array)
    ax1.spines['bottom'].set_linestyle(linestyle_array)
    
    ax1.set_facecolor(spine_color)
    ax1.patch.set_alpha(CCU_Concrete_Constants.Plot_Transperency)
    
    plt.axvline(linewidth=CCU_Concrete_Constants.vline_width_deltarplot, label='_nolegend_', color='black')

   
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xticks(np.arange(-1,1.1,1)) 
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
    ax1.tick_params(axis='x', which='major', pad=CCU_Concrete_Constants.xaxis_tick_padding_deltaplot)
    plt.tick_params(labelcolor=spine_color, top=False, bottom=False, left=False, right=False)
    plt.yticks([]) 
    
    for label in ax1.get_xticklabels():
        label.set_fontproperties(ticks_font)
    
    fig.tight_layout(pad=CCU_Concrete_Constants.Tightlayout_Pad_deltaplot)

print('CCU has higher CO2 impact than Conventional concrete (red)      :', flag)

plt.savefig(output_file_name, format=CCU_Concrete_Constants.output_file_format, \
            dpi=CCU_Concrete_Constants.dpi_figure)

  



        

