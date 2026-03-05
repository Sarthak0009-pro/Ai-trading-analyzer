from fastapi import FastAPI, UploadFile, File
import strategy

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Trading Analyzer Running"}

@app.post("/analyze")
async def analyze_chart(chart: UploadFile = File(...)):

    image = await chart.read()

    result = strategy.generate_trade(image)

    return result
