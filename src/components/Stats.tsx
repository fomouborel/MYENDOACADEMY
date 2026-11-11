import { questions } from '@/data/content';
import { coverage } from '@/services/progress/coverage';
import { useProgress } from '@/state/ProgressContext';

/** Couverture des archives et taux de réussite : calculés uniquement à partir des réponses réelles. */
export function CoverageStats() {
  const { states } = useProgress();
  const c = coverage(questions, states, new Date());
  const noted = [...states.values()].filter((s) => s.lastCorrect !== null);
  const rate = noted.length ? Math.round((noted.filter((s) => s.lastCorrect).length / noted.length) * 100) : null;
  const items = [
    ['Questions d’examen disponibles', c.available],
    ['Travaillées', c.worked],
    ['Réussies', c.succeeded],
    ['Échouées', c.failed],
    ['À revoir', c.toReview],
    ['Maîtrisées', c.mastered],
    ['Restent à travailler', c.remaining],
  ] as const;
  return (
    <>
      <div className="stats">
        {items.map(([label, v]) => (
          <div key={label} className="stat"><span className="stat-v">{v}</span><span className="stat-l">{label}</span></div>
        ))}
        <div className="stat"><span className="stat-v">{rate === null ? '—' : `${rate} %`}</span><span className="stat-l">Taux de réussite (dernière réponse)</span></div>
      </div>
      <p className="muted">
        Une question compte comme « travaillée » seulement après une réponse validée. {c.consultOnly} question(s) incomplète(s) ou sans réponse dans la compilation seront consultables dans « Anciens examens », sans être notées.
      </p>
    </>
  );
}
