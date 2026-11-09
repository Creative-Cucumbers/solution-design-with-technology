# 第7回の講義スライド（36枚）

第6回と同じ16:9の編集可能なHTMLスライドです。白い紙面、黒・黄色、淡色の紙片、手書き注記を継承しています。

- [スライド](index.html)
- [資料・コピー用プロンプト](workbook.html)
- [本文との対応表](slide-map.md)

index.htmlをブラウザで開いてください。矢印・Spaceで移動、Home／Endで先頭／最後、Fで全画面、Hで操作バーを切り替えます。URLの`#番号`でもページを指定できます。

スライドは投影用の要点です。詳しい手順・プロンプト全文は右下の資料リンクから参照します。3限100分・4限100分の演習時間内で説明し、演習中は対応ページを掲示してください。

## 編集

本文はbuild.py、デザインはstyles.css、操作はviewer.jsです。workbook.htmlは講義READMEから生成します。

```bash
python3 build.py
```

index.htmlとworkbook.htmlの直接編集は再生成で上書きされます。レビュー用画像・PDF・画像一覧は生成していません。ブラウザからの印刷は可能です。

## 素材

図形はHTML/CSSです。Noto Sans JP・Archivo Black・YomogiおよびOFLライセンスをassets/fontsに同梱しています。
