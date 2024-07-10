Predict the rate of a certain crime like armed robbery or murder
### Independent Variables can include:
- employment rate
- household income
- education level
- poverty rate
- population density
- age distribution
- police presence/ clearance rate (percentage of crimes solved)
- public infrastructure
- housing condition
- drug/alcohol consumption
## Notes
- should try to differentiate by city
- yea so find any datasets that include city, state, and the above variables

ok new idea: 
- with the crime data, you can combine the columns to determine a crime rate
- You can then try to predict the crime rate of the city given its other socioeconomic factors
### Data

- csv files collected from 2019 us census
- excel files collected from fbi CIUS datatables

- for the csv files, you can refactor the shifting of the columns into:
  - for estimates(skip 2)
  - for percents(skip 3)
  - for city labels but would skip 2 for no percent and 3 for percent

- simplifying the city names would require the csv files to have the same cities, so to check this you could check for the same length after shifting