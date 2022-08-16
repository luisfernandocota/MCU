
# API MCU comics

This project is a compilation of APIs provided by Marvel for querying comics and characters using FLASK technology and MongoDB Atlas to save users.


## API Reference

#### Get all Marvel comics

```http
  GET /api/v1/comics
```
Returns a JSON with all Marvel comics

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `titleStartsWith` | `string` | **Optional**. Title of comic |

#### Get all Marvel characters

```http
  GET /api/v1/characters
```
Returns a JSON with all Marvel characters


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `nameStartsWith`      | `string` | **Optional**. Name character |

#### Register users

```http
  POST /api/v1/users/register
```
Gets the elements to make a record in the database and at the same time have a session 


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. |
| `email`      | `string` | **Required**. |
| `age`      | `int` | **Required**. |
| `password`      | `string` | **Required**. This will be encrypted|

#### Update users

```http
  PUT /api/v1/users/<id>
```
Get the user with the <id> in database and update the fields with the new information


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. |
| `email`      | `string` | **Required**. |
| `age`      | `int` | **Required**. |
| `password`      | `string` | **Required**. This will be encrypted|

#### DELETE users

```http
  DELETE /api/v1/users/<id>
```
Get the user with the <id> in database and delete the user

#### Login user

```http
  POST /api/v1/users/login
  GET /api/v1/users/login
```
To the method POST, return the user logged and a token auth.
To the method GET, return who user is logged. 


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. |
| `password`      | `string` | **Required**. |

#### Get user session

```http
  GET /api/v1/users/session
```
Return information who user is logged

#### Logout user

```http
  GET /api/v1/users/logout
```
Logout user in session active

## Installation

Install mcu-project with docker, clone this project and run this command

```docker
  docker-compose up
```
    
