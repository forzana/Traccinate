# Traccinate
Interactive graphs that display vaccination progress in the United States. This was created for Pearl Hacks 2021.

## Inspiration
COVID-19 has taken the U.S. by storm. Many Americans' lives have drastically changed. We yearn for normalcy once again. With the long-awaited arrival of vaccines, we wanted to be able to visualize vaccination progress in the United States. 

## What it does
Traccinate takes [data](https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/us_state_vaccinations.csv) that is updated daily and presents it using line graphs to help visualize how fast vaccines are being rolled out. The graphs we created show:
* Percentage of population fully vaccinated (2 doses) by state/territory
* Percentage of population vaccinated against Covid per day by state/territory
* Percentage of population that has been given at least one dose of the vaccine by state/territory
* Number of people that have been fully vaccinated with 2 doses of the Covid vaccine by state/territory

## How we built it
We used `pandas` to clean and manipulate data provided by Our World in Data and `plotly` as our graphing agent tot create interactive graphs.

## Challenges we ran into
Although we have used `pandas` before, this was the first time we used it to extract subsections of a complete dataframe. Furthermore, we first attempted to create the graphs using `matplotlib` however we were unable to implement the features we wanted. After switching over to `plotly` and experimenting with the graphs, we were finally able to create a drop down menu that changed the data being displayed on the graph. We had to do a lot of googling to figure things out and at the end, we learned a lot. 

## Accomplishments that we're proud of
We are proud that we were able to make use of real-world data to create an application.

## What we learned
We learned how to add an element of interactivity to a graph with `plotly`. We also learned about dataframe manipulation.

## What's next for Traccinate
Due to shortage of time, we were unable to automate Traccinate to fetch new data everyday, but this would be the ideal next step. We would also like to implement our program on a web browser or app so that it is more accessible everywhere. Finally, we hope to expand Traccinate outwards–we want it to show vaccination progress throughout the world.
