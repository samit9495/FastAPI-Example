from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/calculate")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/rabbitorchicken")
async def get_number(hd: int = Form(...), lg: int = Form(...)):
    for r in range(hd + 1):
        c = hd - r
        if 2 * r + 4 * c == lg:
            return {"Rabbit": r, "Chicken": c}
    return "No solutions!"