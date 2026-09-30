# 演習用スターター（GitHub Spec Kit + Antigravity）

第2回3限目の**演習B**で使うプロジェクトです。仕様駆動開発（Spec-Driven Development）のコマンドが最初から入っています。

**Python や uv のインストールは必要ありません。** フォルダを開くだけで使えます。

## 使い方（3ステップ）

1. 自分のOSのZIPをダウンロードして展開する
   - Windows → **[starter-windows.zip](https://raw.githubusercontent.com/Creative-Cucumbers/solution-design-with-technology/main/2026/2_software_development_methodology_agile/starter-windows.zip)**（約90KB）
   - Mac / Linux → **[starter-mac.zip](https://raw.githubusercontent.com/Creative-Cucumbers/solution-design-with-technology/main/2026/2_software_development_methodology_agile/starter-mac.zip)**（約92KB）
2. 展開してできたフォルダ**そのもの**を **Antigravity IDE で開く**（**ファイル → フォルダーを開く**）
   - Windows の人 → `starter-windows`
   - Mac / Linux の人 → `starter-mac`
3. チャットで `/speckit-` と打ってみる。コマンドの一覧が出れば準備完了

> [!IMPORTANT]
> **開くのは、展開してできたフォルダそのもの**です。その1つ上のフォルダを開くと `/speckit-*` コマンドが読み込まれません（設定は開いたフォルダの直下にある `.agents` フォルダから読まれます）。
> Windows版とMac版の違いは、内部で使うスクリプトが PowerShell 版 / シェル版のどちらかだけです。

## 授業で使うコマンド

| コマンド | 何をするか |
| --- | --- |
| `/speckit-specify` | 仕様書（`spec.md`）を作る |
| `/speckit-plan` | 実装の計画（`plan.md`）を作る |
| `/speckit-tasks` | 作業を分解してタスク一覧（`tasks.md`）を作る |
| `/speckit-implement` | タスクに沿って実装する |

このほかに `/speckit-clarify`（曖昧な点を質問してもらう）、`/speckit-analyze`（仕様・計画・タスクの整合性チェック）、`/speckit-checklist`（品質チェックリスト生成）もあります。授業では使いませんが、興味があれば試してみてください。

## 最初から入っているもの

- `.agents/skills/` — Spec Kit のスキル（`/speckit-*` の中身）
- `.specify/memory/constitution.md` — このプロジェクトの「憲法」。講師が演習向けに書いてあります（ブラウザだけで動く／保存しない／受け入れ条件がすべて など）
- `.specify/templates/` — 仕様書・計画・タスクのテンプレート

`specs/` の下に、実行した段階に応じてファイルが作られます。

- `/speckit-specify`: `spec.md`
- `/speckit-plan`: `plan.md`
- `/speckit-tasks`: `tasks.md`

これらの資料が残ることで、何を作るか、どう進めるかを後から確認できます。

## Antigravity を使うのが初めての人へ

インストールと日本語化は [Antigravity IDE のセットアップ手順](../setup-antigravity-ide.md)（授業の最初に全員で進めます）にあります。バイブコーディング自体が初めての人は [はじめてのバイブコーディング](../vibe-coding-first-steps.md) も見てください。

## うまく動かないとき

| 症状 | 対処 |
| --- | --- |
| `/speckit-` を打ってもコマンドが出ない | ①開いているフォルダが `starter-windows`（または `starter-mac`）**そのもの**か確認する ②ウィンドウを再読み込み、またはアプリを再起動する |
| スクリプトの実行でエラーが出る | 自分のOSに合うZIPか、`.agents` と `.specify` があるフォルダを開いているかを確認する。それでも失敗する場合は、エラー画面を講師に見せる |
| Antigravity IDE が入らなかった | ペアの相手の画面を一緒に見て進める。講師に声をかけてください |

## バージョン

- GitHub Spec Kit: **v1.0.12**（`--integration agy` / スキル方式）
- 動作確認: Antigravity IDE Standalone（2026年9月時点のパブリックプレビュー）

Spec Kit は更新が速いため、最新版ではコマンド名や配置が変わっている可能性があります。
