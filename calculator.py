from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate/")
async def calculate_post(request: CalculationRequest):
    return calculate(request.num1, request.num2, request.operation)

@app.get("/calculate/")
async def calculate_get(
    num1: float = Query(..., description="The first number"),
    num2: float = Query(..., description="The second number"),
    operation: str = Query(..., description="The operation: add, sub, mul, div")
):
    return calculate(num1, num2, operation)

def calculate(num1: float, num2: float, operation: str):
    operation = operation.lower()
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Supported operations are add, sub, mul, and div.")
    return {"result": result}

# To run the application, use: uvicorn calculator_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
