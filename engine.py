from schema import PropertyAnalysisInput

def analyze_property(data: PropertyAnalysisInput) -> dict:
    """Calculates ROI, Cap Rate, and generates an investment decision."""
    
    # 1. Core Financial Calculations
    total_investment = data.asking_price + data.repair_costs + data.closing_costs
    flip_profit = data.after_repair_value - total_investment
    flip_roi = (flip_profit / total_investment) * 100
    
    # Assume 20% of rent goes to maintenance/vacancy for a realistic Net Operating Income (NOI)
    annual_gross_rent = data.monthly_rent * 12
    net_operating_income = annual_gross_rent * 0.80 
    cap_rate = (net_operating_income / total_investment) * 100
    
    # 2. Decision Logic Engine
    if flip_roi >= 20.0:
        verdict = "FIX & FLIP"
    elif cap_rate >= 8.0:
        verdict = "BUY & HOLD (RENT)"
    else:
        verdict = "HIGH RISK: WALK AWAY"
        
    # 3. Package the Results for the Chart Factory / PDF Printer
    return {
        "Total Investment": total_investment,
        "Estimated Flip Profit": flip_profit,
        "Flip ROI (%)": round(flip_roi, 2),
        "Annual NOI": net_operating_income,
        "Cap Rate (%)": round(cap_rate, 2),
        "Final Verdict": verdict
    }

# --- TEST THE ENGINE ---
if __name__ == "__main__":
    # The clean data payload simulating a user input
    test_payload = {
        "asking_price": 100000,
        "repair_costs": 20000,
        "after_repair_value": 160000,
        "monthly_rent": 1200,
        "closing_costs": 8000
    }
    
    # Validate the data using Layer 1 (Schema)
    validated_data = PropertyAnalysisInput(**test_payload)
    
    # Run the data through Layer 2 (Engine)
    results = analyze_property(validated_data)
    
    print("\n--- EXECUTIVE ANALYSIS REPORT ---")
    for key, value in results.items():
        if "Profit" in key or "Investment" in key or "NOI" in key:
            print(f"{key}: ${value:,.2f}")
        else:
            print(f"{key}: {value}")
    print("---------------------------------\n")