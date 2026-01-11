import streamlit as st

def apply_industrial_styles():
    st.markdown("""
        <style>
        /* General Font and Background */
        .stApp {
            font-family: 'Roboto', 'Inter', sans-serif;
        }
        
        /* Remove rounded corners from everything for that 'machinery' hard-edge look */
        .stButton > button {
            border-radius: 0px !important;
            border: 1px solid #5A5A5A;
            background-color: #333333;
            color: #E0E0E0;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            border-color: #4682B4; # Steel Blue
            color: #4682B4;
            background-color: #2D2D2D;
        }

        /* Input fields: sharp edges, dark background */
        .stTextInput > div > div > input {
            border-radius: 0px !important;
            background-color: #2D2D2D;
            color: #E0E0E0;
            border: 1px solid #444;
        }
        .stSelectbox > div > div > div {
            border-radius: 0px !important;
            background-color: #2D2D2D;
            color: #E0E0E0;
        }
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #1a1a1a;
            border-right: 1px solid #333;
        }

        /* Card-like containers for metrics and risks */
        .industrial-card {
            background-color: #2D2D2D;
            border: 1px solid #444;
            padding: 15px;
            margin-bottom: 10px;
            border-left: 4px solid #4682B4; /* Status indicator strip */
        }

        /* Headings */
        h1, h2, h3 {
            color: #B0C4DE; /* Light Steel Blue */
            font-weight: 700;
            text-transform: uppercase;
        }
        
        /* Alert/Status Colors */
        .status-high { border-left-color: #D32F2F !important; } /* Muted Red - Stop */
        .status-medium { border-left-color: #FFA000 !important; } /* Amber - Warning */
        .status-low { border-left-color: #4682B4 !important; } /* Blue - Info */
        
        </style>
    """, unsafe_allow_html=True)

def risk_card(risk_data):
    """
    Renders a custom HTML card for a risk without using just columns.
    risk_data: dict with keys (id, area, task, priority, description)
    """
    priority_color_class = f"status-{risk_data.get('priority_level', 'low').lower()}"
    
    html = f"""
    <div class="industrial-card {priority_color_class}">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;">
            <span style="font-weight:bold; font-size:0.9em; color:#888;">{risk_data.get('area', 'Unknown Area')} | {risk_data.get('id', 'ID-000')}</span>
            <span style="padding: 2px 8px; background:#333; border:1px solid #555; font-size:0.8em;">{risk_data.get('priority_level', 'LOW')}</span>
        </div>
        <div style="font-size:1.1em; font-weight:600; color:#E0E0E0; margin-bottom:5px;">
            {risk_data.get('task', 'Operation')}
        </div>
        <div style="font-size:0.95em; color:#CCC; font-family:'Consolas', monospace;">
            {risk_data.get('description', 'No description')}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
