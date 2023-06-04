FROM python:3.9-alpine

WORKDIR /app/

ADD . .

ENV TZ=Europe/Moscow
ENV DEBIAN_FRONTEND=noninteractive

RUN apk update && apk add tzdata && apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip && \
    pip install -U --pre aiogram && \
    apk del postgresql-dev gcc python3-dev musl-dev && \
    pip install psycopg2-binary


CMD ["./run_bot_post_english_phrases.py"]
ENTRYPOINT ["python3"]