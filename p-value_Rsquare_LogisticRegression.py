import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#Load and split the data file
df = pd.read_csv ("file_clean.csv")
predictors = ['payment_7_day','dau_days','days_between_install_first_pay','total_txns_7_day','total_page_views','total_product_liked','product_like_rate','total_free_coupon_got','total_bonus_xp_points']
y_variable = ['IsVIP_500']
x_train, x_test, y_train, y_test = train_test_split(df[predictors],df[y_variable],train_size = 0.7,random_state=7)

#Running statsmodels only on training data set
x_train = sm.add_constant(x_train, prepend=True) #This command is used to add intercept. 
logit_model=sm.Logit(y_train,x_train)
result_train =logit_model.fit()
print(result_train.summary())

#Output:

 Logit Regression Results                           
==============================================================================
Dep. Variable:              IsVIP_500   No. Observations:                 6972
Model:                          Logit   Df Residuals:                     6962
Method:                           MLE   Df Model:                            9
Date:                Thu, 28 Jun 2018   Pseudo R-squ.:                  0.2804
Time:                        18:06:58   Log-Likelihood:                -424.68
converged:                       True   LL-Null:                       -590.17
                                        LLR p-value:                 6.878e-66
==================================================================================================
                                     coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------------
const                             -7.5812      0.464    -16.345      0.000      -8.490      -6.672
payment_7_day                      0.0278      0.002     13.832      0.000       0.024       0.032
dau_days                           0.3970      0.076      5.232      0.000       0.248       0.546
days_between_install_first_pay    -0.0005      0.000     -3.442      0.001      -0.001      -0.000
total_txns_7_day                   0.0477      0.024      2.030      0.042       0.002       0.094
total_page_views                   0.0005      0.000      1.057      0.291      -0.000       0.001
total_product_liked               -0.0003      0.001     -0.216      0.829      -0.003       0.003
product_like_rate                 -0.1088      0.087     -1.258      0.208      -0.278       0.061
total_free_coupon_got              0.0109      0.028      0.389      0.698      -0.044       0.066
total_bonus_xp_points          -6.816e-08    2.3e-07     -0.296      0.767   -5.19e-07    3.83e-07
==================================================================================================


'''Interpretation of above values:
From the above result we can say:
total_page_views, total_product_liked,product_like_rate,total_free_coupon_got and total_bonus_xp_points are statistically insignificant 
as there p-values are higher than 0.05. We can drop these columns are try to re-run the model. And check if there is any imporvement is 
Rsquare value. Currently Rsquare value is 0.2804. Which means 28.04% variation in the y variable can be explained by predictors.
'''






