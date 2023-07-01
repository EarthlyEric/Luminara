FROM python:3.9-alpine3.17
ENV enable_beta=False


RUN apk update && \
    apk upgrade 
RUN apk add openjdk13 
RUN apk add gcc
RUN apk add build-base linux-headers

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install pipenv
RUN pipenv install --system --deploy
COPY . .
EXPOSE 443
EXPOSE 2333
CMD [ "python3", "bot.py" ]