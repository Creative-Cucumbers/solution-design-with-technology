# 第6回の講義スライド（30枚）

第4回の紙面・黒と黄色・淡色の紙片・手書き注記を継承した、編集可能な16:9のHTMLスライドです。レイアウトは1600×900、PNGは1920×1080です。

- [講義スライド](https://creative-cucumbers.github.io/solution-design-with-technology/2026/6_case_study_design_and_exercise/slides/index.html)
- [レビュー用一覧](https://creative-cucumbers.github.io/solution-design-with-technology/2026/6_case_study_design_and_exercise/slides/review.html)
- [資料・コピー用プロンプト](https://creative-cucumbers.github.io/solution-design-with-technology/2026/6_case_study_design_and_exercise/slides/workbook.html)
- [スライドと本文の対応表](slide-map.md)
- [一覧画像](previews/overview.png)

上記の公開URLは、変更をGitHubへ反映してPagesの公開処理が完了すると閲覧できます。手元ではindex.htmlまたはreview.htmlをブラウザで開いてください。

## 進行

| 枚 | 内容 |
| --- | --- |
| 1〜7 | 導入・授業マップ・目標・チーム編成・テーマ選択 |
| 8〜15 | 調査・事実と仮説・ペルソナ・課題設定・チェックイン |
| 16〜22 | 案出し・比較と選択・価値の概算・ラフ作成 |
| 23〜30 | 中間発表・問い・提出・個人振り返り・次回への接続 |

3限・4限各100分（各予備10分を含む）。説明時間はREADMEの各節の時間内に含め、演習中は該当する手順のページを掲示します。長い例とプロンプトは投影せず、右下の資料リンクから参照・コピーできます。記入先の番号は、講義スライド番号ではなく「成果物テンプレート」の番号です。

ホテルの田中さんは説明用の仮想人物です。年齢・客室数・仕事の状況を確認済みの事実として扱いません。公開資料の読解で確認した記述だけを出典付きFACTとして記入します。

## 操作

矢印キー・Spaceで次へ、Shift+Spaceで前へ。Home／Endで先頭／最後へ。Fで全画面、Hで操作バーの切り替え。番号入力・URLの`#番号`・スマートフォンのスワイプにも対応します。

資料のコピーが許可されない環境では本文が選択されるので、Ctrl/Cmd+Cでコピーしてください。スライドのフォント・図はローカルで表示できます。外部資料はネット接続が必要です。

## 編集と再生成

スライド本文はbuild.py、デザインはstyles.css、操作はviewer.jsです。資料ページは講義READMEから生成します。index.html、workbook.htmlを直接編集すると再生成で上書きされます。

```bash
# このディレクトリで実行
python3 build.py

# PNG・レビュー一覧・ローカルPDFの生成
npm install --prefix /tmp/lecture-slide-tools playwright sharp
PLAYWRIGHT_BROWSERS_PATH=/tmp/lecture-slide-browsers /tmp/lecture-slide-tools/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/lecture-slide-tools/node_modules PLAYWRIGHT_BROWSERS_PATH=/tmp/lecture-slide-browsers node render.cjs
```

PDFはサイズが大きいためGit管理・Pages公開の対象外です。render.cjsは全ページの描画と文字幅、見出し・注記の位置、キー操作・全画面・画面サイズ追従・印刷を検証します。

## 素材

表紙のリサーチボードはHTML/CSSとSVGの線画で制作しています。写真・画像生成は使用していません。Noto Sans JP、Archivo Black、YomogiとOFLライセンスをassets/fontsへ同梱しています。
