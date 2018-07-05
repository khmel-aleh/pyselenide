FROM openjdk:8

MAINTAINER Aleh Khmel <khmel.aleh@gmail.com>

ENV ALLURE_PATH /opt/allure

WORKDIR $ALLURE_PATH

RUN curl -O -J -L https://bintray.com/qameta/generic/download_file?file_path=io%2Fqameta%2Fallure%2Fallure%2F2.6.0%2Fallure-2.6.0.tgz \
    && tar -zxf allure-2.6.0.tgz \
    && rm -f allure-2.6.0.tgz \

EXPOSE 80
VOLUME [/allure]

ENTRYPOINT ["./allure-2.6.0/bin/allure"]
CMD ["serve", "-p", "80", "/allure"]