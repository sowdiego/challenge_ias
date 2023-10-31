import streamlit as st

# Ton code Streamlit habituel ici
st.set_page_config(layout="wide")
# Intégration du code JavaScript avec st.markdown
st.title("Evolution de de l'emission de co2 et de la perte de couverture forestière en fonction du temps")

text_intro = """
        Ici on a l'évolution globale de la perte de couverture forestiere et l'emission du co2 de 2001 à 2022 plus pécisement.
        ainsi qu'une pediction de l'évolution durant les trois prochaines années avec possibilité de filtrer par region.
"""

text_indication = """
                Veuillez survoler les point pour avoir les details!
"""
st.markdown(text_intro)

st.markdown(text_indication)


tableau_dashboard_code2 = """
        <iframe src="https://public.tableau.com/views/challenge_ias_16985824084640/evolution_temporelle_tc_cO2?:language=fr-FR&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true" width="100%" height="700" frameborder="0"></iframe>
"""



st.markdown(tableau_dashboard_code2, unsafe_allow_html=True)
