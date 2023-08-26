FROM python:bookworm
WORKDIR /app
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt -r requirements-dev.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
