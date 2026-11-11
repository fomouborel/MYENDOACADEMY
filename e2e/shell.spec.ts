import { expect, test, type Page } from '@playwright/test';
import { readFileSync } from 'node:fs';

/** Ouvre une rubrique via le menu (bouton ☰ sur smartphone). */
async function navTo(page: Page, label: string) {
  const menu = page.getByRole('button', { name: 'Ouvrir le menu' });
  if (await menu.isVisible()) await menu.click();
  await page.getByRole('navigation', { name: 'Navigation principale' }).getByRole('link', { name: label }).click();
}

test('accueil : les cours intégrés (thyroïde, hypophyse) sont accessibles', async ({ page }) => {
  await page.goto('./');
  await expect(page.getByRole('heading', { name: 'Bienvenue' })).toBeVisible();
  for (const t of ['Pathologies thyroïdiennes', 'Hyperthyroïdie', 'Hypothyroïdie', 'Hypophyse', 'Surrénales']) {
    await expect(page.getByRole('link', { name: new RegExp(t) }).first()).toBeVisible();
  }
});

test('mes cours : un cours ouvert n’apparaît jamais dans « Bientôt »', async ({ page }) => {
  const { chapters } = JSON.parse(readFileSync('content/chapters.json', 'utf8')) as { chapters: { title: string; status: string; lessons: unknown[] }[] };
  await page.goto('./#/cours');
  const open = page.getByRole('list', { name: 'Cours disponibles' });
  const soon = page.getByRole('list', { name: 'Cours bientôt disponibles' });
  for (const c of chapters) {
    const isOpen = c.status === 'available' && c.lessons.length > 0;
    await expect((isOpen ? open : soon).getByText(c.title, { exact: true })).toHaveCount(1);
    await expect((isOpen ? soon : open).getByText(c.title, { exact: true })).toHaveCount(0);
  }
});

test('menu : seules les rubriques disponibles sont proposées', async ({ page }) => {
  await page.goto('./');
  await navTo(page, 'Mes cours');
  await expect(page.getByRole('heading', { name: 'Mes cours' })).toBeVisible();
  const nav = page.getByRole('navigation', { name: 'Navigation principale' });
  // 9 rubriques + le lien « Mode d’emploi » en bas du menu
  await expect(nav.getByRole('link')).toHaveCount(10);
  await expect(nav.getByRole('link', { name: /Mode d’emploi/ })).toHaveCount(1);
});

test('sauvegarde et restauration de la progression', async ({ page }, info) => {
  await page.goto('./');
  await navTo(page, 'Ma progression');
  await expect(page).toHaveURL(/#\/progression$/);
  const [download] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Télécharger ma sauvegarde' }).click()]);
  expect(download.suggestedFilename()).toMatch(/^endocrino-academy-sauvegarde-\d{4}-\d{2}-\d{2}\.json$/);
  const path = info.outputPath('backup.json');
  await download.saveAs(path);
  expect(JSON.parse(readFileSync(path, 'utf8')).app).toBe('endocrino-academy');
  await page.locator('input[type=file]').setInputFiles(path);
  await expect(page.getByRole('status')).toContainText('Progression restaurée');
  await page.locator('input[type=file]').setInputFiles({ name: 'x.json', mimeType: 'application/json', buffer: Buffer.from('{"a":1}') });
  await expect(page.getByRole('status')).toContainText('ne ressemble pas à une sauvegarde');
});

test('rechargement direct d’une adresse (GitHub Pages)', async ({ page }) => {
  await page.goto('./#/cours/hyper/lecon/hyper-basedow');
  await expect(page.getByRole('heading', { name: 'La maladie de Basedow' })).toBeVisible();
});

test('pas de défilement horizontal (responsive)', async ({ page }) => {
  for (const url of ['./', './#/cours/thyroide/lecon/thyr-explo', './#/quiz?mode=exam-level&chapter=thyroide', './#/cours/hyper', './#/examens', './#/cas-cliniques', './#/examens-blancs', './#/erreurs', './#/revisions', './#/cours/hypophyse', './#/cours/hypophyse/lecon/hyph-anatomie', './#/cours/surrenales', './#/cours/surrenales/lecon/surr-hyperandrogenie']) {
    await page.goto(url);
    await page.waitForTimeout(200);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    expect(overflow, url).toBeLessThanOrEqual(0);
  }
});
