import matplotlib.pyplot as plt
from schema import PropertyAnalysisInput

def generate_investment_pie_chart(data: PropertyAnalysisInput, filename="investment_breakdown.png"):
    """Generates a corporate pie chart of capital allocation and saves it as an image."""
    
    # Map the validated data to chart categories
    labels = ['Purchase Price', 'Repair Costs', 'Closing Costs']
    sizes = [data.asking_price, data.repair_costs, data.closing_costs]
    
    # Corporate styling (Blue, Orange, Green)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    explode = (0.05, 0, 0) # Highlight the purchase price slice

    # Build the chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
           autopct='%1.1f%%', shadow=False, startangle=140, 
           textprops={'fontsize': 11})
    
    ax.axis('equal') # Ensure it draws as a perfect circle
    plt.title('Total Capital Allocation Breakdown', fontsize=14, fontweight='bold', pad=20)
    
    # Save the file to your workspace
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    print(f"Chart generated successfully: '{filename}'")
    plt.close()

# --- TEST THE CHART FACTORY ---
if __name__ == "__main__":
    test_payload = {
        "asking_price": 100000,
        "repair_costs": 20000,
        "after_repair_value": 160000,
        "monthly_rent": 1200,
        "closing_costs": 8000
    }
    
    validated_data = PropertyAnalysisInput(**test_payload)
    generate_investment_pie_chart(validated_data)