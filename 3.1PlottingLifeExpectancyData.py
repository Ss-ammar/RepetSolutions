"""

@author: AMMAR

"""
import pandas as pd
#index_col: This is to allow you to set which columns to be used as the index of the dataframe
table = pd.read_csv(r'C:\Users\MyLaptop\Desktop\My STuff\UM6P STUDIES\Master GREEN BEE\PostMaster_Stage\life_expectancy.csv', index_col = 0)
print(table.loc['Belgium', '1980'])

# x: column name to be used as horizontal coordinates for each point
# y: column name to be used as vertical coordinates for each point
# s: size of dots
# c: color of dots
table.plot.scatter(x = '1960', y = '2014', s = 10)
table2 = table.transpose()
print(table2['Belgium'])

table2.to_excel(r'C:\Users\MyLaptop\Desktop\My STuff\UM6P STUDIES\Master GREEN BEE\PostMaster_Stage\RepeatSolutions\table2.xlsx', sheet_name='Table2 = transpose table 1') 