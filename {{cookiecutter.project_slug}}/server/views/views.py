from fastapi import APIRouter
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter()



@router.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <html>
        <body>
            <div>
            Hello World
            </div>
        </body>
    </html>
    """