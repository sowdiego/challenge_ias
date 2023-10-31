import streamlit as st

# Ton code Streamlit habituel ici
st.set_page_config(layout="wide")
# Intégration du code JavaScript avec st.markdown
st.title("Classification de la corrélation entre l'émission de carbonne et La perte de couverture forestière")

text_intro = """
                 Cette type de graphe permet de classer les région suivant la corrélation qui existe entre l'emision de co2 par region 
                 et sa perte de couverture forestière correspondante.
"""

text_indication = """
                Veuillez survoler les point pour avoir les details!
"""
st.markdown(text_intro)

st.markdown(text_indication)


tableau_dashboard_code3 = """
        <iframe src="https://public.tableau.com/views/challenge_ias_16985824084640/correlation_tc_cO2?:language=fr-FR&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true" width="100%" height="700" frameborder="0"></iframe>
"""

st.markdown(tableau_dashboard_code3, unsafe_allow_html=True)