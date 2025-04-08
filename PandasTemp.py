import pandas as pd

table1_df = pd.read_csv('.\TestData\emp.csv')
table2_df = pd.read_csv('.\TestData\emp22.csv')
print(table1_df.to_string())
print("-------------------------------------------------------")
print(table2_df.to_string())
columns_to_compare = ['PK']
# Inner Join
fileName=""
merged_inner_df = pd.merge(table1_df, table2_df, on=columns_to_compare, how='inner', suffixes=('_table1_df','_table2_df'))
print("------------------- Inner Join ------------------",merged_inner_df)
fileName="merged_inner_df"
merged_inner_df.to_csv(f'.\OutPut\{fileName}.csv', index=False)

# Outer Join
merged_outer_df = pd.merge(table1_df, table2_df, on=columns_to_compare, how='outer', suffixes=('_table1_df','_table2_df'))
print("------------------- Outer Join ------------------",merged_outer_df)
fileName="merged_outer_df"
merged_outer_df.to_csv(f'.\OutPut\{fileName}.csv', index=False)

# Left Join
merged_left_df = pd.merge(table1_df, table2_df, on=columns_to_compare, how='left', suffixes=('_table1_df','_table2_df'))
print("------------------- Left Join ------------------",merged_left_df)
fileName="merged_left_df"
merged_left_df.to_csv(f'.\OutPut\{fileName}.csv', index=False)

# Right Join
merged_right_df = pd.merge(table1_df, table2_df, on=columns_to_compare, how='right', suffixes=('_table1_df','_table2_df'))
print("------------------- Right Join ------------------",merged_right_df)
fileName="merged_right_df"
merged_right_df.to_csv(f'.\OutPut\{fileName}.csv', index=False)
