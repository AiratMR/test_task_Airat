import aiohttp
import asyncio

from settings import API_URL


class Client:
    """
    Client for test api
    """
    def __init__(self, base_url):
        self._base_url = base_url

    async def auth_request(self, login: str, password: str) -> dict:
        """
        Authorization request

        :param login: user login
        :param password: password
        :return: authorization token or status
        """
        params = {'login': login, 'password': password}

        async with aiohttp.ClientSession() as session:
            async with session.get(self._base_url + '/auth',
                                   params=params) as response:
                token = await response.json()
                return token

    async def user_info_request(self, username: str, token: str) -> dict:
        """
        Get user info

        :param username: username
        :param token: authorization token
        :return: user info or status
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self._base_url + '/get-user/' + username,
                                   params={'token': token}) as response:
                user_info = await response.json()
                return user_info

    async def update_user_info_request(self, user_id: int, token: str, update_info: dict) -> dict:
        """
        Update user info

        :param user_id: user identifier
        :param token: authorization token
        :param update_info: user update info
                example:
                {
                    "active": "1",
                    "blocked": true,
                    "name": "Petr Petrovich",
                    "permissions": [
                        {
                            "id": 1,
                            "permission": "comment"
                        },
                    ]
                }
        :return: user info or status
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(self._base_url + '/user/' + str(user_id) + '/update',
                                    params={'token': token},
                                    json=update_info) as response:
                status = await response.json()
                return status


async def main():
    test_api_client = Client(API_URL)

    token = await test_api_client.auth_request(login="test", password="12345")
    print(token)

    user_info = await test_api_client.user_info_request(username="ivanov", token=token.get("token"))
    print(user_info)

    update_user_request_status = await test_api_client.update_user_info_request(
        user_id=23,
        token=token.get("token"),
        update_info={
            "active": "1",
            "blocked": True,
            "name": "Petr Petrovich",
            "permissions": [
                {
                    "id": 1,
                    "permission": "comment"
                },
            ]
        }

    )
    print(update_user_request_status)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
