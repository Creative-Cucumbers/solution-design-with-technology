# 講師向けメモ: 第2回 ソフトウェア開発方法論とアジャイルワークショップ

> [!WARNING]
> このファイルは進行用です。**受け入れ条件が書かれているので、授業前に学生には見せないでください。**
> 学生向けの資料は [README.md](./README.md) です。

---

## 受け入れ条件（学生には事前に見せない）

演習Aの後（3節）に、お客さん役として読み上げる。

1. **3チーム分の時間を同時に計れる**
2. **残り3分で表示の色が変わる**
3. **一時停止と再開ができる**
4. **時間を超えたらマイナスで表示され続ける**
5. **リセットは確認してから実行される**

演習B（7節）では、上の5つに次の1つを追加する。

6. **時間が終わったら音で知らせる**

読み上げるときに必ず言うこと:

- 「落ちるように作ってあります。腕の問題ではありません」
- 「この5つは最初から私の頭の中にありました。一言も伝えていません」

## この回の設計（失敗と成功を2周する）

**各コマ100分。** 3限目は 20（セットアップ込み）+10+4+5+6+6+14+4+12+7+10+2 = 100分、4限目は 7+18+10+12+18+10+18+7 = 100分。
90分で回す年度に当たった場合は「時間が押したときの削り方」を上から適用すれば収まる。


| | 第1周: 個人 | 第2周: チーム |
| --- | --- | --- |
| ① 体験（失敗） | 演習A → 受け入れ確認 その1 で落ちる | 演習C → 4機能が1つにならない |
| ② 気づき | 4節（板書1枚目） | 10節（板書2枚目） |
| ③ 教える | 5節（方法論とは）→ 6節（仕様駆動） | 11節（チームで効く方法論） |
| ④ 体験（成功） | 演習B → 受け入れ確認 その2 で通る | 4限: 振り返り → ラウンド2で記録が伸びる |

- **板書は消さない**。4節の1枚目を5.2と6節で、10節の2枚目を11節で名指しで回収する
- **失敗は仕掛けであることを毎回明言する**。個人やチームを責める空気を作らない
- 演習C中は教えない。机を回って**観察メモ**を取る（誰も手を動かしていない時間／同時に別々に作り始めた／どちらのベースを使うか決まらない／統合できず止まった／決める人がいない／手が空く人が出た／全体像を持つ人がいない／時間配分を誰も見ていない）。10節で講師が代弁する

## 未経験者への対応（受講者の約2割）

バイブコーディング未経験者が2〜3名いる前提で進める。

- **ペアは講師が指定する**。経験者と未経験者を組ませ、未経験者だけのペアを作らない（13名なら経験者10名・未経験者3名 → 未経験者は必ず経験者と組む）
- 経験者には「**操作を代わりにやらない。相手に操作させて口で教える**」と最初に伝える。演習Aは速さを競うものではないので、ここで時間を使って構わない
- 演習Aの冒頭で [vibe-coding-first-steps.md](./vibe-coding-first-steps.md)（初めての人向けの手引き）のURLを板書する。手引きの練習題材は**電卓アプリ**（条件3つ付きのプロンプト）で、演習Aのタイマーとは別物。授業中に開いた学生には「3はとばして4・5の頼み方だけ真似する」と伝える。セットアップ自体は [setup-antigravity-ide.md](./setup-antigravity-ide.md) を全員で進めるので、未経験者もそこで操作に一度触れている
- 演習A（2節）の冒頭で「初めての人は手引きを開いていい」と口頭でも言う。**手引きを開いても演習の趣旨は壊れない**（隠しているのは受け入れ条件であって、操作方法ではない）
- 未経験者が手順でつまずいて8分の制作時間を使い切っても構わない。**受け入れ確認その1で落ちるのは全員同じ**なので、考察1には問題なく参加できる

## 前週のSlack告知文テンプレ（持ち物のお願いだけ）

インストールは**授業の最初に全員で行う**（受講者のPCスキルを考えると事前課題は成立しない前提）。前週に送るのは持ち物の連絡だけにする。

```
【第2回（10/XX）の持ち物のお願い】

次回は、Googleの開発環境「Antigravity IDE」を使います。
インストールは授業の最初に一緒にやるので、事前準備は要りません。
以下だけお願いします。

1. ノートPCと「電源アダプタ」を持ってくる
   （ダウンロードとAI利用でバッテリーを使います）
2. 「個人の」Googleアカウントでログインできるか確認しておく
   ※大学のアカウントでは使えない可能性があります
   ※パスワードを忘れている人は、これだけは事前に確認をお願いします
3. PCの空き容量を2GB以上空けておく

手順書はこちらです（当日一緒に進めます。予習は不要です）
<setup-antigravity-ide.md のURL>

不安な人はこのチャンネルで声をかけてください。
```

## 配布物の渡し方（当日）

URLが長いので、**学生に手打ちさせない**。下の3経路を用意しておき、Slackを本線・QRを予備・USBを最終手段とする。

| 経路 | 使う場面 | 準備 |
| --- | --- | --- |
| **① Slackに投稿**（本線） | 通常 | 授業開始時に下のテンプレを授業チャンネルに投稿し、**ピン留め**する |
| **② QRコード＋短縮URL**（予備） | PCでSlackを開けない学生がいる／スライド投影中 | 各URLのQRを作ってスライドに貼る。短縮URLも併記して板書 |
| **③ USBメモリ**（最終手段） | 教室の回線が詰まった・切れた | 2〜3本用意。中身は下記 |

**USBメモリの中身**（回線が死んでも授業が成立する構成にしておく）

```
USB/
├── Antigravity/
│   ├── AntigravityIDE-windows-x64.exe      ← 事前にダウンロードしておく
│   └── AntigravityIDE-macOS-AppleSilicon.dmg
├── starter-windows.zip
├── starter-mac.zip
└── 手順書.pdf                               ← setup-antigravity-ide.md を印刷/PDF化したもの
```

> ログインには回線が必要なので、回線が完全に死んだ場合は演習A・Bを次回に振り、4限のマシュマロチャレンジを先に実施する（4限はネット不要）。

### 当日Slackに投稿する文面（そのまま貼れる）

```
【第2回 今日使うリンク】※上から順に使います

■ セットアップ手順書（まずこれを開いてください）
https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/2_software_development_methodology_agile/setup-antigravity-ide.md

■ Antigravity IDE のダウンロード（「Antigravity IDE Standalone」を選ぶ）
https://antigravity.google/download#antigravity-ide

■ 演習Bで使うファイル（あとで使います。自分のOSのものだけ）
・Windows: https://raw.githubusercontent.com/Creative-Cucumbers/solution-design-with-technology/main/2026/2_software_development_methodology_agile/starter-windows.zip
・Mac:     https://raw.githubusercontent.com/Creative-Cucumbers/solution-design-with-technology/main/2026/2_software_development_methodology_agile/starter-mac.zip

■ バイブコーディングが初めての人向けの手引き
https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/2_software_development_methodology_agile/vibe-coding-first-steps.md

■ 今日の授業資料（全体）
https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/2_software_development_methodology_agile/README.md

つまずいたらこのスレッドに書いてください。すぐ行きます。
```

### 提出物の集め方

- 演習Bの `spec.md` は、**Slackのこのスレッドにファイル添付または本文貼り付け**で提出させる（`specs/` フォルダの中にある）
- 4限の振り返り（名前・チーム名／感想／学び／改善点）も同じスレッドに投稿させる
- 期限は次回授業の前日まで。授業内で全員に口頭で伝える

## セットアップ（1節・20分）の進め方

**時間内に全員が終わらない前提で設計する。** 演習は2人1組なので、ペアで1台動けば成立する。

進行:

1. 開始直後に「手順書の1〜2だけ進めて、ダウンロードを始めてください」と指示する（3分）
2. **ダウンロードの待ち時間に 1.2〜1.4（全体像・前回の振り返り・今日のゴール）を話す**（8分）
3. 終わった人から手順書の3以降（インストール→ログイン→日本語化→フォルダ作成）に進ませる（9分）
4. 終わった人に、詰まっている人を手伝わせる

準備しておくこと:

- [ ] **インストーラを入れたUSBメモリを2〜3本**用意する（13台が同時にダウンロードすると教室の回線が詰まる）。Windows x64 / macOS Apple Silicon の2種があれば大半をカバーできる
- [ ] **配布ZIPのURLを短縮URLかQRコードにして板書できるようにする**（手打ちさせない）
  - Windows: `https://raw.githubusercontent.com/Creative-Cucumbers/solution-design-with-technology/main/2026/2_software_development_methodology_agile/starter-windows.zip`
  - Mac / Linux: `https://raw.githubusercontent.com/Creative-Cucumbers/solution-design-with-technology/main/2026/2_software_development_methodology_agile/starter-mac.zip`
  - **push 後に有効になる**。授業前に自分のブラウザで両方クリックして確認する
- [ ] 講師のPCで、手順書どおりの画面が出るか事前に確認する（**バージョンで画面が変わる**ため）

注意点:

- ダウンロードページには4つの形態（2.0 / IDE / CLI / SDK）が並び、**一番上の「Antigravity 2.0」を押してしまう学生が必ず出る**。板書するURLは**アンカー付きの `https://antigravity.google/download#antigravity-ide`**（IDEの箇所に直接飛ぶ）にして、あわせて「IDE Standalone を選ぶ」と書いておく
  - 学生に配るURLに `?_gl=...` や `_ga=...` が付いていたら**必ず削る**。あれは配った人のGoogle Analytics識別子で、公開資料に載せるものではない
- **日本語化は必須にしない**。詰まったら英語のまま進めてよいと伝える（手順書に必要な操作は全部書いてある）
- 大学PC・管理者権限でインストールできない学生が出たら、その場でペアの相手の端末に寄せる
- IDEを選んでいる理由は「**エージェントが開いているフォルダの中で作業するので、ファイルがどこにできたか画面で見える**」こと。2.0（エージェント中心のデスクトップアプリ）だとファイルの所在が分かりにくい

## 事前確認チェックリスト（講師）## 事前確認チェックリスト（講師）

- [ ] 大学PCで**インストール権限**があるか。大学のポリシー上、個人Googleアカウントの利用が問題ないか
- [ ] **Antigravity IDE Standalone**（ダウンロードページの別項目。2026年9月時点で v2.5.5）を実機に入れ、手順書の画面説明と一致するか確認する
- [ ] 日本語化（拡張機能「Japanese Language Pack for Visual Studio Code」／`Configure Display Language`）が Antigravity IDE で機能するか確認する。機能しない場合は手順書の5節を「英語のまま進める」に書き換える
- [ ] **Windows機（Python未インストール）** で `starter-windows.zip` を展開し、**展開したフォルダを開いて** `/speckit-` でコマンドが出ることを確認したうえで、`/speckit-specify` → `/speckit-plan` → `/speckit-tasks` → `/speckit-implement` が通るか
  - 内部スクリプトは PowerShell 版（`.specify/scripts/powershell/`）。Windows PowerShell 5.1 で動くか確認し、`pwsh`（PowerShell 7）が必要なら事前課題に追記する
- [ ] **仕掛けのドライラン**: 一言プロンプトで作り、受け入れ条件5つのうちいくつ通るか実測する
  - **3つ以上通ってしまう場合は条件を差し替える**（より暗黙度の高い条件にする）
- [ ] 演習Bを通しで実測し、14分に収まるか確認する（`/speckit-implement` の待ち時間を含む）
- [ ] 演習Cのドライラン: 別々に作った2つを持ち寄って4機能を11分でまとめようとして、**実際に詰まる**か確認する（詰まらない場合は機能を5つに増やす）
- [ ] 事前課題の実施状況をSlackで確認し、入れられなかった学生をフォールバック側（AI Studio / Gemini Canvas）に割り振る
- [ ] マシュマロチャレンジの材料を購入する（下記）
- [ ] [setup-antigravity-ide.md](./setup-antigravity-ide.md) と [vibe-coding-first-steps.md](./vibe-coding-first-steps.md) の画面説明を実機と突き合わせる（バージョンで画面が変わるため断定を避けた書き方にしてある。**スクリーンショットを追加すると学生の詰まりが大幅に減る**）

## 時間が押したときの削り方

押したときは、上から順に削る。

0. **セットアップ（1節）が押した場合**: 日本語化を後回しにして英語のまま進める。それでも足りなければ、入っていない学生をペアの相手に寄せて演習Aを始める（セットアップの続きは演習Aの裏で各自やらせる）

1. 11.6の挙手クイズ（2分）→ 事後学習に回す
2. 11.3 リーンと 11.4 DevOps → 11.5の比較表を見せるだけにする（各1分に圧縮）
3. 演習Bの受け入れ条件を6つ→4つに減らす。`/speckit-plan` と `/speckit-tasks` の確認は口頭で流す
4. 演習Cの機能を4つ→3つに減らす（振り返りメモを削る）
5. 4限目は合計100分ぴったりなので、押したら#19の解説を12分に圧縮する（19.3と19.4を口頭だけにする）

**削ってはいけないもの**: 受け入れ確認 その1・その2 と10節冒頭のチーム確認（失敗と成功の対比が消える）、4節と10節の考察（学生が自分で気づく時間）、16節の振り返り（ラウンド2の改善計画）

## 準備物チェックリスト（マシュマロチャレンジ / 3チーム×2ラウンド）

| もの | 1チーム×1ラウンド | 3チーム×2ラウンド | 予備込みの購入目安 |
| --- | --- | --- | --- |
| 乾燥パスタ（1.7mm） | 20本 | 120本 | 500g×1袋（約230本） |
| マスキングテープ | 90cm | 540cm | 1巻（18m）×1 |
| ひも（たこ糸など） | 90cm | 540cm | 1巻×1 |
| マシュマロ | 1つ | 6つ | 1袋（潰れる前提で多め） |
| はさみ | 1つ | 3つ（使い回し） | 3 |

そのほか:

- [ ] 計測用のメジャー（1つ）
- [ ] 記録用のホワイトボード（#1と#2の記録を並べて残す）
- [ ] 振り返り用の紙またはふせん（チーム分）
- [ ] 机または床の養生（テープを貼る面を確認しておく）

## 使用ツールのメモ

- **Antigravity IDE**: [antigravity.google/download#antigravity-ide](https://antigravity.google/download#antigravity-ide)（アンカー付きで該当箇所に直接飛ぶ）の「**Antigravity IDE Standalone**」（2026年9月時点で v2.5.5）。Windows は `.exe`、Mac は `.dmg`、Linux は `.tar.gz`。要件は macOS 12 (Monterey) 以降 / Windows 10 64-bit 以降
  - Antigravityには4つの形態がある: **2.0**（エージェント中心のデスクトップアプリ・v2.17.0）／**IDE**（エージェントがワークスペース内で作業し、変更を1行ずつ承認できる）／**CLI**／**SDK**。今回は**ファイルの所在が画面で見える**ことを重視してIDEを選んでいる
  - パブリックプレビューで無料、Gemini 3 Pro / Deep Think が使える。**個人アカウント向け**（組織アカウントはCLI版が2026年8月から対応）。レート制限あり。バージョンで画面が変わるため当日までに再確認する
- **GitHub Spec Kit**: `starter/` は **v1.0.12** を `--integration agy`（スキル方式・`.agents/skills/`）で初期化済み。学生側に Python / uv / git は不要
  - 学生には **OS別ZIP**（`starter-windows.zip` / `starter-mac.zip`・各約90KB）を配る。リポジトリ全体を落とさせないため、また**展開したフォルダがそのままワークスペースルートになる**ようにするため
  - **スキルの探索場所**: Antigravity は `<ワークスペースルート>/.agents/skills/<スキル名>/SKILL.md` を読む（IDE・2.0・CLI共通）。したがって学生が開くフォルダは、展開してできた `starter-windows` / `starter-mac` **そのもの**でなければならない。`第2回` を開くと `/speckit-*` は出ない
    - どうしても認識されない場合の代替: スキルをユーザー全体の場所 `~/.gemini/config/skills/`（3形態すべてが認識する場所）にコピーする。ドライランで試しておく
    - 追加直後に出ない場合は**ウィンドウの再読み込み／アプリ再起動**で読み込まれる
  - **`starter/` を直したら ZIP を作り直すこと**（内容が食い違う）。作り直しコマンド:
    ```bash
    cd 2026/2_software_development_methodology_agile
    rm -rf /tmp/zs && mkdir -p /tmp/zs
    cp -a starter/windows /tmp/zs/starter-windows && cp -a starter/mac /tmp/zs/starter-mac
    rm -f starter-windows.zip starter-mac.zip
    (cd /tmp/zs && zip -rq starter-windows.zip starter-windows && zip -rq starter-mac.zip starter-mac)
    cp /tmp/zs/starter-windows.zip /tmp/zs/starter-mac.zip .
    ```
- **フォールバック**: ①Spec Kitのスキルが動かない → 手書きの仕様書Markdown＋Antigravity内蔵の `/plan`（計画とタスクを出して承認待ちで止まるので、学びは維持できる） ②Antigravityが入らない → [Google AI Studio](https://aistudio.google.com/) の Build モード、または Gemini の Canvas

---
