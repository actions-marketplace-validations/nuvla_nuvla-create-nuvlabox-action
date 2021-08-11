FROM python:3-alpine

WORKDIR /opt

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "/action.py" ]