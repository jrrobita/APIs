import requests
import matplotlib 

#website with info on connecting to sc api:
#https://towardsdatascience.com/how-to-collect-data-from-statistics-canada-using-python-db8a81ce6475/

#can use the stats-can fn to connet to sc web api
#info on that package:
#https://stats-can.readthedocs.io/en/latest/index.html#

import stats_can

#create a df for the selected vector of the selected table

#vectors to df fn structure:
#df = stats_can.sc.vectors_to_df(vectors, periods = n, start_release_date = None, end_release_date = None)
#table selcted: housing economics accounts
#https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=3610067701

df = stats_can.sc.vectors_to_df("v1478190138", periods=5)

df.head()

#can first create a vector map to select and assign name to various vectors from one table

#eco_vec_map = {'CPI':'v41690973',
#               'Exchange_Rate_USD':'v111666275',
#               'GDP':'v65201210',
#               'Unemployment_Rate':'v91506256',
#               'TSX':'v122620'}

#vectors = list(eco_vec_map.values())
#df1 = stats_can.sc.vectors_to_df(vectors, periods = 36)
#df1.head()

#then rename columns using initial defintion

#inv_map = {v: k for k, v in eco_vec_map.items()}
#df1.columns = df1.columns.to_series().map(inv_map)
#df1.index.names = ['Date']


housing_invest_map = {'General_Gov': 'v1478190138',
                       'Non_Profit': 'v1478190168',
                       'Households': 'v1478190153',
                       'Financial_Corps':'v1478140909',
                       'Other_Corps': 'v1478134429'
                       }



vectors = list(housing_invest_map.values())
df1 = stats_can.sc.vectors_to_df(vectors, periods = 8)
df1.head()

#then rename columns using initial defintion
inv_map = {v: k for k, v in housing_invest_map.items()}

inv_map
df1.columns = df1.columns.to_series().map(inv_map)
df1.index.names = ['Date']

df1.head()

#use the collected data to create vizulations

df1.plot(subplots = True, figsize = (14,8), layout = (3,2))


