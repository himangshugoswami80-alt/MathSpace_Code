from fastapi import FastAPI,WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .config import settings
from .db import Base,engine
from . import models
from .math_service import solve,differentiate,integrate
Base.metadata.create_all(engine)
app=FastAPI(title='MathSpace API',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=[settings.cors_origins],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
class Expr(BaseModel): expression:str
class Question(BaseModel): question:str
@app.get('/api/v1/health')
def health(): return {'status':'ok'}
@app.post('/api/v1/math/solve')
def math_solve(data:Expr): return {'result':solve(data.expression)}
@app.post('/api/v1/math/differentiate')
def math_diff(data:Expr): return {'result':differentiate(data.expression)}
@app.post('/api/v1/math/integrate')
def math_integrate(data:Expr): return {'result':integrate(data.expression)}
@app.post('/api/v1/ai/ask')
def ai_ask(data:Question): return {'answer':f'Development AI provider received: {data.question}\nConnect an LLM provider through environment variables for production answers.'}
@app.websocket('/ws')
async def websocket(ws:WebSocket):
    await ws.accept()
    await ws.send_json({'type':'connected','message':'MathSpace realtime channel'})
    try:
        while True:
            msg=await ws.receive_text()
            await ws.send_json({'type':'echo','message':msg})
    except Exception:
        await ws.close()
