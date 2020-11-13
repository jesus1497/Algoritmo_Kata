FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    flake8 \
    mutmut \
    pytest
    