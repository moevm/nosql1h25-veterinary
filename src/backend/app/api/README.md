# API Documentation

### 1. **Login**
   - **Endpoint**: `/api/users/login` (POST)
   - **Request**:
     ```json
     { "login": "string", "password": "string" }
     ```
   - **Response**:
     - `200 OK`:
       ```json
       { "message": "Login successful", "role": "user" }
       ```
     - `400 Bad Request`: Invalid login or password.

---

### 2. **Register**
   - **Endpoint**: `/api/users/register` (POST)
   - **Request**:
     ```json
     { 
       "second_name": "string", 
       "first_name": "string", 
       "last_name": "string", 
       "login": "string", 
       "password": "string", 
       "email": "string", 
       "role": "user"
     }
     ```
   - **Response**:
     - `201 Created`:
       ```json
       { "message": "User registered successfully" }
       ```
     - `400 Bad Request`: Invalid data.

---

### 3. **Get User**
   - **Endpoint**: `/api/users/user` (GET)
   - **Request**:
     ```json
     { "id": "string" }
     ```
   - **Response**:
     - `200 OK`: User data
     - `400 Bad Request`: Invalid ID.

--- 

> All endpoints include error handling for invalid requests.
