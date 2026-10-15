# 第4回スライド：86枚

16:9（1600×900のレイアウト、PNGは1920×1080）。第2回の紙面、黒・黄色、淡色の紙片、太い日本語見出し、手書き注記を引き継いだ編集可能なHTMLスライドです。

- [スライドを表示](https://creative-cucumbers.github.io/solution-design-with-technology/2026/4_solutioning_and_prototyping/slides/index.html)
- [レビュー用一覧](https://creative-cucumbers.github.io/solution-design-with-technology/2026/4_solutioning_and_prototyping/slides/review.html)
- [一覧画像](https://creative-cucumbers.github.io/solution-design-with-technology/2026/4_solutioning_and_prototyping/slides/previews/overview.png)
- PDF（86ページ）は下記の再出力手順で生成できます。容量が大きいため、Git管理・GitHub Pagesでの配布対象には含めていません。
- [資料・コピー用プロンプト](https://creative-cucumbers.github.io/solution-design-with-technology/2026/4_solutioning_and_prototyping/slides/workbook.html)
- [スライドと本文の対応表](slide-map.md)

## 構成

| 枚 | 内容 |
| --- | --- |
| 01–16 | 導入、7回の授業マップ、準備、開発の往復、機能・品質・制約、D-1 |
| 17–31 | 設計とアーキテクチャ、部品・保存・同期／非同期、約束、投稿の流れ |
| 32–45 | AIと設計する、D-2の日付検索、D-3の個人アプリ・図・確認、3限まとめ |
| 46–55 | 講師の説明例：共同プリンターの受付・状態、通信断と集中、2案の比較・作図 |
| 56–70 | F-1から学生のお題：焼きそば注文サービス。個人の比較・作図・選択、チームの共有・合意 |
| 71–77 | 焼きそばの構成を紙で検証、修正・再確認、他チームレビュー |
| 78–81 | F-6の機材貸出サービス・チーム自主演習・成果、個人の3問 |
| 82–86 | チーム開発の工夫、提出物、事後学習、次回予告、参考資料 |

AIへの長い指示は、スライド右下の「資料・プロンプト」から対応する節・手順を開き、コピーできます。全文は講義READMEから生成しています。構成図はオフラインでも表示できるSVGです。スライドの短い指示は投影用の要約です。

86枚は手順の掲示と講師の具体例を含みます。3限・4限それぞれ100分で使います。D-3は個人18分＋まとめ2分、F-6はチーム20分を確保し、前半の説明・演習時間を調整しています。細かな説明図は補助資料として参照し、演習中は手順のページを掲示します。3枚目では第2回と同じ7回のマップ上で、第4回を黄色で強調しています。

D-3は「やることリスト」のアプリを作り、実際の構成をdraw.ioで説明する演習です。F-6は「学内機材の貸出・返却」を、プロンプト例・構成例なしでチームが設計・検証する演習です。AIとdraw.ioは利用できますが、F-6の問いと指示は学生が考えます。

4限の説明用は共同プリンター、F-1〜F-5の演習用は焼きそば注文サービスです。説明例の構成をそのまま写さず、処理する人・保存する情報・状態を変える人を考え直します。プリンターの比較図は画面への状態通知に範囲を揃え、印刷の依頼を渡すキューとは役割を区別しています。

## 閲覧と操作

`index.html`をブラウザで開きます。閲覧にインストールは不要です。フォントと画像はローカルに同梱しています（外部資料へのアクセスはネット接続が必要）。

- 矢印キー・Space：次／前へ。Shift+Space：前へ。
- Home／End：先頭／最後。F：全画面。H：操作バーの表示切り替え。
- ページ番号の入力、スマートフォンの左右スワイプにも対応。
- ブラウザ印刷は1枚＝1ページ。配布用PDFは再出力手順で生成できます。

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
