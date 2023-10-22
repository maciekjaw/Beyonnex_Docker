FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

WORKDIR /tests

COPY pages /pages
COPY tests /tests

COPY requirements.txt /tests/
RUN pip install -r requirements.txt
CMD [ "pytest" ]