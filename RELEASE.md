
# Чеклист для релиза NataLeePusherForAuroraOS

1. Убедитесь, что все тесты проходят.
2. Обновите `CHANGELOG.md`.
3. Обновите номер версии.
4. Соберите бинарные файлы.
5. Создайте новый Git-тег:
```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```
6. Опубликуйте новый релиз на GitHub.
