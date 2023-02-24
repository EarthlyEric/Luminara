FROM python:3.9-alpine3.17
ENV enable_beta=False


RUN apk update && \
    apk upgrade 
RUN apk add openjdk13 
RUN apk add gcc

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 443
CMD [ "python3", "bot.py" ]