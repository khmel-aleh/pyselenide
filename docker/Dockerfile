FROM ubuntu:14.04

MAINTAINER Aleh Khmel <khmel.aleh@gmail.com>

ENV TORS=/opt/framework

ADD . .

# Customize sources
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe multiverse\n" > /etc/apt/sources.list && \
#    echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates main universe multiverse\n" >> /etc/apt/sources.list && \
#    echo "deb http://archive.ubuntu.com/ubuntu/ trusty-security main universe multiverse\n" >> /etc/apt/sources.list

# Install wget, unzip
RUN apt-get update && \
    apt-get install -yqq \
        wget \
        python-pip && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /tmp/*

VOLUME $TORS

WORKDIR $TORS

CMD ["tests"]

ENTRYPOINT ["pybot", "-i", "debug", "-b", "Debug.log", "-d", "Debug", "-P", ".", "-P", "core"]
