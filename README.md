# login-web-app

Para este challenge decidí usar Python con Flask para el backend ya que es muy legible y sencillo de setuppear y para el front usé JavaScript, CSS y HTML.
-[Setup & Installation](#setup--installation)
- [Endpoints](#endpoints)
  - [POST /login](#post--login)
  - [POST /signup](#post---signup)
- [Data Model](#data-model)
## Setup & Installation

Asegurese de tener la última versión de Python instalada.
1. Clonar el repo

2. `pip install -r requirements.txt`

# Usar la APP
entrar a la url base: `http://127.0.0.1:5000/`
 

## Endpoints

### POST  /login:
- **URL**: `/login`
- **Method**: `POST`
- **Headers**: 
  - `Content-Type`: `application/json`

- **Request Body**:

    ```json
        {
        "email": "user@example.com",
        "password": "yourpassword"
        }
    ```
- **responses**:
    -  `200: (OK) Login successful!` Devuelve un JSON con un token.
        - Token:
               ```json
                {
                    "token": "placeholder-token-123"
                }
                ```
    - ``401: (Unauthorized) Correo, usuario o contraseña inicio de sesión inválidos``

### POST   /signup:
    ````json
    "usuario": "El nombre de usuario que se desea registrar."
    "email": "user@example.com"
    "contraseña": "yourpassword"
    "repetición_de_contraseña":"yourpassword"
    ````
- **responses**:
    -   `201: (OK) Usuario creado correctamente!`
    -   `401: (Unauthorized) Correo, usuario o contraseña inicio de sesión inválidos`
    -    `409: (Conflict) Ya existe un recurso con esos datos.`

## Data Model

Los datos se guardan en users.json donde mantiene una lista de objetos (las credenciales). 
Cada objeto tiene la siguiente estructura:
```json
  {
    "user":"user_example",
    "email": "user@example.com",
    "password": "password"
  }
```
El `user` es opcional.