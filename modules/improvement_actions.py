import streamlit as st
import pandas as pd

def render():
    st.subheader("🔧 IMPROVEMENT ACTIONS (KAIZEN)")
    
    if 'risk_df' not in st.session_state:
        st.warning("No data available.")
        return

    df = st.session_state['risk_df']
    
    # Filter for Open/In Progress
    active_risks = df[df['status'].isin(['Open', 'In Progress', 'Pending Budget'])]
    
    if active_risks.empty:
        st.info("No active risks requiring action.")
        return

    # Select risk to manage
    col1, col2 = st.columns([1, 2])
    
    with col1:
        selected_id = st.selectbox("Select Risk ID", active_risks['id'].unique())
    
    if selected_id:
        # Get the row index in the main dataframe
        idx_list = df.index[df['id'] == selected_id].tolist()
        if not idx_list:
            return
        idx = idx_list[0]
        row = df.loc[idx]
        
        with col2:
            st.info(f"**Task:** {row['task']}\n\n**Issue:** {row['description']}")
            
        st.markdown("---")
        st.markdown("### define Action Plan")
        
        with st.form(key=f"action_form_{selected_id}"):
            c1, c2, c3 = st.columns(3)
            with c1:
                new_status = st.selectbox("Status Update", ["Open", "In Progress", "Pending Budget", "Closed"], index=["Open", "In Progress", "Pending Budget", "Closed"].index(row['status']))
            with c2:
                responsible = st.text_input("Responsible Person", value=row['responsible'])
            with c3:
                training_flag = st.checkbox("Mark as Training Case", value=row['training_case'])
                
            action_note = st.text_area("Action Details / Kaizen Proposal", placeholder="e.g., Install new guard rail, Update SOP 4.1...")
            
            save_btn = st.form_submit_button("UPDATE ACTION")
            
            if save_btn:
                # Update DataFrame directly in session state
                st.session_state['risk_df'].at[idx, 'status'] = new_status
                st.session_state['risk_df'].at[idx, 'responsible'] = responsible
                st.session_state['risk_df'].at[idx, 'training_case'] = training_flag
                # In a real app we would save the 'action_note' to a separate column or table
                st.success(f"Action updated for {selected_id}")
                st.rerun()
