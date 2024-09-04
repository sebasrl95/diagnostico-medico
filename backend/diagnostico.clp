(defrule gripe
    (or (sintoma fiebre) (sintoma dolor-cabeza))
    (or (sintoma tos) (sintoma estornudos) (sintoma congestion-nasal))
    =>
    (assert (diagnostico Gripa)))

(defrule resfriado
    (or (sintoma estornudos) (sintoma tos))
    (or (sintoma fiebre) (sintoma dolor-cabeza) (sintoma congestion-nasal))
    =>
    (assert (diagnostico Resfriado)))

(defrule migraña
    (sintoma dolor-cabeza)
    (or (sintoma nausea) (sintoma mareo))
    =>
    (assert (diagnostico Migraña)))

(defrule bronquitis
    (sintoma tos)
    (or (sintoma dolor-pecho) (sintoma fiebre) (sintoma falta-de-aire))
    =>
    (assert (diagnostico Bronquitis)))

(defrule infeccion-estomacal
    (sintoma dolor-abdominal)
    (or (sintoma nausea) (sintoma vomito) (sintoma diarrea))
    =>
    (assert (diagnostico Infeccion-Estomacal)))

(defrule alergia
    (or (sintoma estornudos) (sintoma picazon-ojo))
    (or (sintoma nariz-congestionada) (sintoma tos) (sintoma dolor-cabeza))
    =>
    (assert (diagnostico Alergia)))

(defrule covid19
    (sintoma fiebre)
    (or (sintoma tos) (sintoma perdida-olfato) (sintoma perdida-gusto) (sintoma dolor-pecho) (sintoma falta-de-aire))
    =>
    (assert (diagnostico COVID-19)))

(defrule sinusitis
    (sintoma dolor-cabeza)
    (or (sintoma congestion-nasal) (sintoma dolor-facial) (sintoma fiebre))
    =>
    (assert (diagnostico Sinusitis)))

(defrule ansiedad
    (sintoma palpitaciones)
    (or (sintoma falta-de-aire) (sintoma mareo) (sintoma dolor-pecho) (sintoma perdida-equilibrio))
    =>
    (assert (diagnostico Ansiedad)))

(defrule salud
    (not (sintoma fiebre))
    (not (sintoma dolor-cabeza))
    (not (sintoma tos))
    (not (sintoma estornudos))
    (not (sintoma nausea))
    (not (sintoma vomito))
    (not (sintoma diarrea))
    (not (sintoma mareo))
    (not (sintoma falta-de-aire))
    (not (sintoma dolor-oido))
    (not (sintoma perdida-audicion))
    (not (sintoma dolor-pecho))
    (not (sintoma dolor-abdominal))
    (not (sintoma ardor-estomago))
    (not (sintoma picazon-ojo))
    (not (sintoma nariz-congestionada))
    (not (sintoma perdida-olfato))
    (not (sintoma congestion-nasal))
    (not (sintoma dolor-facial))
    (not (sintoma palpitaciones))
    (not (sintoma perdida-equilibrio))
    =>
    (assert (diagnostico Saludable)))
