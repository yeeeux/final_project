FROM python:3
WORKDIR /tests
COPY requirements.txt /tests
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /tests
ENTRYPOINT ["python3"]
CMD ["test_users_without_fixtures.py"]
