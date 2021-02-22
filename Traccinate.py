# Traccinate

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

selected_variables = ['date',
                      'location',
                      'people_vaccinated',
                      'people_fully_vaccinated_per_hundred',
                      'people_fully_vaccinated',
                      'people_vaccinated_per_hundred',
                      'daily_vaccinations_per_million']

selected_data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv', 
                                dtype=str, encoding='unicode_escape',
                                usecols=selected_variables)

selected_data['people_vaccinated'] = pd.to_numeric(selected_data['people_vaccinated'])
selected_data['people_fully_vaccinated_per_hundred'] = pd.to_numeric(selected_data['people_fully_vaccinated_per_hundred'])
selected_data['people_fully_vaccinated'] = pd.to_numeric(selected_data['people_fully_vaccinated'])
selected_data['people_vaccinated_per_hundred'] = pd.to_numeric(selected_data['people_vaccinated_per_hundred'])
selected_data['daily_vaccinations_per_million'] = pd.to_numeric(selected_data['daily_vaccinations_per_million'])

for row in selected_data['daily_vaccinations_per_million']:
  try:
    selected_data.loc[selected_data['daily_vaccinations_per_million'] == row, 'daily_vaccinations_per_hundred'] = row/10000
  except:
    continue

new_data = selected_data.drop(columns=['daily_vaccinations_per_million'])

jurisdictions=["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", 
               "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", 
               "Federated States of Micronesia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", 
               "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Marshall Islands", "Maryland",
               "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", 
               "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "New York State", "Nevada", 
               "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", 
               "Pennsylvania", "Puerto Rico", "Republic of Palau", "Rhode Island", "South Carolina", 
               "South Dakota", "Tennessee", "Texas", "United States", "Utah", "Vermont", "Virginia", "Virgin Islands", 
               "Washington", "West Virginia", "Wisconsin", "Wyoming"]


########################## EXPERIMENTS: Making a Dash app ###################################
app = dash.Dash(__name__)

app.layout = html.Div([
	html.Div([
		dcc.Dropdown(
			id = "Location",
			options = [{'label': i, 'value': i} for i in jurisdictions],
			value = 'United States'
		),
	]),

    dcc.Graph(id='daily vacc'),
    dcc.Graph(id='one dose'),
    dcc.Graph(id='fully vacc'),
    dcc.Graph(id='people vacc')
])

@app.callback(
	Output('daily vacc', 'figure'),
	Input('Location', 'value'))
# Graph or Percentage of Population that is vaccinated per day 
def DailyVaccinations(Location="United States"):
    date = new_data.loc[new_data["location"]== Location, "date"]
    percentageDaily = new_data.loc[new_data["location"]== Location, "daily_vaccinations_per_hundred"]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=date, y=percentageDaily, name=Location,
                             connectgaps=True,
                             line=dict(color='firebrick', width=2)))

    # Edit the layout
    fig.update_layout(title='Percentage of Population Vaccinated Against Covid per Day in ' + Location,
                       xaxis_title='Date',
                       yaxis_title='Percentage of Population')

    return fig

@app.callback(
	Output('one dose', 'figure'),
	Input('Location', 'value'))
# Graph of percentage of population that have received at least one dose
def OneDoseOrMore(Location="United States"):
    date = new_data.loc[new_data["location"]== Location, "date"]
    percentageOneDosePlus = new_data.loc[new_data["location"]== Location, "people_vaccinated_per_hundred"]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=date, y=percentageOneDosePlus, name=Location,
                             connectgaps=True,
                             line=dict(color='firebrick', width=2)))

    # Edit the layout
    fig.update_layout(title='Total Percentage of Population Vaccinated (At Least 1 Dose) in ' + Location,
                       xaxis_title='Date',
                       yaxis_title='Percentage of Population')

    return fig

@app.callback(
	Output('fully vacc', 'figure'),
	Input('Location', 'value'))
# Graph of Total Percentage of Population that has been fully vaccinated
def FullyVaccinated(Location="United States"):
    date = new_data.loc[new_data["location"]== Location, "date"]
    percentageVaccinatedTotal = new_data.loc[new_data["location"]== Location, "people_fully_vaccinated_per_hundred"]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=date, y=percentageVaccinatedTotal, name=Location,
                             connectgaps=True,
                             line=dict(color='firebrick', width=2)))

    # Edit the layout
    fig.update_layout(title='Total Percentage of Population Fully Vaccinated Against Covid in ' + Location,
                       xaxis_title='Date',
                       yaxis_title='Percentage of Population')

    return fig

@app.callback(
	Output('people vacc', 'figure'),
	Input('Location', 'value'))
# Graph of raw population that have been fully vaccinated
def PeopleFullyVacc(Location="United States"):
    date = new_data.loc[new_data["location"]== Location, "date"]
    peopleVaccinatedTotal = new_data.loc[new_data["location"]== Location, "people_fully_vaccinated"]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=date, y=peopleVaccinatedTotal, name=Location,
                             connectgaps=True,
                             line=dict(color='firebrick', width=2)))

    # Edit the layout
    fig.update_layout(title='Total Number of People Fully Vaccinated with 2 Doses in ' + Location,
                       xaxis_title='Date',
                       yaxis_title='Number of People')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)