import pandas as pd

# print(pd.__version__)

a = [12, 14, 16]

myvar = pd.Series(a)
print(myvar)
print(myvar[0])
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0,2]])

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])
print(df.loc[["day2","day1"]])

# ------------------------------------ Read DataFrame & Save into CSV ------------
data = {
    'NY': 'New York',
    'AP': 'Andhra Pradesh',
    'MA': 'Massachusetts',
    'BC': 'British Columbia',
    'ON': 'Ontario',
    'TG': 'Telangana',
    'CA': 'California'
}

df = pd.DataFrame(data.items(),columns=['state_Id','state_Name'])
print(df)
print('Table info ',df.info())
df.to_csv(f'.\OutPut\state.csv', index=False)

df = pd.read_csv('.\TestData\Data.csv')
print(df)
print(df.to_string())  # this display all the records
print(df.loc[123])

print(df.to_string(max_rows=100))

print(pd.options.display.max_rows)  # this will display max 60
pd.options.display.max_rows = 100 # this will change the max to 100
print(pd.options.display.max_rows)

# Get the number of rows in the DataFrame
num_rows = df.shape[0]

# Print the number of rows
print(f"Number of records (rows) in the CSV: {num_rows}")

print("CSV file info like columns types : ",df.info())

df = pd.read_json('.\TestData\Data.json')
print(df)
print(f"Json file max reords :",df.shape[0])  # this display all the records

print("Head of 10 records : ",df.head(10)) # 1st 10 records
print("Tail of records : ",df.tail()) # last 5 records
print("Head of records : ",df.head())
print("Tail of 10 records : ",df.tail(10))

print("Json File info like columns types : ",df.info()) # info() method tells us how many Non-Null values there are present in each column & table info

# Return a new Data Frame with no empty cells
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
print("Total number of records in the CSV is : ",df.shape[0])

# Identify the rows that will be dropped (those containing NaN values)
dropped_data = df[df.isna().any(axis=1)]
print("Dropped data from DF : ",dropped_data)

new_df = df.dropna() # drona means drop null values in the data frame
print("After removing nulls : ",new_df)

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
# df.dropna(inplace = True)
# print(df.to_string())

df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
# fillna will fill the null data with MissingData
df.fillna("MissingData", inplace = True)
print(df)


df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
# Replace NULL values in the "Calories" columns with the number 130
df["Calories"].fillna(130, inplace = True)
print(df)

print("-----------------------------------------------------------------------")
# Mean = the average value (the sum of all values divided by number of values).
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
x = df["Calories"].mean()
print("mean() x value : ",x)
df["Calories"].fillna(x, inplace = True)
print(df)

print("-----------------------------------------------------------------------")
# Median = the value in the middle, after you have sorted all values ascending.
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
x = df["Calories"].median()
print("median() x value : ",x)
df["Calories"].fillna(x, inplace = True)
print(df) 

print("-----------------------------------------------------------------------")
# Mode = the value that appears most frequently.
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
x = df["Calories"].mode()[0]
print("mode() x value : ",x)
df["Calories"].fillna(x, inplace = True)
print(df) 

print("-----------------------------------------------------------------------")
#Remove rows with a NULL value in the "Date" column
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
df.dropna(subset=['Date'], inplace = True)
print(df)

print("-----------------------------------------------------------------------")
# Set "Duration" column replace value to 45 for row 7
print('Set "Duration" column replace value to 45 for row 7')
df.loc[7, 'Duration'] = 45
print(df)

print("-----------------------------------------------------------------------")
# Loop through all values in the "Duration" column. If the value is higher than 120, set it to 120
print('-------- in the "Duration" column. If the value is higher than 120, set it to 120 -----')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
    print(df)

print("-----------------------------------------------------------------------")
# Delete rows where "Duration" is higher than 120
print('----------Delete rows where "Duration" is higher than 120 ------')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print("-----------------------------------------------------------------------")
# Returns True for every row that is a duplicate, otherwise False
print('Returns True for every row that is a duplicate, otherwise False')
print(df.duplicated())

print("-----------------------------------------------------------------------")
# Remove all duplicates
df.drop_duplicates(inplace = True)
print(df)

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

# Merge with specific columns
Merge_Specific = pd.merge(table1_df,table2_df, on=columns_to_compare, how='inner')
Merge_Specific["Full_Name"]=table1_df["F_Name"]+' '+table1_df['L_Name']
fileName="Merge_Specific"
print(Merge_Specific)
Merge_Specific.to_csv(f'.\OutPut\{fileName}.csv', index=False)

#-------  If NY change it to New York
print('------------------- using dataFrame NY: New York' )
state_mapping = {
    'NY': 'New York',
    'AP': 'Andhra Pradesh',
    'MA': 'Massachusetts',
    'BC': 'British Columbia',
    'ON': 'Ontario',
    'TG': 'Telangana',
    'CA': 'California'
}

emp_Check= pd.read_csv('.\TestData\Emp_Check.csv')
# Add new column 'State_FullName'
emp_Check['State_FullName'] = emp_Check['State'].map(state_mapping)

# Result
print("----------------------------------",emp_Check)
fileName="State_Full_Emp_Check"
emp_Check.to_csv(f'.\OutPut\{fileName}.csv', index=False)
emp_Check.to_html(f'.\OutPut\{fileName}.html', index=False)

print('--------- State  full name from CSV --------')

data1=pd.read_csv('.\TestData\state.csv')
print(data1)

data2=pd.read_csv('.\TestData\Emp_Check.csv')
print(data2)

# Create a mapping dictionary
state_map=data1.set_index('state_Id')['state_Name'].to_dict()

data2['Before_Map']=data2['State']

# Replace State values with state_Name where matches exist
data2['State']=data2['State'].map(state_map).fillna(data2['State'])

print(data2)


# runiing join with multi columns
print('------------------------------- Join with multi columns where ')
data1 = [('1','ABCD','NY'),
         ('2','EFG','TX'),
         ('3','HIJK','MA'),
         ('4','LMNOP','CA'),
         ]
df1=pd.DataFrame(data1, columns=['Id','Name','City'])
print(df1)

data2 = [('1','QRS','NY'),
         ('2','TUV','TX'),
         ('3','WXYZ','MA'),
         ('8','Good','CA')
         ]
df2=pd.DataFrame(data2, columns=['Row','Name','Town'])
print(df2)

data3=pd.merge(
    df1,
    df2,
    left_on=['Id','City'],
    right_on=['Row','Town'],
    how='outer'
)
print(data3)

#-------------- Map and Dictionay
print('--------------------- Ex of Map and dictionary -------')
emp=[
    ('1','Mr','Raj'),
    ('2','Miss','lusi'),
    ('3','Mr','John'),
    ('4','Miss','rose'),
    ('5','MrMiss','Kal')
]

data1=pd.DataFrame(emp,columns=['Id','Dis','Name'])
print(data1)

missMr=[
    ('Mr','Male'),
    ('Miss','Female')
]
data2=pd.DataFrame(missMr,columns=['Dis','Gender'])
print(data2)

genderMap=data2.set_index('Dis')['Gender'].to_dict()
data1['AfterDis']=data1['Dis'].map(genderMap).fillna('NA')

data1['UpdatedName']=data1['Name'].str.upper()

print(data1)