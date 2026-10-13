# 第4回スライド：65枚

16:9（1600×900のレイアウト、PNGは1920×1080）。第2回の紙面、黒・黄色、淡色の紙片、太い日本語見出し、手書き注記を引き継いだ編集可能なHTMLスライドです。

- [スライドを表示](index.html)
- [レビュー用一覧](review.html)
- [一覧画像](previews/overview.png)
- [PDF（65ページ）](slides.pdf)
- [資料・コピー用プロンプト](workbook.html)
- [スライドと本文の対応表](slide-map.md)

## 構成

| 枚 | 内容 |
| --- | --- |
| 01–13 | 導入、準備、要件、D-1、変更の予測と振り返り |
| 14–26 | アーキテクチャ、部品の役割、保存方法、同期／非同期、つなぎ目の約束 |
| 27–34 | AIと設計する、design.mdの下書き、D-2、3限まとめ |
| 35–42 | 4限導入、模擬店注文サービス、2案の比較、図の描き方 |
| 43–53 | 個人で複数案を理解・作図・選択し、チームで共有・合意する |
| 54–60 | 部品の役を分担した検証、他チームのレビュー、個人の説明 |
| 61–65 | まとめ、提出物、事後学習、次回予告、参考資料 |

AIへの長い指示は、スライド右下の「資料・プロンプト」から対応する節を開き、コピーできます。全文は講義READMEから生成しています。スライドの短い指示は投影用の要約です。

## 閲覧と操作

`index.html`をブラウザで開きます。閲覧にインストールは不要です。フォントと画像はローカルに同梱しています（外部資料へのアクセスはネット接続が必要）。

- 矢印キー・Space：次／前へ。Shift+Space：前へ。
- Home／End：先頭／最後。F：全画面。H：操作バーの表示切り替え。
- ページ番号の入力、スマートフォンの左右スワイプにも対応。
- ブラウザ印刷は1枚＝1ページ。配布用には同梱PDFも使えます。

コピー用ページはクリップボードが使えない環境では文字を選択します。その後Ctrl/Cmd+Cでコピーしてください。

## 編集と再出力

スライド内容は`build.py`、デザインは`styles.css`、操作は`viewer.js`です。`index.html`と`workbook.html`は生成物です。直接編集すると再生成時に上書きされます。

```bash
# このディレクトリで実行
python3 build.py

# PNG・一覧・PDFの出力にのみ必要（閲覧には不要）
npm install --prefix /tmp/lecture-slide-tools playwright sharp
PLAYWRIGHT_BROWSERS_PATH=/tmp/lecture-slide-browsers /tmp/lecture-slide-tools/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/lecture-slide-tools/node_modules PLAYWRIGHT_BROWSERS_PATH=/tmp/lecture-slide-browsers node render.cjs
```

LinuxでChromiumのシステム依存ライブラリが不足する場合は、Playwrightの依存ライブラリも導入してください。

書き出し時に、文字幅・見出しと注記の位置、ページ操作、全画面、画面サイズへの追従、印刷時の全枚表示を確認します。講義本文を変更した場合、コピー用資料は再生成で更新されますが、スライドの要約は`build.py`側も確認してください。

## 素材と出典

- 表紙の写真`assets/architecture-workshop.jpg`は、紙の部品図でアーキテクチャを検討する場面をAIで生成したものです。実際の大学・学生の記録写真ではありません。生成モードとプロンプトは[image-prompt.txt](assets/image-prompt.txt)に記録しています。
- 日本語と図形はHTML/CSS/SVGです。図は講義内容を説明するための構成例で、特定製品の画面や構成を再現したものではありません。
- Noto Sans JP、Archivo Black、YomogiのフォントとOFLライセンスを`assets/fonts/`へ同梱しています。
- 内容の根拠は[講義本文の参考資料](../README.md#参考)を参照してください。
