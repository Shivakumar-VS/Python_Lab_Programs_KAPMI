# 8. Write a python program to create data frame from excel sheet and perform 
# simple operations. 
import pandas as pd   
# Read Excel file into a DataFrame 
df = pd.read_excel('sample.xlsx', sheet_name='Sheet1') 

# Display the DataFrame 
print("Original DataFrame:") 
print(df) 

# Simple operations 
# Sum of a column 
age_sum = df['Age'].sum() 
print("\nSum of Ages:", age_sum) 

# Maximum value in a column 
age_max = df['Age'].max() 
print("Maximum Age:", age_max) 

# Minimum value in a column 
age_min = df['Age'].min() 
print("Minimum Age:", age_min) 

# Filtering rows based on condition (Age > 25) 
filtered_df = df[df['Age'] > 25] 
print("\nFiltered DataFrame (Age > 25):\n", filtered_df) 

# Adding a new column 'Gender' 
df['Gender'] = ['Male', 'Female', 'Male', 'Male', 'Male'] 
print("\nDataFrame with added column:\n", df) 

# Sorting the DataFrame by 'Age' in descending order 
sorted_df = df.sort_values('Age', ascending=False) 
print("\nSorted DataFrame (by Age, Descending):\n", sorted_df)