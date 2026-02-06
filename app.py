import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_endpoint():
    return redirect('http://localhost:5000/hackaicon_ethiack_1337_lmao', code=302)

if __name__ == '__main__':
    # Use environment variables for configuration with safe defaults
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    app.run(host=host, port=port, debug=debug)
