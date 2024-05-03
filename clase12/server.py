from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡hola mundo!'

@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return(
            jsonify({"error": "se requiere un nombre en losparametrso de la url."}),400
        )
    return jsonify({"mensaje": f"¡hola, {nombre}!"})

@app.route("/sumar", methods = ['GET'])
def sumar():
    num1 =int(request.args.get("num1")) 
    num2 =int(request.args.get("num2"))
    if not num1:
        return(
            jsonify({"error": "se requere llenar los dos parametros"}), 400
        )
    return jsonify({"suma": f"la suma es igual a: {num1+num2}"})

if __name__ == '__main__':
    app.run()


