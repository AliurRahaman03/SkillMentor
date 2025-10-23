import { Outlet, Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import Navbar from './components/Navbar';

export default function App() {
  const navigate = useNavigate();

  // optional: auto-redirect if not logged in
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    const currentPath = window.location.pathname;
    if (!token && currentPath !== '/' && currentPath !== '/signup') {
      navigate('/');
    }
  }, [navigate]);

  return (
    <div>
      <Navbar />
      <main style={{ padding: '1.5rem' }}>
        {/* This renders the child route components */}
        <Outlet />
      </main>
    </div>
  );
}
