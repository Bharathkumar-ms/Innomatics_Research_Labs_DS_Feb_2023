from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    if name is not None:
        name_upper = name.upper()
        return f'Hello, {name_upper}!'
    else:
        return 'Please provide a name in the URL query parameter.'

if __name__ == '__main__':
    app.run(Debug=True)
