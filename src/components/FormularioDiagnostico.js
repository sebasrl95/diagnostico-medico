import React, { useState } from 'react';
import SintomaCheckbox from './SintomaCheckbox';

const FormularioDiagnostico = () => {
    const [sintomas, setSintomas] = useState({
        "fiebre": false,
        "dolor-cabeza": false,
        "tos": false,
        "estornudos": false,
        "nausea": false,
        "vomito": false,
        "diarrea": false,
        "mareo": false,
        "falta-de-aire": false,
        "dolor-oido": false,
        "perdida-audicion": false,
        "dolor-pecho": false,
        "dolor-abdominal": false,
        "ardor-estomago": false,
        "picazon-ojo": false,
        "nariz-congestionada": false,
        "perdida-olfato": false,
        "congestion-nasal": false,
        "dolor-facial": false,
        "palpitaciones": false,
        "perdida-equilibrio": false,
    });

    const [diagnostico, setDiagnostico] = useState('');
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setSintomas({
            ...sintomas,
            [e.target.name]: e.target.checked,
        });
    };

    const generarDiagnostico = async () => {
        try {
            // Array de síntomas seleccionados
            const selectedSymptoms = Object.keys(sintomas)
                .filter((key) => sintomas[key]) // Filtrar solo los síntomas seleccionados
                .map((key) => key.replace(/([A-Z])/g, "-$1").toLowerCase()); // Convertir a formato con guiones

            const response = await fetch('http://localhost:5000/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ facts: selectedSymptoms }),
            });

            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }

            const data = await response.json();
            setDiagnostico(data.diagnostico);
        } catch (error) {
            setError('Hubo un problema al generar el diagnóstico. Por favor, inténtelo nuevamente.');
        }
    };

    return (
        <div className="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-6 text-gray-800">Generador de Diagnóstico Médico</h2>
            <form>
                <div className="grid grid-cols-2 gap-4">
                    <SintomaCheckbox
                        label="Fiebre"
                        name="fiebre"
                        checked={sintomas.fiebre}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Dolor de Cabeza"
                        name="dolor-cabeza"
                        checked={sintomas['dolor-cabeza']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Tos"
                        name="tos"
                        checked={sintomas.tos}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Estornudos"
                        name="estornudos"
                        checked={sintomas.estornudos}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Náuseas"
                        name="nausea"
                        checked={sintomas.nausea}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Vómito"
                        name="vomito"
                        checked={sintomas.vomito}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Diarrea"
                        name="diarrea"
                        checked={sintomas.diarrea}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Mareo"
                        name="mareo"
                        checked={sintomas.mareo}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Falta de Aire"
                        name="falta-de-aire"
                        checked={sintomas['falta-de-aire']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Dolor de Oído"
                        name="dolor-oido"
                        checked={sintomas['dolor-oido']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Pérdida de Audición"
                        name="perdida-audicion"
                        checked={sintomas['perdida-audicion']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Dolor en el Pecho"
                        name="dolor-pecho"
                        checked={sintomas['dolor-pecho']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Dolor Abdominal"
                        name="dolor-abdominal"
                        checked={sintomas['dolor-abdominal']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Ardor en Estómago"
                        name="ardor-estomago"
                        checked={sintomas['ardor-estomago']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Picazón en un Ojo"
                        name="picazon-ojo"
                        checked={sintomas['picazon-ojo']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Nariz Congestionada"
                        name="nariz-congestionada"
                        checked={sintomas['nariz-congestionada']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Pérdida de Olfato"
                        name="perdida-olfato"
                        checked={sintomas['perdida-olfato']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Pérdida del Gusto"
                        name="perdida-gusto"
                        checked={sintomas['perdida-gusto']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Congestión Nasal"
                        name="congestion-nasal"
                        checked={sintomas['congestion-nasal']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Dolor Facial"
                        name="dolor-facial"
                        checked={sintomas['dolor-facial']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Palpitaciones"
                        name="palpitaciones"
                        checked={sintomas['palpitaciones']}
                        onChange={handleChange}
                    />
                    <SintomaCheckbox
                        label="Pérdida de Equilibrio"
                        name="perdida-equilibrio"
                        checked={sintomas['perdida-equilibrio']}
                        onChange={handleChange}
                    />
                </div>
                <button
                    type="button"
                    onClick={generarDiagnostico}
                    className="mt-4 w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700"
                >
                    Generar Diagnóstico
                </button>
            </form>
    
            {diagnostico && (
                <div className="mt-6 p-4 bg-green-100 text-green-700 rounded-md">
                    Posible Diagnóstico: <strong>{diagnostico}</strong>
                </div>
            )}
    
            {error && (
                <div className="mt-6 p-4 bg-red-100 text-red-700 rounded-md">
                    <strong>Error:</strong> {error}
                </div>
            )}
        </div>
    );
    
};

export default FormularioDiagnostico;
