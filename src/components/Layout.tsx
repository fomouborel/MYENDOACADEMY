import { NavLink, Outlet } from 'react-router-dom';

/** Navigation : seules les rubriques réellement disponibles sont affichées (aucun bouton factice). */
const NAV = [
  { to: '/', label: 'Accueil', icon: '🏠' },
  { to: '/progression', label: 'Ma progression', icon: '📈' },
];

export function Layout() {
  return (
    <div className="app">
      <header className="topbar">
        <span className="brand">ENDOCRINO <strong>ACADEMY</strong></span>
      </header>
      <nav className="nav" aria-label="Navigation principale">
        {NAV.map((n) => (
          <NavLink key={n.to} to={n.to} end className={({ isActive }) => (isActive ? 'nav-item active' : 'nav-item')}>
            <span aria-hidden>{n.icon}</span> {n.label}
          </NavLink>
        ))}
      </nav>
      <main className="main">
        <Outlet />
      </main>
    </div>
  );
}
