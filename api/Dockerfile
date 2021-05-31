FROM python:3
WORKDIR /api
COPY requirements.txt /api
RUN pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python", "./users.py"]
# Мы хотим пробрасывать порт 8080
EXPOSE 8080
COPY . /api
