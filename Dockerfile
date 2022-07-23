FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app
EXPOSE 443

CMD [ "python", "bot.py" ]