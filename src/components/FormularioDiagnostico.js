import React, { useState } from 'react';
import SintomaCheckbox from './SintomaCheckbox';

const FormularioDiagnostico = () => {
    const [sintomas, setSintomas] = useState({
        "fiebre": false,
        "dolor-cabeza": false,
        "tos": false,
        "estornudos": false,
        "nausea": false,
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
                <SintomaCheckbox
                    label="Fiebre"
                    name="fiebre"
                    checked={sintomas.fiebre}
                    onChange={handleChange}
                />
                <SintomaCheckbox
                    label="Dolor de Cabeza"
                    name="dolorCabeza"
                    checked={sintomas.dolorCabeza}
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
                    Diagnóstico: <strong>{diagnostico}</strong>
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
