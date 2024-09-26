import React from 'react';
import FormularioDiagnostico from './components/FormularioDiagnostico';
import OptimizarSintomas from './components/OptimizarSintomas';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <FormularioDiagnostico />
      <OptimizarSintomas />
    </div>
  );
}

export default App;