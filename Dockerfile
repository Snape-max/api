# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.13.2

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the requirements
COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .


EXPOSE 4725/tcp

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "4725", "--workers", "4",  "app:app"]