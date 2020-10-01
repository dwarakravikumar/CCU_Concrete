import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FormatStrFormatter
import CCU_Concrete_Constants
import CCU_Concrete_Functions
from CCU_Concrete_Functions import f_get_input_array

excel_file = CCU_Concrete_Constants.excel_file
df = pd.read_excel(excel_file, sheet_name=CCU_Concrete_Constants.sheet_name)
plot_rows=CCU_Concrete_Constants.plot_rows
plot_columns=CCU_Concrete_Constants.plot_columns
number_of_studies=CCU_Concrete_Constants.number_of_studies
number_of_samples=CCU_Concrete_Constants.number_of_samples
number_of_parameters=CCU_Concrete_Constants.number_of_parameters
Allocation_Type = CCU_Concrete_Constants.Allocation_Type



if(Allocation_Type == CCU_Concrete_Constants.System_Boundary_Expansion):
    output_file_name = CCU_Concrete_Constants.output_file_name_scatterplot_SE

if(Allocation_Type == CCU_Concrete_Constants.Economic_Allocation):
    output_file_name = CCU_Concrete_Constants.output_file_name_scatterplot_EA

if(Allocation_Type == CCU_Concrete_Constants.Mass_Allocation): 
    output_file_name = CCU_Concrete_Constants.output_file_name_scatterplot_MA

fig, ax = plt.subplots(plot_rows, plot_columns, sharex=True, sharey=True,figsize=(CCU_Concrete_Constants.figsize_width_scatterplot, CCU_Concrete_Constants.figsize_height_scatterplot))

fig.add_subplot(111, frameon=False)

plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)

for a in range(plot_rows):
    for b in range(plot_columns):
        ax[a,b].spines['top'].set_visible(False)
        ax[a,b].spines['right'].set_visible(False)
        ax[a,b].spines['bottom'].set_visible(False)
        ax[a,b].spines['left'].set_visible(False)

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


for i in range((number_of_studies)):
    
    print('i             :',i)
  
    Delta_process_emissions_array_array,Baseline_process_emissions_array_array, CCU_process_emissions_array_array = f_get_input_array(i)
    
    CCU_CO2_Total=np.sum(CCU_process_emissions_array_array,axis=1)
    Baseline_CO2_Total=np.sum(Baseline_process_emissions_array_array,axis=1)
    
    
    
    CCU_betters_Baseline = 0
    
    Y=Baseline_CO2_Total-CCU_CO2_Total

    for p,q in zip(CCU_CO2_Total,Baseline_CO2_Total):
        
        if (p<q):
            CCU_betters_Baseline = CCU_betters_Baseline+1
            
    ax1 = fig.add_subplot(plot_rows, plot_columns,i+1)
    
    cement_CO2_difference_array=Baseline_process_emissions_array_array[:,0]-CCU_process_emissions_array_array[:,0]
    coarse_agg_CO2_difference_array=Baseline_process_emissions_array_array[:,1]-CCU_process_emissions_array_array[:,1]
    fine_agg_CO2_difference_array=Baseline_process_emissions_array_array[:,2]-CCU_process_emissions_array_array[:,2]
    water_CO2_difference_array=Baseline_process_emissions_array_array[:,3]-CCU_process_emissions_array_array[:,3]
    SCM_CO2_difference_array=Baseline_process_emissions_array_array[:,4]-CCU_process_emissions_array_array[:,4]
    Material_Transportation_difference_array=Baseline_process_emissions_array_array[:,5]-CCU_process_emissions_array_array[:,5]
    CO2_capture_MEA_CO2_difference_array=Baseline_process_emissions_array_array[:,6]-CCU_process_emissions_array_array[:,6]
    Power_Plant_difference_array=Baseline_process_emissions_array_array[:,7]-CCU_process_emissions_array_array[:,7]
    CO2_Transportation_difference_array_array=Baseline_process_emissions_array_array[:,8]-CCU_process_emissions_array_array[:,8]
    CO2_Vaporization_Electricity_difference_array=Baseline_process_emissions_array_array[:,9]-CCU_process_emissions_array_array[:,9]
    CO2_Injection_Electricity_difference_array=Baseline_process_emissions_array_array[:,10]-CCU_process_emissions_array_array[:,10]
    CO2_Curing_difference_array=Baseline_process_emissions_array_array[:,11]-CCU_process_emissions_array_array[:,11]
    Steam_Curing_difference_array=Baseline_process_emissions_array_array[:,12]-CCU_process_emissions_array_array[:,12]


#        
#    l1=ax1.scatter(cement_CO2_difference_array, Y,color=color_array[0], s=2)
#    ax1.scatter(coarse_agg_CO2_difference_array, Y,color=color_array[1], s=2)
#    ax1.scatter(fine_agg_CO2_difference_array, Y,color=color_array[2], s=2)
#    ax1.scatter(water_CO2_difference_array, Y,color=color_array[3], s=2)
#    ax1.scatter(SCM_CO2_difference_array, Y,color=color_array[4], s=2)
#    ax1.scatter(Material_Transportation_difference_array, Y,color=color_array[5], s=2)
#    ax1.scatter(CO2_capture_MEA_CO2_difference_array, Y,color=color_array[6], s=2)
#    ax1.scatter(Power_Plant_difference_array,Y,color=color_array[7], s=2)
#    ax1.scatter(CO2_Transportation_difference_array_array, Y,color=color_array[8], s=2)
#    ax1.scatter(CO2_Vaporization_Electricity_difference_array, Y,color=color_array[9], s=2)
#    ax1.scatter(CO2_Injection_Electricity_difference_array, Y,color=color_array[10], s=2)
#    ax1.scatter(CO2_Curing_difference_array, Y,color=color_array[11], s=2)
#    ax1.scatter(Steam_Curing_difference_array, Y,color=color_array[12], s=2)
    
    l1=ax1.scatter(Delta_process_emissions_array_array[:,0], Y,color=color_array[0], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,1], Y,color=color_array[1], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,2], Y,color=color_array[2], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,3], Y,color=color_array[3], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,4], Y,color=color_array[4], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,5], Y,color=color_array[5], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,6], Y,color=color_array[6], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,7],Y,color=color_array[7], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,8], Y,color=color_array[8], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,9], Y,color=color_array[9], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,10], Y,color=color_array[10], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,11], Y,color=color_array[11], s=2)
    ax1.scatter(Delta_process_emissions_array_array[:,12], Y,color=color_array[12], s=2)
            
    if ((CCU_betters_Baseline/number_of_samples)<CCU_Concrete_Constants.Probability_Preference):
        spine_color='red'

        flag=flag+1

    else:
        spine_color='green'
        
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
    plt.axhline(linewidth=CCU_Concrete_Constants.hline_width_scatterplot, label='_nolegend_', color=spine_color)
    plt.axvline(linewidth=CCU_Concrete_Constants.vline_width_scatterplot, label='_nolegend_', color=spine_color)

   
    xticks=ax1.get_xticks()
    yticks=ax1.get_yticks()
    
    
    if(abs(min(xticks))>abs(max(xticks))):
        x_axis_upper_limit=-min(xticks)
        x_axis_lower_limit=min(xticks)
        
    if(abs(min(xticks))<abs(max(xticks)) or abs(min(xticks))==abs(max(xticks))):
        x_axis_upper_limit=max(xticks)
        x_axis_lower_limit=-max(xticks)
        
    if(abs(min(yticks))>abs(max(yticks))):
        y_axis_upper_limit=-min(yticks)
        y_axis_lower_limit=min(yticks)
        
    if(abs(min(yticks))<abs(max(yticks))or abs(min(yticks))==abs(max(yticks))):
        y_axis_upper_limit=max(yticks)
        y_axis_lower_limit=-max(yticks)

    
    text_font = {'family': CCU_Concrete_Constants.font_family,
        'color':  spine_color,
        'weight': CCU_Concrete_Constants.font_weight,
        'size': CCU_Concrete_Constants.xaxis_tick_fontsize,
        }
    
    ax1.text(x_axis_lower_limit,y_axis_lower_limit,"("+str(i+1)+")",fontdict=text_font, verticalalignment='bottom')
    
    if((i+1<=71) or (i+1>=77)):
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
        ax1.yaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
    if((i+1>=72) and (i+1<=76)):
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%0.2f'))
        ax1.yaxis.set_major_formatter(FormatStrFormatter('%0.2f'))
    

    ax1.tick_params(axis='x', which='major', pad=CCU_Concrete_Constants.xaxis_tick_padding_scatterplot)
    ax1.tick_params(axis='y', which='major', pad=CCU_Concrete_Constants.yaxis_tick_padding_scatterplot)
    plt.tick_params(labelcolor=spine_color, top=False, bottom=False, left=False, right=False)
    plt.xticks(np.arange(x_axis_lower_limit, x_axis_upper_limit+.01, abs(x_axis_upper_limit))) 
    plt.yticks(np.arange(y_axis_lower_limit, y_axis_upper_limit+.01, abs(y_axis_upper_limit))) 
  
    for label in ax1.get_xticklabels():
        label.set_fontproperties(ticks_font)
    
    for label in ax1.get_yticklabels():
        label.set_fontproperties(ticks_font)
      
     
    fig.tight_layout(pad=CCU_Concrete_Constants.Tightlayout_Pad_scatterplot)

     
plt.savefig(output_file_name, format=CCU_Concrete_Constants.output_file_format)

  



        

