FROM apache/airflow:3.0.0

USER root

# install cx_Oracle
RUN apt-get update && \
    apt-get install -y libaio1 unzip gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# zip file and install cx_Oracle client
COPY install/instantclient-basic-linux.x64-23.8.0.25.04.zip /opt/oracle/
RUN rm -rf * && \
    unzip -q -o /opt/oracle/instantclient-basic-linux.x64-23.8.0.25.04.zip -d /opt/oracle && \
    rm /opt/oracle/instantclient-basic-linux.x64-23.8.0.25.04.zip

# install java
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk curl gcc python3-dev libffi-dev libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN apt-get update && \
#    apt-get install -y wget gnupg && \
#    mkdir -p /etc/apt/keyrings && \
#    wget -O /etc/apt/keyrings/adoptium.asc https://packages.adoptium.net/artifactory/api/gpg/key/public && \
#    echo "deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://packages.adoptium.net/artifactory/deb bookworm main" | tee /etc/apt/sources.list.d/adoptium.list && \
#    apt-get update && \
#    apt-get install -y temurin-11-jdk && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

# location java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
#ENV JAVA_HOME=/usr/lib/jvm/temurin-11-jdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# location oracle
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_23_8

RUN mkdir -p /opt/spark/jars
RUN curl -L -o /opt/spark/jars/hadoop-aws-3.3.6.jar https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar && \
    curl -L -o /opt/spark/jars/aws-java-sdk-bundle-1.12.787.jar https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.787/aws-java-sdk-bundle-1.12.787.jar && \
    curl -L -o /opt/spark/jars/ojdbc11.jar https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc11/21.9.0.0/ojdbc11-21.9.0.0.jar

USER airflow

# install cx_Oracle
RUN pip install --no-cache-dir --no-build-isolation cx_Oracle==8.3.0

# install oracle
RUN pip install --no-cache-dir apache-airflow-providers-oracle

# install excel
RUN pip install --no-cache-dir openpyxl

# install pyspark
RUN pip install --default-timeout=1200 --no-cache-dir pyspark==4.0.0

# install my_minio & boto3
RUN pip install --no-cache-dir minio boto3

# file dataset
COPY ./dataset /opt/airflow/dataset
ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/dataset"

