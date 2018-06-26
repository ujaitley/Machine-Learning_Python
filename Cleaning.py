#1.Describe the data with statistical information about each feature.
df = pd.read_csv ("Website_VIP_User_data_10000.csv")

#Column data types and null value information
df.info()

#statistical summary 
df.describe()

print(df.head())

#check for missing data
print(df.isnull().sum())

#Check for non-numeric value in numeric column
print(df[pd.to_numeric(df['product_like_rate'], errors='coerce').isnull()])

Output Sample:
  product_like_rate  total_free_coupon_got  total_bonus_xp_points  
279             #NAME?                      0                      0  
394             #NAME?                      5                 262800  
404             #NAME?                      7                 555000  
1067            #NAME?                      3                 645000  
1661            #NAME?                      2                  36000  
1663            #NAME?                      4                 585000  
1676            #NAME?                     11                1253100  
2003            #NAME?                      1                  96000  
2120            #NAME?                      1                  24000  
2168            #NAME?                      4                 225600  
2294            #NAME?                      1                 243000  
2316            #NAME?                      3                 288000  
2843            #NAME?                      1                  60000  
2968            #NAME?                      1                  24000  
3204            #NAME?                      1                  18000  
3504            #NAME?                      0                      0  
3639            #NAME?                      0                      0  
3650            #NAME?                      1                  36000  
3748            #NAME?                      0                      0  
3815            #NAME?                      6                 229200  
3886            #NAME?                      1                 300000  
3928            #NAME?                      1                  90000  
4174            #NAME?                      5                 574500  
4329            #NAME?                      1                 105000  
4355            #NAME?                      2                 924000  
4439            #NAME?                      0                      0  
4862            #NAME?                      2                  72000  
5551            #NAME?                      1                  75000  
6175            #NAME?                      0                      0  
6230            #NAME?                      1                  37500  
6938            #NAME?                      0                      0  
7012            #NAME?                      1                 210000  
7214            #NAME?                      1                  75000  
7714            #NAME?                      0                      0  
8264            #NAME?                      1                 105000  
8525            #NAME?                      0                      0  
8688            #NAME?                      2                 105000  
9732            #NAME?                      2                 153000  
9881            #NAME?                      2                 171000  
9884            #NAME?                      2                 186000  

#Dropping these rows
  df = df[pd.to_numeric(df['product_like_rate'], errors='coerce').notnull()]
  


  

