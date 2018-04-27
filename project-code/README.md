# Twitter Analysis on Digital Ocean

# Service Description

This RESTful service is used to perform twitter analysis using pyspark ml libraries. The service sucessfully
runs within the docker container as well. The docker container was launched from the DigitalOcean cloud platform.

You need have a twitter api endpoint configured in restapi.py for the serviceto work.

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

##### Check the results using your browser
* The results are available at http://159.89.36.6:5000 

