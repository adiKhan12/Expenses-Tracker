FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
