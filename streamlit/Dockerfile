FROM python:3.10

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["streamlit", "run", "ml_app_with_fastapi.py", "--server.port", "8501"]