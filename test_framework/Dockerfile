FROM python:3.9
RUN mkdir -p /tests
WORKDIR /tests
COPY . /tests
RUN  pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ["pytest","tests.py"]



