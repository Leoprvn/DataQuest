####  docker build -t praveenko/pyspark_data_quest:latest .
####  docker run -it praveenko/pyspark_data_quest:latest

### 1. Get Linux
FROM alpine:3.7

### 2. Get Java via the package manager
RUN apk update \
&& apk upgrade \
&& apk add --no-cache bash \
&& apk add --no-cache --virtual=build-dependencies unzip \
&& apk add --no-cache curl \
&& apk add --no-cache openjdk8-jre \
&& apk add --no-cache git

### 3. Get Python, PIP
RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

### 4. Get pyspark, pytest & set up the pyspark with compression native lib
RUN pip install pyspark pytest \
&& cd /lib/ \
&& ln -s ld-musl-x86_64.so.1 ld-linux-x86-64.so.2

### 5.Get the code repo into the container
RUN git clone https://github.com/Leoprvn/DataQuest 

#### 6.Set up the Environment variable
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

#### 7. Working Directory 
WORKDIR DataQuest/scripts
