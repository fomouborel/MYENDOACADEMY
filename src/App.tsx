import { HashRouter, Route, Routes } from 'react-router-dom';
import { Layout } from '@/components/Layout';
import { HomePage } from '@/pages/HomePage';
import { ProgressPage } from '@/pages/ProgressPage';
import { CoursesPage } from '@/pages/CoursesPage';
import { ChapterPage } from '@/pages/ChapterPage';
import { LessonPage } from '@/pages/LessonPage';
import { QuizPage } from '@/pages/QuizPage';
import { TrainingPage } from '@/pages/TrainingPage';
import { ProgressProvider } from '@/state/ProgressContext';

/**
 * HashRouter : les adresses (#/cours/…) fonctionnent sur GitHub Pages sans configuration serveur,
 * y compris après un rechargement de page ou depuis un favori.
 */
export function App() {
  return (
    <ProgressProvider>
      <HashRouter>
        <Routes>
          <Route element={<Layout />}>
            <Route index element={<HomePage />} />
            <Route path="cours" element={<CoursesPage />} />
            <Route path="cours/:chapterId" element={<ChapterPage />} />
            <Route path="cours/:chapterId/lecon/:lessonId" element={<LessonPage />} />
            <Route path="quiz" element={<QuizPage />} />
            <Route path="entrainement" element={<TrainingPage />} />
            <Route path="progression" element={<ProgressPage />} />
            <Route path="*" element={<p>Page introuvable. Utilise le menu pour revenir à l’accueil.</p>} />
          </Route>
        </Routes>
      </HashRouter>
    </ProgressProvider>
  );
}
