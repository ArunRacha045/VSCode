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
# Convert wrong format date values to currect one
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

#Remove rows with a NULL value in the "Date" column
df = pd.read_csv('.\TestData\Data_Duplicate_Null_wrong.csv')
df.dropna(subset=['Date'], inplace = True)
print(df)

print("-----------------------------------------------------------------------")
# Set "Duration" column replace value to 45 for row 7
df.loc[7, 'Duration'] = 45
print(df)

print("-----------------------------------------------------------------------")
# Loop through all values in the "Duration" column. If the value is higher than 120, set it to 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
    print(df)

print("-----------------------------------------------------------------------")
# Delete rows where "Duration" is higher than 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print("-----------------------------------------------------------------------")
# Returns True for every row that is a duplicate, otherwise False
print(df.duplicated())

print("-----------------------------------------------------------------------")
# Remove all duplicates
df.drop_duplicates(inplace = True)
print(df)