FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

WORKDIR /beyonnex

COPY pages /beyonnex/pages
COPY tests /beyonnex/tests

COPY requirements.txt /beyonnex/
RUN pip install -r requirements.txt
CMD [ "pytest" ]