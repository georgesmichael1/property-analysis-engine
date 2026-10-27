from fastapi import FastAPI
from fastapi.responses import FileResponse
from schema import PropertyAnalysisInput
from engine import analyze_property
from chart_factory import generate_investment_pie_chart
from pdf_printer import create_pdf_report
import os

# Initialize the API
app = FastAPI(
    title="Automated Decision Engine",
    description="API for processing property variables and returning a PDF report."
)

@app.post("/api/generate-pdf")
def generate_pdf_endpoint(data: PropertyAnalysisInput):
    """
    Receives JSON input from a web client, runs the 4-layer pipeline, 
    and returns the generated PDF file.
    """
    
    # Layer 2: Run the math
    financial_results = analyze_property(data)
    
    # Layer 3: Generate the visual
    chart_file = "investment_breakdown.png"
    generate_investment_pie_chart(data, filename=chart_file)
    
    # Layer 4: Print the PDF
    pdf_file = "Executive_Report.pdf"
    create_pdf_report(financial_results, chart_file, output_filename=pdf_file)
    
    # Return the physical file over HTTP
    return FileResponse(
        path=pdf_file, 
        filename="Executive_Analysis_Report.pdf", 
        media_type="application/pdf"
    )