
import random as rd

# Definir la lista de todos los síntomas disponibles
todos_sintomas = ["fiebre", "dolor_cabeza", "tos", "dolor_garganta", "dificultad_respirar"]

# El tamaño del individuo será el número de síntomas posibles
tamano = len(todos_sintomas)

# Generar un individuo: una lista de 0s y 1s donde 1 significa que el síntoma está presente
def getIndividuo():
    return [rd.randint(0, 1) for _ in range(tamano)]

# Generar una población de individuos
def getPoblacion(numero):
    return [getIndividuo() for _ in range(numero)]

# Calcular la adaptación (fitness) basado en la predicción del sistema experto
# Ahora recibe directamente la función para evaluar los síntomas
def CalcularAdaptacion(individuo, funcion_evaluar_sintomas):
    sintomas_seleccionados = [todos_sintomas[i] for i in range(tamano) if individuo[i] == 1]
    return funcion_evaluar_sintomas(sintomas_seleccionados)

# Cruce entre dos individuos
def cruce(individuo1, individuo2):
    puntoCruce = rd.randint(1, tamano - 1)
    nuevo_individuo = individuo1[:puntoCruce] + individuo2[puntoCruce:]
    return nuevo_individuo

# Mutación: cambiar al azar un gen del individuo
def mutacion(individuo, tasa_mutacion=0.01):
    for i in range(tamano):
        if rd.random() < tasa_mutacion:
            individuo[i] = 1 - individuo[i]  # cambiar de 0 a 1 o de 1 a 0
    return individuo

# Algoritmo genético
def algoritmo_genetico(funcion_evaluar_sintomas, numero_generaciones=100, tamano_poblacion=50, tasa_mutacion=0.01):
    # Crear la población inicial
    poblacion = getPoblacion(tamano_poblacion)

    for generacion in range(numero_generaciones):
        # Evaluar la adaptación de cada individuo
        adaptaciones = [(individuo, CalcularAdaptacion(individuo, funcion_evaluar_sintomas)) for individuo in poblacion]
        
        # Ordenar por adaptación
        adaptaciones.sort(key=lambda x: x[1], reverse=True)
        
        # Seleccionar los mejores individuos
        mejores_individuos = [ind for ind, adaptacion in adaptaciones[:tamano_poblacion//2]]
        
        # Generar nueva población a partir de cruces de los mejores individuos
        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = rd.choice(mejores_individuos)
            padre2 = rd.choice(mejores_individuos)
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo, tasa_mutacion)
            nueva_poblacion.append(hijo)
        
        # Actualizar la población
        poblacion = nueva_poblacion
    
    # Retornar el mejor individuo de la última generación
    mejor_individuo = max(poblacion, key=lambda ind: CalcularAdaptacion(ind, funcion_evaluar_sintomas))
    sintomas_seleccionados = [todos_sintomas[i] for i in range(tamano) if mejor_individuo[i] == 1]
    
    return sintomas_seleccionados
