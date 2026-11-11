import { expect, test } from '@playwright/test';

test('cas clinique progressif : chaque étape se débloque après la réponse', async ({ page }) => {
  await page.goto('./#/cas-cliniques');
  await expect(page.getByRole('heading', { name: 'Cas cliniques', exact: true })).toBeVisible();
  await page.goto('./#/cas-cliniques/cas-hypo-centrale');
  await expect(page.getByRole('heading', { name: 'Étape 1 / 3' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Étape 2 / 3' })).toHaveCount(0); // pas de révélation anticipée
  await expect(page.getByRole('cell', { name: 'T4 libre' })).toBeVisible(); // tableau biologique avec normes
  await page.getByRole('button', { name: /Hypothyroïdie centrale/ }).click();
  await page.getByRole('button', { name: 'Valider ma réponse' }).click();
  await expect(page.getByRole('heading', { name: 'Étape 2 / 3' })).toBeVisible();
});

test('examen blanc : pas de correction pendant, brouillon conservé, correction à la fin', async ({ page }) => {
  await page.goto('./#/examens-blancs');
  await page.getByLabel('Nombre de questions').selectOption('10');
  await page.getByRole('button', { name: 'Commencer l’examen blanc' }).click();
  await expect(page.getByRole('timer')).toBeVisible();
  await page.locator('.choice').first().click();
  await expect(page.getByText('Réponse attendue')).toHaveCount(0); // aucune correction pendant l'examen
  await expect(page.locator('.dot.done')).toHaveCount(1);
  await expect(page.getByText('✓ réponses enregistrées')).toBeVisible();
  await page.reload(); // interruption
  await expect(page.locator('.choice.selected')).toHaveCount(1); // brouillon repris
  page.once('dialog', (d) => d.accept());
  await page.getByRole('button', { name: 'Terminer maintenant' }).click();
  await expect(page.getByRole('heading', { name: /Correction/ })).toBeVisible();
  await expect(page.getByText('Réponse attendue').first()).toBeVisible();
  await page.goto('./#/examens-blancs');
  await expect(page.getByText(/Score : \d+ %/)).toBeVisible();
});

test('évaluation finale d’un cours, carnet d’erreurs, révisions et tableau de bord', async ({ page }) => {
  await page.goto('./#/cours/hypo');
  await page.getByRole('button', { name: 'Commencer l’évaluation' }).click();
  await expect(page.getByRole('heading', { name: /Évaluation finale — Hypothyroïdie/ })).toBeVisible();
  // répondre « au hasard » à la première question puis terminer
  await page.locator('.choice').first().click();
  page.once('dialog', (d) => d.accept());
  await page.getByRole('button', { name: 'Terminer maintenant' }).click();
  await expect(page.getByRole('heading', { name: /Correction/ })).toBeVisible();

  // une erreur certaine sur un vrai/faux connu (réponse attendue : FAUX)
  await page.goto('./#/quiz?mode=free&ids=ENDO-EX-hypo-VF-001');
  await page.getByRole('button', { name: 'Vrai' }).click();
  await page.getByRole('button', { name: 'Valider ma réponse' }).click();
  await expect(page.getByText('Ce n’est pas la réponse attendue')).toBeVisible();

  await page.goto('./#/erreurs');
  await expect(page.locator('.error-item', { hasText: 'Dans une hypothyroïdie centrale, la TSH est toujours diminuée' })).toBeVisible();
  await expect(page.getByText('Ta réponse : Vrai').first()).toBeVisible();

  await page.goto('./#/revisions');
  const recent = page.locator('.card', { hasText: 'Erreurs récentes' });
  await expect(recent).not.toContainText('0 question(s)');

  await page.goto('./');
  await expect(page.getByRole('heading', { name: 'Dernières erreurs' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Activité des 7 derniers jours' })).toBeVisible();
  await page.goto('./#/cours/hypo');
  await expect(page.getByText(/Dernières évaluations/)).toBeVisible();
});
