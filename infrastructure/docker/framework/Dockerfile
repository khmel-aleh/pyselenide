FROM ubuntu:14.04

MAINTAINER Aleh Khmel <khmel.aleh@gmail.com>

ENV TORS=/opt/framework

RUN apt-get update && \
    apt-get install -yqq \
        wget \
        python-pip && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /tmp/*

VOLUME [$TORS]

WORKDIR [$TORS]

CMD ["-i", "debug", "tests"]

ENTRYPOINT ["pybot", "-b", "Debug.log", "-d", "Debug", "-P", ".", "-P", "core"]
