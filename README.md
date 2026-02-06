# redirect

A simple Flask web application with a redirect endpoint.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000` by default.

## Configuration

You can configure the application using environment variables:

- `FLASK_HOST`: Host to bind to (default: `127.0.0.1`)
- `FLASK_PORT`: Port to listen on (default: `5000`)
- `FLASK_DEBUG`: Enable debug mode (default: `False`)

Example:
```bash
FLASK_HOST=0.0.0.0 FLASK_DEBUG=true python app.py
```

## Usage

Visit `http://localhost:5000/hackaicon_ethiack_1337_lmao` and you will be redirected to the configured URL.