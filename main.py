from fastapi import FastAPI,WebSocket,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
async def main_page(request:Request):
    return templates.TemplateResponse(
        request=request,name="temp",context={"testVar":'this is a test thing'}
    )

@app.websocket("/ws")
async def wss(websocket:WebSocket):
    await websocket.accept()
    while True:
        data=await websocket.receive_text()
        await websocket.send_text(f'{data}')
