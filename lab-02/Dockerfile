FROM python:3.11-alpine

WORKDIR /app

# Устанавливаем зависимости прямо здесь (без requirements.txt для простоты лабы)
RUN pip install --no-cache-dir flask redis

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]