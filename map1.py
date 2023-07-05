# first of all open vscode
# select cmd as terminal and type
# python -m venv myenv 
# now you should see myenv on the expolrer and to activate it type
# path in cmd>myenv\Scripts\activate
# you can verify by line in cmd and now all the required module can be installed through cmd pip command
# other way to do is change the python to anaconda one intepretator, then open cmd as terminal and install with mamba install -c conda-forge folium


import streamlit as st
import pandas as pd
# import folium
# from streamlit_folium import st_folium

# to set app title / nav bar text
app_title = 'Alberta Approved Farmers Market 2023'
app_sub_title = 'Data published by Government of Alberta'
st.set_page_config(app_title)
st.title(app_title)
st.caption(app_sub_title)
# from streamlit_folium import st_folium

df_farmarket = pd.read_csv('data/farmersmarkets.csv',usecols=['marketId','town','venueName','venueAddress','schedule','contact','website','longitude','latitude'])
df_farmarket.columns = ['Market ID','Town','Venue Name','Venue Address','Market Schedule','Contact','Website','longitude','latitude']
# map1
st.write('CSV file pollted on a map with streamlit map function')
st.map(df_farmarket)

# button to show/hide csv table
expander = st.expander("Click here to view original csv file")
expander.write(df_farmarket)



                           
