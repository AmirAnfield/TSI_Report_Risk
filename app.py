import streamlit as st

# Étape 1 : Sélection de l'autorité
autorites = ['Gendarmerie', 'Police', 'Douanes', 'Urssaf', 'DGFIP', 'DIREETS', 'Huissier de justice', 'CPAM', 'CAF', 'Autres']
autorite = st.selectbox("Autorité", autorites)

# Si "Autres" est sélectionné, proposer une entrée texte
if autorite == 'Autres':
    autorite_autre = st.text_input("Veuillez préciser l'autorité")
else:
    autorite_autre = autorite

# Étape 2 : Sélection de la typologie du document
typologies = ['Réquisition judiciaire', 'Droit de communication']
typologie = st.selectbox("Typologie du document", typologies)

# Étape 3 : Sélection du motif
motifs = ['Enquête préliminaire', 'Droit de communication', 'Autres']
motif = st.selectbox("Motif", motifs)

# Si "Autres" est sélectionné, proposer une entrée texte
if motif == 'Autres':
    motif_autre = st.text_input("Veuillez préciser le motif")
else:
    motif_autre = motif

# Étape 4 : Numéro du ticket (champ libre)
numero_ticket = st.text_input("Numéro du ticket")

# Étape 5 : Sélection de l'action sur le compte
actions_compte = ['Non spécifié', 'Autres']
action_compte = st.selectbox("Action sur le compte", actions_compte)

# Si "Autres" est sélectionné, proposer une entrée texte
if action_compte == 'Autres':
    action_compte_autre = st.text_input("Veuillez préciser l'action sur le compte")
else:
    action_compte_autre = action_compte

# Étape 6 : Sélection du statut du compte
statuts_compte = ['Activé', 'Suspendu', 'Désactivé']
statut_compte = st.selectbox("Statut du compte", statuts_compte)

# Génération du texte final avec des sauts de ligne
if st.button("Générer le texte"):
    texte_final = f"""
    Autorité : {autorite_autre}\n
    Typologie du document : {typologie}\n
    Motif : {motif_autre}\n
    Numéro du ticket : {numero_ticket}\n
    Action sur le compte : {action_compte_autre}\n
    Statut du compte : {statut_compte}
    """
    st.text(texte_final)  # Utilisation de st.text() pour respecter les sauts de ligne
