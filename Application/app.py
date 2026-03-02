from fastapi import FastAPI
import uvicorn as uv

app=FastAPI()


@app.get("/")
async def home():
    return {"data":"Hello World cd-3"}




if __name__=="__main__":
    uv.run("app:app",host="0.0.0.0",port=8000,reload=True)
