import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Titre de l'application
st.title("🏠 Collecte Studio - Version Cloud")

# Création de la connexion avec Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Formulaire de collecte
with st.form("form_studio"):
    nom = st.text_input("Nom du bailleur")
    prix = st.number_input("Loyer", min_value=0)
    loc = st.text_input("Quartier")
    
    if st.form_submit_button("Enregistrer"):
        # On récupère les données existantes
        existing_data = conn.read(worksheet="Sheet1")
        
        # On ajoute la nouvelle ligne
        new_row = {"Nom": nom, "Prix": prix, "Localisation": loc}
        # Code pour mettre à jour la feuille...
        st.success("Donnée envoyée sur Google Sheets !")

