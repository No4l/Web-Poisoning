from flask import Flask, request
app = Flask(__name__)

@app.route('/host')
def host():
    forward = request.headers.get('X-Forwarded-Host')
    script = '/js.js'
    if forward != None:
        script = 'http://' + forward + script
    return '<script src="{0}" ></script><h1>Hello World</h1>'.format(script)
    
@app.route('/query')
def query():
    url = request.full_path
    return '<h1>{0}</h1>'.format(url)   


if __name__ == '__main__':
    app.run(host='0.0.0.0')
