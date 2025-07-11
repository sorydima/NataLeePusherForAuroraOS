
# Конфигурация NataLeePusherForAuroraOS

Файл конфигурации должен быть в формате YAML.

## Параметры:
- `server` — адрес сервера отправки уведомлений (обязателен).
- `token` — авторизационный токен (обязателен).
- `devices` — список устройств (обязателен).

## Пример:
```yaml
server: "https://push.example.com"
token: "your_secret_token"
devices:
  - id: "device1"
  - id: "device2"
```
