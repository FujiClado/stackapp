FROM python:3.7.3-alpine3.10

RUN mkdir /usr/app

WORKDIR  /usr/app

COPY .  .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["app.py"] 
