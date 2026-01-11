import pandas as pd
import random
import datetime

def generate_simulated_data(num_records=50):
    """
    Generates a synthetic dataframe of operational risks.
    """
    areas = ["Assembly Line A", "Paint Shop", "Welding Bay", "Logistics Dock", "Maintenance Workshop", "Battery Assy"]
    tasks = [
        "Hydraulic Pump Maintenance", "Spot Welding Robot Calibration", "Forklift Charging", 
        "Conveyor Belt Inspection", "Chassis Alignment", "Solvent Tank Cleaning", "Manual Lifting of Sub-frame"
    ]
    categories = ["Mechanical", "Electrical", "Ergonomic", "Chemical", "Order & Cleanliness"]
    
    descriptions = [
        "Oil leak detected near high-pressure valve.",
        "Grounding cable frayed on unit #4.",
        "Operator reaching overhead repeatedly > 2 hours.",
        "Safety guard loose on rotary cutter.",
        "Pallet obstructing emergency walkway.",
        "Fumes detected during filter change.",
        "Socket wrench slipped - worn bolt head.",
        "Lighting insufficient for precision task.",
        "Lockout/Tagout point not clearly labeled.",
        "Hydraulic hose rubbing against sharp edge."
    ]
    
    responsibles = ["Team Lead A. Smith", "Maint. Tech B. Jones", "Safety Officer C. Ray", "Process Eng. D. Lee", "Unassigned"]

    data = []
    
    for i in range(num_records):
        freq = random.choice(["Low", "Medium", "High"])
        
        # Determine base priority score parts (simulated logic)
        impact_safety = random.choice(["Low", "Medium", "High"])
        impact_quality = random.choice(["Low", "Medium", "High"])
        impact_time = random.choice(["Low", "Medium", "High"])
        
        # Simple heuristic for "Priority Level"
        if (freq == "High" and impact_safety == "High") or (impact_safety == "High"):
            prio = "High"
        elif freq == "Medium" and impact_safety == "Medium":
            prio = "Medium"
        else:
            prio = "Low" if random.random() > 0.3 else "Medium"

        # Action status
        status = random.choice(["Open", "In Progress", "Closed", "Pending Budget"])
        
        datum = {
            "id": f"RSK-{1000+i}",
            "date": datetime.date.today() - datetime.timedelta(days=random.randint(0, 30)),
            "area": random.choice(areas),
            "task": random.choice(tasks),
            "category": random.choice(categories),
            "description": random.choice(descriptions) + f" (Ref: Unit {random.randint(1,99)})",
            "frequency": freq,
            "impact_safety": impact_safety,
            "impact_quality": impact_quality,
            "impact_time": impact_time,
            "impact_rework": random.choice(["None", "Low", "High"]),
            "priority_level": prio,
            "responsible": random.choice(responsibles) if status != "Open" else "Unassigned",
            "status": status,
            "training_case": random.choice([True, False]) if status == "Closed" else False
        }
        data.append(datum)
        
    return pd.DataFrame(data)

def get_initial_session_state():
    """Initializes the session state with data if not present."""
    import streamlit as st
    if 'risk_df' not in st.session_state:
        st.session_state['risk_df'] = generate_simulated_data()
