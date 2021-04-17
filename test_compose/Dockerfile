FROM python:3
WORKDIR /app
COPY requirements_test.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
CMD ["users.py"]