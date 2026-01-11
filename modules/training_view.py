import streamlit as st
from utils.styles import risk_card

def render():
    st.subheader("📚 TECHNICAL TRAINING & LEARNING")
    st.markdown("Use these real operational cases for toolbox talks and technical training.")
    
    if 'risk_df' not in st.session_state:
        st.warning("No data available.")
        return

    df = st.session_state['risk_df']
    
    # Filter for Training Cases
    training_cases = df[df['training_case'] == True]
    
    if training_cases.empty:
        st.info("No cases marked for training yet. Go to 'Improvement Actions' to flag relevant risks.")
        return
        
    for i, row in training_cases.iterrows():
        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"#### 📖 Case ID: {row['id']}")
            st.markdown(f"**Scenario:** {row['description']}")
            st.markdown(f"**Area:** {row['area']} | **Task:** {row['task']}")
            
        with col2:
            st.error(f"Safety Impact: {row['impact_safety'].upper()}")
            st.warning(f"Quality Impact: {row['impact_quality'].upper()}")
            
        with st.expander("Discussion Points for Trainer"):
            st.markdown("""
            *   What is the root cause of this risk?
            *   How could this have been prevented during the design phase?
            *   What is the standard procedure (SOP) for this task?
            """)
