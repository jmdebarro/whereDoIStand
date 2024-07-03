# import xport
# import pandas as pd

# # Load the XPT file
# with open('P_DEMO.xpt', 'rb') as file:
#     data = xport.to_dataframe(file)

# # Save to CSV
# data.to_csv('cdc.csv', index=False)

# import pyreadstat
# import pandas as pd

# # Read the XPT file
# df, meta = pyreadstat.read_xport('example.xpt')

# # Save to CSV
# df.to_csv('example.csv', index=False)

import xport 

import pandas as pd 

df = pd.read_sas("(\Users\jmdeb\OneDrive\Desktop\projects\statCalc/P_DEMO.XPT)")

df = pd.read_sas("\Users\jmdeb\OneDrive\Desktop\projects\statCalc" + "P_DEMO" + '.XPT', index=None)

df.to_csv("\Users\jmdeb\OneDrive\Desktop\projects\statCalc" + "P_DEMO" + '.csv')