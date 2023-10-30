import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Autres visualisations")

# Charger mes données 
carbon_data = pd.read_excel('../tree-cover dataset.xlsx', sheet_name=6)
tc_data = pd.read_excel('../tree-cover dataset.xlsx', sheet_name=5)

# Sidebar
# subnational1_filter = st.sidebar.multiselect("Filtrer par Région", carbon_data["subnational1"].unique())
# subnational2_filter = st.sidebar.multiselect("Filtrer par Département", carbon_data["subnational2"].unique())
# carbon_data_filter = st.sidebar.checkbox("Filtrer par carbon_data")
# tc_data_filter = st.sidebar.checkbox("Filtrer par tc_data")

# Appliquer les filtres aux données
filtered_carbon_data = carbon_data
filtered_tc_data = tc_data
# if subnational2_filter:
#     filtered_carbon_data = filtered_carbon_data[filtered_carbon_data["subnational2"].isin(subnational2_filter)]
#     filtered_tc_data = filtered_tc_data[filtered_tc_data["subnational2"].isin(subnational2_filter)]


# Partie principale du tableau de bord


loss_columns = ['tc_loss_ha_2001', 'tc_loss_ha_2002', 'tc_loss_ha_2003', 'tc_loss_ha_2004', 'tc_loss_ha_2005', 'tc_loss_ha_2006', 'tc_loss_ha_2007', 'tc_loss_ha_2008', 'tc_loss_ha_2009', 'tc_loss_ha_2010', 'tc_loss_ha_2011', 'tc_loss_ha_2012', 'tc_loss_ha_2013', 'tc_loss_ha_2014', 'tc_loss_ha_2015', 'tc_loss_ha_2016', 'tc_loss_ha_2017', 'tc_loss_ha_2018', 'tc_loss_ha_2019', 'tc_loss_ha_2020', 'tc_loss_ha_2021', 'tc_loss_ha_2022']

region_loss_data = filtered_tc_data.groupby("subnational1")[loss_columns].sum()

fig = px.line(region_loss_data.T, x=region_loss_data.columns, y=region_loss_data.index, labels={"index": "Année", "value": "Perte de Couverture Forestière (ha)"})
fig.update_layout(xaxis_tickangle=-60, title="Évolution de la Perte de Couverture Forestière par Région de 2001 a 2022")
st.plotly_chart(fig)

##gain couverture forestiere
gain_column = 'gain_2000-2020_ha'

region_gain_data = filtered_tc_data.groupby("subnational1")[gain_column].sum().reset_index()

fig = px.bar(region_gain_data, x="subnational1", y=gain_column, labels={"subnational1": "Région", gain_column: "Gain de Couverture Forestière (ha)"}, title="Gain de Couverture Forestière par Région (2000-2020)")
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5)
fig.update_xaxes(tickangle=-60)
st.plotly_chart(fig)

## comparaison etendu tc couverture 2000 - 2010

extent_columns = ['extent_2000_ha', 'extent_2010_ha']

region_extent_data = filtered_tc_data.groupby("subnational1")[extent_columns].sum().reset_index()

fig = px.bar(region_extent_data, x="subnational1", y=extent_columns, labels={"subnational1": "Région", extent_columns[0]: "2000", extent_columns[1]: "2010"}, title="Comparaison de l'Étendue de la Couverture Forestière par Région (2000 par rapport 2010)")
fig.update_xaxes(tickangle=-60)
st.plotly_chart(fig)

##diagramme de dispersion
scatter_data = filtered_tc_data[['area_ha', 'extent_2000_ha']]

# fig = px.scatter(scatter_data, x='area_ha', y='extent_2000_ha', labels={'area_ha': 'Superficie (ha)', 'extent_2000_ha': 'Étendue 2000 (ha)'}, title='Relation entre Superficie et Étendue de la Couverture Forestière en 2000')
# st.plotly_chart(fig)


# ##Graphique à barres empilées pour montrer la perte de couverture forestière au fil des ans pour une région donnée 
# if subnational1_filter:
#     loss_columns = ['tc_loss_ha_2001', 'tc_loss_ha_2002', 'tc_loss_ha_2003', 'tc_loss_ha_2004', 'tc_loss_ha_2005', 'tc_loss_ha_2006', 'tc_loss_ha_2007', 'tc_loss_ha_2008', 'tc_loss_ha_2009', 'tc_loss_ha_2010', 'tc_loss_ha_2011', 'tc_loss_ha_2012', 'tc_loss_ha_2013', 'tc_loss_ha_2014', 'tc_loss_ha_2015', 'tc_loss_ha_2016', 'tc_loss_ha_2017', 'tc_loss_ha_2018', 'tc_loss_ha_2019', 'tc_loss_ha_2020', 'tc_loss_ha_2021', 'tc_loss_ha_2022']
#     selected_region_data = filtered_tc_data[filtered_tc_data["subnational1"].isin(subnational1_filter)]
#     fig = px.bar(selected_region_data, x=loss_columns, y=loss_columns, title=f"Perte de Couverture Forestière par Année ({', '.join(subnational1_filter)})")
#     fig.update_xaxes(tickmode='linear', dtick=1)
#     fig.update_layout(barmode='stack')
#     st.plotly_chart(fig)