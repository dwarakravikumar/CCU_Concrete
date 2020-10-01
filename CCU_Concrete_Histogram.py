import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    output_file_name = CCU_Concrete_Constants.output_file_name_histogram_SE

if(Allocation_Type == CCU_Concrete_Constants.Economic_Allocation):
    output_file_name = CCU_Concrete_Constants.output_file_name_histogram_EA

if(Allocation_Type == CCU_Concrete_Constants.Mass_Allocation): 
    output_file_name = CCU_Concrete_Constants.output_file_name_histogram_MA
    
fig, ax = plt.subplots(plot_rows, plot_columns, sharex=True, sharey=True,\
                       figsize=(CCU_Concrete_Constants.figsize_width_histogram, \
                                CCU_Concrete_Constants.figsize_height_histogram))

fig.add_subplot(111, frameon=False)

plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)

for a in range(plot_rows):
    for b in range(plot_columns):
        ax[a,b].spines['top'].set_visible(False)
        ax[a,b].spines['right'].set_visible(False)
        ax[a,b].spines['bottom'].set_visible(False)
        ax[a,b].spines['left'].set_visible(False)

ax[0,0].set_yticks([])
ax[0,0].set_xticks([])

ticks_font = font_manager.FontProperties(family=CCU_Concrete_Constants.font_family, \
                                         style=CCU_Concrete_Constants.font_style,\
                                         size=CCU_Concrete_Constants.xaxis_tick_fontsize,\
                                         weight=CCU_Concrete_Constants.font_weight)

flag=0

for i in range((number_of_studies)):
    
    print('i             :',i)
    
    Delta_process_emissions_array_array,Baseline_process_emissions_array_array, CCU_process_emissions_array_array = f_get_input_array(i)
    
    CCU_CO2_Total=np.sum(CCU_process_emissions_array_array,axis=1)
    Baseline_CO2_Total=np.sum(Baseline_process_emissions_array_array,axis=1)
    
    CCU_betters_Baseline = 0

    for p,q in zip(CCU_CO2_Total,Baseline_CO2_Total):
        
        if (p<q):
            CCU_betters_Baseline = CCU_betters_Baseline+1
           
   
    ax1 = fig.add_subplot(plot_rows, plot_columns,i+1)

    
    delta_CO2=Baseline_CO2_Total-CCU_CO2_Total
    X_max = np.max(delta_CO2)
    X_min = np.min(delta_CO2)
    
    
    if ((CCU_betters_Baseline/number_of_samples)<CCU_Concrete_Constants.Probability_Preference):
        spine_color='red'
        flag = flag+1

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
    
    plt.axvline(linewidth=CCU_Concrete_Constants.vline_width_histogram, label='_nolegend_', color=spine_color)
    
    l1=sns.distplot(delta_CO2, hist=False, kde_kws={'shade': False,'linewidth':CCU_Concrete_Constants.dist_curve_width},color=spine_color)
    xticks=ax1.get_xticks()
    
    if(abs(min(xticks))>abs(max(xticks))):
        x_axis_upper_limit=-min(xticks)
        x_axis_lower_limit=min(xticks)
        
    if(abs(min(xticks))<abs(max(xticks)) or abs(min(xticks))==abs(max(xticks))):
        x_axis_upper_limit=max(xticks)
        x_axis_lower_limit=-max(xticks)

    text_font = {'family': CCU_Concrete_Constants.font_family,
        'color':  spine_color,
        'weight': CCU_Concrete_Constants.font_weight,
        'size': CCU_Concrete_Constants.xaxis_tick_fontsize,
        }  
    ax1.text(x_axis_lower_limit,0.00001,"("+str(i+1)+")",fontdict=text_font, verticalalignment='bottom')
    ax1.text(x_axis_upper_limit,0.00001,str(int((CCU_betters_Baseline/number_of_samples)*100))+"%",verticalalignment='bottom', fontdict=text_font, horizontalalignment='right',)
    
    if((i+1<=71) or (i+1>=77)):
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
    if((i+1>=72) and (i+1<=76)):
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%0.2f'))
   
    ax1.tick_params(axis='x', which='major', pad=CCU_Concrete_Constants.xaxis_tick_padding_histogram)
    ax1.tick_params(axis='y', which='major', pad=CCU_Concrete_Constants.yaxis_tick_padding_histogram)
    plt.tick_params(labelcolor=spine_color, top=False, bottom=False, left=False, right=False)
    plt.xticks(np.arange(x_axis_lower_limit, x_axis_upper_limit+.01, abs(x_axis_upper_limit))) 

    plt.yticks([]) 

    for label in ax1.get_xticklabels():
        label.set_fontproperties(ticks_font)
        
    fig.tight_layout(pad=CCU_Concrete_Constants.Tightlayout_Pad_histogram)
    
print('CCU has higher CO2 impact than Conventional concrete (red)      :', flag)

print('output_file_name      :', output_file_name)

plt.savefig(output_file_name, format=CCU_Concrete_Constants.output_file_format)

  



        

