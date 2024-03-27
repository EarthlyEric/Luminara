FROM python:3.10-alpine3.17
ENV betaMode=False
ENV deployToken default_value

RUN apk update && \
    apk upgrade 
RUN apk add build-base linux-headers

WORKDIR /app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN  pip3 install pipenv  \
    && pipenv requirements > requirements.txt \
    && pip3 install -r requirements.txt
COPY . .
EXPOSE 443
EXPOSE 2333
CMD [ "python3", "bot.py" ]