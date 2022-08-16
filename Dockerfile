FROM python:3.9-alpine

WORKDIR /code

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
