import streamlit as st
from schema import PropertyAnalysisInput
from engine import analyze_property
from chart_factory import generate_investment_pie_chart, generate_cashflow_bar_chart
from pdf_printer import create_pdf_report

st.set_page_config(page_title="Streamline Decision Engine", layout="centered")
st.title("🏗️ Streamline Analysis Engine")
st.markdown("Run your simulation below for a free instant verdict, or unlock the full Executive PDF Report.")

# Check if the user opened a custom link like ?client=george_vip
url_client = st.query_params.get("client", "")

# 1. Input Form (Free for anyone to test)
with st.form("property_form"):
    asking_price = st.number_input("Asking Price ($)", min_value=1.0, value=100000.0, step=1000.0)
    repair_costs = st.number_input("Estimated Repair Costs ($)", min_value=0.0, value=20000.0, step=1000.0)
    after_repair_value = st.number_input("After Repair Value (ARV) ($)", min_value=1.0, value=160000.0, step=1000.0)
    monthly_rent = st.number_input("Estimated Monthly Rent ($)", min_value=0.0, value=1200.0, step=100.0)
    closing_costs = st.number_input("Holding & Closing Costs ($)", min_value=0.0, value=8000.0, step=500.0)
    annual_rent_growth_rate = st.number_input(
        "Annual Rent Growth Rate (%)", min_value=0.0, max_value=50.0, value=3.0, step=0.5
    )
    
    submitted = st.form_submit_button("Run Simulation (Free Preview)")

# Save simulation results in session memory so they stay on screen while unlocking PDF
if submitted:
    data = PropertyAnalysisInput(
        asking_price=asking_price,
        repair_costs=repair_costs,
        after_repair_value=after_repair_value,
        monthly_rent=monthly_rent,
        closing_costs=closing_costs,
        annual_rent_growth_rate=annual_rent_growth_rate
    )
    st.session_state["data"] = data
    st.session_state["results"] = analyze_property(data)

# 2. Show Free Teaser & The 1/0 Gatekeeper if simulation has been run
if "results" in st.session_state:
    res = st.session_state["results"]
    data = st.session_state["data"]
    
    st.divider()
    st.subheader("📊 Instant Executive Preview")
    st.info(f"**STRATEGIC VERDICT:** {res['verdict']}")
    
    col1, col2 = st.columns(2)
    col1.metric("Estimated Flip ROI", f"{res['flip_roi']}%")
    col2.metric("Year 1 Rental Yield", f"{res['rental_yield']}%")
    
    st.divider()
    st.subheader("🔒 Unlock Full Engineering & Bankability PDF")
    st.caption("Includes Capital Allocation Breakdown, 5-Year Compounding Cash Flow Chart, and Full Metrics.")
    
    # Pre-fill the box if they used a custom ?client= link
    access_key = st.text_input(
        "Enter Monthly Client ID or Single-Report Ticket:", 
        value=url_client,
        placeholder="e.g., george_vip or report_991"
    ).strip()
    
    if access_key:
        # Load the 1 and 0 dictionaries from Streamlit Secrets
        clients_db = st.secrets.get("clients", {})
        tickets_db = st.secrets.get("single_tickets", {})
        
        # Check if key exists in either list
        status = clients_db.get(access_key, tickets_db.get(access_key, None))
        
        if status == 1:
            st.success(f"Access Verified ({access_key}). Compiling your executive report...")
            
            pie_path = generate_investment_pie_chart(data, filename="cloud_pie.png")
            bar_path = generate_cashflow_bar_chart(res["five_year_noi"], filename="cloud_bar.png")
            create_pdf_report(res, pie_path, bar_path, client_id=access_key, output_filename="cloud_report.pdf")
            
            with open("cloud_report.pdf", "rb") as pdf_file:
                st.download_button(
                    label="📄 Download Official Executive PDF",
                    data=pdf_file,
                    file_name=f"Streamline_Report_{access_key}.pdf",
                    mime="application/pdf"
                )
        elif status == 0:
            st.error("⛔ Access Deactivated (Status = 0). Your subscription or ticket has expired. Please contact administration to renew.")
        else:
            st.warning("⚠️ Invalid Client ID or Ticket Code. Please check your spelling or purchase a report pass.")
