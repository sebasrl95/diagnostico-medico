import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definir las variables de entrada (sintomas)
fiebre = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'fiebre')
tos = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'tos')
dolor_cabeza = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'dolor_cabeza')
estornudos = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'estornudos')
congestion_nasal = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'congestion_nasal')
nausea = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'nausea')
mareo = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'mareo')
dolor_pecho = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'dolor_pecho')
falta_de_aire = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'falta_de_aire')
dolor_abdominal = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'dolor_abdominal')
vomito = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'vomito')
diarrea = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'diarrea')
picazon_ojo = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'picazon_ojo')
perdida_olfato = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'perdida_olfato')
perdida_gusto = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'perdida_gusto')
dolor_facial = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'dolor_facial')
palpitaciones = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'palpitaciones')
perdida_equilibrio = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'perdida_equilibrio')

# Definir la variable de salida (diagnostico)
diagnostico = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'diagnostico')

# Funciones de pertenencia para los sintomas
for symptom in [fiebre, tos, dolor_cabeza, estornudos, congestion_nasal, nausea, mareo, dolor_pecho,
                falta_de_aire, dolor_abdominal, vomito, diarrea, picazon_ojo, perdida_olfato, 
                perdida_gusto, dolor_facial, palpitaciones, perdida_equilibrio]:
    symptom['bajo'] = fuzz.trimf(symptom.universe, [0, 0, 0.5])
    symptom['medio'] = fuzz.trimf(symptom.universe, [0, 0.5, 1])
    symptom['alto'] = fuzz.trimf(symptom.universe, [0.5, 1, 1])

# Funciones de pertenencia para el diagnostico
diagnostico['saludable'] = fuzz.trimf(diagnostico.universe, [0, 0, 0.2])
diagnostico['leve'] = fuzz.trimf(diagnostico.universe, [0, 0.2, 0.5])
diagnostico['moderado'] = fuzz.trimf(diagnostico.universe, [0.2, 0.5, 0.8])
diagnostico['grave'] = fuzz.trimf(diagnostico.universe, [0.5, 0.8, 1])

rule1 = ctrl.Rule((fiebre['medio'] | fiebre['alto']) &
                 (tos['medio'] | tos['alto']) &
                 (dolor_cabeza['medio'] | dolor_cabeza['alto']),
                 diagnostico['moderado'])

rule2 = ctrl.Rule((estornudos['medio'] | estornudos['alto']) &
                 (tos['medio'] | tos['alto']) &
                 (fiebre['medio'] | fiebre['alto']),
                 diagnostico['leve'])

rule3 = ctrl.Rule(dolor_cabeza['medio'] &
                 (nausea['medio'] | mareo['medio']),
                 diagnostico['moderado'])

rule4 = ctrl.Rule(tos['medio'] &
                 (dolor_pecho['medio'] | fiebre['medio'] | falta_de_aire['medio']),
                 diagnostico['grave'])

rule5 = ctrl.Rule(dolor_abdominal['medio'] &
                 (nausea['medio'] | vomito['medio'] | diarrea['medio']),
                 diagnostico['moderado'])

rule6 = ctrl.Rule((estornudos['medio'] | estornudos['alto']) &
                 (picazon_ojo['medio'] | congestion_nasal['medio']),
                 diagnostico['leve'])

rule7 = ctrl.Rule(fiebre['medio'] &
                 (tos['medio'] | perdida_olfato['medio'] | perdida_gusto['medio']),
                 diagnostico['grave'])

rule8 = ctrl.Rule(dolor_cabeza['medio'] &
                 (congestion_nasal['medio'] | dolor_facial['medio']),
                 diagnostico['moderado'])

rule9 = ctrl.Rule(palpitaciones['medio'] &
                 (falta_de_aire['medio'] | mareo['medio'] | dolor_pecho['medio']),
                 diagnostico['moderado'])

rule10 = ctrl.Rule((fiebre['bajo'] & dolor_cabeza['bajo'] & tos['bajo'] &
                    estornudos['bajo'] & nausea['bajo'] & vomito['bajo'] &
                    diarrea['bajo'] & mareo['bajo'] & falta_de_aire['bajo'] &
                    dolor_pecho['bajo'] & dolor_abdominal['bajo'] &
                    picazon_ojo['bajo'] & congestion_nasal['bajo'] &
                    dolor_facial['bajo'] & palpitaciones['bajo'] &
                    perdida_equilibrio['bajo']),
                   diagnostico['saludable'])

# Crear el sistema de control
diagnostico_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
diagnostico_simulacion = ctrl.ControlSystemSimulation(diagnostico_ctrl)

# Proporcionar entradas para todos los síntomas
diagnostico_simulacion.input['fiebre'] = 0.7
diagnostico_simulacion.input['tos'] = 0.5
diagnostico_simulacion.input['dolor_cabeza'] = 0.3
diagnostico_simulacion.input['estornudos'] = 0
diagnostico_simulacion.input['congestion_nasal'] = 0
diagnostico_simulacion.input['nausea'] = 0
diagnostico_simulacion.input['mareo'] = 0
diagnostico_simulacion.input['dolor_pecho'] = 0
diagnostico_simulacion.input['falta_de_aire'] = 0
diagnostico_simulacion.input['dolor_abdominal'] = 0
diagnostico_simulacion.input['vomito'] = 0
diagnostico_simulacion.input['diarrea'] = 0
diagnostico_simulacion.input['picazon_ojo'] = 0
diagnostico_simulacion.input['perdida_olfato'] = 0
diagnostico_simulacion.input['perdida_gusto'] = 0
diagnostico_simulacion.input['dolor_facial'] = 0
diagnostico_simulacion.input['palpitaciones'] = 0
diagnostico_simulacion.input['perdida_equilibrio'] = 0

# Computar el resultado
diagnostico_simulacion.compute()

# Imprimir el resultado
print("Diagnóstico:", diagnostico_simulacion.output['diagnostico'])

# Graficar resultado
diagnostico.view(sim=diagnostico_simulacion)
plt.show()
