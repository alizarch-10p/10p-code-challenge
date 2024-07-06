FROM python:3.8-slim

WORKDIR /code

COPY ./app /code/app

RUN pip install --upgrade pip
RUN pip install -r /code/app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
