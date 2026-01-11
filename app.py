import streamlit as st
import pandas as pd
from utils.data_generator import get_initial_session_state
from utils.styles import apply_industrial_styles

# Page Config must be first
st.set_page_config(
    page_title="Operational Risk Insight",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Data & Styles
apply_industrial_styles()
get_initial_session_state()

# --- Sidebar / Navigation ---
st.sidebar.title("🏭 OP. INSIGHT")
st.sidebar.markdown("---")
st.sidebar.markdown("**System Mode**: `Simulation`")
st.sidebar.markdown("**User Role**: `Supervisor`")

nav_options = [
    "Dashboard",
    "Risk Observation",
    "Priority Matrix",
    "Improvement Actions",
    "Training View"
]

selection = st.sidebar.radio("MODULE SELECTOR", nav_options)

st.sidebar.markdown("---")
st.sidebar.info(
    "**DISCLAIMER**: This tool is for operational support and training only. "
    "It is NOT a legal Health & Safety compliance record system."
)

# --- Main Routing ---
if selection == "Dashboard":
    st.title("OPERATIONAL DASHBOARD")
    st.markdown("Global overview of workshop risk status and improvement velocity.")
    
    if 'risk_df' in st.session_state:
        df = st.session_state['risk_df']
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Observations", len(df))
        col2.metric("High Priority", len(df[df['priority_level'] == 'High']))
        col3.metric("Open Actions", len(df[df['status'] == 'Open'])) 
        col4.metric("Training Cases", len(df[df['training_case'] == True]))
        
        st.markdown("### RECENT HIGH PRIORITY RISKS")
        high_prio = df[df['priority_level'] == 'High'].head(3)
        from utils.styles import risk_card
        for _, row in high_prio.iterrows():
            risk_card(row.to_dict())

elif selection == "Risk Observation":
    from modules import risk_observation
    risk_observation.render()

elif selection == "Priority Matrix":
    from modules import priority_matrix
    priority_matrix.render()

elif selection == "Improvement Actions":
    from modules import improvement_actions
    improvement_actions.render()

elif selection == "Training View":
    from modules import training_view
    training_view.render()

