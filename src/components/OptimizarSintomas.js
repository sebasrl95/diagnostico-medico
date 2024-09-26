import React, { useState } from 'react';

const OptimizarSintomas = () => {
    const [resultados, setResultados] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Función para optimizar síntomas
    const optimizarSintomas = async () => {
        setLoading(true);  // Indicador de carga
        setError(null);    // Limpiar errores previos
        setResultados(null); // Limpiar resultados previos

        try {
            const response = await fetch('http://localhost:5000/optimize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ sintomas: ['fiebre', 'tos'] }), // Aquí puedes agregar síntomas dinámicos si lo necesitas
            });

            if (!response.ok) {
                throw new Error('Error al realizar la optimización');
            }

            const data = await response.json();
            setResultados(data.sintomas);  // Guardar los síntomas optimizados
        } catch (error) {
            setError('Ocurrió un error al optimizar los síntomas.');
        } finally {
            setLoading(false);  // Finalizar la carga
        }
    };

    return (
        <div>
            <button onClick={optimizarSintomas} className="mt-4 w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700" disabled={loading}>
                {loading ? 'Optimizando...' : 'Optimizar Síntomas'}
            </button>

            {error && <p style={{ color: 'red' }}>{error}</p>}

            {resultados && (
                <div>
                    <h3>Síntomas optimizados:</h3>
                    <ul>
                        {resultados.map((sintoma, index) => (
                            <li key={index}>{sintoma}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default OptimizarSintomas;
