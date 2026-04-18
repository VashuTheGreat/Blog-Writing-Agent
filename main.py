from dotenv import load_dotenv
load_dotenv()

from src.logger import *
from api.app import app


# if __name__=="__main__":
#     import uvicorn as uv
#     uv.run("main:app",host="0.0.0.0",port=7860,reload=True)