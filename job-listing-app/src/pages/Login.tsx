import React from 'react';
import { useForm } from 'react-hook-form';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const { register, handleSubmit, setError, formState: { errors } } = useForm();

  const onLogin = async (data: any) => {
    try {
      const response = await fetch('https://akil-backend.onrender.com/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (!response.ok) throw new Error(result.message || 'Login failed');

      // Assuming API returns { data: { accessToken: "...", ... } }
      // Adjust based on actual API response inspection
      if (result.data && result.data.accessToken) {
        login(result.data.accessToken, result.data);
        navigate('/');
      } else {
        throw new Error('Invalid response from server');
      }
      
    } catch (err: any) {
      setError('root', { message: err.message });
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 p-4">
      <div className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md border border-gray-100">
        <h2 className="text-2xl font-bold text-slate-800 text-center mb-2">Welcome Back</h2>
        <p className="text-slate-500 text-center mb-6">Login to find your dream job</p>

        <form onSubmit={handleSubmit(onLogin)} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">Email</label>
            <input 
              type="email"
              {...register('email', { required: 'Email is required' })}
              className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none"
              placeholder="jane@example.com"
            />
            {errors.email && <p className="text-red-500 text-xs mt-1">{errors.email.message as string}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">Password</label>
            <input 
              type="password"
              {...register('password', { required: 'Password is required' })}
              className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none"
            />
            {errors.password && <p className="text-red-500 text-xs mt-1">{errors.password.message as string}</p>}
          </div>

          {errors.root && <div className="text-red-500 text-sm text-center bg-red-50 p-2 rounded">{errors.root.message}</div>}

          <button type="submit" className="w-full bg-primary text-white py-2 rounded-lg hover:bg-indigo-700 transition">
            Login
          </button>

          <p className="text-center text-sm text-slate-600 mt-4">
            Don't have an account? <Link to="/signup" className="text-primary font-bold">Sign Up</Link>
          </p>
        </form>
      </div>
    </div>
  );
};