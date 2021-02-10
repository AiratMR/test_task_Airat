from client import Client

from settings import TEST_API_URL


async def test_auth_request_ok() -> None:
    test_api_client = Client(TEST_API_URL)
    resp = await test_api_client.auth_request("test", "12345")

    assert resp["status"] == "OK"


async def test_user_info_request_ok() -> None:
    test_api_client = Client(TEST_API_URL)
    resp = await test_api_client.user_info_request("ivanov", "dsfd79843r32d1d3dx23d32d")

    assert resp["status"] == "OK"


async def test_user_info_request_not_found() -> None:
    test_api_client = Client(TEST_API_URL)
    resp = await test_api_client.user_info_request("sidorov", "dsfd79843r32d1d3dx23d32d")

    assert resp["status"] == "NOT FOUND"


async def test_user_info_request_error() -> None:
    test_api_client = Client(TEST_API_URL)
    resp = await test_api_client.user_info_request("ivanov", "dsfd79843r32d1d3dx23")

    assert resp["status"] == "ERROR"


async def test_update_user_info_ok() -> None:
    test_api_client = Client(TEST_API_URL)
    resp = await test_api_client.update_user_info_request(23, "dsfd79843r32d1d3dx23d32d",
                                                          {
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
    assert resp["status"] == "OK"
