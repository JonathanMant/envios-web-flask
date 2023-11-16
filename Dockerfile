FROM python:3.10-slim-buster as test


RUN apt-get update \
    && apt-get install -y libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /test
COPY . /test
COPY /requirements/requirements.t-xt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


FROM test
RUN echo "Building image..."
WORKDIR /app
COPY . $WORKDIR

CMD [ "python3", "-m" , "flask", "--app", "main.py",  "run", "--host=0.0.0.0"]