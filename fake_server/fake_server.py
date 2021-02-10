from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/auth')
async def auth(request):
    """
    Returns fake authorization token
    """
    login = request.rel_url.query['login']
    password = request.rel_url.query['password']

    response = {
        "status": "OK",
        "token": "dsfd79843r32d1d3dx23d32d"
    }

    return web.json_response(response)


@routes.get('/get-user/{username}')
async def get_user(request):
    """
    Returns fake user info
    """
    token = request.rel_url.query["token"]
    if token != "dsfd79843r32d1d3dx23d32d":
        return web.json_response({
            "status": "ERROR"
        })

    username = request.match_info["username"]
    if username != "ivanov":
        return web.json_response({
            "status": "NOT FOUND"
        })

    response = {
        "status": "OK",
        "active": "1",
        "blocked": False,
        "created_at": 1587457590,
        "id": 23,
        "name": "Ivanov Ivan",
        "permissions": [
            {
                "id": 1,
                "permission": "comment"
            },
            {
                "id": 2,
                "permission": "upload photo"
            },
            {
                "id": 3,
                "permission": "add event"
            }
        ]
    }

    return web.json_response(response)


@routes.post('/user/{userid}/update')
async def update_user(request):
    """
    Update user info
    """
    token = request.rel_url.query['token']

    response = {
        "status": "OK",
    }

    return web.json_response(response)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
