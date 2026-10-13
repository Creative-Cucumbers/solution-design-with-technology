"""Build editable lecture slides and the prompt workbook; no third-party packages."""
from pathlib import Path
def esc(s,quote=True):
    s=s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return s.replace(chr(34),"&quot;").replace(chr(39),"&#x27;") if quote else s
import re
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'README.md'
slides=[]
def add(title,content='',kind='',section=1,note='',eyebrow='DESIGN / MAKE / LEARN'):
    slides.append(dict(title=title,content=content,kind=kind,section=section,note=note,eyebrow=eyebrow))
def table(headers,rows,compact=False):
    return '<table class="s4-table'+(' compact' if compact else '')+'"><thead><tr>'+''.join('<th>'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def split(a,al,b,bl,colors=('blue','pink')):
    return '<div class="s4-split">'+''.join(f'<article class="paper {c}"><h2>{h}</h2><ul>'+''.join('<li>'+v+'</li>' for v in vals)+'</ul></article>' for h,vals,c in [(a,al,colors[0]),(b,bl,colors[1])])+'</div>'
def cards(items):
    return '<div class="s4-row">'+''.join(f'<article class="paper {c}"><span class="n">0{i+1}</span><h2>{h}</h2><p>{t}</p></article>' for i,(h,t,c) in enumerate(items))+'</div>'
def quote(q,side): return f'<div class="s4-quote"><blockquote>{q}</blockquote><aside>{side}</aside></div>'
def exercise(minutes,steps,output):
    return f'<div class="s4-exercise"><div class="s4-clock"><b>{minutes}</b><span>MINUTES<br>まず、手を動かそう。</span></div><div><ol class="s4-steps">'+''.join(f'<li><strong>{h}</strong><small>{t}</small></li>' for h,t in steps)+f'</ol><div class="s4-output">残すもの → {output}</div></div></div>'
def prompt(txt,section,aside):
    return '<div class="s4-prompt"><pre>'+esc(txt)+'</pre><aside>'+aside+f'<a href="workbook.html#section-{section}" target="_blank" rel="noopener">全文を開いてコピー ↗</a></aside></div>'
def sheet(rows,note):
    return '<div class="s4-sheet">'+''.join(f'<div><span>{a}</span><em>{b}</em></div>' for a,b in rows)+f'</div><aside class="s4-sheet-note">{note}</aside>'
def timeline(items):
    return '<div class="s4-timeline">'+''.join(('<span class="arrow">→</span>' if i else '')+f'<div class="stage"><b>{a}</b><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(items))+'</div>'
def diagram(nodes,edges):
    # Fixed diagram canvas. Edge labels use a paper-colored halo for legibility.
    out=['<svg class="s4-diagram" viewBox="0 0 1440 495" role="img" aria-label="部品と情報の流れ"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#151515"/></marker></defs>']
    for x1,y1,x2,y2,label,lx,ly in edges:
        out.append(f'<path class="edge" d="M{x1} {y1}L{x2} {y2}" marker-end="url(#arrow)"/>')
        if label: out.append(f'<text class="edge-label" x="{lx}" y="{ly}" text-anchor="middle">{esc(label)}</text>')
    for x,y,w,h,title,sub,color in nodes:
        out.append(f'<rect class="node" x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/><text class="node-title" x="{x+w/2}" y="{y+42}" text-anchor="middle">{esc(title)}</text><text class="node-sub" x="{x+w/2}" y="{y+79}" text-anchor="middle">{esc(sub)}</text>')
    return ''.join(out)+'</svg>'
Y='#fff34d'; B='#dceaf0'; P='#f5d9df'; G='#dcecd9'; W='#ffffff'
# Introduction and the individual design cycle.
add('つなぎ方を、<br><mark>デザインする。</mark>', '<div class="cover-black"></div><img class="cover-photo" src="assets/architecture-workshop.jpg" alt="紙の部品図と矢印でソフトウェアの構成を考えるイメージ"><div class="cover-sub">ソリューショニングとプロトタイピング<br><span style="font-size:25px;font-weight:500">第4回 ／ 3限・4限<br>部品を選ぶ。理由を話す。つないで確かめる。</span></div><div class="note yellow cover-note">その構成は、<br>誰の、何のため？</div>', 'cover',1,eyebrow='LECTURE 04 — SOLUTIONING & PROTOTYPING')
add('今日は、<mark>判断を説明できる人へ。</mark>',split('3限：ひとりで理解する',['部品と流れを図にする','変更する場所を予測する','選んだ理由を言える'],'4限：チームで決める',['AIと複数の案を比べる','図と理由を持ち寄る','合意した案を確かめる']),section=1,note='第2回「進め方」→ 第3回「誰のため」→ 第4回「どうつなぐ」')
add('今日の<mark>作業場所をつくる。</mark>',split('第4回のフォルダ',['新しくZIPをダウンロード・展開','starter-windows / starter-mac を開く','第2回の作業済みフォルダは使い回さない'],'準備チェック',['Antigravity IDEでフォルダを開いた','/speckit- の候補が出た','困ったらペアの画面で参加する']),section=1,note='ZIPのリンク・OS別の操作は、右下の資料リンクから。')
add('図は、<mark>四角と矢印でいい。</mark>',exercise('3',[('Draw.io Integrationを入れる','作者：Henning Dieterichs'),('test.drawio.svg を作る','四角を置き、矢印を引き、保存する'),('開けなければブラウザ版へ','app.diagrams.net ／ 紙に描いても参加できる')],'編集できる図のファイル'),section=1,note='準備14分の中で確認。きれいに描くことが目的ではありません。')
add('設計は、<mark>行き来する。</mark>',timeline([('WHAT','要件','何を満たす？'),('HOW','設計','どう実現する？'),('MAKE','実装','小さく作る'),('CHECK','検証','確かめて戻る')]),section=2,note='試して分かったことは、要件や設計へ戻す。')
add('願いを、<mark>確かめられる条件へ。</mark>',table(['段階','落とし物掲示板の例'],[['願い','落とした傘を、早く見つけたい'],['必要なこと','場所で絞って探したい'],['作る約束','図書館を選ぶと、図書館の投稿だけを表示する'],['確かめる例','図書館2件＋食堂1件 → 図書館の2件が出る']]),section=3,note='この授業での整理です。言葉の分類より、どう確かめるか。')
add('できることと、<mark>使える品質。</mark>',split('機能：何ができる？',['投稿できる','一覧を見られる','選んだ投稿だけ削除できる'],'品質：どんな条件で？',['指定のスマホ幅で操作できる','指定の件数・環境で3秒以内','対象・条件・測り方まで決める']),section=3,note='問い：検索結果が0件なら、何を見せる？')
add('お題：<mark>学内の落とし物掲示板。</mark>',cards([('投稿する','品名・拾った場所・<br>拾った日を入力する。','blue'),('一覧を見る','登録した落とし物が<br>全部見える。','yellow'),('一件を消す','同じ品名の別の投稿は<br>そのまま残る。','pink')]),section=4,note='AC1・AC2・AC3 ／ ブラウザ内だけ。リロードで消えてよい。')
add('比べるときは、<mark>同じ3件。</mark>',table(['品名','拾った場所','拾った日'],[['傘','図書館','2026-10-10'],['傘','食堂','2026-10-11'],['ノート','図書館','2026-10-12']]),section=4,note='変更前後で登録し直す。同じ名前でも、別の落とし物。')
add('D-1｜まず作って、<mark>確かめる。</mark>',exercise('8',[('specify → plan','本文のプロンプトをコピー。計画の詳しいレビューは後へ。'),('tasks → implement','生成したアプリをブラウザで開く。'),('3件を入れ、AC1〜AC3を確認','未完了なら記録して、講師の基準版へ。')],'使った版と、できた／未完了の記録'),section=4,note='AIの設計は存在する。人がまだ理解・確認していない状態を観察する。')
add('「場所で<mark>絞り込みたい」。</mark>',quote('どの部品を、<br>直せばいい？','まず2分、AIに変更を頼まず予測。<br><br>変更する部品は？<br>データは変わる？<br>何を検査する？'),section=5,note='5節：予測2分 → 変更・確認4分。分からなければ「不明」と書く。')
add('変更したら、<mark>元の動きも確かめる。</mark>',table(['操作','期待する結果'],[['場所なし','3件が出る'],['図書館','傘とノートの2件'],['該当なし','0件だと分かる'],['投稿・一覧・削除','元のAC1〜AC3が通る']]),section=5,note='今回、リロードでデータが消えるのは仕様どおり。設計の失敗とは判定しない。')
add('予測と実際を、<mark>分けて残す。</mark>',sheet([('使ったもの','自分の生成物 ／ 講師の基準版'),('予測した場所','どこを直すと思った？'),('実際の変更','何が変わった？'),('確認結果・疑問','観察した事実と、原因の推測を分ける')],'3分で投稿<br>3分で共有<br><br>Slackへ。'),section=6,note='動いた人も、止まった人も。何が理解の手がかりになった？')
add('全体の構造を、<br><mark>理由と一緒に考える。</mark>','<div class="chapter-n">01</div><p class="chapter-copy">設計：誰が何をして、どうつながるか。<br>アーキテクチャ：全体の構造と重要な品質の判断。</p><div class="chapter-note">最初に全部を<br>決め切らなくていい。</div>','chapter',7,eyebrow='ARCHITECTURE / WHY THIS STRUCTURE?')
add('コンポーネントは、<mark>役割を持つ部品。</mark>',table(['役割の分類','やさしく言うと','例'],[['UI','見たり操作したりする','投稿フォーム・一覧'],['コンピュート','調べる・計算する・加工する','入力確認・写真加工'],['ストレージ・データ管理','置いて、取り出す','DB・写真の保存先'],['通信・メッセージング','つなぎ、情報や依頼を届ける','通信の窓口・キュー']]),section=7,note='役割を理解する分類。一つの製品が複数の役割を持つこともある。')
add('今回は、<mark>情報の置き場所を詳しく。</mark>',quote('何を、<br>いつまで残す？','処理中だけ？<br>翌日も必要？<br>一覧の情報？<br>写真そのもの？'),section=7,note='全体像のうち、ストレージ・データ管理へ。')
add('メモリとDBは、<mark>二択ではない。</mark>',split('メモリ：作業机',['素早く読み書きする場所','一般的なRAMは揮発性','ページ内の変数はリロードで失われる'],'DB：整理する仕組み',['情報を検索・更新・管理する','SSD等への永続化で再起動後に復元','DBも内部でメモリを使う']),section=7,note='速さは処理・通信・データ量にもよる。永続化してもバックアップ等は必要。')
add('写真はどこへ？ <mark>控えはいつまで？</mark>',split('ファイル／オブジェクト保存',['写真本体などを置く','DBに写真の保存先を持たせる案も','閲覧権限・削除の連動を考える'],'キャッシュ：一時的な控え',['よく使う結果を再利用する','古い情報が残ることがある','更新・期限・破棄を決める'],('blue','green')),section=7,note='RAMは媒体、DBは管理の仕組み、キャッシュは使い方。')
add('「受付」と「完了」を、<mark>分けられる。</mark>',split('同期：結果を待つ',['保存結果を待って「登録しました」','流れを追いやすい','重い処理では待ち時間を考える'],'非同期：後で完了する',['まず「受付・処理中」を返す','完了や失敗を後から伝える','状態の管理・再試行が必要']),section=7,note='非同期にしても、仕事そのものが速くなるとは限らない。')
add('依頼を渡す部品と、<mark>実行する部品。</mark>',diagram([(0,155,310,120,'アプリケーション','加工を依頼する',B),(560,155,310,120,'メッセージキュー','依頼を受け渡す',Y),(1120,155,310,120,'ワーカー','写真を加工する',P)],[(310,215,560,215,'依頼を入れる',435,187),(870,215,1120,215,'依頼を受け取る',995,187)]),section=7,note='キュー自身は写真を加工しない。ワーカーが計算し、結果を保存する。')
add('部品を組み合わせると、<mark>流れになる。</mark>',diagram([(0,160,250,120,'ブラウザ','受付と状態を見る',W),(380,160,280,120,'アプリ／API','保存・受付を担当',B),(820,0,260,110,'DB','投稿・状態を残す',G),(820,345,260,110,'画像ストレージ','写真を残す',G),(820,168,250,110,'キュー','加工の依頼',Y),(1160,168,270,110,'ワーカー','写真を加工',P)],[(250,210,380,210,'投稿',310,182),(660,180,820,65,'保存',716,99),(660,255,820,400,'写真',715,360),(660,222,820,222,'依頼',735,196),(1070,222,1160,222,'',1110,192),(1280,168,1080,65,'完了状態',1250,65),(1280,278,1080,400,'加工結果',1260,397)]),section=7,note='構成例。通知失敗・再配信・重複への対処も必要。必ず一度だけ処理されるとは限らない。')
add('その部品は、<mark>本当に必要？</mark>',cards([('授業で試す','画面の使いやすさだけなら、<br>メモリで足りる？','yellow'),('翌日も使う','別端末と共有するなら、<br>どこへ保存する？','blue'),('加工に30秒','待たせたくないなら、<br>受付と完了をどう分ける？','pink')]),section=7,note='隣の人と3分。必要な部品と、まだ要らない部品を選ぶ。')
add('難しい言葉を、<mark>自分の言葉へ。</mark>',table(['設計の言葉','やさしく言うと'],[['データ','扱う情報。何を覚えておく？'],['責務','担当する仕事。誰が何をする？'],['入出力','渡すもの・返ってくるもの。何を頼む？'],['失敗・境界','うまくいかないとき・ぎりぎりの条件では？'],['更新の通知','変わったことの伝え方。誰に知らせる？']],True),section=8,note='契約＝部品どうしで共有する約束。')
add('同じ「傘」でも、<mark>別の一件。</mark>',split('item-001',['品名：傘','場所：図書館','日付：2026-10-10'],'item-002',['品名：傘','場所：食堂','日付：2026-10-11']),section=8,note='削除するときは品名ではなく番号を渡す。返事は「削除できた／できなかった」。')
add('画面とデータ管理の、<mark>担当を分ける。</mark>',diagram([(30,35,370,115,'投稿フォーム','入力を受け取る',B),(30,320,370,115,'一覧・検索','条件と結果を表示',Y),(825,170,450,120,'データ管理','追加・取得・削除',G)],[(400,95,825,200,'追加して',604,115),(400,370,825,260,'条件に合う一覧を返して',620,375),(200,150,200,320,'成功したら再表示',332,243)]),section=8,note='保存方法を変えると、通信や失敗の約束も見直すことがある。')
add('「同じ意味」を、<mark>具体例で確かめる。</mark>',quote('「図書館で絞る」<br>それ、同じ答え？','完全一致？<br>部分一致？<br>条件なしなら？<br>0件なら？'),section=8,note='担当者が同じ例に同じ答えを返せるか。書かれていなければ決める。')
add('AIに、<mark>選択肢を出してもらう。</mark>',prompt('場所の絞り込みを設計します。\n実装はまだしないでください。\n\n画面側で絞る案と、\nデータ管理に条件を渡す案を比べてください。\n利点・負担・あとから変わる部品は？',9,'AIは案を出す。<br>自分は理由を理解して選ぶ。'),section=9,note='講師実演。選んだ理由を一文でメモする。')
add('design.mdは、<mark>AIと一緒に書く。</mark>',timeline([('ASK','質問してもらう','一問ずつ・具体例で'),('DRAFT','下書きを作る','未決定は「要確認」'),('EXPLAIN','言い直す','傘1件の流れで'),('SAVE','確認して保存','人が意味を確かめる')]),section=9,note='白紙から一人で書かなくてよい。プロンプトとひな形はコピー用ページへ。')
add('下書きを、<mark>自分の判断にする。</mark>',sheet([('選んだ案','私は、この案で進めたい'),('理由','大切にしたいことは？'),('負担','不便になること・増える手間は？'),('見直す条件','いつ選び直したほうがよい？')],'言えない行は<br>AIに聞き直す。<br><br>分からないまま<br>保存しない。'),section=9,note='重要な判断の背景・選択・結果を残す＝ADRの考え方。')
add('D-2｜<mark>日付でも絞れるように。</mark>',split('出発点：5節のアプリ',['場所で絞れる作業フォルダを複製','そのコピーをIDEで開く','未完了なら講師の基準版を使う'],'追加すること',['拾った日を一日だけ指定する','場所＋日付なら、両方に合う投稿','条件を空にすると、その条件を外す']),section=10,note='例：図書館＋2026-10-12 → ノート1件。日付を空に戻す → 図書館の2件。')
add('D-2｜<mark>この順番で進めよう。</mark>',exercise('24',[('理解・比較｜4＋4分','AIと今の構成を読む → 画面で絞る案／データ管理で絞る案を比べる'),('設計メモ｜5分','AIとdesign.mdを作る → 選んだ理由と動きをペアに説明'),('変更・確認｜7＋4分','specと計画に反映 → 実装 → 同じ3件で検査する')],'design.md・部品の図・アプリと確認記録'),section=10,note='時間で区切る。完成しなくても、選んだ理由・できたこと・未完了の場所を残す。')
add('D-2｜AIに頼み、<mark>自分で確かめる。</mark>',prompt('まずコードを読み、変更せずに説明して。\n入力・検索・表示を担う実際のファイルは？\n\n日付で絞る2案の利点と負担を比べて。\n私が選んだ案でdesign.mdを下書きして。\n未決定のことは、質問してください。',10,'図はまず3つの四角。<br>変更する場所と<br>空欄・0件の動きを確認。<br><br>spec更新 → plan確認<br>→ tasks → implement'),section=10,note='「日付を空に戻すと？」に答えられるか。全文と手順は資料の10節へ。')
add('D-2｜<mark>この結果になればOK。</mark>',table(['場所 ／ 日付','期待する結果'],[['空欄 ／ 空欄','3件すべて'],['図書館 ／ 空欄','図書館の傘＋ノート：2件'],['空欄 ／ 2026-10-11','食堂の傘：1件'],['図書館 ／ 2026-10-12','ノート：1件'],['図書館 ／ 2026-10-11','0件だと分かる'],['条件を空にし、図書館の傘を削除','食堂の傘＋ノートが残る']],True),section=10,note='確認前に同じ3件を登録。結果・未完了・予測と実際の違いを記録する。')
add('その判断を、<mark>一文にしよう。</mark>',quote('私は＿＿を、<br>＿＿に担当させた。','理由は＿＿。<br><br>次に＿＿が必要なら、<br>この判断を見直す。'),section=11,note='2分。どの設計メモが、変更の予測や確認に役立った？')
# Team architecture studio.
add('自分の案を、<br><mark>チームの判断へ。</mark>','<div class="chapter-n">02</div><p class="chapter-copy">各自で比較する。図にする。理由を持ち寄る。<br>合意したら、部品の役を分けて確かめる。</p><div class="chapter-note">違うお題で、<br>同じ考え方を使おう。</div>','chapter',12,eyebrow='4限 / ARCHITECTURE STUDIO')
add('新しいお題：<mark>学園祭の注文サービス。</mark>',timeline([('ORDER','来場者が注文','スマホで焼きそば2つ'),('ACCEPT','店が確認','別の端末で受付'),('COOK','状態を更新','受付済み → 調理中'),('PICK UP','番号で受け取る','受け取り可を確認')]),section=12,note='3〜4人のチーム。料理を作るのは人。ソフトウェアは情報をつなぐ。')
add('比べる前に、<mark>条件を揃える。</mark>',split('必ず満たすこと',['来場者とスタッフが同じ注文を見る','保存済みの注文は再起動後も復元','スタッフが状態を更新し、来場者が確認'],'今回の範囲',['一店舗・焼きそば一種類・数量と番号','支払いは店頭。オンライン決済は扱わない','在庫・本人確認等の詳細は実運用前に検討']),section=12,note='6分：条件を読む3分＋分からない言葉と優先したいことを共有3分。')
add('「注文が集中したら」を、<mark>考える。</mark>',quote('店の端末が、<br>一時的につながらない。','注文を見落とさない？<br>復旧後に見つけられる？<br>運用する人は困らない？'),section=12,note='件数や速度は未測定。調理の順番待ちと、技術部品のキューは同じではない。')
add('案A｜画面から、<mark>定期的に取りに行く。</mark>',diagram([(0,165,330,125,'スタッフ画面','一定間隔で問い合わせ',Y),(550,165,350,125,'アプリケーション','注文を取得して返す',B),(1130,165,300,125,'DB','注文・状態を保存',G)],[(330,215,550,215,'未対応の注文は？',438,185),(900,215,1130,215,'取得',1015,185)]),section=13,note='部品を少なくできる可能性。問い合わせ間隔・古い表示・復旧後の再取得を考える。')
add('案B｜通知の仕事を、<mark>受け渡す。</mark>',diagram([(0,170,270,120,'受付アプリ','注文を受け付ける',B),(430,10,310,110,'DB','注文本体を残す',G),(430,265,310,110,'キュー','通知の依頼',Y),(850,265,260,110,'通知処理','届ける仕事',P),(1140,20,290,115,'スタッフ画面','注文を確認',W)],[(270,190,430,65,'保存',345,110),(270,240,430,320,'通知依頼',342,320),(740,320,850,320,'',797,300),(1000,265,1250,135,'通信も設計する',1210,224)]),section=13,note='DB保存と通知の食い違い、再試行、重複も考える。キューだけで画面には届かない。')
add('どちらも、<mark>よいところと負担がある。</mark>',table(['比較','案A：取りに行く','案B：通知を届ける'],[['画面の情報','問い合わせまで古い場合がある','通知遅延や通信失敗もある'],['必要な工夫','間隔・再取得・未対応の見分け','再試行・重複・保存との連動'],['作る・運用する負担','構成を少なくできる可能性','部品と監視する場所が増える']]),section=13,note='例は正解集ではない。誰にとって何がよいか、今回の条件で比べる。')
add('図は、<mark>操作を追える地図。</mark>',cards([('四角','名前＋担当する仕事。<br>「受付アプリ：注文を保存」','blue'),('矢印','何を渡すか＋順番。<br>①注文 → ②保存 → ③返事','yellow'),('注記','待つ場所・後で処理する場所。<br>失敗したら、どうなる？','pink')]),section=13,note='主要な部品は5〜7個程度。部品の役割と、人の担当は区別する。')
add('F-1｜各自、<mark>最低2案を考える。</mark>',exercise('16',[('案を出してもらう｜5分','全員が同じお題・条件をAIへ渡す'),('1件の注文をたどる｜7分','両方の案を理解し、AIの理解確認問題に答える'),('比較メモ｜4分','利点・負担・分からない前提を自分の言葉で')],'2案の比較メモ'),section=14,note='最初から一人一案に分担しない。自分で比較してから持ち寄る。')
add('AIに頼むのは、<mark>条件の同じ2案。</mark>',prompt('同じ条件を満たす構成を2案出してください。\nまだコードやファイルは作らないでください。\n\n部品・注文の流れ・残す情報・待つ場所、\n今回の条件での利点と負担を説明してください。\n専門用語は言い換えてください。',14,'製品名だけでなく、<br>仕事の分け方や<br>情報の流れを比べる。'),section=14,note='図だけでは速度・費用を断定できない。未確認のことは印を付ける。')
add('「焼きそば2つ」で、<mark>説明してもらう。</mark>',quote('誰が、誰に、<br>何を渡す？','何が返る？<br>画面はどう変わる？<br>保存・受付・調理完了は<br>いつ起きる？'),section=14,note='自分で流れを言い直す。AIの説明は7節の表とも照合する。')
add('比較メモは、<mark>理由まで書く。</mark>',table(['見ること','案A','案B'],[['必須条件を満たす方法','どこに保存？ 誰と共有？','同じ条件で比べる'],['待ち時間・見える状態','誰が何を待つ？','同左'],['失敗への対応','どこで気づく？ どう戻す？','同左'],['負担・要確認','増える仕事は？ 未検証は？','同左']],True),section=14,note='「速い」「簡単」で止めず、誰にとって、何が、なぜそうなるか。')
add('F-2｜2案を並べて、<mark>図にする。</mark>',exercise('12',[('左右に案A・案B｜8分','draw.ioの1画面に。共通の役割には同じ名前を使う'),('推奨案を一つ選ぶ｜4分','優先した条件、理由、弱点を図の下に書く')],'architecture-options-自分の名前.drawio.svg'),section=15,note='AIに四角と矢印の作業順を聞いてよい。意味を確認して採用する。')
add('推奨案には、<mark>弱点も添える。</mark>',sheet([('私の推奨案','A ／ B'),('優先する条件','今回いちばん大切なのは？'),('選んだ理由','その条件に、どう合う？'),('弱点と要確認','負担・不利益・確かめたいこと')],'採らなかった案の<br>よいところも<br>言ってみよう。'),section=15,note='個人の提案は、チームとの対話で変わって構わない。')
add('F-3｜図と理由を、<mark>持ち寄る。</mark>',exercise('12',[('注文の流れを指でたどる','まず、利用者の操作を説明する'),('2案の違いと、選んだ理由','弱点も隠さず伝える'),('聞く人が言い直す','「あなたは＿＿を優先した案だと理解した」')],'共通点・違い・未決定のメモ'),section=16,note='4人なら1人3分。3人なら1人4分。質問の時間も含める。')
add('その矢印の意味、<mark>伝わっている？</mark>',cards([('残る？','どの注文情報が、<br>再起動後も残りますか？','green'),('いつ？','受付済みと受け取り可は、<br>同じタイミングですか？','yellow'),('止まったら？','この部品が使えないと、<br>何ができなくなりますか？','pink')]),section=16,note='全員が自分の図を説明する。聞いた人が理解を返す。')
add('F-4｜同じ基準で、<mark>一つに決める。</mark>',exercise('12',[('必須条件と優先順位｜4分','満たせる根拠を確認し、優先する品質を二つ選ぶ'),('選択と不利益を合意｜4分','意見が割れたら、暫定案と見直す条件を残す'),('チームの図を揃える｜4分','個人図を複製し、合意した違いを反映')],'team-design.md ＋ team-architecture.drawio.svg'),section=17,note='よいところを全部足すと、接点や運用の負担も増える。')
add('チームのメモも、<mark>AIと書く。</mark>',prompt('話し合いを、team-design.mdの下書きに。\n\n決まったことと、意見が分かれたことを区別。\n未決定は勝手に決めず、質問してください。\n専門用語には、やさしい言い換えを。\n全員が確認してから保存してください。',17,'記録係が一人で<br>全部を書く必要はない。<br><br>一項目ずつ、<br>意味を確認しよう。'),section=17,note='条件・比較した案・選択理由・不利益・見直す条件・部品間の約束を残す。')
add('描いた人以外が、<mark>説明できる？</mark>',quote('「この注文は、<br>こう流れます。」','最新の図とメモを<br>全員が持つ。<br><br>接点を変えるときは、<br>影響する人と相談する。'),section=17,note='図と文章が食い違っていたら、揃えてから進む。')
add('F-5｜図を、<mark>小さく動かしてみる。</mark>',exercise('14',[('問いと役を決める｜3分','何を確かめたいか、期待する動きを書く'),('紙・付箋で動かす｜6分','正常な流れ → 失敗や再試行の流れ'),('不足を直して再確認｜5分','約束と図を更新し、該当箇所をもう一度')],'予想・詰まった場所・修正・再確認の記録'),section=18,note='サーバー一式の実装は必須ではない。役を分け、情報を実際に受け渡す。')
add('あなたが、<mark>部品の役になる。</mark>',table(['役','受け取る・渡すもの'],[['来場者画面・受付','焼きそば2つの注文 → 受付結果を見る'],['注文の保存・受け渡し','注文番号・数量・状態を残し、伝える'],['スタッフ画面・状態更新','注文を確認 → 調理中・受け取り可へ'],['観察・記録','図と約束だけで進められるか見る']]),section=18,note='3人なら観察役を兼ねる。実際に料理は作らず、状態を模擬する。')
add('付箋に書くのは、<mark>具体的な情報。</mark>',sheet([('注文番号','order-001'),('数量','焼きそば × 2'),('現在の状態','受付済み → 調理中 → 受け取り可'),('渡す相手','次はどの部品へ、何を知らせる？')],'必要な情報が<br>なかったら、<br>「未決定」と記録。'),section=18,note='図にない判断を、役の人が黙って補わない。')
add('うまくいかないときも、<mark>たどってみる。</mark>',cards([('通信が切れた','保存済みの注文を、<br>復旧後に見つけられる？','blue'),('同じ通知が来た','別の注文だと思って、<br>二重に指示しない？','pink'),('調理中','来場者は何を見て、<br>何を待っている？','yellow')]),section=18,note='選んだ案で重要なシナリオを一つ選ぶ。')
add('不足が見つかったら、<mark>約束を更新。</mark>',timeline([('OBSERVE','事実を記録','どこで詰まった？'),('AGREE','関係者と決める','何が足りなかった？'),('UPDATE','図とメモを直す','変更を全員へ'),('RETRY','もう一度たどる','今度は進める？')]),section=18,note='紙で分かるのは情報・役割・状態の不足。速度や永続性の保証は別途検証する。')
add('別チームの目で、<mark>案を見直す。</mark>',exercise('12',[('説明と質問を交代｜4分ずつ','図・理由・検証で分かったことを伝える'),('自分たちの案を見直す｜4分','採用・保留・不採用と、その理由を記録')],'レビューへの対応と更新した図'),section=19,note='質問：意味が曖昧な矢印は？ 条件を満たす根拠は？ 増える負担は？')
add('最後は、<mark>自分の言葉で。</mark>',exercise('8',[('個人で答える｜5分','2案の違いと選択理由は？'),('判断の変化を振り返る','個人案とチーム案の違い、変えた／維持した理由は？'),('一つ共有する｜3分','検証で見つかった不足、修正、まだ分からないことは？')],'本文20節の3問への個人回答'),section=20,note='図やメモは見てよい。この回答はAIに作らせず、自分で説明する。')
add('部品を選ぶ。<br><mark>判断を共有する。</mark>','<div class="chapter-n">04</div><p class="chapter-copy">条件を揃える。複数案を比べる。弱点も引き受ける。<br>つないで分かったことから、設計を見直す。</p><div class="chapter-note">全部の部品を<br>使わなくていい。</div>','chapter',20,eyebrow='TAKEAWAY / DESIGN TOGETHER')
add('提出するのは、<mark>判断の跡。</mark>',split('全員、個別に',['2案の図と比較表','推奨案・選択理由','20節の3問への回答'],'チームで',['最終図＋team-design.md','検証記録とレビューへの対応','3限D-2の記録は個人またはペア']),section=20,note='Slackの提出用スレッドへ。締切：第5回の前日。未完了・未検証も明記。')
add('授業のあとも、<mark>一つ確かめる。</mark>',split('試作品を改善｜3時間程度',['注文サービスの画面をモックで試す','他の人が迷うところを観察する','本物のDB等につないでいない部分を明記'],'構成を見直す｜2時間程度',['注文が増えたら？','通信や保存先が止まったら？','変える部品・約束と測り方を図に追記']),section=20,note='4限は、DBやキューを実装・公開できたかでは評価しない。')
add('次は、<mark>価値を合わせる対話へ。</mark>',quote('誰の、何を<br>優先する？','第5回<br>対話と問いを用いた<br>価値のデザイン<br><br>担当：竹田先生'),section=20,note='今日の「違う案からどう合意するか」を、次の授業へ。')
add('もっと知りたい人へ。',split('設計と部品',['<a href="https://www.sei.cmu.edu/software-architecture/">SEI：Software Architecture ↗</a>','<a href="https://redis.io/docs/latest/management/persistence/">Redis：Persistence ↗</a>','<a href="https://www.rabbitmq.com/tutorials/tutorial-two-javascript">RabbitMQ：Work Queues ↗</a>'],'授業で使うもの',['<a href="workbook.html">プロンプト・ひな形を開く ↗</a>','<a href="https://app.diagrams.net/">draw.io ブラウザ版 ↗</a>','<a href="../README.md">第4回の講義本文 ↗</a>']),section=20,note='資料の出典と追加の参考文献は、講義本文の末尾へ。')
# Optical variation: adjacent slides use different compositions.
slides[2]['content']=sheet([('ソフトウェア開発演習','第4回フォルダを作る'),('新しいZIPを展開','starter-windows ／ starter-mac'),('そのフォルダを開く','Antigravity IDE → /speckit- の候補を確認')],'前回の作業済み<br>フォルダは<br>使い回さない。')
slides[17]['content']=table(['置き方','役割と例','考えること'],[['ファイル／オブジェクト','写真本体を保存する','誰が見られる？ 投稿と一緒に消す？'],['DBとの組み合わせ','DBには写真の保存先を記録する','情報と写真をどう結び付ける？'],['キャッシュ','よく使う結果を一時保持する','いつ更新・期限切れ・破棄にする？']])
labels={1:'GET READY',2:'DEVELOPMENT CYCLE',3:'REQUIREMENTS',4:'EXERCISE D-1',5:'PREDICT THE CHANGE',6:'REFLECT',7:'ARCHITECTURE',8:'INTERFACE AGREEMENTS',9:'DESIGN WITH AI',10:'EXERCISE D-2',11:'REFLECT',12:'TEAM BRIEF',13:'COMPARE & DRAW',14:'EXERCISE F-1',15:'EXERCISE F-2',16:'EXERCISE F-3',17:'EXERCISE F-4',18:'EXERCISE F-5',19:'PEER REVIEW',20:'REFLECT & SHARE'}
for d in slides:
    if d['eyebrow']=='DESIGN / MAKE / LEARN': d['eyebrow']=f"{d['section']:02d} / {labels[d['section']]}"

# Render all slide markup.
header='<header class="identity"><div>KYOTO UNIVERSITY OF THE ARTS<br>Department of Information Design</div><span class="identity-line"></span><div>Solution Design with Technology<br>2026 Spring</div></header>'
footer='<footer class="identity-bottom">PEOPLE<br>TECHNOLOGY<br>IDEAS<br>FOR A BETTER TOMORROW.</footer>'
total=len(slides); sections=[]
for i,d in enumerate(slides,1):
    title=re.sub('<[^>]+>','',d['title']).replace('&','＆')
    content=d['content'] if d['kind'] in ('chapter','cover') else '<div class="s4-content">'+d['content']+'</div>'
    note='<div class="takeaway">'+d['note']+'</div>' if d['note'] else ''
    sections.append(f'<section class="slide s4 s4-{d["kind"]}" data-title="{esc(title,quote=True)}" aria-label="{i}：{esc(title,quote=True)}"'+(' hidden' if i>1 else '')+'>'+header+f'<div class="page-tag">{i:02d} / {total}</div><div class="eyebrow">{d["eyebrow"]}</div><h1>{d["title"]}</h1>'+content+note+footer+f'<div class="s4-foot"><span>LECTURE 04 · {"3限" if d["section"]<12 else "4限"}</span><a href="workbook.html#section-{d["section"]}" target="_blank" rel="noopener">資料・プロンプト ↗</a></div></section>')
nav=f'<nav aria-label="スライド操作"><button id="prev" aria-label="前のスライド">← 前へ</button><label><input id="page" type="number" min="1" max="{total}" value="1" aria-label="スライド番号"> / {total}</label><button id="next" aria-label="次のスライド">次へ →</button><button id="fullscreen">全画面</button><a href="review.html">一覧</a><span class="help">← → / Space：移動 · F：全画面 · H：操作バー</span></nav>'
(ROOT/'index.html').write_text('<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第4回 ソリューショニングとプロトタイピング</title><link rel="stylesheet" href="styles.css"></head><body><main id="stage" aria-label="第4回の講義スライド"><div id="deck">'+ '\n'.join(sections)+'</div></main>'+nav+'<span id="status" class="sr-only" aria-live="polite"></span><noscript><a href="review.html">画像一覧を開く</a></noscript><script src="viewer.js"></script></body></html>')
# Browser-readable course material; safe local markdown subset. Exact code blocks stay copyable.
source=SOURCE.read_text(); lines=source.splitlines(); out=[]; i=0; current=0; skip=False
while i<len(lines):
    line=lines[i]
    if line=='## 目次':
        i+=1
        while i<len(lines) and lines[i]!='---': i+=1
        continue
    if line.startswith('```'):
        lang=line[3:]; block=[]; i+=1
        while i<len(lines) and not lines[i].startswith('```'): block.append(lines[i]); i+=1
        code='\n'.join(block)
        if lang=='mermaid': out.append('<details><summary>構成図のテキスト</summary><pre>'+esc(code)+'</pre></details>')
        else: out.append('<div class="code"><button type="button" class="copy">コピー</button><pre>'+esc(code)+'</pre></div>')
        i+=1; continue
    def inline(t):
        t=esc(t); t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t); t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
        def link(m):
            url=m[2]
            if not re.match(r'https?://|#',url): url='../'+url
            return '<a href="'+url+'">'+m[1]+'</a>'
        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,t)
    m=re.match(r'^(#{1,4}) (.+)',line)
    if m:
        h=min(len(m[1])+1,4); n=re.match(r'(\d+)\.',m[2]); attr=f' id="section-{n[1]}"' if len(m[1])==2 and n else ''
        out.append(f'<h{h}{attr}>'+inline(m[2])+f'</h{h}>')
    elif line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].startswith('|'):
            row=lines[i].strip('|').split('|')
            if not all(re.match(r'^\s*:?-+:?\s*$',x) for x in row): rows.append(row)
            i+=1
        out.append('<div class="table-wrap"><table>'+''.join('<tr>'+''.join('<'+('th' if ri==0 else 'td')+'>'+inline(c.strip())+'</'+('th' if ri==0 else 'td')+'>' for c in row)+'</tr>' for ri,row in enumerate(rows))+'</table></div>'); continue
    elif line.startswith('>'): out.append('<p class="callout">'+inline(re.sub(r'^>\s*(\[![A-Z]+\])?','',line))+'</p>')
    elif line.strip()=='---': out.append('<hr>')
    elif line: out.append('<p>'+inline(line)+'</p>')
    i+=1
workcss='body{max-width:1000px;margin:40px auto;padding:0 24px;background:#f5f4ef;color:#111;font:17px/1.85 system-ui,sans-serif}h1,h2,h3{line-height:1.5}h2{margin-top:60px;border-bottom:4px solid #fff34d}h3{margin-top:35px;scroll-margin-top:20px}a{color:#222}table{border-collapse:collapse;width:100%;background:white}td,th{padding:12px;border:1px solid #ccc;text-align:left}th{background:#eeecd9}.table-wrap{overflow:auto}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.8 monospace;margin:0}.code{background:white;padding:24px;margin:24px 0;border-left:6px solid #fff34d}.copy{float:right;cursor:pointer;padding:8px 16px;background:#fff34d;border:1px solid #aaa}.callout{border-left:3px solid #b0b6aa;padding-left:16px}code{background:#e7e5dc}header{border-bottom:2px solid #111;padding-bottom:20px}'
script="""document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',async()=>{const t=b.nextElementSibling.textContent;try{await navigator.clipboard.writeText(t);b.textContent='コピーしました';}catch{const r=document.createRange();r.selectNodeContents(b.nextElementSibling);const s=window.getSelection();s.removeAllRanges();s.addRange(r);b.textContent='選択しました（Ctrl/Cmd+C）';}}));"""
(ROOT/'workbook.html').write_text('<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第4回 資料・コピー用プロンプト</title><style>'+workcss+'</style><body><header><h1>第4回 · 資料とプロンプト</h1><a href="index.html">スライドへ</a> ／ <a href="review.html">一覧へ</a><p>プロンプトはボタンからコピーできます。講義本文から生成した資料です。</p></header>'+''.join(out)+'<script>'+script+'</script></body></html>')
(ROOT/'slide-map.md').write_text('# スライドと講義本文の対応\n\n| 枚 | タイトル | 本文の節 |\n| --- | --- | --- |\n'+''.join(f'| {i:02d} | {re.sub("<[^>]+>","",d["title"])} | {d["section"]} |\n' for i,d in enumerate(slides,1)))
print(f'Built {total} slides and workbook.html')
