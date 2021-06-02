FROM python:3.9
RUN mkdir -p /api
WORKDIR /api
COPY . /api
RUN pip3 install -r docker_requirements.txt --no-cache-dir
ENTRYPOINT ["python", "users.py"]
# We want port 8000
EXPOSE 8000

