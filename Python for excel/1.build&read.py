import pandas as pd  # select python interpretor
dataframe = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Lucy', 'Lily', 'Lina']})
dataframe = dataframe.set_index('ID')
# pip install openpyxl;relative path(setting launch.json)
dataframe.to_excel('output.xlsx')
print(dataframe)
output = pd.read_excel('output.xlsx')
print(output.shape)  # (row,column)
print(output.columns)  # Index(['ID', 'Name'], dtype='object')
print(output.head(2))  # default:top 5 rows
print(output.tail(2))  # default:last 5 rows
output = pd.read_excel('output.xlsx', header=None)  # default:header=0
output.columns = ['COL1', 'COL2']
print(output.columns)
output.set_index('COL1', inplace=True)  # index:COL1
output.to_excel('output.xlsx')
# output=output.to_excel('output.xlsx')
output = pd.read_excel('output.xlsx', index_col='COL1')  # lock index_col
output.to_excel('output.xlsx')
