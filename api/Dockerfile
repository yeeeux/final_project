FROM python:3
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
#&& \
#    apt-get update && \
#        apt-get -y install python3-pandas
COPY . /app
ENTRYPOINT ["python3"]
CMD ["users.py"]