# Importar librerias necesarias
from flask import Flask, request, jsonify
from flask_cors import CORS
import clips

app = Flask(__name__)

# Habilitar CORS en la aplicación
CORS(app)

# Inicializar el entorno de CLIPS
env = clips.Environment()

# Ruta para evaluar los sintomas
@app.route('/evaluate', methods=['POST'])
def evaluate():
    # Reiniciar ambiente de CLIPS
    env.reset()

    # Recuperar la data del request
    data = request.json

    # Cargar las reglas desde el archivo CLIPS
    env.load('diagnostico.clp')

    # Agregar los hechos basados según los síntomas recibidos
    for fact in data['facts']:
        env.assert_string(f'(sintoma {fact})')
    
    # Ejecutar reglas
    env.run()
    
    # Recuperar el diagnóstico
    diagnosticos = [str(fact) for fact in env.facts() if "diagnostico" in str(fact)]

    # Validar diagnostico
    if diagnosticos:
        response = {
            "diagnostico": f"{diagnosticos[0].split(" ")[1].split(")")[0]}"
        }
    else:
        response = {
            "diagnostico": "No se pudo determinar un diagnóstico."
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)