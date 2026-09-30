// Optional build-time tools: playwright and sharp. Viewing slides needs neither.
const { chromium } = require('playwright');
const sharp = require('sharp');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const assert = require('node:assert/strict');
(async () => {
  const root = __dirname;
  await fs.mkdir(path.join(root, 'previews'), { recursive: true });
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1.2 });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('requestfailed', request => errors.push(request.url()));
    const url = pathToFileURL(path.join(root, 'index.html')).href;
    await page.goto(url + '?export#1');
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => Promise.all([...document.images].map(im => im.decode())));
    const total = await page.locator('.slide').count();
    assert.equal(await page.locator('#page').getAttribute('max'), String(total), 'nav max matches slide count');
    const titles = [];
    for (let i = 1; i <= total; i++) {
      await page.evaluate(n => { location.hash = String(n); }, i);
      await page.waitForFunction(n => document.querySelector('#page').value === String(n), i);
      const slide = page.locator('.slide:not([hidden])');
      titles.push(await slide.getAttribute('data-title'));
      await slide.screenshot({ path: path.join(root, 'previews', `${String(i).padStart(2, '0')}.png`) });
      const overflow = await slide.evaluate(el => [...el.querySelectorAll('h1,h2,h3,p,li')].filter(x => x.scrollWidth > x.clientWidth + 2).map(x => x.textContent));
      assert.deepEqual(overflow, [], `Text overflow on slide ${i}`);
    }
    assert.deepEqual(errors, [], 'Browser load/runtime errors');
    await page.goto(url + '#1');
    await page.keyboard.press('ArrowRight'); assert.equal(await page.locator('#page').inputValue(), '2');
    await page.keyboard.press('Space'); assert.equal(await page.locator('#page').inputValue(), '3');
    await page.keyboard.press('Shift+Space'); assert.equal(await page.locator('#page').inputValue(), '2');
    await page.keyboard.press('End'); assert.equal(await page.locator('#page').inputValue(), String(total));
    assert(await page.locator('#next').isDisabled());
    await page.keyboard.press('Home'); assert(await page.locator('#prev').isDisabled());
    await page.keyboard.press('h'); assert(await page.locator('nav').isHidden());
    await page.keyboard.press('Escape'); assert(await page.locator('nav').isVisible());
    await page.locator('#page').fill('99'); await page.locator('#page').dispatchEvent('change');
    assert.equal(await page.locator('#page').inputValue(), String(total));
    await page.goto(url + '#invalid');
    await page.waitForFunction(() => document.querySelector('#page').value === '1');
    await page.locator('#fullscreen').click();
    await page.waitForFunction(() => Boolean(document.fullscreenElement));
    await page.evaluate(() => document.exitFullscreen());
    for (const [width, height] of [[1280,720],[390,844]]) {
      await page.setViewportSize({width,height});
      await page.waitForTimeout(100);
      const box=await page.locator('.slide:not([hidden])').boundingBox();
      assert(box.x >= -1 && box.y >= -1 && box.x+box.width <= width+1 && box.y+box.height <= height+1);
    }
    await page.setViewportSize({width:1600,height:900});
    await page.emulateMedia({media:'print'});
    assert.equal(await page.locator('.slide:visible').count(),total);
    await page.pdf({path:'/tmp/lecture2-print-check.pdf',printBackground:true,preferCSSPageSize:true});
    const layers=[];
    for(let i=0;i<total;i++) layers.push({input:await sharp(path.join(root,'previews',`${String(i+1).padStart(2,'0')}.png`)).resize(800,450).toBuffer(),left:24+(i%2)*824,top:24+Math.floor(i/2)*474});
    await sharp({create:{width:1672,height:24+Math.ceil(total/2)*474,channels:3,background:'#d7d6d0'}}).composite(layers).png().toFile(path.join(root,'previews','overview.png'));
    const tiles=titles.map((title,i)=>`<a href="index.html#${i+1}"><img src="previews/${String(i+1).padStart(2,'0')}.png" alt="${i+1}. ${title}"><p>${String(i+1).padStart(2,'0')} — ${title}</p></a>`).join('\n');
    await fs.writeFile(path.join(root,'review.html'),`<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>第2回スライド — ${total}枚のレビュー</title><style>body{margin:32px;background:#eeede8;color:#111;font-family:system-ui,sans-serif}h1{font-size:28px}main{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px}img{width:100%;display:block;box-shadow:0 3px 12px #0002}a{color:inherit;text-decoration:none}p{font-size:15px}header{margin-bottom:28px}header a{text-decoration:underline}@media(max-width:750px){main{grid-template-columns:1fr}body{margin:16px}}</style></head><body><header><h1>第2回 — ${total}枚</h1><p>各画像をクリックすると、そのページを投影表示できます。</p><a href="index.html">スライドを開く →</a>　<a href="previews/overview.png">一覧画像を開く ↗</a></header><main>${tiles}</main></body></html>`);
    console.log(`PASS: ${total} slides exported at 1920×1080; local fonts/images; text width; navigation; URL; responsive sizing; print visibility.`);
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exit(1)});
