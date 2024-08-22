from flask import Flask

app = Flask(__name__) # Crea una instancia de la clase Flask

@app.route('/taxis', methods=['GET'])  # Usa route() para definir la URL que activará la función y GET para definir el método HTTP
def hello_world():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run() # run the application