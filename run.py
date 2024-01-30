from flask import Flask

app = Flask(__name__) # Instancia de la clase Flask

@app.route('/')
def hello_world():
	return 'Hello, World!'