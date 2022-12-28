FROM python:3.8.14-slim

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY src /app/

EXPOSE 8000

CMD ["uvicorn", "main:api", "--host", "0.0.0.0"]
