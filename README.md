# Overview
This project aims to assess the investment potential of all Github repositories. The goal is to be able to identify fast growing repositories as well as analyze a specific repository. The data will be delivered in the format of a SQL database which will update at a daily frequency.

# Metrics

The metrics/data points we would like to analyze are as follows:

1. Growth rate of stars
2. Growth rate of commits
3. Custom Analysis

The growth rate of stars and growth rate of commits are the metrics we will use to decide which repositories to invest in. The final product also needs to have the functionality to conduct Ad hoc custom analysis. We can better assess investment potential with specific, tailored analyses.

# Data Source
The choice for the data source was between the Github API and GH Archive.

### Github API
#### Pros:
* Live, fresh data
* No 3rd party involved
  
#### Cons:
* Complex load logic; we would exceed the alotted number of API calls

### GH Archive
#### Pros:
*  Simple load logic; it is easier for us to gather all the necessary data

#### Cons:
*  Refreshes every hour (not the most up-to-date data)
*  3rd party is involved

Ultimately, we chose our data source to be GH Archive due to the feasibility issue that the Github API introduces. As we only need the data to be updated daily, the refresh frequency of 1 hour is acceptable. The potential issues that could arise due to the fact that the data is from a 3rd party can be mitigated with data quality tests.
