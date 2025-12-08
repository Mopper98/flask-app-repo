# базовый образ с Python
FROM python:3.11-slim

# рабочая директория
WORKDIR /app

# копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копируем приложение
COPY . .

# назначаем порт, который документируем (не обязателен, но полезен)
EXPOSE 5000

# запускаем приложение
CMD ["python", "app.py"]

