import { useState } from 'react';

export default function AuthForm() {
    const [isLogin, setIsLogin] = useState(true);

    return (
        <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-2xl shadow-xl">
            <div className="flex justify-around mb-6">
                <button
                    onClick={() => setIsLogin(true)}
                    className={`px-4 py-2 font-medium rounded ${
                        isLogin ? 'bg-blue-500 text-white' : 'bg-gray-100'
                    }`}
                >
                    Вход
                </button>
                <button
                    onClick={() => setIsLogin(false)}
                    className={`px-4 py-2 font-medium rounded ${
                        !isLogin ? 'bg-blue-500 text-white' : 'bg-gray-100'
                    }`}
                >
                    Регистрация
                </button>
            </div>

            <form className="space-y-4">
                {!isLogin && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Имя</label>
                        <input
                            type="text"
                            placeholder="Ваше имя"
                            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-300"
                        />
                    </div>
                )}
                <div>
                    <label className="block text-sm font-medium text-gray-700">Email</label>
                    <input
                        type="email"
                        placeholder="Email"
                        className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-300"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700">Пароль</label>
                    <input
                        type="password"
                        placeholder="Пароль"
                        className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-300"
                    />
                </div>
                <button
                    type="submit"
                    className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
                >
                    {isLogin ? 'Войти' : 'Зарегистрироваться'}
                </button>
            </form>
        </div>
    );
}

