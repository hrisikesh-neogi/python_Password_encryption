FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD uvicorn --workers=1 --host 0.0.0.0 --port $PORT app:app







