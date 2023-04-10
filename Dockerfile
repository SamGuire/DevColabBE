FROM python:3.9 as base

WORKDIR /dev-colab-api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV PYTHONPATH "/dev-colab-api/app"


FROM base as debug
# Debug image reusing the base
# Install dev dependencies for debugging
RUN pip install debugpy
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


FROM base as prod
# Production image
RUN pip install gunicorn
COPY . .
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "app:app"]