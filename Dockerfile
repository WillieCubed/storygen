# Dockerfile for deployment
FROM ubuntu:22.04

# Install Python 3.10
RUN apt update && apt install -y \
    python3.10 \
    python3-pip \
    ## Headers for box2d-py
    python3-dev

COPY . /usr/local/src/app

WORKDIR /usr/local/src/app

# Install all dependencies
## Copy file first to take advantage of caching
COPY requirements.txt .

## Now install general package requirements
RUN pip install -r requirements.txt

## Add package CLI to executables
RUN pip install -e .

# By default, run the demo
CMD ["python3", "app.py"]