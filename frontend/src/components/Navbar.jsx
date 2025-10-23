import { Link, useNavigate } from 'react-router-dom';

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/');
  };

  return (
    <nav style={{
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      background: '#007bff',
      color: '#fff',
      padding: '1rem 2rem'
    }}>
      <div style={{ fontWeight: 'bold' }}>SkillMentor AI</div>
      <div style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/dashboard" style={{ color: '#fff', textDecoration: 'none' }}>Dashboard</Link>
        <Link to="/roadmap" style={{ color: '#fff', textDecoration: 'none' }}>Roadmap</Link>
        <button onClick={handleLogout} style={{
          background: '#fff',
          color: '#007bff',
          border: 'none',
          borderRadius: '6px',
          padding: '0.5rem 1rem',
          cursor: 'pointer'
        }}>
          Logout
        </button>
      </div>
    </nav>
  );
}
