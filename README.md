# Family Web Portal

A simple Flask web application that provides a central landing page for family websites and services.

## Features

- Clean, responsive web interface
- List of family websites and services
- Lightweight Flask-based backend
- Docker support for easy deployment

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t family-portal .
```

2. Run the container:
```bash
docker run -p 5000:5000 family-portal
```

## Project Structure

```
family_main_land_page/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md          # Documentation
```

## Configuration

The application is configured to run on port 5000 by default. You can modify the settings in `app.py` as needed.

## Requirements

- Python 3.7+
- Flask
- Docker (optional, for containerized deployment)

## Usage

This portal serves as a central hub for accessing various family websites and services. The interface displays a organized list of available resources with easy navigation.

## License

This project is intended for personal/family use.