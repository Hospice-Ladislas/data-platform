FROM python:3.10.13-slim AS builder
LABEL authors="d_hos"

ENV APP_HOME /app

# Define environment variable
ENV PORT 8080

# Set the working directory in the container
WORKDIR $APP_HOME

# Copy the current directory contents into the container at /app
COPY src/. ./

# Run app.py when the container launches
CMD ["python", "generic-collect-api-data.py"]