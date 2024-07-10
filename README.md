# Crime Rate Prediction

- Created a model that predicts the crime rate in American cities 
based on socioeconomic factors 
- Utilized a Linear and Random Forest regression model, yielding 
a mae of 0.0107 and 0.0089 respectively
- Created Features from the given data to evaluate per capita data
## Data
- csv files collected from 2019 us census
- excel files collected from fbi CIUS datatables
### Cleaning

- Cleaned up Excel format (removed headers, footers, and notes)
- Reformatted CSV files to remove excess rows dedicated only to the city name or the estimates
- Replaced/removed nan values from data frame
- Parsed out state and location type from city column
- Created per capita data columns
- Merged separate data frames based on city 
## EDA

- Looked at distribution of the data and removed egregious outliers
- Crafted a Pairplot for the factors traditionally 
believed to be associated with crime rate
- Created a Heatmap to outline any variables with high correlation
- dropped unnecessary variables

## Model Building
- I tried two models which I believed would be effective
  - Multiple Linear Regression was the baseline model 
  - Random Forest was chosen because I was unfamiliar with using the model in practice
  and wanted to compare the results
- The random forest model performed better than the mlr model in both mae score and 
r2 score, although both models performed relatively poorly in r2 score
  - Multiple Linear Regression: r2 of -0.13786
  - Random Forest Regression: r2 of 0.29087
