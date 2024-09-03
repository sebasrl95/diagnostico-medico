(defrule gripe
    (sintoma fiebre)
    (sintoma dolor-cabeza)
    (sintoma tos)
    =>
    (assert (diagnostico Gripa)))

(defrule resfriado
    (sintoma estornudos)
    (sintoma tos)
    =>
    (assert (diagnostico Resfriado)))

(defrule migraña
    (sintoma dolor-cabeza)
    (sintoma nausea)
    =>
    (assert (diagnostico Migraña)))

(defrule salud
    (not (sintoma fiebre))
    (not (sintoma dolor-cabeza))
    (not (sintoma tos))
    (not (sintoma estornudos))
    =>
    (assert (diagnostico Saludable)))

(defrule bronquitis
    (sintoma tos)
    (sintoma dolor-pecho)
    (sintoma falta-de-aire)
    =>
    (assert (diagnostico Bronquitis)))

(defrule infeccion-estomacal
    (sintoma dolor-abdominal)
    (sintoma nausea)
    (sintoma vomito)
    =>
    (assert (diagnostico Infeccion-Estomacal)))

(defrule alergia
    (sintoma estornudos)
    (sintoma picazon-ojo)
    (sintoma nariz-congestionada)
    =>
    (assert (diagnostico Alergia)))

(defrule covid19
    (sintoma fiebre)
    (sintoma tos)
    (sintoma perdida-olfato)
    (sintoma perdida-gusto)
    =>
    (assert (diagnostico COVID-19)))

(defrule sinusitis
    (sintoma dolor-cabeza)
    (sintoma congestion-nasal)
    (sintoma dolor-facial)
    =>
    (assert (diagnostico Sinusitis)))

(defrule ansiedad
    (sintoma palpitaciones)
    (sintoma falta-de-aire)
    (sintoma mareo)
    =>
    (assert (diagnostico Ansiedad)))
(defrule faringitis
    (sintoma fiebre)
    (sintoma dolor-garganta)
    (sintoma tos)
    =>
    (assert (diagnostico Faringitis)))

(defrule rinitis-alergica
    (sintoma estornudos)
    (sintoma nariz-congestionada)
    (sintoma picazon-ojo)
    =>
    (assert (diagnostico Rinitis-Alérgica)))

(defrule gastritis
    (sintoma dolor-abdominal)
    (sintoma nausea)
    (sintoma ardor-estomago)
    =>
    (assert (diagnostico Gastritis)))

(defrule neumonia
    (sintoma fiebre)
    (sintoma tos)
    (sintoma dolor-pecho)
    (sintoma falta-de-aire)
    =>
    (assert (diagnostico Neumonia)))

(defrule tension-alta
    (sintoma dolor-cabeza)
    (sintoma mareo)
    (sintoma palpitaciones)
    =>
    (assert (diagnostico Tension-Alta)))

(defrule vertigo
    (sintoma mareo)
    (sintoma nausea)
    (sintoma perdida-equilibrio)
    =>
    (assert (diagnostico Vertigo)))

(defrule intoxicacion-alimentaria
    (sintoma dolor-abdominal)
    (sintoma vomito)
    (sintoma diarrea)
    =>
    (assert (diagnostico Intoxicacion-Alimentaria)))

(defrule otitis
    (sintoma dolor-oido)
    (sintoma fiebre)
    (sintoma perdida-audicion)
    =>
    (assert (diagnostico Otitis)))
