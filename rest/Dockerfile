# Используем официальный Python образ
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Сначала копируем только requirements.txt, чтобы использовать кеш Docker
COPY requirements.txt .

# Устанавливаем зависимости, включая gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Теперь копируем оставшиеся файлы
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт 8000 для входящих соединений
EXPOSE 8000

# Команда для запуска gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rest.wsgi:application"]
