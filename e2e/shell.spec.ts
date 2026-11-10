import { expect, test } from '@playwright/test';
import { readFileSync } from 'node:fs';

test('l’accueil s’affiche avec les trois cours de thyroïde', async ({ page }) => {
  await page.goto('./');
  await expect(page.getByRole('heading', { name: 'Bienvenue' })).toBeVisible();
  for (const t of ['Pathologies thyroïdiennes', 'Hyperthyroïdie', 'Hypothyroïdie']) {
    await expect(page.getByText(t, { exact: true })).toBeVisible();
  }
});

test('navigation, sauvegarde et restauration de la progression', async ({ page }, info) => {
  await page.goto('./');
  await page.getByRole('link', { name: /Ma progression/ }).click();
  await expect(page).toHaveURL(/#\/progression$/);
  const [download] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Télécharger ma sauvegarde' }).click()]);
  expect(download.suggestedFilename()).toMatch(/^endocrino-academy-sauvegarde-\d{4}-\d{2}-\d{2}\.json$/);
  const path = info.outputPath('backup.json');
  await download.saveAs(path);
  const json = JSON.parse(readFileSync(path, 'utf8'));
  expect(json.app).toBe('endocrino-academy');

  // restauration du fichier exporté
  await page.locator('input[type=file]').setInputFiles(path);
  await expect(page.getByRole('status')).toContainText('Progression restaurée');

  // fichier invalide : message compréhensible
  await page.locator('input[type=file]').setInputFiles({ name: 'x.json', mimeType: 'application/json', buffer: Buffer.from('{"a":1}') });
  await expect(page.getByRole('status')).toContainText('ne ressemble pas à une sauvegarde');
});

test('rechargement direct d’une rubrique (GitHub Pages)', async ({ page }) => {
  await page.goto('./#/progression');
  await expect(page.getByRole('heading', { name: 'Ma progression' })).toBeVisible();
});

test('pas de défilement horizontal (responsive)', async ({ page }) => {
  await page.goto('./');
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(0);
});
