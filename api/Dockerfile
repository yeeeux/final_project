FROM python:3
WORKDIR /api
COPY requirements.txt /api
RUN pip3 install -r requirements.txt --no-cache-dir
#&& \
#    apt-get update && \
#        apt-get -y install python3-pandas
COPY . /api
ENTRYPOINT ["python3"]
CMD ["users.py"]