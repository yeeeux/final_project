FROM python:3.9
RUN mkdir -p /tests
WORKDIR /tests
COPY . /tests
RUN  pip3 install -r requirements.txt --no-cache-dir
ENV SERVICE_URL = http://127.0.0.1:5000/
ENTRYPOINT ["pytest","tests.py"]



