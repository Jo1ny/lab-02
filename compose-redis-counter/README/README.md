# Flask + Redis Counter (Docker Compose & Volumes)

Учебный проект для отработки персистетности данных (named volumes) и межконтейнерного взаимодействия в Docker Compose

## Архитектура

- **web**: Flask-приложение на Python 3.11, слушающее порт 5000. Собирается из локального 'Dockerfile'.
- **redis**: Официальный образ `redis:7-alpine`. Работает с включенным AOF (`--appendonly yes`).
- **redis_data**: Именованный том (named volume), примонтированный в `/data` контейнера Redis для сохранения данных между перезапусками.

## Запуск и проверка 

1. Сборка и фоновый запуск:
	bash
	`docker compose up -d --build`

2. Проверка работы счетчика:
	curl http://localhost:5000

3. Проверка персистентности:
	 bash
	 `docker compose down`
	 `docker compose up -d`
	 `curl http://localhost:5000` # значение счетчика продолжает расти

