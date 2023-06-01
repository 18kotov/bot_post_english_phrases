
FROM python:3.9-alpine

WORKDIR /app/

ADD . .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip && \
    pip install -U --pre aiogram && \
    apk del postgresql-dev gcc python3-dev musl-dev && \
    pip install psycopg2-binary


CMD ["./run_bot_post_english_phrases.py"]
ENTRYPOINT ["python3"]
