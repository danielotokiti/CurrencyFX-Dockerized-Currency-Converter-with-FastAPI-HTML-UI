from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure static files (using your exact 'Static' directory name)
app.mount("/Static", StaticFiles(directory="Static"), name="static")

# Configure templates (using your exact 'Templates' directory name)
templates = Jinja2Templates(directory="Templates")

class ConversionResult(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    result: float
    rate: float
    success: bool
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/convert", response_model=ConversionResult)
async def convert(
    from_currency: str = Query(..., min_length=3, max_length=3, example="USD"),
    to_currency: str = Query(..., min_length=3, max_length=3, example="EUR"),
    amount: float = Query(1.0, gt=0)
):
    api_key = os.getenv("EXCHANGERATE_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API key missing")

    url = f"https://api.exchangerate.host/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if not data.get('success'):
            raise HTTPException(
                status_code=400,
                detail=data.get('error', {}).get('info', 'Conversion failed')
            )
        
        result = round(data['result'], 4)
        rate = round(data['result'] / amount, 6)
        
        return {
            "from_currency": from_currency.upper(),
            "to_currency": to_currency.upper(),
            "amount": amount,
            "result": result,
            "rate": rate,
            "success": True,
            "message": "Success"
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Service error: {str(e)}")