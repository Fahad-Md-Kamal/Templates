# Use an official Python runtime as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Command to run your application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]







# # pull official base image
# FROM python:3.11-slim-buster

# # set working directory
# WORKDIR /usr/src/app


# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install system dependencies
# RUN apt-get update \
#   && apt-get -y install netcat gcc postgresql \
#   && apt-get clean

# # install python dependencies
# RUN pip install --upgrade pip
# # COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # add app
# COPY ./app ./app

