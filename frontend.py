import streamlit as st
from schema import PropertyAnalysisInput
from engine import analyze_property
from chart_factory import generate_investment_pie_chart
from pdf_printer import create_pdf_report

st.set_page_config(page_title="Automated Decision Engine", layout="centered")
st.title("🏗️ Property Analysis Engine")
st.markdown("Enter the property details below to instantly generate your executive bankability report.")

with st.form("property_form"):
    asking_price = st.number_input("Asking Price ($)", min_value=1.0, value=100000.0, step=1000.0)
    repair_costs = st.number_input("Estimated Repair Costs ($)", min_value=0.0, value=20000.0, step=1000.0)
    after_repair_value = st.number_input("After Repair Value (ARV) ($)", min_value=1.0, value=160000.0, step=1000.0)
    monthly_rent = st.number_input("Estimated Monthly Rent ($)", min_value=0.0, value=1200.0, step=100.0)
    closing_costs = st.number_input("Holding & Closing Costs ($)", min_value=0.0, value=8000.0, step=500.0)
    
    submitted = st.form_submit_button("Generate Executive PDF")

if submitted:
    with st.spinner("Running optimizations and compiling report..."):
        # 1. Load variables into Pydantic schema
        data = PropertyAnalysisInput(
            asking_price=asking_price,
            repair_costs=repair_costs,
            after_repair_value=after_repair_value,
            monthly_rent=monthly_rent,
            closing_costs=closing_costs
        )
        
        # 2. Run the decoupled pipeline directly
        financial_results = analyze_property(data)
        generate_investment_pie_chart(data, filename="cloud_chart.png")
        create_pdf_report(financial_results, "cloud_chart.png", output_filename="cloud_report.pdf")
        
        # 3. Serve the PDF
        with open("cloud_report.pdf", "rb") as pdf_file:
            st.success("Report generated successfully!")
            st.download_button(
                label="📄 Download Executive Report",
                data=pdf_file,
                file_name="Executive_Analysis_Report.pdf",
                mime="application/pdf"
            )
