The CCU_Concrete code repository accompanies the manuscript titled “Carbon dioxide utilization in concrete curing or mixing might not produce a climate benefit” authored by Dr. Dwarakanath Ravikumar, Dr. Duo Zhang, Dr. Gregory Keoleian, Dr. Shelie Miller, Dr. Volker Sick and Dr. Victor Li from the University of Michigan, Ann Arbor, USA.

The code is used to determine the net CO2 benefit from carbon, capture and utilization for concrete production (CCU concrete). The net CO2 benefit is defined as the difference between the life cycle CO2 emissions from producing conventional and CCU concrete. In addition, the code is used to determine the key processes contributing to the net CO2 benefit of CCU concrete.

The code was authored by Dr. Dwarakanath Ravikumar who can be contacted at dtriplic@umich.edu

The repository consists of 6 files, which should be placed in the same folder.

1.	CCU_Concrete_Constants.py: This python file contains the constants required to conduct the histogram (Figure 3 manuscript), scatter plot (Figure 4 manuscript) and delta indices analysis (Figure 5 manuscript).

2.	Dataset.xlsx: This file contains the life cycle inventory material and energy data for conventional and CCU concrete across 99 datasets, which were obtained from a literature review. 

3.	CCU_Concrete_Histogram.py: This python file plots the histogram of the net CO2 benefit of CCU concrete (Figure 3 manuscript). The histogram analysis is conducted for the 99 datasets. Set the ‘Allocation_Type’ parameter in the ‘CCU_Concrete_Constants.py’ file to 'System Boundary Expansion', 'Mass Allocation' or 'Economic Allocation' to determine the net CO2 benefit histogram with system boundary expansion, economic value and mass-based allocation, respectively.

4.	CCU_Concrete_Scatter_Plot.py: This python file generates a scatter plot of the net CO2 benefit of CCU concrete on the y-axis and the difference in the CO2 emissions of the 13 processes required to produce conventional and CCU concrete (Figure 4 manuscript). The scatter plot analysis is conducted for the 99 datasets. Set the ‘Allocation_Type’ parameter in the ‘CCU_Concrete_Constants.py’ file to 'System Boundary Expansion', 'Mass Allocation' or 'Economic Allocation' to determine the scatter plot with system boundary expansion, mass or economic value allocation, respectively.

5.	CCU_Concrete_Delta_Indices.py: This python file conducts a moment independent sensitivity analysis to determine the delta index for each of the 13 processes required to produce conventional and CCU concrete (Figure 5 manuscript). The net CO2 benefit of CCU concrete is most sensitive to the process with the highest delta index value. The moment independent sensitivity analysis is conducted for the 99 datasets. Set the ‘Allocation_Type’ parameter in the ‘CCU_Concrete_Constants.py’ file to 'System Boundary Expansion', 'Mass Allocation' or 'Economic Allocation' to determine the delta indices with system boundary expansion, mass or economic value allocation, respectively.

6.	CCU_Concrete_Functions.py: This python file contains the functions used in generating the Histogram, Scatter plot and delta indices plot.





