import streamlit as st
import requests

# Configure the web page appearance
st.set_page_config(page_title="Automated Decision Engine", layout="centered")

st.title("🏗️ Property Analysis Engine")
st.markdown("Enter the property details below to instantly generate your executive bankability report.")

# Create the form matching your Pydantic Schema
with st.form("property_form"):
    asking_price = st.number_input("Asking Price ($)", min_value=1.0, value=100000.0, step=1000.0)
    repair_costs = st.number_input("Estimated Repair Costs ($)", min_value=0.0, value=20000.0, step=1000.0)
    after_repair_value = st.number_input("After Repair Value (ARV) ($)", min_value=1.0, value=160000.0, step=1000.0)
    monthly_rent = st.number_input("Estimated Monthly Rent ($)", min_value=0.0, value=1200.0, step=100.0)
    closing_costs = st.number_input("Holding & Closing Costs ($)", min_value=0.0, value=8000.0, step=500.0)
    
    # The submit button
    submitted = st.form_submit_button("Generate Executive PDF")

# What happens when the user clicks the button
if submitted:
    payload = {
        "asking_price": asking_price,
        "repair_costs": repair_costs,
        "after_repair_value": after_repair_value,
        "monthly_rent": monthly_rent,
        "closing_costs": closing_costs
    }
    
    with st.spinner("Running optimizations and compiling report..."):
        try:
            # Send the data to your FastAPI backend
            response = requests.post("http://127.0.0.1:8000/api/generate-pdf", json=payload)
            
            if response.status_code == 200:
                st.success("Report generated successfully!")
                st.download_button(
                    label="📄 Download Executive Report",
                    data=response.content,
                    file_name="Executive_Analysis_Report.pdf",
                    mime="application/pdf"
                )
            else:
                st.error(f"Backend Error: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect. Is the FastAPI backend running? Error: {e}")