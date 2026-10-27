from pydantic import BaseModel, Field

class PropertyAnalysisInput(BaseModel):
    asking_price: float = Field(..., gt=0, description="Purchase price of the property ($)")
    repair_costs: float = Field(..., ge=0, description="Estimated renovation costs ($)")
    after_repair_value: float = Field(..., gt=0, description="Estimated value after repairs (ARV) ($)")
    monthly_rent: float = Field(..., ge=0, description="Estimated monthly rental income ($)")
    closing_costs: float = Field(..., ge=0, description="Holding and closing costs ($)")
    annual_rent_growth_rate: float = Field(default=3.0, ge=0, le=50, description="Annual compounding rent growth (%)")

if __name__ == "__main__":
    sample = PropertyAnalysisInput(
        asking_price=100000,
        repair_costs=20000,
        after_repair_value=160000,
        monthly_rent=1200,
        closing_costs=8000,
        annual_rent_growth_rate=3.0
    )
    print("Schema Validated Successfully:", sample.model_dump())
