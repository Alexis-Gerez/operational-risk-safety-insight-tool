import streamlit as st
import pandas as pd
import altair as alt

def render():
    st.subheader("🚨 OPERATIONAL PRIORITY MATRIX")
    
    if 'risk_df' not in st.session_state:
        st.warning("No data available.")
        return

    df = st.session_state['risk_df']
    
    # --- Matrix Visualization ---
    st.markdown("### Risk Distribution (Impact vs. Frequency)")
    
    # Prepare data for heatmap
    # We map Low/Medium/High to 1/2/3 for plotting
    mapping = {"Low": 1, "Medium": 2, "High": 3}
    df['freq_score'] = df['frequency'].map(mapping)
    df['safety_score'] = df['impact_safety'].map(mapping)
    
    # Aggregation for the heatmap
    heatmap_data = df.groupby(['frequency', 'impact_safety']).size().reset_index(name='count')
    
    # Altair Chart
    base = alt.Chart(heatmap_data).encode(
        x=alt.X('frequency', sort=['Low', 'Medium', 'High'], title='Frequency'),
        y=alt.Y('impact_safety', sort=['Low', 'Medium', 'High'], title='Safety Impact')
    )

    heatmap = base.mark_rect().encode(
        color=alt.Color('count', scale=alt.Scale(scheme='orangered'))
    ).properties(width=500, height=400)

    text = base.mark_text(baseline='middle').encode(
        text='count',
        color=alt.value('white')
    )

    st.altair_chart(heatmap + text, use_container_width=True)
    
    # --- Priority List ---
    st.markdown("### 📋 Prioritized Observations")
    
    filter_prio = st.multiselect("Filter by Priority", ["High", "Medium", "Low"], default=["High", "Medium"])
    
    filtered_df = df[df['priority_level'].isin(filter_prio)]
    
    st.dataframe(
        filtered_df[['id', 'priority_level', 'area', 'task', 'description', 'status']],
        use_container_width=True,
        hide_index=True
    )
