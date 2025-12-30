# 1. Беремо базовий образ Python 3.11 (легка версія)
FROM python:3.11-slim

# 2. Вимикаємо створення зайвих .pyc файлів та буферизацію (щоб логи бачити відразу)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Створюємо робочу папку всередині контейнера
WORKDIR /app

# 4. Спочатку копіюємо файл залежностей (щоб Докер закешував цей крок)
COPY requirements.txt .

# 5. Встановлюємо бібліотеки
RUN pip install --no-cache-dir -r requirements.txt

# 6. Тепер копіюємо весь інший код проекту в контейнер
COPY . .

# 7. Запускаємо сервер
# Увага: app.main:app — бо папка app, файл main.py, об'єкт app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]