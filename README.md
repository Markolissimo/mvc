# FastAPI MVC Application

A modern web application built with FastAPI following the MVC (Model-View-Controller) pattern.

## Features

- FastAPI backend with SQLAlchemy ORM
- MySQL database
- Docker containerization
- User authentication
- Post management
- Token-based authentication
- Response caching
- Type validation

## Prerequisites

- Docker
- Docker Compose
- Python 3.9+

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Markolissimo/mvc.git
cd mvc
```

2. Build and start the containers:
```bash
docker-compose up --build
```

The application will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
mvc/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── mysql/
│   ├── conf.d/
│   └── init.sql
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest
```

## License

MIT 