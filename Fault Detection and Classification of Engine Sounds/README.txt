Fault Detection and Classification of Engine Sounds - Code Files
By Elizabeth Sales
Date Completed: 27/04/2024
------
README includes a user manual, links to the used datasets for this project, and the package requirements.

------
User Manual:
The following list is a set of instructions for downloading and executing the implemented code from the Fault Detection and Classification of Engine Sounds project. 

1. Download the ZIP folder and extract all files. There should be 11 total files: 7 Python files, 3 MATLAB code files and one text file.
2. Download each of the datasets from the respective websites using the links in the README.txt file. 
3. Download and run the Orion Anomaly Pipeline scripts on the CWRU dataset. The pipeline is also linked in the README.txt file and has its own set of instructions for use.
4. Run importNPY.py on the HIT dataset. The “File Directory” string must be changed to the location of the NumPy file to be converted. 
5. Run each MATLAB script. Manual adjustments to each one are required as the file directories and number of files must be changed. 
6. Extract all necessary files according to Table 9.
7. Change all file directories in the directories.py and experiments.py scripts.
8. Run the mainImplementation.py file. Change the exp_num variable based on the experiments list before every experiment is run. 

------
Dataset Links:
CWRU Dataset: https://engineering.case.edu/bearingdatacenter/download-data-file
HIT Dataset: https://drive.google.com/drive/folders/1Km1Go4ilB_bI033SBJ7eJ0uCzbqEqbgt
XJTU-SY Dataset: https://drive.google.com/drive/folders/1_ycmG46PARiykt82ShfnFfyQsaXv3_VK

orion_anomaly_pipeline: https://github.com/SebiChesh/orion_anomaly_pipeline/tree/main/orion_anomaly_pipeline

------
Package Requirements:
Python = 3.11.8
MATLAB = R2023b

keras=3.1.1
matplotlib=3.8.0
numpy=1.26.4
opencv=4.9.0.80
pandas=2.2.1
pillow=10.2.0
tensorflow=2.16.1