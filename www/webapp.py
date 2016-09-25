import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    #return web.Response(body=b'<h1>Awesome</h1>')  if use this , will return a file to browser
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8')
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    #logging.info('The app is ',app)
    app_addroute=app.router.add_route('GET', '/', index)
    #logging.info('the add_route for app is ',app_addroute)
    sr = loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    print("loop.create_server is ", sr)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    print("return srv of yield from loop create_server is ",srv)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
print('before new loop start:')
loop = asyncio.get_event_loop()
print('The loop asyncio is :',loop)
loop.run_until_complete(init(loop))
print('the function of init(loop) is:',init(loop))
print('start run_forever here')
loop.run_forever()
print('end run_forever here')