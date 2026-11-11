import { expect, test } from '@playwright/test';

test('parcours complet : leçon, vérification, niveau examen, progression', async ({ page }) => {
  // 1. Ouvrir un cours et une leçon
  await page.goto('./#/cours/thyroide');
  await expect(page.getByRole('heading', { name: /Pathologies thyroïdiennes/ })).toBeVisible();
  await page.getByRole('link', { name: /Physiologie et exploration/ }).click();
  await expect(page.getByText('🟦 Archives UCL — ce que les examens interrogent', { exact: false })).toBeVisible();
  await expect(page.getByText('🟨 Explication complémentaire — à valider')).toBeVisible();
  await expect(page.getByRole('heading', { name: /À retenir/ })).toBeVisible();
  await page.getByRole('button', { name: 'J’ai terminé cette leçon' }).click();
  await expect(page.getByRole('button', { name: /Leçon terminée/ })).toBeVisible();

  // 2. Vérifier ma compréhension (vrai/faux) avec indices
  await page.goto('./#/quiz?mode=check&chapter=thyroide');
  await expect(page.getByText('Exercice d’entraînement (hors archives)')).toBeVisible();
  await page.getByRole('button', { name: /Afficher un indice/ }).click();
  await expect(page.getByText(/Indice 1 :/)).toBeVisible();
  await page.getByRole('button', { name: /Indice suivant/ }).click();
  await expect(page.getByText(/Indice 2 :/)).toBeVisible();
  const validate = page.getByRole('button', { name: 'Valider ma réponse' });
  await expect(validate).toBeDisabled(); // pas de correction sans tentative
  await page.getByRole('button', { name: 'Faux' }).click();
  await validate.click();
  await expect(page.getByText(/Bonne réponse|Ce n’est pas la réponse attendue/)).toBeVisible();
  await expect(page.getByText('Réponse attendue :')).toBeVisible();
  await expect(page.getByText('Exercice créé — à valider')).toBeVisible();

  // 3. Niveau examen : vraie question d'archives, sans indice
  await page.goto('./#/quiz?mode=exam-level&chapter=hyper');
  await expect(page.getByText(/Ancien examen/)).toBeVisible();
  await expect(page.getByRole('button', { name: /indice/i })).toHaveCount(0);
  await page.locator('.choice').first().click();
  await page.getByRole('button', { name: 'Valider ma réponse' }).click();
  await expect(page.getByText('Réponse proposée (compilation)')).toBeVisible();
  await expect(page.getByText(/non officielle/)).toBeVisible();
  await expect(page.getByRole('link', { name: /Revoir :/ }).first()).toBeVisible();

  // 4. La progression est enregistrée et survit au rechargement
  await page.goto('./#/progression');
  await page.reload();
  const worked = page.locator('.stat', { hasText: 'Travaillées' }).locator('.stat-v');
  await expect(worked).toHaveText('1');
  await expect(page.locator('.card', { hasText: 'Pathologies thyroïdiennes' })).toContainText('1/5 leçons');
});

test('QCM « deux fausses » : deux propositions exigées', async ({ page }) => {
  await page.goto('./#/quiz?mode=lesson&lesson=thyr-thyroidites');
  // avancer jusqu'à la question « thyroïdite silencieuse »
  for (let i = 0; i < 10; i++) {
    if (await page.getByText('Cochez les deux propositions FAUSSES.').isVisible()) break;
    await page.locator('.choice').first().click();
    await page.getByRole('button', { name: 'Valider ma réponse' }).click();
    await page.getByRole('button', { name: /Question suivante|Voir le bilan/ }).click();
  }
  await expect(page.getByText('Cochez les deux propositions FAUSSES.')).toBeVisible();
  const validate = page.getByRole('button', { name: 'Valider ma réponse' });
  await page.getByRole('button', { name: /Douleur cervicale/ }).click();
  await expect(validate).toBeDisabled();
  await page.getByRole('button', { name: /Thyroglobuline indosable/ }).click();
  await validate.click();
  await expect(page.getByText('✅ Bonne réponse')).toBeVisible();
});

test('entraînement libre : composer une série', async ({ page }) => {
  await page.goto('./#/entrainement');
  await page.getByLabel('Type').selectOption('archive');
  await page.getByLabel('Nombre').selectOption('5');
  await page.getByRole('button', { name: 'Commencer la série' }).click();
  await expect(page.getByText('Question 1 sur 5')).toBeVisible();
});
