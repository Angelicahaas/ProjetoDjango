FROM python:3.7-alpine
RUN pip install --no-cache-dir "Django>=3.0.3,<4"
COPY django_demo/ /app/
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
CMD python /app/manage.py runserver 0.0.0.0:8000
