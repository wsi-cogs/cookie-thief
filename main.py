from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest


async def steal(request):
    name = request.query.get("cookie", None)
    if name is None:
        raise HTTPBadRequest(text="Requires cookie param")
    return web.Response(text=request.cookies.get(name, ""))

app = web.Application()
app.add_routes([web.get('/', steal)])
web.run_app(app, host="0.0.0.0", port=8000)
