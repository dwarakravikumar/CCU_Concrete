-----
ABOUT
-----

The CCU_Concrete code repository accompanies the manuscript titled "Carbon dioxide utilization in concrete production may or may not produce a climate benefit" authored by Dr. Dwarakanath Ravikumar, Dr. Duo Zhang, Dr. Gregory Keoleian, Dr. Shelie Miller, Dr. Volker Sick and Dr. Victor Li from the University of Michigan, Ann Arbor, USA.

The code is used to determine the net CO2 benefit from carbon, capture and utilization for concrete production (CCU concrete). The net CO2 benefit is defined as the difference between the life cycle CO2 emissions from producing conventional and CCU concrete. In addition, the code is used to determine the key processes contributing to the net CO2 benefit of CCU concrete.

------------------------------
AUTHORSHIP AND CONTACT DETAILS
------------------------------

The code was authored by Dr. Dwarakanath Ravikumar who can be contacted at dtriplic@umich.edu

------------------
REPOSITORY DETAILS
------------------

The repository consists of 11 files, which should be placed in the same folder.

1. CCU_Concrete_Constants.py: This python file contains the constants required to conduct the histogram (Figure 3 manuscript), scatter plot (Figure 4 manuscript) and delta indices analysis (Figure 5 manuscript).

2. Dataset.xlsx: This file contains the life cycle inventory material and energy data for conventional and CCU concrete for 99 datasets, which were obtained from a literature review. 

3. CCU_Concrete_Histogram_SE.py, CCU_Concrete_Histogram_EA.py and CCU_Concrete_Histogram_MA.py: These three python files plot the histogram of the net CO2 benefit of CCU concrete (Figure 3 manuscript). The histogram analysis is conducted for the 99 datasets. 
"SE", "EA" and "MA" in the file name corresponds to the use of system boundary expansion, economic value and mass-based allocation, respectively to determine the CO2 impact of fly ash and steel slag, which are used as supplementary cementitious materials.

4. CCU_Concrete_Scatter_Plot_SE.py, CCU_Concrete_Scatter_Plot_EA.py and CCU_Concrete_Scatter_Plot_MA.py: These three python files generate a scatter plot of the net CO2 benefit of CCU concrete on the y-axis and the difference in the CO2 emissions of the 13 processes required to produce conventional and CCU concrete (Figure 4 manuscript). The scatter plot analysis is conducted for the 99 datasets.
"SE", "EA" and "MA" in the file name corresponds to the use of system boundary expansion, economic value and mass-based allocation, respectively to determine the CO2 impact of fly ash and steel slag, which are used as supplementary cementitious materials.

5. CCU_Concrete_Delta_Indices_SE.py, CCU_Concrete_Delta_Indices_EA.py and CCU_Concrete_Delta_Indices_MA.py: These three python files conduct a moment independent sensitivity analysis to determine the delta index for each of the 13 processes required to produce conventional and CCU concrete (Figure 5 manuscript). The net CO2 benefit of CCU concrete is most sensitive to the process with the highest delta index value. The moment independent sensitivity analysis is conducted for the 99 datasets.
"SE", "EA" and "MA" in the file name corresponds to the use of system boundary expansion, economic value and mass-based allocation, respectively to determine the CO2 impact of fly ash and steel slag, which are used as supplementary cementitious materials.



