/** État de progression partagé par toute l'application (lu depuis IndexedDB, rafraîchi après chaque action). */
import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from 'react';
import type { Attempt, LessonProgress, QuestionState, SessionRecord } from '@/schemas/progress';
import { getAttempts, getLessons, getSessions, getStates, markLesson, recordAttempt, saveSession, setDraft, setFlag } from '@/services/storage/db';

interface ProgressValue {
  ready: boolean;
  states: Map<string, QuestionState>;
  lessons: Map<string, LessonProgress>;
  sessions: SessionRecord[];
  attempts: Attempt[];
  saveSession: (s: SessionRecord) => Promise<void>;
  setDraft: (ids: string[], draft: boolean) => Promise<void>;
  record: (a: Attempt) => Promise<void>;
  flag: (questionId: string, flagged: boolean) => Promise<void>;
  lessonDone: (lessonId: string, done: boolean) => Promise<void>;
  reload: () => Promise<void>;
}

const Ctx = createContext<ProgressValue | null>(null);

export function ProgressProvider({ children }: { children: ReactNode }) {
  const [ready, setReady] = useState(false);
  const [states, setStates] = useState(new Map<string, QuestionState>());
  const [lessons, setLessons] = useState(new Map<string, LessonProgress>());
  const [sessions, setSessions] = useState<SessionRecord[]>([]);
  const [attempts, setAttempts] = useState<Attempt[]>([]);

  const reload = useCallback(async () => {
    const [s, l, ss, at] = await Promise.all([getStates(), getLessons(), getSessions(), getAttempts()]);
    setAttempts(at);
    setStates(s);
    setLessons(new Map(l.map((x) => [x.lessonId, x])));
    setSessions(ss);
    setReady(true);
  }, []);

  useEffect(() => {
    void reload();
  }, [reload]);

  const value = useMemo<ProgressValue>(
    () => ({
      ready,
      states,
      lessons,
      sessions,
      attempts,
      reload,
      record: async (a) => {
        const next = await recordAttempt(a);
        setStates((prev) => new Map(prev).set(next.questionId, next));
        setAttempts((prev) => [...prev, a]);
      },
      saveSession: async (s) => {
        await saveSession(s);
        setSessions((prev) => [...prev.filter((x) => x.id !== s.id), s]);
      },
      setDraft: async (ids, d) => {
        await setDraft(ids, d);
        const fresh = await getStates();
        setStates(fresh);
      },
      flag: async (id, f) => {
        await setFlag(id, f);
        await reload();
      },
      lessonDone: async (id, d) => {
        await markLesson(id, d);
        await reload();
      },
    }),
    [ready, states, lessons, sessions, attempts, reload],
  );
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useProgress(): ProgressValue {
  const v = useContext(Ctx);
  if (!v) throw new Error('useProgress doit être utilisé dans ProgressProvider');
  return v;
}
