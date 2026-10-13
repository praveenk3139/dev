import numpy as np
import pandas as pd
hafeez = ['Hafeez', 19]
aslam = ['Aslam', 21]
kareem = ['Kareem', 18]
dataframe = pd.DataFrame([hafeez, aslam, kareem], columns=['Name', 'Age'])
print(dataframe)