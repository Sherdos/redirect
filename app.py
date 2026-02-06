import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/hackaicon_ethiack_1337_lmao')
def redirect_endpoint():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ', code=302)

if __name__ == '__main__':
    # Use environment variables for configuration with safe defaults
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    app.run(host=host, port=port, debug=debug)
