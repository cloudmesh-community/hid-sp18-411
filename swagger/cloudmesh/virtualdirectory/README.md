# Swagger

# Service Description

This NOSQL swagger service is used to list all contents of the database in the predefined format. The service sucessfully
runs within the docker container as well.
 
# Instructions for Execution :

* Clone the repository with the command

    `
    git clone https://github.com/cloudmesh-community/hid-sp18-411.git
    `  

* Navigate to the project directory

    `
    cd /hid-sp18-411/swagger/cloudmesh/virtualdirectory
    `

#### Makefile
* The swagger service can then be run locally with the command, make sure the database is up and running: 

    `
    sudo make start-service
    `  

##### Check the results using your browser
* The results are then available at http://localhost:8080/NoSQL  

# Sample Output

* The contents of the NoSQL database are displayed as below

    "[[\"Venkatesh Aditya, Kaveripakam\", \"hid-sp18-411\"], [\"Surya Prakash, Sekar\", \"hid-sp18-418\"]]"

# Docker Commands

* The docker container can be built with the command: 

    `
    sudo make start-docker
    `  
* The docker container can be stopped with the command: 

    `
    sudo make stop-docker
    `  
    
* Clean can be executed with the command: 

    `
    sudo make clean
    `  
