# Overview

Car Shop API is a Restful API project that implements a system to handle sales of Cars to Car Owners. This project is written in Python 3 Django + MySQL


**Requirements**

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install)
  
**Setup**

Copy environment variables of the project:
```
cp .env.example .env
```

Build container and start development environment:
```
 docker-compose up --build
```

After all these steps, the project will be running on port 8080: http://localhost:8000. All http requests send and receive JSON data.

To view changes in the database, go to http://localhost:8181/ on browser and you will be able to access phpmyadmin.

### ER Database Diagram
(click the image to zoom it or just download the image and zoom it by yourself so you can see better all tables relationships)

![](https://raw.githubusercontent.com/paduanton/car-shop-api/main/docs/ER-diagram.png)


#### Entity Relationship:
- CarOwners 1 - N Cars


## Documentation

You can access the Restful API public documentarion in the link below or [clicking here](https://www.postman.com/paduanton/workspace/antonio-de-pdua-s-public-workspace/collection/5889563-7f6ae96e-f38e-4ee8-971f-a877b996bbde?ctx=documentation). 

https://www.postman.com/paduanton/workspace/antonio-de-pdua-s-public-workspace/collection/5889563-7f6ae96e-f38e-4ee8-971f-a877b996bbde?ctx=documentation

Also in the root dir there is a file called car-shop-api.postman_collection that you can import in your postman in order to see the API requests.
## Endpoints

In **all** http calls you must have the header `Accept:application/json`. In http requests made with http POST verb you need to set the header `Content-Type:application/json`.

