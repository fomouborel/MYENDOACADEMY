import { useEffect, useState } from 'react';
import { NavLink, Outlet, useLocation } from 'react-router-dom';

/**
 * Navigation principale (prompt § 14). Seules les rubriques réellement disponibles sont affichées :
 * les autres (Cas cliniques, Examens blancs, Mes erreurs, Mes révisions) apparaîtront
 * au fur et à mesure de leur mise en service — aucun bouton factice.
 */
export const NAV = [
  { to: '/', label: 'Accueil', icon: '🏠', end: true },
  { to: '/cours', label: 'Mes cours', icon: '📘' },
  { to: '/entrainement', label: 'Entraînement', icon: '🎯' },
  { to: '/examens', label: 'Anciens examens', icon: '🗂️' },
  { to: '/progression', label: 'Ma progression', icon: '📈' },
];

export function Layout() {
  const [open, setOpen] = useState(false);
  const location = useLocation();
  useEffect(() => {
    setOpen(false);
    window.scrollTo?.(0, 0);
  }, [location.pathname, location.search]);

  return (
    <div className="app">
      <header className="topbar">
        <button className="menu-btn" aria-label={open ? 'Fermer le menu' : 'Ouvrir le menu'} aria-expanded={open} aria-controls="sidebar" onClick={() => setOpen((o) => !o)}>
          {open ? '✕' : '☰'}
        </button>
        <span className="brand">ENDOCRINO <strong>ACADEMY</strong></span>
      </header>
      <nav id="sidebar" className={open ? 'sidebar open' : 'sidebar'} aria-label="Navigation principale">
        <span className="brand side-brand">ENDOCRINO <strong>ACADEMY</strong></span>
        {NAV.map((n) => (
          <NavLink key={n.to} to={n.to} end={n.end} className={({ isActive }) => (isActive ? 'nav-item active' : 'nav-item')}>
            <span aria-hidden className="nav-icon">{n.icon}</span>
            {n.label}
          </NavLink>
        ))}
        <p className="side-note">Autres rubriques (cas cliniques, examens blancs, erreurs, révisions) : en préparation.</p>
      </nav>
      {open && <div className="backdrop" onClick={() => setOpen(false)} aria-hidden />}
      <main className="main">
        <Outlet />
      </main>
    </div>
  );
}
