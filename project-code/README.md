# Twitter Analysis on Digital Ocean

* The service is hosted on DigitalOcean cloud at http://159.89.36.6:5000 

# Service Description

This RESTful service is used to perform twitter analysis using pyspark ml libraries. The service sucessfully
runs within the docker container as well. The docker container was launched from the DigitalOcean cloud platform.

You need to have a twitter api endpoint configured in restapi.py for the service to work. Spark needs to be installed on local machine.
* Download Spark
    `
    RUN curl -sL "http://www-us.apache.org/dist/spark/spark-$SPARK_VERSION/spark-2.1.2-bin-hadoop2.7.tgz" | tar -xz -C /usr/local
    `
# Instructions for Running the service manually

* Clone repository
    `
    git clone https://github.com/cloudmesh-community/hid-sp18-411.git
    `  

* Navigate to the project directory
    `
    cd /hid-sp18-411/project-code/
    `
    
* Install requirements
    `
    pip install -r requirements.txt
    `
* Runs Service
    `
    python3 /tweets/restapi.py
    `
##### Check the results using your browser
* The results are available at
    `
    http://127.0.0.1:5000
    `

# Instructions for Creating Docker image :

* Clone repository

    `
    git clone https://github.com/cloudmesh-community/hid-sp18-411.git
    `  

* Navigate to the project directory

    `
    cd /hid-sp18-411/project-code/
    `


# Docker Commands

* The docker container can be built with the command: 

    `
    sudo docker build -t [image_name] .
    `  
* The docker container can be stopped with the command: 

    `
    sudo docker container stop [container_id]
    `  
    
* The docker container can be executed with the command: 

    `
    sudo docker run -d -p 5000:5000 [image_name]
    `  


