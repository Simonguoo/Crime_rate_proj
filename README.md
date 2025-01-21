# Crime Rate Prediction

## Data
- csv files collected from 2019 us census
- excel files collected from fbi CIUS datatables
- 11 total data tables merged into one
### Cleaning

- Cleaned up Excel format (removed headers, footers, and notes)
- Reformatted CSV files to remove excess rows dedicated only to the city name or the estimates
- Replaced/removed nan values from data frame
- Parsed out state and location type from city column
- Created per capita data columns
- Merged separate data frames based on city 
## EDA
- A histogram revealed extreme outliers in several variables, to the extent where z-score thresholds were skewed
so i opted for IQR to eliminate outliers
- This removed quite a substantial portion of the data set 
- By graphing a pairplot of the predictor variables to the target variables I noticed that each predictor
had a poor relationship with the target variable regardless, so I considered the removal of the outliers to be
irrelevant to the poor performance of the model
- Population was the most correlated variable with respect to Crime rate, followed by poverty, law enforcement, home
vacancy, and median earnings. All these variables were still poor predictors of Crime rate

## Model Building
- As a result of the poor relationship between each predictor variable and the target variable, I deemed linear regression
to be a poor fit and tried random forest and gradient boosting in an attempt to build a model with any statistical signifcance
- the results were poor, random forest after hyperparameter tuning yielded an r2 score of 29.87%, and an rmse of 1029.78
- the gradient boosted model performed similarly although with slightly different hyperparameters
- regardless, the models performed poorly and I may revisit this project again and use the data for something else
