import streamlit as st
import pandas as pd
import datetime
from utils.data_generator import generate_simulated_data

def render():
    st.subheader("📝 NEW RISK OBSERVATION")
    
    with st.form("new_risk_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            area = st.selectbox("Area / Workstation", [
                "Assembly Line A", "Paint Shop", "Welding Bay", 
                "Logistics Dock", "Maintenance Workshop", "Battery Assy"
            ])
            task = st.text_input("Task or Operation", placeholder="e.g. Hydraulic Pump Maintenance")
            category = st.selectbox("Risk Category", [
                "Mechanical", "Electrical", "Ergonomic", "Chemical", "Order & Cleanliness"
            ])
            
        with col2:
            freq = st.select_slider("Frequency", options=["Low", "Medium", "High"], value="Medium")
            st.markdown("**Potential Impact**")
            imp_safe = st.select_slider("Safety", options=["Low", "Medium", "High"], value="Low")
            imp_qual = st.select_slider("Quality", options=["Low", "Medium", "High"], value="Low")
            imp_time = st.select_slider("Time", options=["Low", "Medium", "High"], value="Low")
            
        description = st.text_area("Technical Description (Plain Operations Language)", 
                                   placeholder="Describe exactly what happened or what could happen...")
        
        submitted = st.form_submit_button("LOG OBSERVATION")
        
        if submitted:
            if not task or not description:
                st.error("Please fill in Task and Description.")
            else:
                # Calculate Priority (Simple Logic)
                prio = "Low"
                if imp_safe == "High" or (freq == "High" and imp_qual == "High"):
                    prio = "High"
                elif imp_safe == "Medium" or imp_qual == "Medium":
                    prio = "Medium"
                
                new_entry = {
                    "id": f"RSK-{random.randint(2000, 9999)}", # Needs random import, usually passed in context but we'll add import here
                    "date": datetime.date.today(),
                    "area": area,
                    "task": task,
                    "category": category,
                    "description": description,
                    "frequency": freq,
                    "impact_safety": imp_safe,
                    "impact_quality": imp_qual,
                    "impact_time": imp_time,
                    "impact_rework": "Low", # Default
                    "priority_level": prio,
                    "responsible": "Unassigned",
                    "status": "Open",
                    "training_case": False
                }
                
                # Append to session state
                import random # Late import for this function scope
                new_entry["id"] = f"RSK-{random.randint(2000, 9999)}"
                
                df_new = pd.DataFrame([new_entry])
                st.session_state['risk_df'] = pd.concat([st.session_state['risk_df'], df_new], ignore_index=True)
                st.success(f"Observation logged successfully! Priority Level: {prio}")
