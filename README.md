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

Run migrations:
```
 docker exec -it car-shop-web python manage.py migrate
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

In order to make any http request data to the API you MUST first have an API secure token and order to do that you must follow the next steps:

1 - Create a superuser
 ```
docker exec -it car-shop-web python manage.py createsuperuser --username paduanton --email antonio@example.com
```

2 - Generate API token with username

To do that you can run the command below on bash or you can make a POST request to `/api-token-auth` (request details are on postman API docs)
 ```
docker exec -it car-shop-web python manage.py drf_create_token paduanton 
```

3 - Set `Authorization: Token {your-token}` header in all  API requests

With your API token in hands you must set the Authorization header together with your token, after that your http header shoud look like this:

**Authorization: Token 1dd260a72829986fad06988bfe80cc7431d3aa71**

4 - Enjoy the API

## Testing

The whole models layer and API endpoints are covered by unit/integration tests. To run the automated testing you can use the bash command below:

```
docker exec -it car-shop-web python manage.py test 
```




