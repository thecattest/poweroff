from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from os import popen

app = FastAPI()
favicon_path = 'poweroff.ico'


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get('/', response_class=HTMLResponse)
async def root():
    return '''
    <div style="display: flex;justify-content: center;align-items: center;height: 100%;">
        <a href="/poweroff"><img src="favicon.ico"></a>
    </div>
    '''


@app.get('/poweroff')
async def root():
    # return popen('shutdown now --reboot').read()
    return popen('shutdown now --poweroff').read()
