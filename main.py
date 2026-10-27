from fastapi import FastAPI
from fastapi.responses import FileResponse
from schema import PropertyAnalysisInput
from engine import analyze_property
from chart_factory import generate_investment_pie_chart, generate_cashflow_bar_chart
from pdf_printer import create_pdf_report

app = FastAPI(
    title="Automated Decision Engine",
    description="API for processing property variables and returning a multi-chart PDF report."
)

@app.post("/api/generate-pdf")
def generate_pdf_endpoint(data: PropertyAnalysisInput):
    financial_results = analyze_property(data)
    
    pie_file = generate_investment_pie_chart(data, filename="investment_breakdown.png")
    bar_file = generate_cashflow_bar_chart(financial_results["five_year_noi"], filename="cashflow_projection.png")
    
    pdf_file = create_pdf_report(
        financial_results, 
        pie_chart_path=pie_file, 
        bar_chart_path=bar_file, 
        output_filename="Executive_Report.pdf"
    )
    
    return FileResponse(
        path=pdf_file, 
        filename="Executive_Analysis_Report.pdf", 
        media_type="application/pdf"
    )
