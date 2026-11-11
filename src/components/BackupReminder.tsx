import { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useProgress } from '@/state/ProgressContext';
import { getMeta } from '@/services/storage/db';
import { needsBackupReminder, REMINDER_DAYS } from '@/services/storage/reminder';

export function BackupReminder() {
  const { attempts } = useProgress();
  const [last, setLast] = useState<string | undefined | null>(null);
  const onProgress = useLocation().pathname === '/progression';
  useEffect(() => {
    const load = () => void getMeta<string>('lastExportAt').then((v) => setLast(v));
    load();
    window.addEventListener('endo-exported', load);
    return () => window.removeEventListener('endo-exported', load);
  }, []);
  if (last === null || !needsBackupReminder(attempts.length, last, new Date())) return null;
  return (
    <div className="notice warn" role="status">
      💾 <strong>Pense à sauvegarder ta progression.</strong>{' '}
      {last ? `Ta dernière sauvegarde date de plus de ${REMINDER_DAYS} jours.` : 'Tu n’as encore jamais téléchargé de sauvegarde.'}{' '}
      Elle n’existe que dans ce navigateur.{' '}
      {onProgress ? 'Utilise le bouton « Télécharger ma sauvegarde » ci-dessous.' : <Link to="/progression">Sauvegarder maintenant</Link>}
    </div>
  );
}
