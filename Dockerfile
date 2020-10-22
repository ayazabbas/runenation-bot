FROM python:3.8.5-slim-buster

RUN mkdir /bot
WORKDIR /bot
COPY bot/ ./
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]