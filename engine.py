from schema import PropertyAnalysisInput

def analyze_property(data: PropertyAnalysisInput) -> dict:
    # 1. Capital & Flip Calculations
    total_investment = data.asking_price + data.repair_costs + data.closing_costs
    flip_profit = data.after_repair_value - total_investment
    flip_roi = (flip_profit / total_investment) * 100
    
    # 2. Year 1 Rental Calculations (Assuming 20% Operating Expense Ratio)
    annual_gross_rent = data.monthly_rent * 12
    annual_noi = annual_gross_rent * 0.80
    rental_yield = (annual_noi / total_investment) * 100
    
    # 3. 5-Year Compounding Cash Flow Projection
    growth_multiplier = 1 + (data.annual_rent_growth_rate / 100.0)
    five_year_noi = []
    current_noi = annual_noi
    
    for _ in range(5):
        five_year_noi.append(round(current_noi, 2))
        current_noi *= growth_multiplier
        
    total_5yr_cashflow = sum(five_year_noi)
    
    # 4. Strategic Decision Matrix
    if flip_roi >= 20.0:
        verdict = "FIX & FLIP (High Short-Term ROI)"
    elif rental_yield >= 8.0:
        verdict = "BUY & HOLD (Strong Cash Flow Yield)"
    else:
        verdict = "WALK AWAY (Below Hurdle Rates)"
        
    return {
        "total_investment": round(total_investment, 2),
        "flip_profit": round(flip_profit, 2),
        "flip_roi": round(flip_roi, 2),
        "annual_noi": round(annual_noi, 2),
        "rental_yield": round(rental_yield, 2),
        "five_year_noi": five_year_noi,
        "total_5yr_cashflow": round(total_5yr_cashflow, 2),
        "verdict": verdict
    }
