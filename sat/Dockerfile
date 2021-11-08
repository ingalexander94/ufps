FROM python:3.8.10

RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio-dev \
    && apt-get -y install \
        make linux-headers-amd64 libffi-dev libjpeg-dev libz-dev \
        gcc python3-dev musl-dev \
    && mkdir -p /opt/data/src

ADD ./oracle-instantclient/ /opt/data
ADD ./install-instantclient.sh /opt/data
ADD ./requirements.txt /opt/data

WORKDIR /opt/data

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

ENV OCI_HOME=/opt/oracle/instantclient
ENV OCI_LIB_DIR=/opt/oracle/instantclient
ENV OCI_INCLUDE_DIR=/opt/oracle/instantclient/sdk/include

COPY requirements.txt requirements.txt

RUN chmod +x ./install-instantclient.sh \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8080