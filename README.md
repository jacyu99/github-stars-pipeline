# User Requirements for Github Repository Investment Project
To assess investment potential of all Github repositories, the client would like to be able to identify fast growing repositories as well as analyze a specific repository.

## Metrics
The metrics/data points that the client would like to analyze is as follows:
1. Growth rate of stars
2. Growth rate of commits
3. Custom Analysis

The client will use the growth rate of stars and growth rate of commits as metrics to decide which repositories to invest in. The client would also like to be able to do Ad hoc custom analysis to conduct specific, tailored analyses to assess investment potential. The final product needs to be flexible enough to provide this functionality.

## Data Source
The choice for the data source was between the Github API and GH Archive. 

The pros of the Github API are that it provides live fresh data and no 3rd party is involved. The con of Github API is that there is complex load logic; we would end up exceeding the alotted number of API calls.
The pros of GH archive is that it has simple load logic; it is easier for us to gather all the necessary data. The cons of GH archive are that it refreshes every hour (is not the most up-to-date data) and a 3rd party is involved.

Ultimately, we chose our data source to be GH Archive due to the feasibility issue that the Github API introduces. As the client only requires a daily refresh on the data, the refresh frequency of 1 hour is acceptable. The potential issues that could arise due to the fact that the data is from a 3rd party can be mitigated with data quality tests.

## Data Format
The client requests that the data be delivered in the format of a SQL database.

## Update Frequency
The client requests that the data be updated daily.
