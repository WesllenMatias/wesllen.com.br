from bottle import run, route, template

@route('/')
def home():
    return template('index.html')

run(host='localhost',port=9090,debug=True)