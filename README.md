## URL Shortener API Documentation

## Introduction
The URL Shortener API provides the backend functionality for shortening long URLs into shorter, more manageable links. It handles user authentication, link management, analytics tracking, and other related features.

## Technologies Used
- Python: A programming language used for building the API.
- Flask: A micro web framework for creating APIs in Python.
- Flask-RESTful: An extension for Flask that adds support for building RESTful APIs.
- MongoDB: A NoSQL database for storing user information, links, and analytics data.
- PyMongo: A Python driver for MongoDB, providing connectivity to the database.
- JSON Web Tokens (JWT): For user authentication and authorization.
- Werkzeug: A comprehensive WSGI web application library for handling HTTP requests.

## Endpoints

### User Endpoints

#### Register a new user
- **Endpoint:** `POST /https://quicklink.onrender.com/register`
- **Request Body:**
  ```json
  {
    "last_name": "string",
    "first_name": "string",
    "email": "user@example.com",
    "password": "string",
    "confirm_password": "string",
    "username": "string"
  }
  ```
- **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    {
      "message": "User registered successfully"
    }
    ```

#### Authenticate a user and generate an access token
- **Endpoint:** `POST /https://quicklink.onrender.com/login`
- **Request Body:**
  ```json
  {
    "email": "example_user",
    "password": "password123"
  }
  ```
- **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    {
      "accessToken": "your-access-token"
    }
    ```

#### Log out a user and invalidate the access token
- **Endpoint:** `DELETE /https://quicklink.onrender.com/logout`
- **Request Header:**
  ```
  Authorization: Bearer your-access-token
  ```
- **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    {
      "message": "User logged out successfully"
    }
    ```

#### Get the user's profile information
- **Endpoint:** `GET /https://quicklink.onrender.com/user`
- **Request Header:**
  ```
  Authorization: Bearer your-access-token
  ```
- **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    {
      "username": "example_user",
      "email": "user@example.com",
      "firstName": "Gift",
      "lastName": "Emete"
    }
    ```

### Link Endpoints

#### Get all the user's shortened links
- **Endpoint:** `GET /api/

links`
- **Request Header:**
  ```
  Authorization: Bearer your-access-token
  ```

  - **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    [
      {
        "id": "1",
        "originalUrl": "https://www.example.com/long-url",
        "shortUrl": "https://short.ly/abcd",
        "createdAt": "2023-06-01 10:00:00",
        "clicks": 10
      },
      {
        "id": "2",
        "originalUrl": "https://www.example.com/another-long-url",
        "shortUrl": "https://short.ly/efgh",
        "createdAt": "2023-06-02 15:30:00",
        "clicks": 5
      }
    ]
    ```

#### Shorten a long URL
- **Endpoint:** `POST /https://quicklink.onrender.com/short_urls`
- **Request Header:**
  ```
  Authorization: Bearer your-access-token
  ```
- **Request Body:**
  ```json
  {
    "original_url": "https://www.example.com/long-url",
    "custom_url":" "
  }
  ```
- **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    {
      "originalUrl": "https://www.example.com/long-url",
      "shortUrl": "https://short.ly/abcd"
    }
    ```

    ```

#### Get analytics for a shortened link
- **Endpoint:** `GET /https://quicklink.onrender.com/dashboard'
- **Request Header:**
  ```
  Authorization: Bearer your-access-token
  ```
- **Response:**
  - Status: 200 (OK)
  - Body:
    ```json
    {
      "linkId": "1",
      "clicks": 10,
      "countries": {
        "US": 7,
        "CA": 3
      },
      "browsers": {
        "Chrome": 5,
        "Firefox": 3,
        "Safari": 2
      },
      "platforms": {
        "Windows": 6,
        "MacOS": 4
      }
    }
    ```

## Error Responses

### 401 Unauthorized
- **Status Code:** 401 (Unauthorized)
- **Body:**
  ```json
  {
    "error": "Unauthorized",
    "message": "Invalid or expired access token"
  }
  ```

### 404 Not Found
- **Status Code:** 404 (Not Found)
- **Body:**
  ```json
  {
    "error": "Not Found",
    "message": "The requested resource was not found"
  }
  ```

### 500 Internal Server Error
- **Status Code:** 500 (Internal Server Error)
- **Body:**
  ```json
  {
    "error": "Internal Server Error",
    "message": "An internal server error occurred"
  }
  ```

## Conclusion
This documentation provides an overview of the URL Shortener API endpoints, their request/response structures, and the authentication requirements. It serves as a guide for developers to understand and utilize the API effectively. Feel free to reach out to the project maintainers for further assistance or clarification.







![URL shortener API img](https://github.com/Emetegift/url-shortener-api/assets/104801555/b8e47d21-03a2-4c6a-8a53-fb7098ae1d37)







https://github.com/Emetegift/url-shortener-api/assets/104801555/6fd1dd05-417e-4a06-b8b1-f25ab1616f55



https://github.com/Emetegift/url-shortener-api/assets/104801555/314ab9e6-4400-4950-a502-9ae02a18a3d6

