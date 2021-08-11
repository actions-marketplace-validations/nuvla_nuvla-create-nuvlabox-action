FROM python:3-alpine

COPY action.py /

ENTRYPOINT [ "/action.py" ]