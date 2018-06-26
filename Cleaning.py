#1.Describe the data with statistical information about each feature.
df = pd.read_csv ("Website_VIP_User_data_10000.csv")

#Column data types and null value information
df.info()

#statistical summary 
df.describe()

print(df.head())

#check for missing data
print(df.isnull().sum())
