# Dockerfile
FROM --platform=linux/x86_64 python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    poppler-utils \
    locales-all && \
    apt-get clean

# Install Poetry globally
RUN pip install poetry