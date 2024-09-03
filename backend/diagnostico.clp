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