import aiohttp
import asyncio

API_URL = 'http://localhost:8080'


async def auth_request(login: str, password: str) -> dict:
    """
    Authorization request

    :param login: user login
    :param password: password
    :return: authorization token or status
    """
    async with aiohttp.ClientSession() as session:
        params = {'login': login, 'password': password}
        async with session.get(API_URL + '/auth',
                               params=params) as resp:
            token = await resp.json()
            return token


async def user_info_request(username: str, token: str) -> dict:
    """
    Authorization request

    :param username: username
    :param token: authorization token
    :return: user info or status
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL + '/get-user/' + username,
                               params={'token': token}) as resp:
            user_info = await resp.json()
            return user_info


async def update_user_info_request(user_id: int, token: str) -> dict:
    """
    Authorization request

    :param user_id: user identifier
    :param token: authorization token
    :return: user info or status
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL + '/user/' + str(user_id) + '/update',
                                params={'token': token}) as resp:
            response = await resp.json()
            return response


async def main():
    token = await auth_request(login="test", password="12345")
    print(token)
    user_info = await user_info_request(username="ivanov", token=token.get("token"))
    print(user_info)
    update_user_request_status = await update_user_info_request(user_id=23, token=token.get("token"))
    print(update_user_request_status)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
