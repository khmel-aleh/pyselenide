# Common Framework

This is the common testing framework on python.

## Run tests

#### Local Run
 - Install requirements via `pip install requirements.txt`.
 - Make changes in the configuration [default.json](config/default.json)
 - Run command `pybot -i debug -b Debug.log -d Debug -P . -P core tests`

#### Via Docker
 - Build docker image `docker build -t framework docker/framework`
 - Make changes in the configuration [default.json](config/default.json)
 - Run container `docker run --rm -v $(pwd):/opt/framework framework`

 #### Serve Allure Report
 - Build docker image `docker build -t allure_report docker/allure_report`
 - Run container `docker run --rm -v $(pwd)/allure_report/:/allure -p 80:80 allure_report`
