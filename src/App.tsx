import React from "react"

const apiKey = import.meta.env.VITE_GEMINI_API_KEY;

const App = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-100 to-indigo-200 text-gray-900">
      <h1 className="text-3xl font-bold pb-4">Гитти — AI Учитель Гитары для Детей</h1>
      <p className="mb-4">Тестовый ключ: <span className="bg-white rounded px-2">{apiKey ? 'Есть' : 'Нет'}</span></p>
      {/* Ваш основной UI */}
    </div>
  )
}

export default App
