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

### 4. **Filter Entities**
- **Endpoint**: `/api/filter/<entity_name>`  
- **Method**: `GET`  
- **Description**: Фильтрация сущностей с поддержкой:
  - `__icontains`: поиск по подстроке, регистронезависимый (в том числе для кириллицы)
  - `__start`: поиск по полю, начиная с указанного значения включительно
  - `__end`: поиск по полю до указанного значения включительно

---

#### 🔹 Request Example:
```json
{
  "name__icontains": "рекс",
  "gender": "male",
  "birthdate__start": "2020-01-01",
  "birthdate__end": "2021-12-31"
}

#### Successfull response

[
  {
    "id": "245906d6...",
    "name": "Рекс",
    "breed": "Овчарка",
    "gender": "male",
    "birthdate": "2021-05-05",
    "photo_url": "",
    "owner": [
      {
        "id": "14d3d7ad...",
        "first_name": "Иван",
        "second_name": "Иванович",
        "last_name": "Иванов",
        "email": "test@example.com",
        "login": "test_login",
        "gender": "male"
      }
    ],
    "pet_type": [
      {
        "type_name": "кот"
      }
    ],
    "appointments": [
      {
        "id": "12345",
        "date": "2025-04-20T14:30:00Z",
        "_status": "ожидает подтверждения",
        "reason": "Обследование питомца",
        "comment": "Пациент выглядит здоровым, но требуется дополнительное обследование.",
        "diagnosis": "Здоров",
        "recommend": "Продолжить наблюдение через месяц.",
        "file_urls": [
          "http://example.com/files/pet_report_1.pdf",
          "http://example.com/files/pet_report_2.pdf"
        ]
      }
    ]
  }
]
