import streamlit as st

# Ton code Streamlit habituel ici
st.set_page_config(layout="wide")
# Intégration du code JavaScript avec st.markdown
st.subheader("test code js")

tableau_dashboard_code = """
        <iframe src="https://public.tableau.com/views/competion_ias/CartedevolutiondeCO2ETpertedecouvertureforestiere?:language=fr-FR&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true" width="100%" height="700" frameborder="0"></iframe>
"""

st.markdown(tableau_dashboard_code, unsafe_allow_html=True)