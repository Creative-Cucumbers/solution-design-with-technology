# 第7回 スターター（Mac / Linux 用）

**このフォルダ（配布ZIPを展開すると `starter-mac` という名前になります）を Antigravity IDE で開いて**ください（**ファイル → フォルダーを開く**）。1つ上のフォルダを開くとコマンドが読み込まれません。内部スクリプトは シェル 版です。

チャットで `/speckit-` と打ってコマンド一覧が出れば準備完了です。

## このスターターの約束

`.specify/memory/constitution.md` に、第7回の制約を書いてあります。AIはこれに従います。

- **受け入れ条件は1〜3項目。** チームが合意した**絞り込みシートが原本**。成果物テンプレート8はその要約。AIは勝手に足さない
- **AC1は端から端まで。** これだけ動けば、その人に価値が届く流れにする。削るのは AC2 以降から。流れを残したままの簡略化（対象を一件に絞る、画面を統合する、外部処理を模擬する）はしてよい
- **75分で動く範囲に収める。** 間に合わなければ機能を足さず、範囲を削る（AC3から落とす）
- **ブラウザだけで動く。** 保存は `localStorage` まで。外部サービス・DBは作らず、模擬したら明記する

## 授業での流れ

1. **絞り込みシートを埋める**（ここが人間の仕事）。要約を成果物テンプレート8に貼る
2. **シート全文**（確認例と制約を含む）を `/speckit-specify` に渡す → **中身をレビューして直す**
3. `/speckit-plan` → `/speckit-tasks` — 計画とタスクに落とす
4. `/speckit-implement AC1だけ…` — **範囲を指定して**実装する。AC1が動いたら確認し、次へ
5. AC1 から順に、人が操作して確認する

作られた `spec.md` / `plan.md` / `tasks.md` は `specs/` の下に残ります。

**提出は、プロジェクト一式をまとめたZIPの共有リンク**です。次を入れてください。

- ソース一式
- `specs/` 配下の `spec.md` / `plan.md` / `tasks.md`
- 起動手順を書いた `README.txt`（どのファイルを開くか、最初に何を入れるか）
- 初期データ

**他の人が開いて同じ手順で動かせる形**にしてください。

> **仕様書の受け入れ条件が4項目以上になっていたら、それは誤りです。** 人間が削ってから次へ進んでください。確認例が複数あることは誤りではありません。

詳細は [第7回の講義資料](https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/7_case_study_solutioning_and_presentation/README.md) と [絞り込みシート](https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/7_case_study_solutioning_and_presentation/handout/scope-and-spec.md) を参照してください。
