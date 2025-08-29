# Q&A API Service

Сервис вопросов и ответов на FastAPI + PostgreSQL + Docker.

---

## 📂 Структура проекта

<pre>
qa_service/
├── alembic/ # Миграции Alembic
│ ├── versions/ # Файлы ревизий
│ └── env.py
├── app/
│ ├── api/
│ │ ├── questions.py # Роуты вопросов
│ │ └── answers.py # Роуты ответов
│ ├── core/
│ │ ├── db.py # SQLAlchemy engine и сессии
│ │ ├── config.py # Настройки приложения (Pydantic Settings)
│ │ └── logger.py # Логирование
│ ├── models/
│ │ ├── init.py
│ │ ├── questions.py
│ │ └── answers.py
│ ├── schemas/
│ │ ├── init.py
│ │ ├── questions_schema.py
│ │ └── answers_schema.py
│ └── main.py # FastAPI приложение
├── tests/
│ ├── conftest.py
│ ├── test_questions.py
│ └── test_answers.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
</pre>

---

## ⚙️ Установка и запуск через Docker

1. Сборка и запуск контейнеров:

```bash
docker-compose up --build

    Проверка доступности API:

    Healthcheck: http://localhost:8000/health

    Swagger UI: http://localhost:8000/docs
```

🗄 Миграции Alembic

Создание ревизии и применение миграций:

docker-compose run --rm web alembic revision --autogenerate -m "init models"
docker-compose run --rm web alembic upgrade head

    Таблицы questions и answers будут созданы в PostgreSQL.

## 📌 API Эндпоинты

Вопросы

Метод	URL	Описание
```Pre
GET	/questions/	Список всех вопросов
POST	/questions/	Создать новый вопрос
Пример: {"text": "Текст вопроса"}
GET	/questions/{id}	Получить вопрос и все ответы
DELETE	/questions/{id}	Удалить вопрос (каскадное удаление ответов)
```
Ответы

Метод	URL	Описание
```Pre
POST	/questions/{id}/answers/	Добавить ответ к вопросу
Пример: {"user_id": "uuid", "text": "Текст ответа"}
GET	/answers/{id}	Получить конкретный ответ
DELETE	/answers/{id}	Удалить ответ
```
## 📝 Логирование

    Все CRUD операции логируются через app/core/logger.py.

    Пример:
```bash
2025-08-29 12:00:01 [INFO] qa_service: Question created: id=1, text='Что такое FastAPI?'
2025-08-29 12:00:05 [INFO] qa_service: Answer created: id=1 for question_id=1 by user=123e4567
2025-08-29 12:00:10 [WARNING] qa_service: Tried to delete non-existent answer id=99
```
    [INFO] — успешные операции

    [WARNING] — предупреждения (например, объект не найден)

    [ERROR] — необработанные ошибки через глобальный exception handler

## 🧪 Тесты

Тесты находятся в tests/

Фикстуры используют SQLite in-memory.

Запуск тестов:
```bash
docker-compose run --rm web pytest -v
```
Проверяются:

    Создание и получение вопросов
  
    Добавление и удаление ответов
  
    Каскадное удаление вопросов с ответами

## 🚀 Особенности

    FastAPI + SQLAlchemy + PostgreSQL

    Pydantic

    Docker + docker-compose

    Миграции Alembic

    Логирование CRUD операций и ошибок

    Простые тесты с pytest

## 📦 Примечание

    Для локального подключения к базе (из PyCharm, DBeaver) используйте порт 5432 или измените в docker-compose.yml.

    Все миграции выполняются через контейнер web.
