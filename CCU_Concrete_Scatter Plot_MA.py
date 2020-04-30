import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FormatStrFormatter
import CCU_Concrete_Constants

excel_file = CCU_Concrete_Constants.excel_file
df = pd.read_excel(excel_file, sheet_name=CCU_Concrete_Constants.sheet_name)
plot_rows=CCU_Concrete_Constants.plot_rows
plot_columns=CCU_Concrete_Constants.plot_columns
number_of_studies=CCU_Concrete_Constants.number_of_studies
number_of_samples=CCU_Concrete_Constants.number_of_samples

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

Baseline_cement_LB_array=(df[CCU_Concrete_Constants.Baseline_Cement_LB].tolist())
Baseline_cement_UB_array=(df[CCU_Concrete_Constants.Baseline_Cement_UB].tolist())

Baseline_coarse_agg_LB_array=(df[CCU_Concrete_Constants.Baseline_Coarse_Aggregate_LB].tolist())
Baseline_coarse_agg_UB_array=(df[CCU_Concrete_Constants.Baseline_Coarse_Aggregate_UB].tolist())

Baseline_fine_agg_LB_array=(df[CCU_Concrete_Constants.Baseline_Fine_Aggregate_LB].tolist())
Baseline_fine_agg_UB_array=(df[CCU_Concrete_Constants.Baseline_Fine_Aggregate_UB].tolist())

Baseline_water_LB_array=(df[CCU_Concrete_Constants.Baseline_Water_LB].tolist())
Baseline_water_UB_array=(df[CCU_Concrete_Constants.Baseline_Water_UB].tolist())

Baseline_SCM_LB_array=(df[CCU_Concrete_Constants.Baseline_SCM_LB].tolist())
Baseline_SCM_UB_array=(df[CCU_Concrete_Constants.Baseline_SCM_UB].tolist())

CCU_cement_LB_array=(df[CCU_Concrete_Constants.CCU_Cement_LB].tolist())
CCU_cement_UB_array=(df[CCU_Concrete_Constants.CCU_Cement_UB].tolist())

CCU_coarse_agg_LB_array=(df[CCU_Concrete_Constants.CCU_Coarse_Aggregate_LB].tolist())
CCU_coarse_agg_UB_array=(df[CCU_Concrete_Constants.CCU_Coarse_Aggregate_UB].tolist())

CCU_fine_agg_LB_array=(df[CCU_Concrete_Constants.CCU_Fine_Aggregate_LB].tolist())
CCU_fine_agg_UB_array=(df[CCU_Concrete_Constants.CCU_Fine_Aggregate_UB].tolist())

CCU_water_LB_array=(df[CCU_Concrete_Constants.CCU_Water_LB].tolist())
CCU_water_UB_array=(df[CCU_Concrete_Constants.CCU_Water_UB].tolist())

CCU_SCM_LB_array=(df[CCU_Concrete_Constants.CCU_SCM_LB].tolist())
CCU_SCM_UB_array=(df[CCU_Concrete_Constants.CCU_SCM_UB].tolist())

CCU_CO2_absorbed_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Absorbed_LB].tolist())
CCU_CO2_absorbed_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Absorbed_UB].tolist())

SCM_Type=(df[CCU_Concrete_Constants.Baseline_SCM_Type].tolist())

CCU_CO2_Vaporization_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_vaporizer_energy_requirement_LB].tolist())
CCU_CO2_Vaporization_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_vaporizer_energy_requirement_UB].tolist())

CCU_CO2_Injecter_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Injecter_LB].tolist())
CCU_CO2_Injecter_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Injecter_UB].tolist())

Baseline_CO2_Steam_Curing_LB_array=(df[CCU_Concrete_Constants.Baseline_CO2_Steam_Curing_LB].tolist())
Baseline_CO2_Steam_Curing_UB_array=(df[CCU_Concrete_Constants.Baseline_CO2_Steam_Curing_UB].tolist())

CCU_CO2_Steam_Curing_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Steam_Curing_LB].tolist())
CCU_CO2_Steam_Curing_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Steam_Curing_UB].tolist())

CCU_CO2_Curing_Hours_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Curing_Hours_LB].tolist())
CCU_CO2_Curing_Hours_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Curing_Hours_UB].tolist())

CCU_Injection_Electricity=CCU_Concrete_Constants.CCU_Injection_Electricity
CCU_Cooling_Electricity=CCU_Concrete_Constants.CCU_Cooling_Electricity
CCU_Vaporization_Electricity=CCU_Concrete_Constants.CCU_Vaporization_Electricity
CO2_captured_intensity=CCU_Concrete_Constants.CO2_captured_intensity
CO2_Not_captured_intensity=CCU_Concrete_Constants.CO2_Not_captured_intensity
CO2_Compression_Elec_Requirement_LB=CCU_Concrete_Constants.CO2_Compression_Elec_Requirement_LB
CO2_Compression_Elec_Requirement_UB=CCU_Concrete_Constants.CO2_Compression_Elec_Requirement_UB
Power_Required_CO2_Curing=CCU_Concrete_Constants.Power_Required_CO2_Curing
Heat_to_electricity_LB=CCU_Concrete_Constants.Heat_to_electricity_LB
Heat_to_electricity_UB=CCU_Concrete_Constants.Heat_to_electricity_UB
CO2_Capture_Elec_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Elec_Requirement_LB
CO2_Capture_Elec_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Elec_Requirement_UB
CO2_Capture_Heat_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Heat_Requirement_LB
CO2_Capture_Heat_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Heat_Requirement_UB

cement_CO2_intensity_mean=CCU_Concrete_Constants.cement_CO2_intensity_mean
cement_CO2_intensity_sd=CCU_Concrete_Constants.cement_CO2_intensity_sd
m1 = math.log((cement_CO2_intensity_mean**2)/math.sqrt(cement_CO2_intensity_sd**2+cement_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(cement_CO2_intensity_sd**2/(cement_CO2_intensity_mean**2)+1))
cement_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)

coarse_agg_CO2_intensity_mean=CCU_Concrete_Constants.coarse_agg_CO2_intensity_mean
coarse_agg_CO2_intensity_sd=CCU_Concrete_Constants.coarse_agg_CO2_intensity_sd
m1 = math.log((coarse_agg_CO2_intensity_mean**2)/math.sqrt(coarse_agg_CO2_intensity_sd**2+coarse_agg_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(coarse_agg_CO2_intensity_sd**2/(coarse_agg_CO2_intensity_mean**2)+1))
coarse_agg_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)

fine_agg_CO2_intensity_mean=CCU_Concrete_Constants.fine_agg_CO2_intensity_mean
fine_agg_CO2_intensity_sd=CCU_Concrete_Constants.fine_agg_CO2_intensity_sd
m1 = math.log((fine_agg_CO2_intensity_mean**2)/math.sqrt(fine_agg_CO2_intensity_sd**2+fine_agg_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(fine_agg_CO2_intensity_sd**2/(fine_agg_CO2_intensity_mean**2)+1))
fine_agg_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)

water_CO2_intensity_mean=CCU_Concrete_Constants.water_CO2_intensity_mean
water_CO2_intensity_sd=CCU_Concrete_Constants.water_CO2_intensity_sd
m1 = math.log((water_CO2_intensity_mean**2)/math.sqrt(water_CO2_intensity_sd**2+water_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(water_CO2_intensity_sd**2/(water_CO2_intensity_mean**2)+1))
water_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)

Transportation_CO2_Intensity=CCU_Concrete_Constants.Transportation_CO2_Intensity

CO2_Capture_Penalty_Coal_Elec_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Penalty_Coal_Elec_Requirement_LB
CO2_Capture_Penalty_Coal_Elec_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Penalty_Coal_Elec_Requirement_UB

CO2_Capture_Penalty_Coal_Heat_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Penalty_Coal_Heat_Requirement_LB
CO2_Capture_Penalty_Coal_Heat_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Penalty_Coal_Heat_Requirement_UB

elec_coal_CO2_intensity_LB=CCU_Concrete_Constants.elec_coal_CO2_intensity_LB
elec_coal_CO2_intensity_UB=CCU_Concrete_Constants.elec_coal_CO2_intensity_UB
elec_coal_CO2_intensity=np.random.uniform(elec_coal_CO2_intensity_LB,elec_coal_CO2_intensity_UB,number_of_samples)

heat_coal_CO2_intensity_mean=CCU_Concrete_Constants.heat_coal_CO2_intensity_mean
heat_coal_CO2_intensity_sd=CCU_Concrete_Constants.heat_coal_CO2_intensity_sd
m1 = math.log((heat_coal_CO2_intensity_mean**2)/math.sqrt(heat_coal_CO2_intensity_sd**2+heat_coal_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(heat_coal_CO2_intensity_sd**2/(heat_coal_CO2_intensity_mean**2)+1))
heat_coal_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)

CCU_CO2_Curing_Elec_CO2_intensity_LB = CCU_Concrete_Constants.CCU_CO2_Curing_Elec_CO2_intensity_LB
CCU_CO2_Curing_Elec_CO2_intensity_UB = CCU_Concrete_Constants.CCU_CO2_Curing_Elec_CO2_intensity_UB
CCU_CO2_Curing_CO2_intensity_array=np.random.uniform(CCU_CO2_Curing_Elec_CO2_intensity_LB,CCU_CO2_Curing_Elec_CO2_intensity_UB,number_of_samples)

CCU_Injection_Elec_CO2_Intensity_LB = CCU_Concrete_Constants.CCU_Injection_Elec_CO2_Intensity_LB
CCU_Injection_Elec_CO2_Intensity_UB = CCU_Concrete_Constants.CCU_Injection_Elec_CO2_Intensity_UB
CCU_Injection_Elec_CO2_Intensity_array=np.random.uniform(CCU_Injection_Elec_CO2_Intensity_LB,CCU_Injection_Elec_CO2_Intensity_UB,number_of_samples)

CCU_Cooling_Elec_CO2_Intensity_LB = CCU_Concrete_Constants.CCU_Cooling_Elec_CO2_Intensity_LB
CCU_Cooling_Elec_CO2_Intensity_UB = CCU_Concrete_Constants.CCU_Cooling_Elec_CO2_Intensity_UB
CCU_Cooling_Elec_CO2_Intensity_array=np.random.uniform(CCU_Cooling_Elec_CO2_Intensity_LB,CCU_Cooling_Elec_CO2_Intensity_UB,number_of_samples)

CCU_Vaporization_Elec_CO2_Intensity_LB = CCU_Concrete_Constants.CCU_Vaporization_Elec_CO2_Intensity_LB
CCU_Vaporization_Elec_CO2_Intensity_UB = CCU_Concrete_Constants.CCU_Vaporization_Elec_CO2_Intensity_UB
CCU_Vaporization_Elec_CO2_Intensity_array=np.random.uniform(CCU_Vaporization_Elec_CO2_Intensity_LB,CCU_Vaporization_Elec_CO2_Intensity_UB,number_of_samples)

CO2_Transportation_Distance_LB=CCU_Concrete_Constants.CO2_Transportation_Distance_LB
CO2_Transportation_Distance_UB=CCU_Concrete_Constants.CO2_Transportation_Distance_UB
CO2_Transportation_Distance_array=np.random.uniform(CO2_Transportation_Distance_LB,CO2_Transportation_Distance_UB,number_of_samples)

MEA_CO2_intensity_mean=CCU_Concrete_Constants.MEA_CO2_intensity_mean
MEA_CO2_intensity_sd=CCU_Concrete_Constants.MEA_CO2_intensity_sd
m1 = math.log((MEA_CO2_intensity_mean**2)/math.sqrt(MEA_CO2_intensity_sd**2+MEA_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(MEA_CO2_intensity_sd**2/(MEA_CO2_intensity_mean**2)+1))
MEA_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)

CO2_Infra_Air_Comp_CO2_intensity_mean=CCU_Concrete_Constants.CO2_Infra_Air_Comp_CO2_intensity_mean
CO2_Infra_Air_Comp_CO2_intensity_sd=CCU_Concrete_Constants.CO2_Infra_Air_Comp_CO2_intensity_sd
m1 = math.log((CO2_Infra_Air_Comp_CO2_intensity_mean**2)/math.sqrt(CO2_Infra_Air_Comp_CO2_intensity_sd**2+CO2_Infra_Air_Comp_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(CO2_Infra_Air_Comp_CO2_intensity_sd**2/(CO2_Infra_Air_Comp_CO2_intensity_mean**2)+1))
Infra_Air_Comp_CO2_array_array=np.random.lognormal(m1, sd1, number_of_samples)

CO2_Infra_Injector_CO2_intensity_mean=CCU_Concrete_Constants.CO2_Infra_Injector_CO2_intensity_mean
CO2_Infra_Injector_CO2_intensity_sd=CCU_Concrete_Constants.CO2_Infra_Injector_CO2_intensity_sd
m1 = math.log((CO2_Infra_Injector_CO2_intensity_mean**2)/math.sqrt(CO2_Infra_Injector_CO2_intensity_sd**2+CO2_Infra_Injector_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(CO2_Infra_Injector_CO2_intensity_sd**2/(CO2_Infra_Injector_CO2_intensity_mean**2)+1))
Infra_Injector_CO2_array_array=np.random.lognormal(m1, sd1, number_of_samples)

CO2_Infra_Truck_CO2_intensity_mean=CCU_Concrete_Constants.CO2_Infra_Truck_CO2_intensity_mean
CO2_Infra_Truck_CO2_intensity_sd=CCU_Concrete_Constants.CO2_Infra_Truck_CO2_intensity_sd
m1 = math.log((CO2_Infra_Truck_CO2_intensity_mean**2)/math.sqrt(CO2_Infra_Truck_CO2_intensity_sd**2+CO2_Infra_Truck_CO2_intensity_mean**2))
sd1= math.sqrt(math.log(CO2_Infra_Truck_CO2_intensity_sd**2/(CO2_Infra_Truck_CO2_intensity_mean**2)+1))
Infra_Truck_CO2_array_array=np.random.lognormal(m1, sd1, number_of_samples)

Transportation_road_CO2_Intensity=CCU_Concrete_Constants.Transportation_road_CO2_Intensity
Transportation_rail_CO2_Intensity=CCU_Concrete_Constants.Transportation_rail_CO2_Intensity
Transportation_ocean_CO2_Intensity=CCU_Concrete_Constants.Transportation_ocean_CO2_Intensity
Transportation_barge_CO2_Intensity=CCU_Concrete_Constants.Transportation_barge_CO2_Intensity

cement_road_transport_distance_LB=CCU_Concrete_Constants.cement_road_transport_distance_LB
cement_road_transport_distance_UB=CCU_Concrete_Constants.cement_road_transport_distance_UB
cement_road_transport_distance_array=np.random.uniform(cement_road_transport_distance_LB,cement_road_transport_distance_UB,number_of_samples)

cement_rail_transport_distance_LB=CCU_Concrete_Constants.cement_rail_transport_distance_LB
cement_rail_transport_distance_UB=CCU_Concrete_Constants.cement_rail_transport_distance_UB
cement_rail_transport_distance_array=np.random.uniform(cement_rail_transport_distance_LB,cement_rail_transport_distance_UB,number_of_samples)

cement_ocean_transport_distance_LB=CCU_Concrete_Constants.cement_ocean_transport_distance_LB
cement_ocean_transport_distance_UB=CCU_Concrete_Constants.cement_ocean_transport_distance_UB
cement_ocean_transport_distance_array=np.random.uniform(cement_ocean_transport_distance_LB,cement_ocean_transport_distance_UB,number_of_samples)

cement_barge_transport_distance_LB=CCU_Concrete_Constants.cement_barge_transport_distance_LB
cement_barge_transport_distance_UB=CCU_Concrete_Constants.cement_barge_transport_distance_UB
cement_barge_transport_distance_array=np.random.uniform(cement_barge_transport_distance_LB,cement_barge_transport_distance_UB,number_of_samples)

coarse_agg_road_transport_distance_LB=CCU_Concrete_Constants.coarse_agg_road_transport_distance_LB
coarse_agg_road_transport_distance_UB=CCU_Concrete_Constants.coarse_agg_road_transport_distance_UB
coarse_agg_road_transport_distance_array=np.random.uniform(coarse_agg_road_transport_distance_LB,coarse_agg_road_transport_distance_UB,number_of_samples)

coarse_agg_rail_transport_distance_LB=CCU_Concrete_Constants.coarse_agg_rail_transport_distance_LB
coarse_agg_rail_transport_distance_UB=CCU_Concrete_Constants.coarse_agg_rail_transport_distance_UB
coarse_agg_rail_transport_distance_array=np.random.uniform(coarse_agg_rail_transport_distance_LB,coarse_agg_rail_transport_distance_UB,number_of_samples)

coarse_agg_ocean_transport_distance_LB=CCU_Concrete_Constants.coarse_agg_ocean_transport_distance_LB
coarse_agg_ocean_transport_distance_UB=CCU_Concrete_Constants.coarse_agg_ocean_transport_distance_UB
coarse_agg_ocean_transport_distance_array=np.random.uniform(coarse_agg_ocean_transport_distance_LB,coarse_agg_ocean_transport_distance_UB,number_of_samples)

coarse_agg_barge_transport_distance_LB=CCU_Concrete_Constants.coarse_agg_barge_transport_distance_LB
coarse_agg_barge_transport_distance_UB=CCU_Concrete_Constants.coarse_agg_barge_transport_distance_UB
coarse_agg_barge_transport_distance_array=np.random.uniform(coarse_agg_barge_transport_distance_LB,coarse_agg_barge_transport_distance_UB,number_of_samples)

fine_agg_road_transport_distance_LB=CCU_Concrete_Constants.fine_agg_road_transport_distance_LB
fine_agg_road_transport_distance_UB=CCU_Concrete_Constants.fine_agg_road_transport_distance_UB
fine_agg_road_transport_distance_array=np.random.uniform(fine_agg_road_transport_distance_LB,fine_agg_road_transport_distance_UB,number_of_samples)

fine_agg_rail_transport_distance_LB=CCU_Concrete_Constants.fine_agg_rail_transport_distance_LB
fine_agg_rail_transport_distance_UB=CCU_Concrete_Constants.fine_agg_rail_transport_distance_UB
fine_agg_rail_transport_distance_array=np.random.uniform(fine_agg_rail_transport_distance_LB,fine_agg_rail_transport_distance_UB,number_of_samples)

fine_agg_ocean_transport_distance_LB=CCU_Concrete_Constants.fine_agg_ocean_transport_distance_LB
fine_agg_ocean_transport_distance_UB=CCU_Concrete_Constants.fine_agg_ocean_transport_distance_UB
fine_agg_ocean_transport_distance_array=np.random.uniform(fine_agg_ocean_transport_distance_LB,fine_agg_ocean_transport_distance_UB,number_of_samples)

fine_agg_barge_transport_distance_LB=CCU_Concrete_Constants.fine_agg_barge_transport_distance_LB
fine_agg_barge_transport_distance_UB=CCU_Concrete_Constants.fine_agg_barge_transport_distance_UB
fine_agg_barge_transport_distance_array=np.random.uniform(fine_agg_barge_transport_distance_LB,fine_agg_barge_transport_distance_UB,number_of_samples)

water_road_transport_distance_LB=CCU_Concrete_Constants.water_road_transport_distance_LB
water_road_transport_distance_UB=CCU_Concrete_Constants.water_road_transport_distance_UB
water_road_transport_distance_array=np.random.uniform(water_road_transport_distance_LB,water_road_transport_distance_UB,number_of_samples)

water_rail_transport_distance_LB=CCU_Concrete_Constants.water_rail_transport_distance_LB
water_rail_transport_distance_UB=CCU_Concrete_Constants.water_rail_transport_distance_UB
water_rail_transport_distance_array=np.random.uniform(water_rail_transport_distance_LB,water_rail_transport_distance_UB,number_of_samples)

water_ocean_transport_distance_LB=CCU_Concrete_Constants.water_ocean_transport_distance_LB
water_ocean_transport_distance_UB=CCU_Concrete_Constants.water_ocean_transport_distance_UB
water_ocean_transport_distance_array=np.random.uniform(water_ocean_transport_distance_LB,water_ocean_transport_distance_UB,number_of_samples)

water_barge_transport_distance_LB=CCU_Concrete_Constants.water_barge_transport_distance_LB
water_barge_transport_distance_UB=CCU_Concrete_Constants.water_barge_transport_distance_UB
water_barge_transport_distance_array=np.random.uniform(water_barge_transport_distance_LB,water_barge_transport_distance_UB,number_of_samples)

flag=0


for i in range((number_of_studies)):

  
    Baseline_cement_array = np.random.uniform(Baseline_cement_LB_array[i],Baseline_cement_UB_array[i],number_of_samples)
    Baseline_cement_CO2_array_array = cement_CO2_intensity*Baseline_cement_array

     
    CCU_CO2_captured_array = Baseline_cement_array*np.random.uniform(CCU_CO2_absorbed_LB_array[i],CCU_CO2_absorbed_UB_array[i],number_of_samples)
    
  
    Baseline_coarse_agg_array=np.random.uniform(Baseline_coarse_agg_LB_array[i],Baseline_coarse_agg_UB_array[i],number_of_samples)
    Baseline_coarse_agg_CO2_array_array = coarse_agg_CO2_intensity*Baseline_coarse_agg_array
    
    Baseline_fine_agg_array = np.random.uniform(Baseline_fine_agg_LB_array[i],Baseline_fine_agg_UB_array[i],number_of_samples)
    Baseline_fine_agg_CO2_array_array = fine_agg_CO2_intensity*Baseline_fine_agg_array
    
    
    Baseline_water_array = np.random.uniform(Baseline_water_LB_array[i],Baseline_water_UB_array[i],number_of_samples)
    Baseline_water_CO2_array_array = water_CO2_intensity*Baseline_water_array
    
    
    if (SCM_Type[i]==CCU_Concrete_Constants.SCM_Slag):

        Pig_Iron_CO2_intensity_mean=CCU_Concrete_Constants.Pig_Iron_CO2_intensity_mean
        Pig_Iron_CO2_intensity_sd=CCU_Concrete_Constants.Pig_Iron_CO2_intensity_sd
        m1 = math.log((Pig_Iron_CO2_intensity_mean**2)/math.sqrt(Pig_Iron_CO2_intensity_sd**2+Pig_Iron_CO2_intensity_mean**2))
        sd1= math.sqrt(math.log(Pig_Iron_CO2_intensity_sd**2/(Pig_Iron_CO2_intensity_mean**2)+1))
        
        #THIS IS THE CODE FOR SYSTEM BOUNDARY EXPANSION
#        SCM_CO2_intensity=7.7*np.random.lognormal(m1, sd1, number_of_samples)
        
#        #THIS IS THE CODE FOR ECONOMIC ALLOCATION
#        SCM_CO2_intensity=0.008*7.7*np.random.lognormal(m1, sd1, number_of_samples)
#        
#        #THIS IS THE CODE FOR MASS ALLOCATION
        SCM_CO2_intensity=0.11*7.7*np.random.lognormal(m1, sd1, number_of_samples)
        
        SCM_road_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_slag
        SCM_road_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_slag
        SCM_road_transport_distance_array=np.random.uniform(SCM_road_transport_distance_LB,SCM_road_transport_distance_UB,number_of_samples)
        
        SCM_rail_transport_distance_LB=CCU_Concrete_Constants.SCM_rail_transport_distance_LB_slag
        SCM_rail_transport_distance_UB=CCU_Concrete_Constants.SCM_rail_transport_distance_UB_slag
        SCM_rail_transport_distance_array=np.random.uniform(SCM_rail_transport_distance_LB,SCM_rail_transport_distance_UB,number_of_samples)
        
        SCM_ocean_transport_distance_LB=CCU_Concrete_Constants.SCM_ocean_transport_distance_LB_slag
        SCM_ocean_transport_distance_UB=CCU_Concrete_Constants.SCM_ocean_transport_distance_UB_slag
        SCM_ocean_transport_distance_array=np.random.uniform(SCM_ocean_transport_distance_LB,SCM_ocean_transport_distance_UB,number_of_samples)
        
        SCM_barge_transport_distance_LB=CCU_Concrete_Constants.SCM_barge_transport_distance_LB_slag
        SCM_barge_transport_distance_UB=CCU_Concrete_Constants.SCM_barge_transport_distance_UB_slag
        SCM_barge_transport_distance_array=np.random.uniform(SCM_barge_transport_distance_LB,SCM_barge_transport_distance_UB,number_of_samples)

    elif (SCM_Type[i]==CCU_Concrete_Constants.SCM_Fly_Ash):
        
        #Case when SCM type is fly ash, which is a by product of the coal industry
        Coal_Elec_CO2_intensity_mean=CCU_Concrete_Constants.Coal_Elec_CO2_intensity_mean
        Coal_Elec_CO2_intensity_sd=CCU_Concrete_Constants.Coal_Elec_CO2_intensity_sd
        m1 = math.log((Coal_Elec_CO2_intensity_mean**2)/math.sqrt(Coal_Elec_CO2_intensity_sd**2+Coal_Elec_CO2_intensity_mean**2))
        sd1= math.sqrt(math.log(Coal_Elec_CO2_intensity_sd**2/(Coal_Elec_CO2_intensity_mean**2)+1))
        
        #THIS IS THE CODE FOR SYSTEM BOUNDARY EXPANSION
#        SCM_CO2_intensity=22.7*np.random.lognormal(m1, sd1, number_of_samples)
        
#        #THIS IS THE CODE FOR ECONOMIC ALLOCATION
#        SCM_CO2_intensity=0.013*22.7*np.random.lognormal(m1, sd1, number_of_samples)  
#        
#        #THIS IS THE CODE FOR MASS ALLOCATION
        SCM_CO2_intensity=0.06*22.7*np.random.lognormal(m1, sd1, number_of_samples)  
        
        SCM_road_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
        SCM_road_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
        SCM_road_transport_distance_array=np.random.uniform(SCM_road_transport_distance_LB,SCM_road_transport_distance_UB,number_of_samples)
        
        SCM_rail_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
        SCM_rail_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
        SCM_rail_transport_distance_array=np.random.uniform(SCM_rail_transport_distance_LB,SCM_rail_transport_distance_UB,number_of_samples)
        
        SCM_ocean_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
        SCM_ocean_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
        SCM_ocean_transport_distance_array=np.random.uniform(SCM_ocean_transport_distance_LB,SCM_ocean_transport_distance_UB,number_of_samples)
        
        SCM_barge_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
        SCM_barge_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
        SCM_barge_transport_distance_array=np.random.uniform(SCM_barge_transport_distance_LB,SCM_barge_transport_distance_UB,number_of_samples)
 
    elif (SCM_Type[i]==CCU_Concrete_Constants.SCM_None):
        SCM_CO2_intensity=CCU_Concrete_Constants.SCM_CO2_intensity_no_SCM
        
        SCM_road_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_no_SCM
        SCM_road_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_no_SCM
        SCM_road_transport_distance_array=np.random.uniform(SCM_road_transport_distance_LB,SCM_road_transport_distance_UB,number_of_samples)
        
        SCM_rail_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_no_SCM
        SCM_rail_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_no_SCM
        SCM_rail_transport_distance_array=np.random.uniform(SCM_rail_transport_distance_LB,SCM_rail_transport_distance_UB,number_of_samples)
        
        SCM_ocean_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_no_SCM
        SCM_ocean_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_no_SCM
        SCM_ocean_transport_distance_array=np.random.uniform(SCM_ocean_transport_distance_LB,SCM_ocean_transport_distance_UB,number_of_samples)
        
        SCM_barge_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_no_SCM
        SCM_barge_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_no_SCM
        SCM_barge_transport_distance_array=np.random.uniform(SCM_barge_transport_distance_LB,SCM_barge_transport_distance_UB,number_of_samples)
       
    
    Baseline_SCM_array = np.random.uniform(Baseline_SCM_LB_array[i],Baseline_SCM_UB_array[i],number_of_samples)
    Baseline_SCM_CO2_array_array = SCM_CO2_intensity*Baseline_SCM_array
        
    
    Baseline_SCM_CO2_array_array = SCM_CO2_intensity*np.random.uniform(Baseline_SCM_LB_array[i],Baseline_SCM_UB_array[i],number_of_samples)
    Baseline_CO2_captured_array_array = np.zeros(number_of_samples)
    #CO2 captured in the CCU scenario is assumed to be released in the baseline scenario
    #as the power plant is operating without carbon capture
    Baseline_CO2_Not_captured_array_array = CCU_CO2_captured_array
    Baseline_CO2_Power_Plant_array_array=Baseline_CO2_Not_captured_array_array
    Baseline_Energy_Penalty_CO2_array_array = np.zeros(number_of_samples)
    Baseline_CO2_Pipeline_CO2_array_array = np.zeros(number_of_samples)
    Baseline_CO2_Air_Comp_CO2_array_array = np.zeros(number_of_samples)
    Baseline_CO2_Vaporization_CO2_array_array = np.zeros(number_of_samples)
    Baseline_CO2_Injecter_CO2_array_array = np.zeros(number_of_samples)
    Baseline_CO2_capture_MEA_array_array = np.zeros(number_of_samples)
    Baseline_CO2_Steam_Curing_array_array=np.random.uniform(Baseline_CO2_Steam_Curing_LB_array[i],Baseline_CO2_Steam_Curing_UB_array[i],number_of_samples)

    Baseline_Material_Transportation_CO2_array_array=\
    (cement_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_water_array)+\
    (SCM_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_SCM_array)+\
    (cement_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_water_array)+\
    (SCM_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_SCM_array)+\
    (cement_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_water_array)+\
    (SCM_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_SCM_array)+\
    (cement_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_water_array)+\
    (SCM_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_SCM_array)
      
    CCU_cement_array = np.random.uniform(CCU_cement_LB_array[i],CCU_cement_UB_array[i],number_of_samples)
    CCU_coarse_agg_array = np.random.uniform(CCU_coarse_agg_LB_array[i],CCU_coarse_agg_UB_array[i],number_of_samples)
    CCU_fine_agg_array = np.random.uniform(CCU_fine_agg_LB_array[i],CCU_fine_agg_UB_array[i],number_of_samples)
    CCU_water_array = np.random.uniform(CCU_water_LB_array[i],CCU_water_UB_array[i],number_of_samples)
    CCU_SCM_array = np.random.uniform(CCU_SCM_LB_array[i],CCU_SCM_UB_array[i],number_of_samples)
    CO2_Capture_Penalty_Coal_Heat_Requirement_array=np.random.uniform(CO2_Capture_Penalty_Coal_Heat_Requirement_LB,CO2_Capture_Penalty_Coal_Heat_Requirement_UB,number_of_samples)
    CO2_Capture_Penalty_Coal_Elec_Requirement_array= np.random.uniform(CO2_Capture_Penalty_Coal_Elec_Requirement_LB,CO2_Capture_Penalty_Coal_Elec_Requirement_UB,number_of_samples)
    
    CCU_cement_CO2_array_array = cement_CO2_intensity*CCU_cement_array
    CCU_coarse_agg_CO2_array_array = coarse_agg_CO2_intensity*CCU_coarse_agg_array
    CCU_fine_agg_CO2_array_array = fine_agg_CO2_intensity*CCU_fine_agg_array
    CCU_water_CO2_array_array = water_CO2_intensity*CCU_water_array
    CCU_SCM_CO2_array_array = SCM_CO2_intensity*CCU_SCM_array
    CCU_CO2_captured_array_array = CO2_captured_intensity*CCU_CO2_captured_array
    CCU_CO2_Not_captured_array_array = CO2_Not_captured_intensity*(CCU_CO2_captured_array/9)
  
    CCU_cement_array = np.random.uniform(CCU_cement_LB_array[i],CCU_cement_UB_array[i],number_of_samples)
    CCU_coarse_agg_array = np.random.uniform(CCU_coarse_agg_LB_array[i],CCU_coarse_agg_UB_array[i],number_of_samples)
    CCU_fine_agg_array = np.random.uniform(CCU_fine_agg_LB_array[i],CCU_fine_agg_UB_array[i],number_of_samples)
    CCU_water_array = np.random.uniform(CCU_water_LB_array[i],CCU_water_UB_array[i],number_of_samples)
    CCU_SCM_array = np.random.uniform(CCU_SCM_LB_array[i],CCU_SCM_UB_array[i],number_of_samples)
    CO2_Capture_Heat_Requirement_array=np.random.uniform(CO2_Capture_Heat_Requirement_LB,CO2_Capture_Heat_Requirement_UB,number_of_samples)
    CO2_Capture_Elec_Requirement_array= np.random.uniform(CO2_Capture_Elec_Requirement_LB,CO2_Capture_Elec_Requirement_UB,number_of_samples)
    CO2_Compression_Elec_Requirement_array= np.random.uniform(CO2_Compression_Elec_Requirement_LB,CO2_Compression_Elec_Requirement_UB,number_of_samples)
    CCU_CO2_Curing_Hours_array=np.random.uniform(CCU_CO2_Curing_Hours_LB_array[i],CCU_CO2_Curing_Hours_UB_array[i],number_of_samples)
    Heat_to_electricity_array=np.random.uniform(Heat_to_electricity_LB, Heat_to_electricity_UB,number_of_samples)
    CCU_cement_CO2_array_array = cement_CO2_intensity*CCU_cement_array
    CCU_coarse_agg_CO2_array_array = coarse_agg_CO2_intensity*CCU_coarse_agg_array
    CCU_fine_agg_CO2_array_array = fine_agg_CO2_intensity*CCU_fine_agg_array
    CCU_water_CO2_array_array = water_CO2_intensity*CCU_water_array
    CCU_SCM_CO2_array_array = SCM_CO2_intensity*CCU_SCM_array
    CCU_CO2_captured_array_array = CCU_CO2_captured_array
    CCU_CO2_Not_captured_array_array = CCU_CO2_captured_array/9
    CCU_CO2_Injection_Electricity_array_array=CCU_Injection_Elec_CO2_Intensity_array*CCU_Injection_Electricity*CCU_CO2_captured_array
    CCU_CO2_Cooling_Electricity_array_array=CCU_Cooling_Elec_CO2_Intensity_array*CCU_Cooling_Electricity*CCU_CO2_captured_array
    CCU_CO2_Vaporization_Electricity_CO2_array_array = CCU_Vaporization_Elec_CO2_Intensity_array*CCU_Vaporization_Electricity*CCU_CO2_captured_array
    CCU_CO2_Transportation_CO2_array_array=CO2_Transportation_Distance_array*Transportation_CO2_Intensity*CCU_CO2_captured_array
   
    CCU_Material_Transportation_CO2_array_array=\
    (cement_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_fine_agg_array)+\
    (water_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_water_array)+\
    (SCM_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_SCM_array)+\
    (cement_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_fine_agg_array)+\
    (water_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_water_array)+\
    (SCM_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_SCM_array)+\
    (cement_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_fine_agg_array)+\
    (water_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_water_array)+\
    (SCM_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_SCM_array)+\
    (cement_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_fine_agg_array)+\
    (water_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_water_array)+\
    (SCM_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_SCM_array)

    CCU_CO2_Capture_Total_Electricity_Penalty_CO2_array_array = ((elec_coal_CO2_intensity*Heat_to_electricity_array*0.277*CO2_Capture_Heat_Requirement_array*CCU_CO2_captured_array)\
    +(elec_coal_CO2_intensity*CO2_Capture_Elec_Requirement_array*CCU_CO2_captured_array)\
    +(elec_coal_CO2_intensity*CO2_Compression_Elec_Requirement_array*CCU_CO2_captured_array))

    CCU_CO2_capture_MEA_array_array = MEA_CO2_intensity*CCU_CO2_captured_array
    CO2_Infra_Total_array_array = CCU_CO2_captured_array*(Infra_Air_Comp_CO2_array_array+Infra_Injector_CO2_array_array+Infra_Truck_CO2_array_array)

    CCU_CO2_Curing_CO2_array_array = CCU_CO2_Curing_CO2_intensity_array*CCU_CO2_Curing_Hours_array*Power_Required_CO2_Curing
    CCU_CO2_Steam_Curing_array_array=np.random.uniform(CCU_CO2_Steam_Curing_LB_array[i],CCU_CO2_Steam_Curing_UB_array[i],number_of_samples)

    CCU_CO2_Power_Plant_array_array=CCU_CO2_Capture_Total_Electricity_Penalty_CO2_array_array+CCU_CO2_Cooling_Electricity_array_array+\
    CCU_CO2_Not_captured_array_array

    CCU_CO2_Total = CCU_cement_CO2_array_array\
       +CCU_coarse_agg_CO2_array_array\
       +CCU_fine_agg_CO2_array_array\
       +CCU_water_CO2_array_array\
       +CCU_SCM_CO2_array_array\
       +CCU_CO2_Power_Plant_array_array\
       +CCU_CO2_capture_MEA_array_array\
       +CCU_CO2_Curing_CO2_array_array\
       +CCU_CO2_Steam_Curing_array_array\
       +CCU_CO2_Injection_Electricity_array_array\
       +CCU_CO2_Transportation_CO2_array_array\
       +CCU_CO2_Vaporization_Electricity_CO2_array_array\
       +CCU_Material_Transportation_CO2_array_array
       
    Baseline_CO2_Total = Baseline_cement_CO2_array_array\
          +Baseline_coarse_agg_CO2_array_array\
          +Baseline_fine_agg_CO2_array_array\
          +Baseline_water_CO2_array_array\
          +Baseline_SCM_CO2_array_array\
          +Baseline_CO2_Power_Plant_array_array\
          +Baseline_CO2_Steam_Curing_array_array\
          +Baseline_Material_Transportation_CO2_array_array
    
    CCU_betters_Baseline = 0
    
    Y=Baseline_CO2_Total-CCU_CO2_Total

    for p,q in zip(CCU_CO2_Total,Baseline_CO2_Total):
        
        if (p<q):
            CCU_betters_Baseline = CCU_betters_Baseline+1
            
    ax1 = fig.add_subplot(plot_rows, plot_columns,i+1)
    
    cement_CO2_difference_array=Baseline_cement_CO2_array_array-CCU_cement_CO2_array_array
    coarse_agg_CO2_difference_array=Baseline_coarse_agg_CO2_array_array-CCU_coarse_agg_CO2_array_array
    fine_agg_CO2_difference_array=Baseline_fine_agg_CO2_array_array-CCU_fine_agg_CO2_array_array
    water_CO2_difference_array=Baseline_water_CO2_array_array-CCU_water_CO2_array_array
    SCM_CO2_difference_array=Baseline_SCM_CO2_array_array-CCU_SCM_CO2_array_array
    Material_Transportation_difference_array=Baseline_Material_Transportation_CO2_array_array-CCU_Material_Transportation_CO2_array_array
    CO2_capture_MEA_CO2_difference_array=-CCU_CO2_capture_MEA_array_array
    Power_Plant_difference_array=Baseline_CO2_Power_Plant_array_array-CCU_CO2_Power_Plant_array_array
    CO2_Transportation_difference_array_array=-CCU_CO2_Transportation_CO2_array_array
    CO2_Vaporization_Electricity_difference_array=-CCU_CO2_Vaporization_Electricity_CO2_array_array
    CO2_Injection_Electricity_difference_array=-CCU_CO2_Injection_Electricity_array_array
    CO2_Curing_difference_array=-CCU_CO2_Curing_CO2_array_array
    Steam_Curing_difference_array=Baseline_CO2_Steam_Curing_array_array-CCU_CO2_Steam_Curing_array_array

        
    l1=ax1.scatter(cement_CO2_difference_array, Y,color=color_array[0], s=2)
    ax1.scatter(coarse_agg_CO2_difference_array, Y,color=color_array[1], s=2)
    ax1.scatter(fine_agg_CO2_difference_array, Y,color=color_array[2], s=2)
    ax1.scatter(water_CO2_difference_array, Y,color=color_array[3], s=2)
    ax1.scatter(SCM_CO2_difference_array, Y,color=color_array[4], s=2)
    ax1.scatter(Material_Transportation_difference_array, Y,color=color_array[5], s=2)
    ax1.scatter(CO2_capture_MEA_CO2_difference_array, Y,color=color_array[6], s=2)
    ax1.scatter(Power_Plant_difference_array,Y,color=color_array[7], s=2)
    ax1.scatter(CO2_Transportation_difference_array_array, Y,color=color_array[8], s=2)
    ax1.scatter(CO2_Vaporization_Electricity_difference_array, Y,color=color_array[9], s=2)
    ax1.scatter(CO2_Injection_Electricity_difference_array, Y,color=color_array[10], s=2)
    ax1.scatter(CO2_Curing_difference_array, Y,color=color_array[11], s=2)
    ax1.scatter(Steam_Curing_difference_array, Y,color=color_array[12], s=2)
            
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

     
plt.savefig(CCU_Concrete_Constants.output_file_name_scatterplot, format=CCU_Concrete_Constants.output_file_format)

  



        

