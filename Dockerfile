FROM python:3.8
LABEL maintainer="Edgardo Peregrino"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -e .
RUN pip install -e ".[dev]"

# command to run on container start
CMD [ "pserve", "development.ini", "--reload", "--server-name", "main"]