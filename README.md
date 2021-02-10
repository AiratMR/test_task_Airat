# Клиент для тестового API

## Запуск тестов:
1. Указать в файле settings.py url для тестого сервера в переменной TEST_API_URL (http://localhost:8080 по умолчанию);
2. Запустить тестовый сервер командой: ```python fake_server/fake_server.py```
3. Запустить тесты командой: ```pytest client_app/integration_tests.py```