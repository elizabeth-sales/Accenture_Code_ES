import numpy as np
import pandas as pd

#Import the .npy files from downloaded dataset
data = np.load("File Directory")

#Iterate through file and convert each series to a CSV file
for i in range(0, series_size):
    df = pd.DataFrame(data[i])
    dfT = np.transpose(df)
    title = "New File Directory" + str(i) + ".csv"
    dfT.to_csv(title, index=False)

