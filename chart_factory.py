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

import matplotlib.pyplot as plt
from schema import PropertyAnalysisInput

def generate_investment_pie_chart(data: PropertyAnalysisInput, filename="investment_breakdown.png"):
    labels = ['Asking Price', 'Repair Costs', 'Closing Costs']
    sizes = [data.asking_price, data.repair_costs, data.closing_costs]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.set_title("Total Capital Allocation Breakdown", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(fig)
    return filename

# NEW CHART FUNCTION ADDED BELOW:
def generate_cashflow_bar_chart(five_year_noi: list, filename="cashflow_projection.png"):
    years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
    
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(years, five_year_noi, color='#2ca02c', width=0.5)
    
    ax.set_title("5-Year Projected Net Operating Income (NOI)", fontsize=13, fontweight='bold')
    ax.set_ylabel("Annual NOI ($)")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Stamp exact dollar values on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'${height:,.0f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
                    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(fig)
    return filename

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
