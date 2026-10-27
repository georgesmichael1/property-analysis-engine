from fpdf import FPDF
from schema import PropertyAnalysisInput
from engine import analyze_property
from chart_factory import generate_investment_pie_chart

def create_pdf_report(results: dict, image_filename: str, output_filename="Executive_Report.pdf"):
    """Compiles the financial data and chart into a branded PDF report."""
    
    # Initialize the PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(0, 15, "Automated Property Analysis Report", ln=True, align="C")
    pdf.ln(5)
    
    # The Executive Verdict
    pdf.set_font("helvetica", "B", 14)
    if "FLIP" in results['Final Verdict']:
        pdf.set_text_color(44, 160, 44)  # Green for Flip
    else:
        pdf.set_text_color(255, 127, 14)  # Orange for others
        
    pdf.cell(0, 10, f"EXECUTIVE VERDICT: {results['Final Verdict']}", ln=True)
    pdf.set_text_color(0, 0, 0)  # Reset to Black
    pdf.ln(10)
    
    # Financial Breakdown Section
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "Financial Breakdown", ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y()) # Draw a divider line
    pdf.ln(5)
    
    pdf.set_font("helvetica", "", 12)
    pdf.cell(100, 8, f"Total Investment:", border=0)
    pdf.cell(0, 8, f"${results['Total Investment']:,.2f}", border=0, ln=True)
    
    pdf.cell(100, 8, f"Estimated Flip Profit:", border=0)
    pdf.cell(0, 8, f"${results['Estimated Flip Profit']:,.2f}", border=0, ln=True)
    
    pdf.cell(100, 8, f"Flip ROI:", border=0)
    pdf.cell(0, 8, f"{results['Flip ROI (%)']}%", border=0, ln=True)
    
    pdf.cell(100, 8, f"Annual Net Operating Income (NOI):", border=0)
    pdf.cell(0, 8, f"${results['Annual NOI']:,.2f}", border=0, ln=True)
    
    pdf.cell(100, 8, f"Cap Rate:", border=0)
    pdf.cell(0, 8, f"{results['Cap Rate (%)']}%", border=0, ln=True)
    pdf.ln(10)
    
    # Insert the Chart
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "Capital Allocation", ln=True)
    
    # x and y coordinates position the image cleanly on the page
    pdf.image(image_filename, x=40, y=pdf.get_y(), w=120)
    
    # Output the file
    pdf.output(output_filename)
    print(f"PIPELINE COMPLETE: PDF successfully generated as '{output_filename}'")

# --- EXECUTE THE FULL PIPELINE ---
if __name__ == "__main__":
    # 1. The Input (Simulating the web form)
    test_payload = {
        "asking_price": 100000,
        "repair_costs": 20000,
        "after_repair_value": 160000,
        "monthly_rent": 1200,
        "closing_costs": 8000
    }
    
    # 2. Validate Data (Layer 1)
    validated_data = PropertyAnalysisInput(**test_payload)
    
    # 3. Calculate Math (Layer 2)
    financial_results = analyze_property(validated_data)
    
    # 4. Generate Visuals (Layer 3)
    chart_file = "investment_breakdown.png"
    generate_investment_pie_chart(validated_data, filename=chart_file)
    
    # 5. Print PDF (Layer 4)
    create_pdf_report(financial_results, chart_file)