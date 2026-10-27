from pydantic import BaseModel, Field, ValidationError

# Layer 1: The Input Schema
class PropertyAnalysisInput(BaseModel):
    asking_price: float = Field(..., gt=0, description="The purchase price of the property in USD")
    repair_costs: float = Field(..., ge=0, description="Estimated cost of renovations in USD")
    after_repair_value: float = Field(..., gt=0, description="Estimated sale price after repairs (ARV) in USD")
    monthly_rent: float = Field(..., ge=0, description="Estimated monthly rental income in USD")
    closing_costs: float = Field(..., ge=0, description="Holding, closing, and administrative fees in USD")
    annual_rent_growth_rate: float = Field(default=3.0, ge=0, le=50, description="Annual rent growth percentage")

print("Schema Defined Successfully.\n")

# --- TEST 1: Valid Data (What the UI will send to the backend) ---
valid_payload = {
    "asking_price": 100000,
    "repair_costs": 20000,
    "after_repair_value": 160000,
    "monthly_rent": 1200,
    "closing_costs": 8000
}

try:
    clean_data = PropertyAnalysisInput(**valid_payload)
    print("Test 1 Passed: Valid data accepted.")
    # You can access variables cleanly like this:
    print(f"Loaded Asking Price: ${clean_data.asking_price:,.2f}\n")
except ValidationError as e:
    print(e)

# --- TEST 2: Invalid Data (Testing the guardrails) ---
# We intentionally pass a negative price and a text string to trigger the firewall.
invalid_payload = {
    "asking_price": 50000,  # Fails: Must be greater than 0 (gt=0)
    "repair_costs": "20000",  # Fails: Must be a float/number
    "after_repair_value": 160000,
    "monthly_rent": 1200,
    "closing_costs": 8000
}

try:
    print("Running Test 2 with bad data...")
    bad_data = PropertyAnalysisInput(**invalid_payload)
except ValidationError as e:
    print("Test 2 Passed: Pydantic successfully blocked the bad data. Error details:")
    print(e)
