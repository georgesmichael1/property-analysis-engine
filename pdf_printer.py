from fpdf import FPDF

def create_pdf_report(
    results: dict, 
    pie_chart_path: str, 
    bar_chart_path: str, 
    client_id: str = "Standard User",
    output_filename: str = "Executive_Report.pdf"
) -> str:
    pdf = FPDF()
    pdf.add_page()
    
    # Authorized Client Header Stamp
    pdf.set_font("Helvetica", style="I", size=9)
    pdf.cell(0, 6, f"Authorized License: {client_id.upper()} | Generated via Streamline Engine", ln=True, align="R")
    pdf.ln(2)
    
    # Report Header
    pdf.set_font("Helvetica", style="B", size=18)
    pdf.cell(0, 12, "Executive Property Investment Report", ln=True, align="C")
    pdf.ln(4)
    
    # Strategic Verdict Banner
    pdf.set_font("Helvetica", style="B", size=13)
    pdf.cell(0, 10, f"STRATEGIC VERDICT: {results['verdict']}", ln=True)
    pdf.ln(2)
    
    # Key Financial Metrics Summary
    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 7, f"Total Capital Required: ${results['total_investment']:,.2f}", ln=True)
    pdf.cell(0, 7, f"Estimated Flip Profit: ${results['flip_profit']:,.2f} ({results['flip_roi']}% ROI)", ln=True)
    pdf.cell(0, 7, f"Year 1 Net Operating Income: ${results['annual_noi']:,.2f} ({results['rental_yield']}% Yield)", ln=True)
    pdf.cell(0, 7, f"5-Year Cumulative Cash Flow: ${results['total_5yr_cashflow']:,.2f}", ln=True)
    pdf.ln(5)
    
    # Visual 1: Capital Allocation Pie Chart
    pdf.image(pie_chart_path, x=45, w=120)
    pdf.ln(4)
    
    # Visual 2: 5-Year Cash Flow Bar Chart
    pdf.image(bar_chart_path, x=25, w=160)
    
    pdf.output(output_filename)
    return output_filename
