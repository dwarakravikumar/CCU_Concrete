#from matplotlib.ticker import FormatStrFormatter
import math
import CCU_Concrete_Constants
import numpy as np
import pandas as pd

def f_get_input_array(i):
    
    excel_file = CCU_Concrete_Constants.excel_file
    df = pd.read_excel(excel_file, sheet_name=CCU_Concrete_Constants.sheet_name)
    number_of_samples=CCU_Concrete_Constants.number_of_samples
    number_of_parameters=CCU_Concrete_Constants.number_of_parameters
   
    CO2_Capture_Source = CCU_Concrete_Constants.CO2_Capture_Source
    Allocation_Type = CCU_Concrete_Constants.Allocation_Type
   
    #Scenario when CO2 is captured from a coal power plant
    if(CO2_Capture_Source==CCU_Concrete_Constants.Coal_Power_Plant):
        CO2_Capture_Heat_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Heat_Requirement_Coal_Plant_LB
        CO2_Capture_Heat_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Heat_Requirement_Coal_Plant_UB
        CO2_Capture_Elec_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Elec_Requirement_Coal_Plant_LB
        CO2_Capture_Elec_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Elec_Requirement_Coal_Plant_UB
        
        if(Allocation_Type == CCU_Concrete_Constants.System_Boundary_Expansion):
            Fly_Ash_Allocation_Factor=1
            Slag_Allocation_Factor=1
            Power_Plant_Electrcity_Allocation_Factor=1
        
        if(Allocation_Type == CCU_Concrete_Constants.Economic_Allocation):
            Fly_Ash_Allocation_Factor=0.02
            Slag_Allocation_Factor = 0.008
            Power_Plant_Electrcity_Allocation_Factor=0.98
        
        if(Allocation_Type == CCU_Concrete_Constants.Mass_Allocation): 
            Fly_Ash_Allocation_Factor=0.06
            Slag_Allocation_Factor = 0.11
            Power_Plant_Electrcity_Allocation_Factor=0.94
            
        Power_Plant_CO2_Intensity_mean=CCU_Concrete_Constants.Coal_Elec_CO2_intensity_mean
        Power_Plant_CO2_Intensity_sd=CCU_Concrete_Constants.Coal_Elec_CO2_intensity_sd
        m1 = math.log((Power_Plant_CO2_Intensity_mean**2)/math.sqrt(Power_Plant_CO2_Intensity_sd**2+Power_Plant_CO2_Intensity_mean**2))
        sd1= math.sqrt(math.log(Power_Plant_CO2_Intensity_sd**2/(Power_Plant_CO2_Intensity_mean**2)+1))
        Power_Plant_CO2_Intensity_array_array=np.random.lognormal(m1, sd1, number_of_samples)*Power_Plant_Electrcity_Allocation_Factor
       
    #Scenario when CO2 is captured from a NGCC power plant
    if(CO2_Capture_Source==CCU_Concrete_Constants.NGCC_Power_Plant):
        CO2_Capture_Heat_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Heat_Requirement_NGCC_Plant_LB
        CO2_Capture_Heat_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Heat_Requirement_NGCC_Plant_UB
        CO2_Capture_Elec_Requirement_LB=CCU_Concrete_Constants.CO2_Capture_Elec_Requirement_NGCC_Plant_LB
        CO2_Capture_Elec_Requirement_UB=CCU_Concrete_Constants.CO2_Capture_Elec_Requirement_NGCC_Plant_UB
        
        if(Allocation_Type == CCU_Concrete_Constants.System_Boundary_Expansion):
            Fly_Ash_Allocation_Factor=1
            Slag_Allocation_Factor=1
        
        if(Allocation_Type == CCU_Concrete_Constants.Economic_Allocation):
            Fly_Ash_Allocation_Factor=0.02
            Slag_Allocation_Factor = 0.008
        
        if(Allocation_Type == CCU_Concrete_Constants.Mass_Allocation): 
            Fly_Ash_Allocation_Factor=0.06
            Slag_Allocation_Factor = 0.11

        Power_Plant_Electrcity_Allocation_Factor=1
        
        Power_Plant_CO2_Intensity_mean=CCU_Concrete_Constants.NGCC_Elec_CO2_Intensity_mean
        Power_Plant_CO2_Intensity_sd=CCU_Concrete_Constants.NGCC_Elec_CO2_Intensity_sd
        m1 = math.log((Power_Plant_CO2_Intensity_mean**2)/math.sqrt(Power_Plant_CO2_Intensity_sd**2+Power_Plant_CO2_Intensity_mean**2))
        sd1= math.sqrt(math.log(Power_Plant_CO2_Intensity_sd**2/(Power_Plant_CO2_Intensity_mean**2)+1))
        Power_Plant_CO2_Intensity_array_array=np.random.lognormal(m1, sd1, number_of_samples)*Power_Plant_Electrcity_Allocation_Factor

    Baseline_cement_LB_array=(df[CCU_Concrete_Constants.Baseline_Cement_LB].tolist())
    Baseline_cement_UB_array=(df[CCU_Concrete_Constants.Baseline_Cement_UB].tolist())
    
    Baseline_coarse_agg_LB_array=(df[CCU_Concrete_Constants.Baseline_Coarse_Aggregate_LB].tolist())
    Baseline_coarse_agg_UB_array=(df[CCU_Concrete_Constants.Baseline_Coarse_Aggregate_UB].tolist())
    
    Baseline_fine_agg_LB_array=(df[CCU_Concrete_Constants.Baseline_Fine_Aggregate_LB].tolist())
    Baseline_fine_agg_UB_array=(df[CCU_Concrete_Constants.Baseline_Fine_Aggregate_UB].tolist())
    
    Baseline_water_LB_array=(df[CCU_Concrete_Constants.Baseline_Water_LB].tolist())
    Baseline_water_UB_array=(df[CCU_Concrete_Constants.Baseline_Water_UB].tolist())
    
    Baseline_SCM_Slag_LB_array=(df[CCU_Concrete_Constants.Baseline_SCM_Slag_LB].tolist())
    Baseline_SCM_Slag_UB_array=(df[CCU_Concrete_Constants.Baseline_SCM_Slag_UB].tolist())
    
    Baseline_SCM_Fly_Ash_LB_array=(df[CCU_Concrete_Constants.Baseline_SCM_Fly_Ash_LB].tolist())
    Baseline_SCM_Fly_Ash_UB_array=(df[CCU_Concrete_Constants.Baseline_SCM_Fly_Ash_UB].tolist())
    
    CCU_cement_LB_array=(df[CCU_Concrete_Constants.CCU_Cement_LB].tolist())
    CCU_cement_UB_array=(df[CCU_Concrete_Constants.CCU_Cement_UB].tolist())
    
    CCU_coarse_agg_LB_array=(df[CCU_Concrete_Constants.CCU_Coarse_Aggregate_LB].tolist())
    CCU_coarse_agg_UB_array=(df[CCU_Concrete_Constants.CCU_Coarse_Aggregate_UB].tolist())
    
    CCU_fine_agg_LB_array=(df[CCU_Concrete_Constants.CCU_Fine_Aggregate_LB].tolist())
    CCU_fine_agg_UB_array=(df[CCU_Concrete_Constants.CCU_Fine_Aggregate_UB].tolist())
    
    CCU_water_LB_array=(df[CCU_Concrete_Constants.CCU_Water_LB].tolist())
    CCU_water_UB_array=(df[CCU_Concrete_Constants.CCU_Water_UB].tolist())
    
    CCU_SCM_Slag_LB_array=(df[CCU_Concrete_Constants.CCU_SCM_Slag_LB].tolist())
    CCU_SCM_Slag_UB_array=(df[CCU_Concrete_Constants.CCU_SCM_Slag_UB].tolist())
    
    CCU_SCM_Fly_Ash_LB_array=(df[CCU_Concrete_Constants.CCU_SCM_Fly_Ash_LB].tolist())
    CCU_SCM_Fly_Ash_UB_array=(df[CCU_Concrete_Constants.CCU_SCM_Fly_Ash_UB].tolist())
    
    CCU_CO2_absorbed_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Absorbed_LB].tolist())
    CCU_CO2_absorbed_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Absorbed_UB].tolist())
    
    Baseline_CO2_Steam_Curing_LB_array=(df[CCU_Concrete_Constants.Baseline_CO2_Steam_Curing_LB].tolist())
    Baseline_CO2_Steam_Curing_UB_array=(df[CCU_Concrete_Constants.Baseline_CO2_Steam_Curing_UB].tolist())
    
    CCU_CO2_Steam_Curing_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Steam_Curing_LB].tolist())
    CCU_CO2_Steam_Curing_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Steam_Curing_UB].tolist())
    
    CCU_CO2_Curing_Hours_LB_array=(df[CCU_Concrete_Constants.CCU_CO2_Curing_Hours_LB].tolist())
    CCU_CO2_Curing_Hours_UB_array=(df[CCU_Concrete_Constants.CCU_CO2_Curing_Hours_UB].tolist())
    
    CCU_Injection_Electricity=CCU_Concrete_Constants.CCU_Injection_Electricity
    CCU_Liquefaction_Electricity=CCU_Concrete_Constants.CCU_Liquefaction_Electricity
    CCU_Vaporization_Electricity=CCU_Concrete_Constants.CCU_Vaporization_Electricity
#    CO2_Compression_Elec_Requirement_LB=CCU_Concrete_Constants.CO2_Compression_Elec_Requirement_LB
#    CO2_Compression_Elec_Requirement_UB=CCU_Concrete_Constants.CO2_Compression_Elec_Requirement_UB
    Power_Required_CO2_Curing=CCU_Concrete_Constants.Power_Required_CO2_Curing
    Heat_to_electricity_LB=CCU_Concrete_Constants.Heat_to_electricity_LB
    Heat_to_electricity_UB=CCU_Concrete_Constants.Heat_to_electricity_UB

    
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
    
#    Transportation_CO2_Electricity_CO2_intensity_LB=CCU_Concrete_Constants.Transportation_CO2_Electricity_CO2_intensity_LB
#    Transportation_CO2_Electricity_CO2_intensity_UB=CCU_Concrete_Constants.Transportation_CO2_Electricity_CO2_intensity_UB
#    Transportation_CO2_Electricity_CO2_intensity=np.random.uniform(Transportation_CO2_Electricity_CO2_intensity_LB,Transportation_CO2_Electricity_CO2_intensity_UB,number_of_samples)
#    Transportation_CO2_Electricity_Requirement=CCU_Concrete_Constants.Transportation_CO2_Electricity_Requirement

    External_Compensation_Power_Plant_CO2_intensity_LB=CCU_Concrete_Constants.External_Compensation_Power_Plant_CO2_intensity_LB
    External_Compensation_Power_Plant_CO2_intensity_UB=CCU_Concrete_Constants.External_Compensation_Power_Plant_CO2_intensity_UB
    External_Power_Plant_CO2_intensity=np.random.uniform(External_Compensation_Power_Plant_CO2_intensity_LB,External_Compensation_Power_Plant_CO2_intensity_UB,number_of_samples)
    
    CCU_CO2_Curing_Elec_CO2_intensity_LB = CCU_Concrete_Constants.CCU_CO2_Curing_Elec_CO2_intensity_LB
    CCU_CO2_Curing_Elec_CO2_intensity_UB = CCU_Concrete_Constants.CCU_CO2_Curing_Elec_CO2_intensity_UB
    CCU_CO2_Curing_CO2_intensity_array=np.random.uniform(CCU_CO2_Curing_Elec_CO2_intensity_LB,CCU_CO2_Curing_Elec_CO2_intensity_UB,number_of_samples)
    
    CCU_Injection_Elec_CO2_Intensity_LB = CCU_Concrete_Constants.CCU_Injection_Elec_CO2_Intensity_LB
    CCU_Injection_Elec_CO2_Intensity_UB = CCU_Concrete_Constants.CCU_Injection_Elec_CO2_Intensity_UB
    CCU_Injection_Elec_CO2_Intensity_array=np.random.uniform(CCU_Injection_Elec_CO2_Intensity_LB,CCU_Injection_Elec_CO2_Intensity_UB,number_of_samples)
    
    CCU_Liquefaction_Elec_CO2_Intensity_LB = CCU_Concrete_Constants.CCU_Liquefaction_Elec_CO2_Intensity_LB
    CCU_Liquefaction_Elec_CO2_Intensity_UB = CCU_Concrete_Constants.CCU_Liquefaction_Elec_CO2_Intensity_UB
    CCU_Liquefaction_Elec_CO2_Intensity_array=np.random.uniform(CCU_Liquefaction_Elec_CO2_Intensity_LB,CCU_Liquefaction_Elec_CO2_Intensity_UB,number_of_samples)
    
    CCU_Vaporization_Elec_CO2_Intensity_LB = CCU_Concrete_Constants.CCU_Vaporization_Elec_CO2_Intensity_LB
    CCU_Vaporization_Elec_CO2_Intensity_UB = CCU_Concrete_Constants.CCU_Vaporization_Elec_CO2_Intensity_UB
    CCU_Vaporization_Elec_CO2_Intensity_array=np.random.uniform(CCU_Vaporization_Elec_CO2_Intensity_LB,CCU_Vaporization_Elec_CO2_Intensity_UB,number_of_samples)
    
#    CO2_Transportation_Distance_LB=CCU_Concrete_Constants.CO2_Transportation_Distance_LB
#    CO2_Transportation_Distance_UB=CCU_Concrete_Constants.CO2_Transportation_Distance_UB
#    CO2_Transportation_Distance_array=np.random.uniform(CO2_Transportation_Distance_LB,CO2_Transportation_Distance_UB,number_of_samples)
    
    MEA_CO2_intensity_mean=CCU_Concrete_Constants.MEA_CO2_intensity_mean
    MEA_CO2_intensity_sd=CCU_Concrete_Constants.MEA_CO2_intensity_sd
    m1 = math.log((MEA_CO2_intensity_mean**2)/math.sqrt(MEA_CO2_intensity_sd**2+MEA_CO2_intensity_mean**2))
    sd1= math.sqrt(math.log(MEA_CO2_intensity_sd**2/(MEA_CO2_intensity_mean**2)+1))
    MEA_CO2_intensity=np.random.lognormal(m1, sd1, number_of_samples)
    
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
    
    CO2_absorbed_during_mixing_LB=CCU_Concrete_Constants.CO2_absorbed_during_mixing_LB
    CO2_absorbed_during_mixing_UB=CCU_Concrete_Constants.CO2_absorbed_during_mixing_UB
    CO2_absorbed_during_mixing_array=np.random.uniform(CO2_absorbed_during_mixing_LB,CO2_absorbed_during_mixing_UB,number_of_samples)
    
    Baseline_cement_array = np.random.uniform(Baseline_cement_LB_array[i],Baseline_cement_UB_array[i],number_of_samples)
    Baseline_cement_CO2_array_array = cement_CO2_intensity*Baseline_cement_array
 
    Baseline_coarse_agg_array=np.random.uniform(Baseline_coarse_agg_LB_array[i],Baseline_coarse_agg_UB_array[i],number_of_samples)
    Baseline_coarse_agg_CO2_array_array = coarse_agg_CO2_intensity*Baseline_coarse_agg_array
    
    Baseline_fine_agg_array = np.random.uniform(Baseline_fine_agg_LB_array[i],Baseline_fine_agg_UB_array[i],number_of_samples)
    Baseline_fine_agg_CO2_array_array = fine_agg_CO2_intensity*Baseline_fine_agg_array
   
    Baseline_water_array = np.random.uniform(Baseline_water_LB_array[i],Baseline_water_UB_array[i],number_of_samples)
    Baseline_water_CO2_array_array = water_CO2_intensity*Baseline_water_array

    CO2_Transportation_Distance_LB=CCU_Concrete_Constants.CO2_Transportation_Distance_LB
    CO2_Transportation_Distance_UB=CCU_Concrete_Constants.CO2_Transportation_Distance_UB
    CO2_Transportation_Distance_array=np.random.uniform(CO2_Transportation_Distance_LB,CO2_Transportation_Distance_UB,number_of_samples)
    
    Pig_Iron_CO2_intensity_mean=CCU_Concrete_Constants.Pig_Iron_CO2_intensity_mean
    Pig_Iron_CO2_intensity_sd=CCU_Concrete_Constants.Pig_Iron_CO2_intensity_sd
    m1 = math.log((Pig_Iron_CO2_intensity_mean**2)/math.sqrt(Pig_Iron_CO2_intensity_sd**2+Pig_Iron_CO2_intensity_mean**2))
    sd1= math.sqrt(math.log(Pig_Iron_CO2_intensity_sd**2/(Pig_Iron_CO2_intensity_mean**2)+1))
    SCM_Slag_CO2_intensity=Slag_Allocation_Factor*7.7*np.random.lognormal(m1, sd1, number_of_samples)
    
    SCM_Slag_road_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_slag
    SCM_Slag_road_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_slag
    SCM_Slag_road_transport_distance_array=np.random.uniform(SCM_Slag_road_transport_distance_LB,SCM_Slag_road_transport_distance_UB,number_of_samples)
    
    SCM_Slag_rail_transport_distance_LB=CCU_Concrete_Constants.SCM_rail_transport_distance_LB_slag
    SCM_Slag_rail_transport_distance_UB=CCU_Concrete_Constants.SCM_rail_transport_distance_UB_slag
    SCM_Slag_rail_transport_distance_array=np.random.uniform(SCM_Slag_rail_transport_distance_LB,SCM_Slag_rail_transport_distance_UB,number_of_samples)
    
    SCM_Slag_ocean_transport_distance_LB=CCU_Concrete_Constants.SCM_ocean_transport_distance_LB_slag
    SCM_Slag_ocean_transport_distance_UB=CCU_Concrete_Constants.SCM_ocean_transport_distance_UB_slag
    SCM_Slag_ocean_transport_distance_array=np.random.uniform(SCM_Slag_ocean_transport_distance_LB,SCM_Slag_ocean_transport_distance_UB,number_of_samples)
    
    SCM_Slag_barge_transport_distance_LB=CCU_Concrete_Constants.SCM_barge_transport_distance_LB_slag
    SCM_Slag_barge_transport_distance_UB=CCU_Concrete_Constants.SCM_barge_transport_distance_UB_slag
    SCM_Slag_barge_transport_distance_array=np.random.uniform(SCM_Slag_barge_transport_distance_LB,SCM_Slag_barge_transport_distance_UB,number_of_samples)
    
    #Case when SCM type is fly ash, which is a by product of the coal industry
    Coal_Elec_CO2_intensity_mean=CCU_Concrete_Constants.Coal_Elec_CO2_intensity_mean
    Coal_Elec_CO2_intensity_sd=CCU_Concrete_Constants.Coal_Elec_CO2_intensity_sd
    m1 = math.log((Coal_Elec_CO2_intensity_mean**2)/math.sqrt(Coal_Elec_CO2_intensity_sd**2+Coal_Elec_CO2_intensity_mean**2))
    sd1= math.sqrt(math.log(Coal_Elec_CO2_intensity_sd**2/(Coal_Elec_CO2_intensity_mean**2)+1))
    SCM_Fly_Ash_CO2_intensity=Fly_Ash_Allocation_Factor*22.7*np.random.lognormal(m1, sd1, number_of_samples)

    
    SCM_Fly_Ash_road_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
    SCM_Fly_Ash_road_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
    SCM_Fly_Ash_road_transport_distance_array=np.random.uniform(SCM_Fly_Ash_road_transport_distance_LB,SCM_Fly_Ash_road_transport_distance_UB,number_of_samples)
    
    SCM_Fly_Ash_rail_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
    SCM_Fly_Ash_rail_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
    SCM_Fly_Ash_rail_transport_distance_array=np.random.uniform(SCM_Fly_Ash_rail_transport_distance_LB,SCM_Fly_Ash_rail_transport_distance_UB,number_of_samples)
    
    SCM_Fly_Ash_ocean_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
    SCM_Fly_Ash_ocean_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
    SCM_Fly_Ash_ocean_transport_distance_array=np.random.uniform(SCM_Fly_Ash_ocean_transport_distance_LB,SCM_Fly_Ash_ocean_transport_distance_UB,number_of_samples)
    
    SCM_Fly_Ash_barge_transport_distance_LB=CCU_Concrete_Constants.SCM_road_transport_distance_LB_fly_ash
    SCM_Fly_Ash_barge_transport_distance_UB=CCU_Concrete_Constants.SCM_road_transport_distance_UB_fly_ash
    SCM_Fly_Ash_barge_transport_distance_array=np.random.uniform(SCM_Fly_Ash_barge_transport_distance_LB,SCM_Fly_Ash_barge_transport_distance_UB,number_of_samples)
 
    Baseline_SCM_Slag_array = np.random.uniform(Baseline_SCM_Slag_LB_array[i],Baseline_SCM_Slag_UB_array[i],number_of_samples)
    Baseline_SCM_Slag_CO2_array_array = SCM_Slag_CO2_intensity*Baseline_SCM_Slag_array
    
    Baseline_SCM_Fly_Ash_array = np.random.uniform(Baseline_SCM_Fly_Ash_LB_array[i],Baseline_SCM_Fly_Ash_UB_array[i],number_of_samples)
    Baseline_SCM_Fly_Ash_CO2_array_array = SCM_Fly_Ash_CO2_intensity*Baseline_SCM_Fly_Ash_array     
    
    #CO2 captured in the CCU scenario is assumed to be released in the baseline scenario
    #as the power plant is operating without carbon capture
#    Baseline_CO2_Not_captured_array_array = CCU_CO2_captured_array
#    Baseline_CO2_Power_Plant_array_array=Baseline_CO2_Not_captured_array_array
    Baseline_CO2_Steam_Curing_array_array=np.random.uniform(Baseline_CO2_Steam_Curing_LB_array[i],Baseline_CO2_Steam_Curing_UB_array[i],number_of_samples)

    Baseline_Material_Transportation_CO2_array_array=\
    (cement_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_water_array)+\
    (SCM_Slag_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_SCM_Slag_array)+\
    (SCM_Fly_Ash_road_transport_distance_array*Transportation_road_CO2_Intensity*Baseline_SCM_Fly_Ash_array)+\
    (cement_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_water_array)+\
    (SCM_Slag_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_SCM_Slag_array)+\
    (SCM_Fly_Ash_rail_transport_distance_array*Transportation_rail_CO2_Intensity*Baseline_SCM_Fly_Ash_array)+\
    (cement_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_water_array)+\
    (SCM_Slag_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_SCM_Slag_array)+\
    (SCM_Fly_Ash_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*Baseline_SCM_Fly_Ash_array)+\
    (cement_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_cement_array)+\
    (coarse_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_coarse_agg_array)+\
    (fine_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_fine_agg_array)+\
    (water_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_water_array)+\
    (SCM_Slag_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_SCM_Slag_array)+\
    (SCM_Fly_Ash_barge_transport_distance_array*Transportation_barge_CO2_Intensity*Baseline_SCM_Fly_Ash_array)
      
    CCU_cement_array = np.random.uniform(CCU_cement_LB_array[i],CCU_cement_UB_array[i],number_of_samples)
    CCU_coarse_agg_array = np.random.uniform(CCU_coarse_agg_LB_array[i],CCU_coarse_agg_UB_array[i],number_of_samples)
    CCU_fine_agg_array = np.random.uniform(CCU_fine_agg_LB_array[i],CCU_fine_agg_UB_array[i],number_of_samples)
    CCU_water_array = np.random.uniform(CCU_water_LB_array[i],CCU_water_UB_array[i],number_of_samples)
#    CCU_SCM_array = np.random.uniform(CCU_SCM_LB_array[i],CCU_SCM_UB_array[i],number_of_samples)

    CCU_CO2_captured_array = CCU_cement_array*np.random.uniform(CCU_CO2_absorbed_LB_array[i],CCU_CO2_absorbed_UB_array[i],number_of_samples)

    
    CCU_cement_array = np.random.uniform(CCU_cement_LB_array[i],CCU_cement_UB_array[i],number_of_samples)
    CCU_coarse_agg_array = np.random.uniform(CCU_coarse_agg_LB_array[i],CCU_coarse_agg_UB_array[i],number_of_samples)
    CCU_fine_agg_array = np.random.uniform(CCU_fine_agg_LB_array[i],CCU_fine_agg_UB_array[i],number_of_samples)
    CCU_water_array = np.random.uniform(CCU_water_LB_array[i],CCU_water_UB_array[i],number_of_samples)
    CCU_SCM_Slag_array = np.random.uniform(CCU_SCM_Slag_LB_array[i],CCU_SCM_Slag_UB_array[i],number_of_samples)
    CCU_SCM_Fly_Ash_array = np.random.uniform(CCU_SCM_Fly_Ash_LB_array[i],CCU_SCM_Fly_Ash_UB_array[i],number_of_samples)
    CO2_Capture_Heat_Requirement_array=np.random.uniform(CO2_Capture_Heat_Requirement_LB,CO2_Capture_Heat_Requirement_UB,number_of_samples)
    CO2_Capture_Elec_Requirement_array= np.random.uniform(CO2_Capture_Elec_Requirement_LB,CO2_Capture_Elec_Requirement_UB,number_of_samples)
#    CO2_Compression_Elec_Requirement_array= np.random.uniform(CO2_Compression_Elec_Requirement_LB,CO2_Compression_Elec_Requirement_UB,number_of_samples)
    CCU_CO2_Curing_Hours_array=np.random.uniform(CCU_CO2_Curing_Hours_LB_array[i],CCU_CO2_Curing_Hours_UB_array[i],number_of_samples)
    Heat_to_electricity_array=np.random.uniform(Heat_to_electricity_LB, Heat_to_electricity_UB,number_of_samples)
    CCU_cement_CO2_array_array = cement_CO2_intensity*CCU_cement_array
    CCU_coarse_agg_CO2_array_array = coarse_agg_CO2_intensity*CCU_coarse_agg_array
    CCU_fine_agg_CO2_array_array = fine_agg_CO2_intensity*CCU_fine_agg_array
    CCU_water_CO2_array_array = water_CO2_intensity*CCU_water_array
    CCU_SCM_Slag_CO2_array_array = SCM_Slag_CO2_intensity*CCU_SCM_Slag_array
    CCU_SCM_Fly_Ash_CO2_array_array = SCM_Fly_Ash_CO2_intensity*CCU_SCM_Fly_Ash_array
    CCU_CO2_Not_captured_array_array = CCU_CO2_captured_array/9
    
    #CO2 released during mixing is zero for curing datasets (0 to 69)
    if (i< (CCU_Concrete_Constants.Number_of_Category1_Studies+CCU_Concrete_Constants.Number_of_Category2_Studies)):
        CO2_released_during_mixing_array=0
    #CO2 released during mixing is not zero for mixing datasets (70 to 98)
    else:
        CO2_released_during_mixing_array = 1-CO2_absorbed_during_mixing_array

    CCU_CO2_Injection_Electricity_array_array=(CCU_Injection_Elec_CO2_Intensity_array*CCU_Injection_Electricity*CCU_CO2_captured_array)+\
                                              (CO2_released_during_mixing_array*CCU_CO2_captured_array)
                                              
    CCU_CO2_Liquefaction_Electricity_array_array=CCU_Liquefaction_Elec_CO2_Intensity_array*CCU_Liquefaction_Electricity*CCU_CO2_captured_array
    CCU_CO2_Vaporization_Electricity_CO2_array_array = CCU_Vaporization_Elec_CO2_Intensity_array*CCU_Vaporization_Electricity*CCU_CO2_captured_array
#    CCU_CO2_Transportation_CO2_array_array=Transportation_CO2_Electricity_CO2_intensity*Transportation_CO2_Electricity_Requirement*CCU_CO2_captured_array
    
    #Multiple by 1.4 to to account for onward trip with  CO2 load. The extra 40% accounts for tare weight. Refer SI Section 3
    #Multiple by 0.4 to to account for return trip with no CO2 load. Refer SI Section 3
    CCU_CO2_Transportation_CO2_array_array=(CO2_Transportation_Distance_array*Transportation_road_CO2_Intensity*CCU_CO2_captured_array*1.4)\
                                          +(CO2_Transportation_Distance_array*Transportation_road_CO2_Intensity*CCU_CO2_captured_array*0.4)
       
    CCU_Material_Transportation_CO2_array_array=\
    (cement_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_fine_agg_array)+\
    (water_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_water_array)+\
    (SCM_Slag_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_SCM_Slag_array)+\
    (SCM_Fly_Ash_road_transport_distance_array*Transportation_road_CO2_Intensity*CCU_SCM_Fly_Ash_array)+\
    (cement_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_fine_agg_array)+\
    (water_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_water_array)+\
    (SCM_Slag_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_SCM_Slag_array)+\
    (SCM_Fly_Ash_rail_transport_distance_array*Transportation_rail_CO2_Intensity*CCU_SCM_Fly_Ash_array)+\
    (cement_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_fine_agg_array)+\
    (water_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_water_array)+\
    (SCM_Slag_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_SCM_Slag_array)+\
    (SCM_Fly_Ash_ocean_transport_distance_array*Transportation_ocean_CO2_Intensity*CCU_SCM_Fly_Ash_array)+\
    (cement_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_cement_array)+\
    (coarse_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_coarse_agg_array)+\
    (fine_agg_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_fine_agg_array)+\
    (water_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_water_array)+\
    (SCM_Slag_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_SCM_Slag_array)+\
    (SCM_Fly_Ash_barge_transport_distance_array*Transportation_barge_CO2_Intensity*CCU_SCM_Fly_Ash_array)

    CCU_CO2_Capture_Total_Electricity_Penalty_CO2_array_array = ((External_Power_Plant_CO2_intensity*Heat_to_electricity_array*0.277*CO2_Capture_Heat_Requirement_array*CCU_CO2_captured_array)\
    +(External_Power_Plant_CO2_intensity*CO2_Capture_Elec_Requirement_array*CCU_CO2_captured_array))
#    +(External_Power_Plant_CO2_intensity*CO2_Compression_Elec_Requirement_array*CCU_CO2_captured_array))

    CCU_CO2_capture_MEA_array_array = MEA_CO2_intensity*CCU_CO2_captured_array

    CCU_CO2_Curing_CO2_array_array = CCU_CO2_Curing_CO2_intensity_array*CCU_CO2_Curing_Hours_array*Power_Required_CO2_Curing
    CCU_CO2_Steam_Curing_array_array=np.random.uniform(CCU_CO2_Steam_Curing_LB_array[i],CCU_CO2_Steam_Curing_UB_array[i],number_of_samples)

    CCU_CO2_Power_Plant_array_array=CCU_CO2_Capture_Total_Electricity_Penalty_CO2_array_array+CCU_CO2_Liquefaction_Electricity_array_array+\
    CCU_CO2_Not_captured_array_array
    
    CCU_process_emissions_array_array= np.zeros((number_of_samples,number_of_parameters))
    CCU_process_emissions_array_array[:,0]=CCU_cement_CO2_array_array
    CCU_process_emissions_array_array[:,1]=CCU_coarse_agg_CO2_array_array 
    CCU_process_emissions_array_array[:,2]=CCU_fine_agg_CO2_array_array 
    CCU_process_emissions_array_array[:,3]=CCU_water_CO2_array_array 
    #When CO2 is sourced from a coal plant scenario, there is a 90% capture of CO2.
    #As a result, we multiply the CO2 intensity of fly ash by 0.1
    if(CO2_Capture_Source==CCU_Concrete_Constants.Coal_Power_Plant):
        CCU_process_emissions_array_array[:,4]=CCU_SCM_Slag_CO2_array_array+(0.1*CCU_SCM_Fly_Ash_CO2_array_array)
    if(CO2_Capture_Source==CCU_Concrete_Constants.NGCC_Power_Plant):
        CCU_process_emissions_array_array[:,4]=CCU_SCM_Slag_CO2_array_array+(CCU_SCM_Fly_Ash_CO2_array_array)
    CCU_process_emissions_array_array[:,5]=CCU_Material_Transportation_CO2_array_array
    CCU_process_emissions_array_array[:,6]=CCU_CO2_capture_MEA_array_array
    CCU_process_emissions_array_array[:,7]=CCU_CO2_Power_Plant_array_array
    CCU_process_emissions_array_array[:,8]=CCU_CO2_Transportation_CO2_array_array
    CCU_process_emissions_array_array[:,9]=CCU_CO2_Vaporization_Electricity_CO2_array_array
    CCU_process_emissions_array_array[:,10]=CCU_CO2_Injection_Electricity_array_array
    CCU_process_emissions_array_array[:,11]=CCU_CO2_Curing_CO2_array_array
    CCU_process_emissions_array_array[:,12]=CCU_CO2_Steam_Curing_array_array
    
    
    CCU_Electricity_Penalty_array_array = \
    ((Heat_to_electricity_array*0.277*CO2_Capture_Heat_Requirement_array*CCU_CO2_captured_array)\
    +(CO2_Capture_Elec_Requirement_array*CCU_CO2_captured_array))
#    +(CO2_Compression_Elec_Requirement_array*CCU_CO2_captured_array))
    
    Baseline_CO2_Power_Plant_array_array=CCU_Electricity_Penalty_array_array*Power_Plant_CO2_Intensity_array_array
    
    Baseline_process_emissions_array_array= np.zeros((number_of_samples,number_of_parameters))
    Baseline_process_emissions_array_array[:,0]=Baseline_cement_CO2_array_array
    Baseline_process_emissions_array_array[:,1]=Baseline_coarse_agg_CO2_array_array
    Baseline_process_emissions_array_array[:,2]=Baseline_fine_agg_CO2_array_array
    Baseline_process_emissions_array_array[:,3]=Baseline_water_CO2_array_array
    Baseline_process_emissions_array_array[:,4]=Baseline_SCM_Slag_CO2_array_array+Baseline_SCM_Fly_Ash_CO2_array_array
    Baseline_process_emissions_array_array[:,5]=Baseline_Material_Transportation_CO2_array_array
    Baseline_process_emissions_array_array[:,6]=np.zeros(number_of_samples)
    Baseline_process_emissions_array_array[:,7]=Baseline_CO2_Power_Plant_array_array
    Baseline_process_emissions_array_array[:,8]=np.zeros(number_of_samples)
    Baseline_process_emissions_array_array[:,9]=np.zeros(number_of_samples)
    Baseline_process_emissions_array_array[:,10]=np.zeros(number_of_samples)
    Baseline_process_emissions_array_array[:,11]=np.zeros(number_of_samples)
    Baseline_process_emissions_array_array[:,12]=Baseline_CO2_Steam_Curing_array_array
    
    Delta_process_emissions_array_array= np.zeros((number_of_samples,number_of_parameters))
    Delta_process_emissions_array_array=Baseline_process_emissions_array_array-CCU_process_emissions_array_array
    
    return Delta_process_emissions_array_array, Baseline_process_emissions_array_array, CCU_process_emissions_array_array
