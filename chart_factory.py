import matplotlib
matplotlib.use("Agg")  # Prevents GUI thread warnings on web servers
import matplotlib.pyplot as plt
from schema import PropertyAnalysisInput

def generate_investment_pie_chart(data: PropertyAnalysisInput, filename: str = "investment_breakdown.png") -> str:
    labels = ['Asking Price', 'Repair Costs', 'Closing Costs']
    sizes = [data.asking_price, data.repair_costs, data.closing_costs]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.set_title("Total Capital Allocation Breakdown", fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(fig)
    return filename

def generate_cashflow_bar_chart(five_year_noi: list, filename: str = "cashflow_projection.png") -> str:
    years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
    
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(years, five_year_noi, color='#2ca02c', width=0.5)
    
    ax.set_title("5-Year Projected Net Operating Income (NOI)", fontsize=13, fontweight='bold')
    ax.set_ylabel("Annual NOI ($)")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add room above the tallest bar for text labels
    max_val = max(five_year_noi) if five_year_noi and max(five_year_noi) > 0 else 1000
    ax.set_ylim(0, max_val * 1.18)
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'${height:,.0f}',
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha='center', va='bottom', fontsize=9, fontweight='bold'
        )
                    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(fig)
    return filename
