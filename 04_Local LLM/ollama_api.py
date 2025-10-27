from fastapi import FastAPI, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from ollama import Client
from fastapi import Body

app = FastAPI()
client = Client(
    host='http://localhost:11434'
)

client.pull('gemma3:1b')

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: Request):
    try:
        if request.headers.get('content-type') == 'application/json':
            data = await request.json()
            message = data.get('message', '')
        else:
            message = (await request.form()).get('message', '')
            
        if not message:
            return {"error": "No message provided"}
            
        response = client.chat(model="gemma3:1b", messages=[
            { "role": "user", "content": message }
        ])
        
        return response['message']['content']
    except Exception as e:
        return {"error": str(e)}

@app.post("/chat/form")
def chat_form(message: str = Form(...)):
    try:
        response = client.chat(model="gemma3:1b", messages=[
            { "role": "user", "content": message }
        ])
        return response['message']['content']
    except Exception as e:
        return {"error": str(e)}