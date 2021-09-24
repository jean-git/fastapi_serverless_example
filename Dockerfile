FROM python:3.8

COPY  ./requirements.txt /
RUN pip install -r /requirements.txt
#COPY  ./app /app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
 