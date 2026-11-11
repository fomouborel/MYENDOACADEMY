import { expect, test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const PAGES = ['./', './#/cours', './#/cours/thyroide', './#/cours/hyper/lecon/hyper-diagnostic', './#/quiz?mode=exam-level&chapter=hypo',
  './#/entrainement', './#/examens', './#/cas-cliniques/cas-hyper-basedow', './#/examens-blancs', './#/erreurs', './#/revisions', './#/progression', './#/aide',
  './#/cours/hypophyse', './#/cours/hypophyse/lecon/hyph-anatomie', './#/quiz?mode=check&chapter=hypophyse',
  './#/cours/surrenales', './#/cours/surrenales/lecon/surr-incidentalome', './#/cours/pharmaco', './#/cours/obesite', './#/cours/obesite/lecon/obes-traitement'];

test('accessibilité : aucune violation grave ou critique (axe-core)', async ({ page }) => {
  const all: string[] = [];
  for (const url of PAGES) {
    await page.goto(url);
    await page.waitForTimeout(150);
    const r = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa']).analyze();
    const serious = r.violations.filter((v) => v.impact === 'serious' || v.impact === 'critical');
    all.push(...serious.map((v) => `${url} → ${v.id} : ${v.help} (${v.nodes.length}) ${v.nodes[0]?.target.join(' ')}`));
  }
  expect(all).toEqual([]);
});

test('hors connexion : l’application se recharge sans réseau après une première visite', async ({ page, context }) => {
  await page.goto('./');
  await page.evaluate(async () => { await navigator.serviceWorker.ready; });
  await page.reload(); // la page est désormais contrôlée par le service worker
  await page.evaluate(async () => { await navigator.serviceWorker.ready; });
  await context.setOffline(true);
  await page.reload();
  await expect(page.getByRole('heading', { name: 'Bienvenue' })).toBeVisible();
  await page.goto('./#/cours/hypo/lecon/hypo-traitement');
  await expect(page.getByRole('heading', { name: /L-thyroxine/ }).first()).toBeVisible();
  await context.setOffline(false);
});
