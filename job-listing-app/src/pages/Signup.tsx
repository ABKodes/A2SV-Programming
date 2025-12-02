import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link, useNavigate } from 'react-router-dom';

export const Signup = () => {
  const [step, setStep] = useState<'signup' | 'verify'>('signup');
  const [emailToVerify, setEmailToVerify] = useState('');
  const navigate = useNavigate();
  
  const { register, handleSubmit, formState: { errors }, watch, setError } = useForm();

  const onSignup = async (data: any) => {
    try {
      const response = await fetch('https://akil-backend.onrender.com/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...data, role: 'user' }), // Default role
      });

      const result = await response.json();

      if (!response.ok) throw new Error(result.message || 'Signup failed');

      // On success, move to verification step
      setEmailToVerify(data.email);
      setStep('verify');
    } catch (err: any) {
      setError('root', { message: err.message });
    }
  };

  const onVerify = async (data: any) => {
    try {
      const response = await fetch('https://akil-backend.onrender.com/verify-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: emailToVerify, OTP: data.otp }),
      });

      if (!response.ok) throw new Error('Verification failed');

      // Redirect to login after verification
      navigate('/login');
    } catch (err: any) {
      setError('root', { message: err.message });
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 p-4">
      <div className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md border border-gray-100">
        <h2 className="text-2xl font-bold text-slate-800 text-center mb-6">
          {step === 'signup' ? 'Create an Account' : 'Verify Email'}
        </h2>

        {step === 'signup' ? (
          <form onSubmit={handleSubmit(onSignup)} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Full Name</label>
              <input 
                {...register('name', { required: 'Name is required' })}
                className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none"
                placeholder="Jane Doe"
              />
              {errors.name && <p className="text-red-500 text-xs mt-1">{errors.name.message as string}</p>}
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Email</label>
              <input 
                type="email"
                {...register('email', { required: 'Email is required' })}
                className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none"
                placeholder="jane@example.com"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Password</label>
              <input 
                type="password"
                {...register('password', { required: 'Password is required', minLength: { value: 6, message: 'Min 6 chars' } })}
                className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Confirm Password</label>
              <input 
                type="password"
                {...register('confirmPassword', { 
                  validate: (val) => watch('password') === val || "Passwords do not match"
                })}
                className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none"
              />
              {errors.confirmPassword && <p className="text-red-500 text-xs mt-1">{errors.confirmPassword.message as string}</p>}
            </div>

            {errors.root && <div className="text-red-500 text-sm text-center">{errors.root.message}</div>}

            <button type="submit" className="w-full bg-primary text-white py-2 rounded-lg hover:bg-indigo-700 transition">
              Sign Up
            </button>
            
            <p className="text-center text-sm text-slate-600 mt-4">
              Already have an account? <Link to="/login" className="text-primary font-bold">Login</Link>
            </p>
          </form>
        ) : (
          <form onSubmit={handleSubmit(onVerify)} className="space-y-4">
            <p className="text-sm text-slate-600 text-center mb-4">
              We sent a code to <b>{emailToVerify}</b>
            </p>
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">OTP Code</label>
              <input 
                {...register('otp', { required: 'OTP is required' })}
                className="w-full p-2 border rounded-lg focus:ring-2 focus:ring-primary outline-none text-center tracking-widest"
                placeholder="1234"
              />
            </div>
             {errors.root && <div className="text-red-500 text-sm text-center">{errors.root.message}</div>}
            <button type="submit" className="w-full bg-primary text-white py-2 rounded-lg hover:bg-indigo-700 transition">
              Verify Account
            </button>
          </form>
        )}
      </div>
    </div>
  );
};