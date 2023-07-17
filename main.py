import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()

st.write(df)

year_options = df['year'].unique().tolist()
year = st.selectbox('Which year would you like to see?',year_options,0)
df = df[df['year']==year]

fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="continent", log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig.update_layout(width=800)

st.write(fig)

covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Code', 'Date', 'Confirmed', 'Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%M-%D')
country_options = covid['Country'].unique().tolist()
