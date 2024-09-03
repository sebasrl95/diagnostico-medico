import React from 'react';

const SintomaCheckbox = ({ label, name, checked, onChange }) => {
    return (
        <div className="flex items-center mb-4">
            <input
                type="checkbox"
                name={name}
                checked={checked}
                onChange={onChange}
                className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
            />
            <label className="ml-2 text-gray-700">{label}</label>
        </div>
    );
};

export default SintomaCheckbox;