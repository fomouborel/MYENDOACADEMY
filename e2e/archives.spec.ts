import { expect, test } from '@playwright/test';

test('anciens examens : filtrer, consulter, travailler', async ({ page }) => {
  await page.goto('./#/examens');
  await expect(page.getByRole('heading', { name: 'Anciens examens' })).toBeVisible();
  const total = Number(await page.locator('p strong').first().textContent());
  expect(total).toBeGreaterThanOrEqual(130);

  // Filtre par session : composition annoncée affichée, jamais présentée comme complète
  await page.getByLabel('Année / session').selectOption('2026-01');
  await expect(page.getByText(/composition annoncée/)).toBeVisible();
  await expect(page.getByText(/la session n’est pas complète/)).toBeVisible();
  await expect(page.locator('.archive-item').first()).toContainText('Janvier 2026');

  // Ouvrir une question jouable et y répondre
  await page.getByLabel('Recherche').fill('amiodarone');
  await expect(page.locator('.archive-item')).toHaveCount(1);
  // Ouverture au clavier (focus + Entrée) : vérifie aussi l'accessibilité sans souris.
  await page.locator('.archive-item').first().focus();
  await page.keyboard.press('Enter');
  await expect(page.getByText('Identifiant : ENDO-2026-01')).toBeVisible();
  await page.locator('.choice').first().click();
  await page.getByRole('button', { name: 'Valider ma réponse' }).click();
  await expect(page.getByText('Réponse attendue :')).toBeVisible();
});

test('anciens examens : une question incomplète est consultable mais non notée', async ({ page }) => {
  await page.goto('./#/examens?reliability=incomplete');
  await page.locator('.archive-item').first().focus();
  await page.keyboard.press('Enter');
  await expect(page.getByText('Question consultable, non notée.')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Valider ma réponse' })).toHaveCount(0);
});

test('anciens examens : filtre pédiatrie et ancien titulaire', async ({ page }) => {
  await page.goto('./#/examens?teacher=Beauloye');
  const items = page.locator('.archive-item');
  await expect(items.first()).toContainText('Beauloye');
  await expect(items.first()).toContainText('Pédiatrie');
});
