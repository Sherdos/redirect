from flask import Flask, redirect

app = Flask(__name__)

@app.route('/hackaicon_ethiack_1337_lmao')
def redirect_endpoint():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
