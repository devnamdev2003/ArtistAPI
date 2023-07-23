
# Artist API using Django REST Framework

This repository contains a customized Artist API built using Django REST Framework. The API allows users to perform CRUD operations on artists and their works. Token-based authentication is implemented using Django REST Framework's built-in authentication classes to ensure that only authenticated users can perform the CRUD operations.

## Setup and Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/ArtistAPI.git
cd ArtistAPI
```

2. Create a virtual environment and activate it (optional but recommended):

```bash
python -m venv env
source env/bin/activate

# On Windows
env\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the database migrations:

```bash
python manage.py migrate
```

5. Create a superuser to access the Django admin interface (optional but useful for testing):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

The API will now be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

**httpie** : HTTPie (pronounced aitch-tee-tee-pie) is a command-line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible. HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers. The http & https commands allow for creating and sending arbitrary HTTP requests. They use simple and natural syntax and provide formatted and colorized output.
[Documentation](https://httpie.io/docs/cli/examples)

```bash
pip install httpie
```


#### User Registration

- `POST /api/register/`: Register a new user by providing a username and password in the request body. Example:

```bash
http POST http://127.0.0.1:8000/api/register/ username=new_user password=new_password
```

#### Authentication

To perform CRUD operations, users need to be authenticated. The following endpoints are available for authentication:

- `POST /api/token/`: Obtain an access token by providing valid username and password in the request body. Example:

```bash
http POST http://127.0.0.1:8000/api/token/ username=your_username password=your_password
```

This will return an access token that should be included in the headers for subsequent API requests.



### Artist Endpoints

- `GET /api/artists/`: Retrieve a list of all artists.

```bash
http GET http://127.0.0.1:8000/api/artists/ "Authorization: Token your_access_token"
```

- `POST /api/artists/`: Create a new artist by providing the required data in the request body.


```bash
http POST http://127.0.0.1:8000/api/artists/ name="pawan" user=1 works=1 "Authorization:Token your_access_token"
```

- `GET /api/artists/{artist_id}/`: Retrieve details of a specific artist.

```bash
http GET http://127.0.0.1:8000/api/artists/1/ "Authorization: Token your_access_token"
```

- `PUT /api/artists/{artist_id}/`: Update the details of a specific artist.


```bash
http POST http://127.0.0.1:8000/api/artists/ name="Dev" user=1 works=1 "Authorization:Token your_access_token"
```

- `DELETE /api/artists/{artist_id}/`: Delete a specific artist.


```bash
http GET http://127.0.0.1:8000/api/artists/1/ "Authorization: Token your_access_token"
```

### Work Endpoints

- `GET /api/works/`: Retrieve a list of all works.

```bash
http GET http://127.0.0.1:8000/api/works/ "Authorization: Token your_access_token"
```

- `POST /api/works/`: Create a new work by providing the required data in the request body.

```bash
http POST http://127.0.0.1:8000/api/works/ link=https://example.com/video work_type=YT "Authorization:Token your_access_token"
```

- `GET /api/works/{work_id}/`: Retrieve details of a specific work.

```bash
http GET http://127.0.0.1:8000/api/works/1/ "Authorization: Token your_access_token"
```

- `PUT /api/works/{work_id}/`: Update the details of a specific work.
  
```bash
http POST http://127.0.0.1:8000/api/works/ link=https://example.com/video work_type=YT "Authorization:Token your_access_token"
```

- `DELETE /api/works/{work_id}/`: Delete a specific work.

```bash
http GET http://127.0.0.1:8000/api/works/1/ "Authorization: Token your_access_token"
```

### Filtering and Searching

- Filtering by work type: To filter works by work type (e.g., Youtube or Instagram), use the `work_type` query parameter. Example:

```bash
http http://127.0.0.1:8000/api/works/?work_type=YT/ "Authorization: Token your_access_token"
```

- Searching by artist name: To search for works by artist name, use the `artist` query parameter. Example:

```bash
http http://127.0.0.1:8000/api/works/?artist=ArtistName "Authorization: Token your_access_token"
```

### Proper Authentication Headers

For all API endpoints that require authentication, include the access token in the headers as follows:

```bash
http GET http://127.0.0.1:8000/api/artists/ "Authorization: Token your_access_token"
```

Replace `your_access_token` with the actual access token obtained from the `/api/token/` endpoint.

## Dummy Data

To test the API with some initial dummy data, log in to the Django admin interface using the superuser credentials created earlier (`/admin/`). You can then add artists and works using the admin interface.

## Note

This project serves as a basic example of how to build a customized Artist API using Django REST Framework. For production environments, consider implementing additional security measures and performance optimizations.

**API Testing with Postman**

If you are testing the API endpoints using Postman, please note that the Token prefix should be "token" instead of "bearer." This is essential for successful authentication and access to protected resources.

**Authentication Token Prefix:**

When making requests that require authentication, ensure that the provided access token is prefixed with the word "token" as follows:

```
Header: Authorization: Token YOUR_ACCESS_TOKEN
```
