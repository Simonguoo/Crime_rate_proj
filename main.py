import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# read in data
df = pd.read_csv("final_df.csv")

# choose relevant columns
Y = df.Crime_Rate
X = df.drop(["Crime_Rate", "City"], axis=1)
# train test split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)
kf = KFold(n_splits=10, shuffle=True, random_state=10)
# multiple linear regression
x_sm = sm.add_constant(X)
model = sm.OLS(Y, x_sm)
print(model.fit().summary())

lm = LinearRegression()
lm.fit(X_train, Y_train)
cv = np.mean(cross_val_score(lm, X_train, Y_train, scoring="neg_mean_absolute_error", cv=kf))
print("linear regression mae: "+ str(cv))


# random forest regression (gradient boosted tree)
rf = RandomForestRegressor()

cv_rf = np.mean(cross_val_score(rf, X_train, Y_train, scoring="neg_mean_absolute_error", cv = kf))
print("Random forest regression mae raw: " + str(cv_rf))


# model tuning
parameters = {'n_estimators': range(10, 100, 10), "criterion": ("friedman_mse", "poisson"), "max_features":
              ('auto', 'sqrt', 'log2')}
gs = GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error', cv=3)
gs.fit(X_train, Y_train)

# model metrics
pred_lm = lm.predict(X_test)
pred_rf = gs.best_estimator_.predict(X_test)

lm_mae = mean_absolute_error(Y_test, pred_lm)
rf_mae = mean_absolute_error(Y_test, pred_rf)
print("Linear regression mae tuned: " + str(lm_mae))
print("Random forest mae tuned: " + str(rf_mae))

lm_r2 = r2_score(Y_test, pred_lm)
rf_r2 = r2_score(Y_test, pred_rf)
print("Linear regression r2 tuned: " + str(lm_r2))
print("Random forest r2 tuned: " + str(rf_r2))