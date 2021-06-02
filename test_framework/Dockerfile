FROM python:3.9
RUN mkdir -p /tests
WORKDIR /tests
COPY . /tests
RUN  pip3 install -r docker_requirements.txt --no-cache-dir
#RUN  ["--junitxml=reports/result.xml"]
ENV SERVICE_URL http://api:8000
ENTRYPOINT ["pytest","tests.py"]



