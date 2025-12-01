import React from 'react';
import { useForm, type SubmitHandler } from 'react-hook-form';
import './ContactForm.css';

// 1. Define the shape of our form data
interface IFormInput {
  name: string;
  email: string;
  message: string;
}

export const ContactForm: React.FC = () => {
  // 2. Initialize the useForm hook
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitSuccessful },
  } = useForm<IFormInput>();

  // 3. Define the submit handler
  const onSubmit: SubmitHandler<IFormInput> = (data) => {
    console.log('Form Data Submitted:', data);
    // Simulate an API call here if needed
    setTimeout(() => {
      alert(`Thank you, ${data.name}! Your message has been sent.`);
      reset(); // Clear the form after success
    }, 500);
  };

  return (
    <div className="form-container">
      <h2>Get in Touch</h2>
      <p>We'd love to hear from you. Please fill out this form.</p>
      
      {/* 4. Handle Submit using the hook's handleSubmit */}
      <form onSubmit={handleSubmit(onSubmit)} noValidate>
        
        {/* Name Field */}
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            id="name"
            type="text"
            placeholder="Jane Doe"
            // 5. Register the input with validation rules
            {...register('name', { 
              required: 'Name is required',
              minLength: { value: 2, message: 'Name must be at least 2 characters' }
            })}
            className={errors.name ? 'error-input' : ''}
          />
          {errors.name && <span className="error-msg">{errors.name.message}</span>}
        </div>

        {/* Email Field */}
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            placeholder="jane@example.com"
            {...register('email', {
              required: 'Email is required',
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: 'Invalid email address',
              },
            })}
            className={errors.email ? 'error-input' : ''}
          />
          {errors.email && <span className="error-msg">{errors.email.message}</span>}
        </div>

        {/* Message Field */}
        <div className="form-group">
          <label htmlFor="message">Message</label>
          <textarea
            id="message"
            rows={5}
            placeholder="How can we help you?"
            {...register('message', {
              required: 'Message is required',
              minLength: { value: 10, message: 'Message must be at least 10 characters' }
            })}
            className={errors.message ? 'error-input' : ''}
          />
          {errors.message && <span className="error-msg">{errors.message.message}</span>}
        </div>

        <button type="submit" className="submit-btn">
          Send Message
        </button>

        {isSubmitSuccessful && <p className="success-msg">Message sent successfully!</p>}
      </form>
    </div>
  );
};