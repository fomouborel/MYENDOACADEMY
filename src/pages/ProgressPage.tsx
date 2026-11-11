import { useRef, useState } from 'react';
import { CoverageStats } from '@/components/Stats';
import { ChapterCard } from '@/components/ChapterCard';
import { openChapters } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { BackupError, backupFileName, exportBackup, importBackup, markExported, parseBackup } from '@/services/storage/backup';
import { BackupReminder } from '@/components/BackupReminder';

export function ProgressPage() {
  const [message, setMessage] = useState<{ kind: 'ok' | 'error'; text: string } | null>(null);
  const [mode, setMode] = useState<'merge' | 'replace'>('merge');
  const fileRef = useRef<HTMLInputElement>(null);
  const { reload } = useProgress();

  async function onExport() {
    const data = await exportBackup();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = backupFileName();
    a.click();
    URL.revokeObjectURL(url);
    await markExported();
    window.dispatchEvent(new Event('endo-exported'));
    setMessage({ kind: 'ok', text: 'Sauvegarde téléchargée. Garde ce fichier en lieu sûr (par exemple dans ton cloud personnel).' });
  }

  async function onImport(file: File) {
    try {
      const backup = parseBackup(await file.text());
      if (mode === 'replace' && !window.confirm('Remplacer toute ta progression actuelle par celle du fichier ?')) return;
      const r = await importBackup(backup, mode);
      await reload();
      setMessage({ kind: 'ok', text: `Progression restaurée : ${r.attemptsAdded} réponse(s) importée(s), ${r.questionsUpdated} question(s) mises à jour.` });
    } catch (e) {
      setMessage({ kind: 'error', text: e instanceof BackupError ? e.message : 'La restauration a échoué. Vérifie que le fichier est bien une sauvegarde.' });
    } finally {
      if (fileRef.current) fileRef.current.value = '';
    }
  }

  return (
    <section>
      <h1>Ma progression</h1>
      <p className="lead">Tes réponses sont enregistrées automatiquement sur cet appareil, dans ce navigateur.</p>
      <BackupReminder />
      <h2>Archives travaillées</h2>
      <CoverageStats />
      <h2>Par cours</h2>
      <ul className="cards">{openChapters.map((c) => <ChapterCard key={c.id} c={c} />)}</ul>
      <h2>Sauvegarde et restauration</h2>
      <div className="notice">
        Ta progression n’est <strong>pas synchronisée</strong> entre ton ordinateur, ta tablette et ton téléphone. Pour passer d’un appareil à l’autre, télécharge une sauvegarde puis restaure-la sur l’autre appareil.
      </div>
      <h3>Sauvegarder</h3>
      <button className="btn" onClick={onExport}>Télécharger ma sauvegarde</button>
      <h3>Restaurer</h3>
      <fieldset className="choices">
        <label><input type="radio" name="mode" checked={mode === 'merge'} onChange={() => setMode('merge')} /> Ajouter à ma progression actuelle (recommandé)</label>
        <label><input type="radio" name="mode" checked={mode === 'replace'} onChange={() => setMode('replace')} /> Remplacer ma progression actuelle</label>
      </fieldset>
      <label className="btn secondary">
        Choisir un fichier de sauvegarde
        <input ref={fileRef} type="file" accept="application/json,.json" hidden onChange={(e) => e.target.files?.[0] && onImport(e.target.files[0])} />
      </label>
      {message && <p role="status" className={message.kind === 'ok' ? 'msg ok' : 'msg error'}>{message.text}</p>}
    </section>
  );
}
