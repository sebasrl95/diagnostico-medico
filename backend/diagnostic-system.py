# Importar librerias necesarias
from flask import Flask, request, jsonify
from flask_cors import CORS
from algoritmo_genetico_seleccion_sintomas import algoritmo_genetico
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

# Ruta para algoritmos geneticos
@app.route('/optimize', methods=['POST'])
def optimize_sintomas():
    try:
        # Recuperar los síntomas seleccionados por el usuario si es necesario
        sintomas_usuario = request.json.get('sintomas', [])

        # Función para evaluar la adaptación de cada individuo (combinación de síntomas)
        def evaluar_sintomas_individuo(sintomas):
            # Reiniciar el entorno de CLIPS
            env.reset()

            # Cargar las reglas desde el archivo CLIPS
            env.load('diagnostico.clp')

            # Agregar los hechos (síntomas seleccionados) en el entorno CLIPS
            for sintoma in sintomas:
                env.assert_string(f'(sintoma {sintoma})')

            # Ejecutar reglas
            env.run()

            # Recuperar el diagnóstico
            diagnosticos = [str(fact) for fact in env.facts() if "diagnostico" in str(fact)]

            # Si se obtuvo un diagnóstico, retornamos 1 como adaptación (éxito), sino 0
            return 1 if diagnosticos else 0

        # Ejecutar el algoritmo genético usando CLIPS para calcular la adaptación
        sintomas_optimizados = algoritmo_genetico(evaluar_sintomas_individuo)

        # Retornar los síntomas optimizados
        return jsonify({"sintomas": sintomas_optimizados}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)