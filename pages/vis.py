import streamlit as st

# Ton code Streamlit habituel ici

# Intégration du code JavaScript avec st.markdown
st.subheader("test code js")
# st.markdown("""
#     <div id="vizContainer"></div>
#     <script src="https://public.tableau.com/javascripts/api/tableau-2.min.js">
#         function initViz() {
#             var containerDiv = document.getElementById("vizContainer"),
#             url = "https://public.tableau.com/views/competition_ias/comparaison_gainperte";

#             var viz = new tableau.Viz(containerDiv, url);
#             }
#             initViz();
#     </script>
# """, unsafe_allow_html=True)



tableau_dashboard_code = """
        <iframe src="https://public.tableau.com/app/profile/abdou.seye4723/viz/shared/JNFQBB2K6" width="100%" height="600" frameborder="0"></iframe>
"""

st.markdown(tableau_dashboard_code, unsafe_allow_html=True)