FROM python:3.9-slim
LABEL author='Earlinn' version=1
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "django_stripe_api.wsgi:application", "--bind", "0:8000"]
