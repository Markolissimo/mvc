# FastAPI MVC Application

A modern web application built with FastAPI following the MVC (Model-View-Controller) pattern, featuring user authentication and post management.

## Features

- **Authentication & Authorization**
  - JWT token-based authentication
  - Secure password hashing with bcrypt
  - Email validation
  - Protected routes

- **Database & ORM**
  - MySQL 8.0 database
  - SQLAlchemy ORM
  - Automatic table creation
  - Connection pooling

- **API Features**
  - FastAPI with automatic OpenAPI documentation
  - Request/Response validation with Pydantic
  - Response caching with cachetools
  - File upload support
  - Comprehensive error handling

- **Development & Deployment**
  - Docker containerization
  - Docker Compose for multi-container setup
  - Environment variable configuration
  - Health checks and container orchestration

## Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for local development)
- MySQL client (optional, for direct database access)

## Quick Start

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

Once the application is running, you can access:
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## Project Structure

```
mvc/
├── src/                    # Source code
│   ├── controllers/       # Route handlers and request processing
│   ├── models/           # SQLAlchemy and Pydantic models
│   ├── services/         # Business logic and data processing
│   ├── auth.py          # Authentication utilities
│   ├── database.py      # Database configuration
│   └── main.py          # FastAPI application entry point
├── mysql/                # MySQL configuration
│   ├── conf.d/          # MySQL configuration files
│   └── init.sql         # Database initialization script
├── tests/               # Test files
├── docker-compose.yml   # Docker Compose configuration
├── Dockerfile          # Web application container definition
├── requirements.txt    # Python dependencies
├── wait_for_db.py     # Database connection check script
└── README.md          # Project documentation
```

## Development Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the development server:
```bash
uvicorn src.main:app --reload
```

## API Endpoints

### Authentication
- `POST /auth/signup` - Register a new user
- `POST /auth/login` - Login and receive JWT token

### Posts
- `POST /posts/` - Create a new post
- `GET /posts/` - List all posts
- `GET /posts/{post_id}` - Get a specific post
- `PUT /posts/{post_id}` - Update a post
- `DELETE /posts/{post_id}` - Delete a post

## Docker Configuration

The application uses two containers:
1. Web application (FastAPI)
   - Port: 8000
   - Environment variables from .env
   - Volume mount for code changes

2. MySQL database
   - Port: 3306
   - Persistent volume for data
   - Custom configuration
   - Initialization script

## Testing

Run the test suite:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details 