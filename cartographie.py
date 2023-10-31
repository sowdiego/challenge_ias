import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import streamlit as st 


st.set_page_config(layout="wide")
df = pd.read_excel("./SEN.xlsx", sheet_name="Subnational 2 carbon data")

# Renommer les colonnes
df.rename(columns={"country":"pays", "subnational1":"region", "subnational2":"departement"}, inplace=True)

mask = df.isnull()

region_choose = st.sidebar.multiselect(
    "Prédir le taux de co2:",
    options=df["region"].unique(),
    default=df["region"].unique()[0]
)
# st.write(region_choose)

plt.figure(figsize=(14,7))
sns.heatmap(mask)


category_columns_names = list(df.select_dtypes(include="object").columns)
numerical_columns_names = list(df.select_dtypes(exclude="object").columns)

imputer = KNNImputer(n_neighbors=5)

imputer_data = imputer.fit_transform(df.select_dtypes(exclude="object"))

imputer_data = pd.DataFrame(imputer_data, columns=numerical_columns_names)

df = pd.concat([df.select_dtypes(include="object"), imputer_data], axis=1)

plt.figure(figsize=(14,7))
sns.heatmap(df.isnull())

names_emissions = [f"gfw_forest_carbon_gross_emissions_{i}__Mg_CO2e" for i in range(2001, 2023)]

df["taux_emissions_co2"] = df[names_emissions].mean(axis=1)


df.drop(columns=names_emissions, axis=1, inplace=True)

y = df["taux_emissions_co2"]

X = df.drop(columns=["taux_emissions_co2","pays"], axis=1)
# st.write(X)
# st.write(y)

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.15)

encoder = OneHotEncoder()
encoder_data = encoder.fit_transform(X_train.select_dtypes(include="object")).toarray()

X_train = np.concatenate([encoder_data, X_train.select_dtypes(exclude="object").values], axis=1)

encoder_data_test = encoder.transform(X_test.select_dtypes(include="object")).toarray()

X_test = np.concatenate([encoder_data_test, X_test.select_dtypes(exclude="object").values], axis=1)

model = LinearRegression()
model.fit(X_train, y_train)
#y_test_2D = y_test.reshape(-1, 1)
test = np.array(X_test, y_test)

# st.write(test)

# st.write(model.score(X_test, y_test))

predict = model.predict(test)

results = pd.DataFrame({'Vraies Valeurs (y_test)': y_test, 'Prédictions': predict})
# st.write(results)
mean = round(predict.mean(), 2)

left_column,center_column = st.columns(2)
with left_column:
    st.title("Prédiction du taux du taux de co2 : ")
with center_column:
        st.title(mean)
# with right_column:
#         st.title("")


#model_3 = RandomForestRegressor()
#model_3.fit(X_train, y_train)

#st.write(model_3.score(X_test, y_test))




# Intégration du code JavaScript avec st.markdown
st.title("Surveillance de la couverture forestiére et de l'activité carbonne")

text_intro = """
                La déforestation contribue significativement aux émissions mondiales de CO2 et aggrave le changement climatique.
                Par le biais de cette carte on peut suivre la couverture forrestiére par region ainsi que les taux de carbonne.
"""

text_indication = """
                Veuillez cliquer sur les regions identifiées pour avoir les details!
"""
st.markdown(text_intro)

st.markdown(text_indication)

tableau_dashboard_code = """
        <iframe src="https://public.tableau.com/views/competion_ias/CartedevolutiondeCO2ETpertedecouvertureforestiere?:language=fr-FR&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true" width="100%" height="700" frameborder="0"></iframe>
"""

st.markdown(tableau_dashboard_code, unsafe_allow_html=True)