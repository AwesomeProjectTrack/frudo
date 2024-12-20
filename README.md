# This document does not exists

Библиотека для генерации синтетических документов на русском языке. Используется только для генерации данных для обучения/валидации VLM моделей.
Позволяет сгенерировать следующие типы документов:
- паспорта
- снилс
- ИНН
- водительские права
- многостраничные документы
- договора
- различные справки

## Установка библиотек
### Poetry
В данной библиотеке используется poetry. Чтобы установить зависимости, необходимо сделать следюущие шаги:
1. Инициализировать venv командной
```shell
poetry shell
```
2. Установить библиотеки, запустив команду
```shell
poetry install --no-root
```
### VSCode Remote Container
1. Установить [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. Установить [Dev Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Откройте Command Pallete, выберите Dev Container: Reopen in Container
4. У вас автоматически откроется папка проекта и запустится установка библиотек.
5. Готово, можно разрабатывать и пушить прямо из контейнера, он подтянет ваши .ssh ключи

### PyCharm Pro Remote Container
1. Установить [Dev Container](https://plugins.jetbrains.com/plugin/21962-dev-containers)
2. File > Remote Development > Dev Container > New Dev Container > From local project
3. Укажите path to devcontainer.json
4. Нажмите Build Container and Continue
5. Начнется сборка. После сборки можно нажать кнопку Connect и подключиться внутрь контейнера

## Запуск
1. Откройте файл src/pipeline.py и измените там __main__ в соответствии с вашими запросами. Пример
```shell
if __name__ == "__main__":
    Pipeline.generate(
        num_samples=100,
        document_types=[SnilsDocumentGenerator()],
        output_formater=MTVQAOutputFormater(),
    )
```
2. Выполните команду
```shell
python src/pipeline.py
```
