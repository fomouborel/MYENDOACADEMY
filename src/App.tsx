import { HashRouter, Route, Routes } from 'react-router-dom';
import { Layout } from '@/components/Layout';
import { HomePage } from '@/pages/HomePage';
import { ProgressPage } from '@/pages/ProgressPage';

/**
 * HashRouter : les adresses (#/progression) fonctionnent sur GitHub Pages sans configuration serveur,
 * y compris après un rechargement de page ou depuis un favori.
 */
export function App() {
  return (
    <HashRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path="progression" element={<ProgressPage />} />
        </Route>
      </Routes>
    </HashRouter>
  );
}
