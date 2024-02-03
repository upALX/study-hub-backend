# Order-API

**Overview**

This is an API to management the order flow of e-commerce.

🛠️*This project is under development*🛠️

![giphy](https://github.com/upALX/All-Assets/blob/main/construction-little-girl.webp)

---

## Tech stack
![Typescript](https://img.shields.io/badge/-Typescript-05122A?style=flat&logo=Typescript)&nbsp;
![nodedotjs](https://img.shields.io/badge/-NodeJS-05122A?style=flat&logo=nodedotjs)&nbsp;
![NestJS](https://img.shields.io/badge/-NestJS-05122A?style=flat&logo=NestJS)&nbsp;
![TypeORM](https://img.shields.io/badge/-TypeORM-05122A?style=flat&logo=typeform)&nbsp;
![RabbitMQ](https://img.shields.io/badge/-RabbitMQ-05122A?style=flat&logo=RabbitMQ)&nbsp;
![docker](https://img.shields.io/badge/-Docker-05122A?style=flat&logo=docker)&nbsp;

## How to use 🫁

**requirements:**
  - Node >= 18.17.1

If you has a Python 3 installed on your desktop, follow this:

**1 - Clone this repo:**
```
git clone git@github.com:upALX/Order-API.git
```

**2 - Up the database with docker compose:**
```
docker compose up
```

**3 - Access the database using command line:**
```
docker compose exec db bash
```
*db is a service name of database up with docker compose and declared on compose file*

**4 - Login on your database:**
```
mysql -u root -p

```
*to access, use your password in ``` docker-compose.yaml``` where variable name is ``` MYSQL_DATABASE```*


**5 - Check if the databases and tables was created:**
```
SHOW DATABASES;

USE your_database_name;

SHOW TABLES;
```

## Make your mark :triangular_flag_on_post:   

**If you have any problems with this app or have an idea that contributes, open a [issue](https://github.com/upALX/Order-API/issues), [pull request](https://github.com/upALX/Order-API/pulls) or find me on [Linkedin](https://www.linkedin.com/in/alxinc/). Don't forget to give the project a star 🌟 :D**

## License :unlock:

This project is under the [MIT license](https://github.com/upALX/Order-API/blob/main/LICENSE).

---

**Developed with 💜 by ME**
