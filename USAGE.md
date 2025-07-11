
# Использование NataLeePusherForAuroraOS

## Конфигурация
Пример файла `config.yaml`:
```yaml
server: "https://push.example.com"
token: "your_secret_token"
devices:
  - id: "device1"
  - id: "device2"
```

## Запуск
```bash
./pusher --config config.yaml
```

## Параметры командной строки
- `--config <file>` — путь до файла конфигурации
- `--verbose` — подробный вывод

## Примеры
```bash
./pusher --config my_config.yaml --verbose
```
