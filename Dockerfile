# Base image
FROM python:3.13-slim

# Ishchi papka
WORKDIR /app

# requirements copy va install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini copy qilish
COPY . .

# Static fayllarni collect qilish
RUN python manage.py collectstatic --noinput

# Gunicorn bilan run qilish
EXPOSE 8000
CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
