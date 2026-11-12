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
def agenda(period, rows, goal):
    assert sum(minutes for _, minutes, _ in rows) == 100
    return '<div class="s7-agenda"><aside><span>'+period+'限</span><b>100</b><small>MINUTES</small><p>'+goal+'</p></aside><ol>'+''.join('<li><strong>'+title+'</strong><span>'+detail+'</span><b>'+str(minutes)+'<small>分</small></b></li>' for title,minutes,detail in rows)+'</ol></div>'
def work(do, minutes, steps, dest, also=''):
    assert do and minutes and steps and len(steps)<=3 and len(dest)==2 and all(dest)
    body='<ol class="s4-steps">'+''.join(f'<li><strong>{a}</strong><small>{b}</small></li>' for a,b in steps)+'</ol>'
    return body

def destination(dest, also=''):
    name, detail=dest
    cls=' template' if name.startswith('テンプレート') else ''
    return f'<aside class="s7-dest{cls}"><small>書く場所・残す場所</small><strong>{name}</strong><span>{detail}</span><em>{also}</em></aside>'

diagram_count=0
def diagram(nodes,edges):
    # Fixed diagram canvas. Edge labels use a paper-colored halo for legibility.
    global diagram_count
    diagram_count+=1
    arrow_id=f'arrow-{diagram_count}'
    out=[f'<svg class="s4-diagram" viewBox="0 0 1440 495" role="img" aria-label="部品と情報の流れ"><defs><marker id="{arrow_id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#151515"/></marker></defs>']
    for edge in edges:
        x1,y1,x2,y2,label,lx,ly=edge[:7]
        route=edge[7] if len(edge)>7 else f'M{x1} {y1}L{x2} {y2}'
        out.append(f'<path class="edge" d="{route}" marker-end="url(#{arrow_id})"/>')
        if label: out.append(f'<text class="edge-label" x="{lx}" y="{ly}" text-anchor="middle">{esc(label)}</text>')
    for x,y,w,h,title,sub,color in nodes:
        out.append(f'<rect class="node" x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/><text class="node-title" x="{x+w/2}" y="{y+42}" text-anchor="middle">{esc(title)}</text><text class="node-sub" x="{x+w/2}" y="{y+79}" text-anchor="middle">{esc(sub)}</text>')
    return ''.join(out)+'</svg>'
Y='#fff34d'; B='#dceaf0'; P='#f5d9df'; G='#dcecd9'; W='#ffffff'
def slide(title,content,section=1,note='',kind='',target=None):
    add(title,content,kind,section,note,eyebrow='LECTURE 07 / '+('DEFINE / DESIGN / BUILD' if section<5 else 'TEST / IMPROVE / SHARE'))
    if target: slides[-1]['target']=target
slide('現実に向き合い、<br><mark>動く形で</mark><br><mark>確かめる。</mark>',
    '''<div class="cover-sub">考え抜いたソリューションを、プロトタイプへ。<br>使ってもらい、学び、もう一度よくする。</div>
    <div class="s7-cover-course">第7回 ／ ケーススタディ<br><strong>ソリューショニングと成果発表</strong></div>
    <div class="s7-cover-board" aria-label="構成を考え、動く画面をつくり、使う様子から学ぶ">
      <div class="s7-cover-backdrop"></div><span class="s7-cover-number" aria-hidden="true">07</span>
      <article class="s7-sketch"><i class="tape"></i><span class="s7-kicker">01 / DESIGN</span><h2>どうつなぐ？</h2>
        <svg viewBox="0 0 360 125" role="img" aria-label="使う人から画面、記録へつながる構成のスケッチ"><g fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="32" cy="36" r="14"/><path d="M10 100V76Q32 52 54 76V100 M65 66H112 M104 59L113 66L104 73"/><rect x="122" y="30" width="98" height="70" rx="3"/><path d="M122 47H220 M233 66H280 M272 59L281 66L272 73"/><ellipse cx="319" cy="40" rx="28" ry="10"/><path d="M291 40V91C291 106 347 106 347 91V40"/></g><g fill="currentColor" font-size="18" text-anchor="middle"><text x="171" y="79">画面</text><text x="319" y="79">記録</text></g></svg>
      </article>
      <article class="s7-prototype"><div class="s7-window-bar"><span>● ● ●</span> PROTOTYPE</div><div class="s7-window-body"><span class="s7-kicker">02 / BUILD</span><h2>アイデアを、動く形に。</h2><div class="s7-ui-row"><span>502号室</span><b>清掃完了 ✓</b></div><div class="s7-ui-row"><span>503号室</span><span>清掃中</span></div><small>画面例：清掃状況を共有する</small></div></article>
      <article class="s7-test-note"><i class="tape"></i><span class="s7-kicker">03 / LEARN</span><h2>使ってみたら、<br>何がわかった？</h2><span class="hand">観察 → 改善 → 次の問い</span></article>
      <svg class="s7-cover-arrow" viewBox="0 0 180 120" aria-hidden="true"><path d="M155 100Q20 125 24 22M8 40L24 20L40 40" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>''',kind='cover',target='section-1-4')
slide('今日のゴールは、<mark>一本を通すこと。</mark>',split('3限｜最小の流れを動かす',['条件を1〜3項目に絞り、構成図を描く', 'AC1：入力から結果まで動く'],'4限｜確かめ、直し、伝える',['他チームの操作を観察し、修正・再確認', '判断の理由と、次に確かめたいことを発表']),section=1,note='今日更新するのは成果物テンプレート8〜11。講義スライドのページ番号とは別です。',target='section-1-3')
slide('3限の時間割｜<mark>絞って、つくり始める。</mark>',agenda('3',[
    ('イントロダクションと準備',10,'前回の指摘を整理し、役割を決める'),
    ('受け入れ条件を絞り、仕様書にする',20,'考える8分 → AIで整理7分 → 仕様書を確認5分'),
    ('構成を決めて、技術を選ぶ',12,'2案を比較5分 → 図にする5分 → 理由を記録2分'),
    ('つくって、確かめる',50,'計画・タスク → AC1を実装 → 人が動作確認'),
    ('予備',8,'絞り直しと仕様書の確認に使う')], '入力から結果まで、<br>最小の流れを通す。'),section=1,note='予備を含めて100分。説明を聞いたら、その場でチームの作業へ。')
slide('始める前に、<mark>手元を揃える。</mark>',table(['開くもの','準備・確認すること'],[['第6回の成果物','対象・課題・選んだ案（成果物テンプレート5〜7）'],['今日の記録先','成果物テンプレート8〜11と、絞り込みシート'],['第7回用スターター','展開したフォルダそのものをAntigravity IDEで開く'],['準備完了の確認','チャットで /speckit- を入力し、コマンド一覧を確認']]),section=1,target='section-2-7',note='未準備ならイントロ中に準備。資料にOS別ダウンロードリンクがあります。')
slide('今回は、<mark>ブラウザの中で試す。</mark>',split('つくる範囲',['主要な流れを一本。条件は1〜3項目', '保存はlocalStorageまで：このブラウザ内に残す'],'代わりの方法で試す',['外部サービス・DBは使わない', 'ログイン・外部連携・端末間共有は模擬']),section=2,target='section-2-4',note='模擬＝代わりの方法で試すこと。模擬した範囲と、確かめられないことも残す。')
slide('指摘を全部、<mark>実装しなくていい。</mark>',split('KEEP／CHANGE',['残すものと、変える候補を分ける', '指摘の背景と根拠を話し合う'],'QUESTION',['まだ分からないことを残す', '変えない判断にも理由を書く']),section=1,note='5分：第6回の中間発表を振り返る。',target='section-1-4')
slide('一つの画面を、<mark>全員で考える。</mark>',split('操作する人',['AIへ指示し、画面を操作', '考えを声に出す'],'見ている人',['目的・範囲・確認漏れを点検', '分からないことをその場で聞く']),section=1,note='10分ごと、またはACが一つ通ったら交代。スターターは事前に準備。',target='section-1-5')
slide('何をつくるかの前に、<mark>何を確かめたい？</mark>',exercise('8',[('①問い・②場面・③結果を決める', '何が分かれば一歩前へ？ 誰が、いつ、何をできればよい？'), ('④小さくする・⑤線を引く', '対象・画面・データを減らす。つくる／代用する／今回は扱わない'), ('⑥確かめ方を書く', '何を操作して、どんな結果なら予定どおり？')],'<a href="https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/7_case_study_solutioning_and_presentation/handout/scope-and-spec.md" target="_blank" rel="noopener">絞り込みシート前半①〜⑥ ↗</a>'),section=2,target='section-2-2',note='チームで判断。言葉にできないときはAIへ相談してよい。')
slide('残すか削るかは、<mark>目的から決める。</mark>',quote('それをつくらなくても、<br>確かめたいことは<br>確かめられる？','はい → 後回し・模擬へ。<br>いいえ → 残すか、簡単な方法へ。'),section=2,target='section-2-3',note='例：通知なしでも状態表示は試せる。状態表示そのものがなければ試せない。')
slide('条件は一つでも、<mark>確かめ方は複数。</mark>',table(['役割','ホテルの例'],[['AC1：できるようにすること','清掃担当が完了を記録 → フロントの一覧で状態が分かる'],['確認例1：正しく変わる？','502号室を完了にし、一覧で502号室だけが変わる'],['確認例2：繰り返しても大丈夫？','同じ部屋を2回完了にしても、一覧の行が増えない']]),section=2,target='section-2-4',note='確認例を増やすことは、機能の追加ではない。シート全文に残して仕様書へ渡す。')
slide('AIで整理し、<mark>人が判断する。</mark>',exercise('7',[('資料2.4の完全版プロンプトをコピー', '①〜⑥を入力欄へ貼り、AIに後半の下書きを依頼'), ('条件は1〜3項目。AC1で一本通す', '例：清掃完了を記録 → フロントの一覧で状態を確認できる'), ('増えていないか・目的が残るかを確認', '勝手な機能追加はない？ 模擬範囲と検証の限界は正しい？')],'合意したシート原本・成果物テンプレート8への要約'),section=2,target='section-2-4',note='AC＝受け入れ条件。予定どおりかを判断する条件。項目数だけでは範囲は小さくならない。')
slide('使い続けてもらうには、<mark>何が障害？</mark>',split('今回、確かめられること',['状態の表示を読み取れるか', '操作する場所が伝わるか'],'今回だけでは分からないこと',['繁忙時にも入力してもらえるか', '実際の端末間で情報を共有できるか']),section=2,target='section-2-5',note='ホテルの仮想例。同じPCでの代用と実運用は違う。障害と次の検証をQUESTIONへ。')
slide('仕様書を、<mark>自分たちの条件と照合。</mark>',exercise('5',[('シート全文を /speckit-specify へ', '要約ではなく、確認例・制約を含む全文を渡す'), ('spec.md の条件と範囲を確認', '条件が増えていない？ AC1で入力から結果まで通る？'), ('除外した機能と確認例も照合', '「今回つくらないもの」が混ざっていない？ 確認例は一致？')],'確認済みのspec.md'),section=2,target='section-2-7',note='スターターは事前に展開。未完了なら予備8分で絞り直し・仕様確認。')
slide('構成は2案。<mark>理由を持って選ぶ。</mark>',exercise('5',[('AIに、違いのある2案を依頼', '部品の仕事・情報の置き場所・AC1の流れを比較'), ('仕事への適合と負担を比べる', 'その人の仕事に合う？ 手間が増えない？'), ('全員が説明できる案を選ぶ', '残り時間でつくれるか。選んだ理由を話す')],'選択した構成案'),section=3,target='section-3-1',note='技術名の好みではなく、採用した条件とのつながりで判断する。')
slide('図を描き、<mark>一件の操作をたどる。</mark>',exercise('5',[('AIにdraw.ioの下書きを依頼', '主要な部品3〜5個。やさしい名前と、渡す情報・返事の矢印'), ('編集できる形式で保存し、開く', '.drawio または .drawio.svg。AC1を一件、指でたどる'), ('描いた人以外が説明する', '分からない線は聞いて直す。図のファイル名を計画に渡す')],'成果物テンプレート9に貼る構成図'),section=3,target='section-3-2',note='「502号室の完了」から「フロントの表示」まで、情報の流れを説明できる？')
slide('選んだ技術を、<mark>理由と一緒に。</mark>',sheet([('選んだ技術','何を使い、どう組み合わせる？'),('選んだ理由','今回の条件にどう合う？'),('採らなかったもの','何を採らず、なぜそう判断した？')],'2分で記録。<br>成果物テンプレート9へ。'),section=3,target='section-3-3',note='「AIが選んだから」ではなく、チームの判断を書く。')
slide('決めた構成を、<mark>計画とタスクへ。</mark>',timeline([('PLAN','計画する','図の参照先と選択理由をAIへ'),('REVIEW','人が読む','つなぎ目と追加された前提を確認'),('TASKS','作業に分ける','確認できる単位のタスクへ')]),section=4,target='section-4-1',note='開発50分の中で実施。/speckit-plan → 内容確認 → /speckit-tasks。')
slide('一度に全部ではなく、<mark>AC1から。</mark>',prompt('/speckit-implement\nAC1に必要な共通準備と実装だけを。\nAC2・AC3固有の実装には進まないで。\n確認手順を示して停止し、\n私たちの確認を待ってください。','4-2','人がブラウザで確認。<br>採用した次のACへ。'),section=4,target='section-4-2',note='投影用の要約。全文は右下の資料へ。次の条件を追加したら、AC1も再確認。')
slide('範囲が膨らんだら、<mark>立ち止まる。</mark>',cards([('見つける','採用した条件にない機能が<br>増えていない？','blue'),('影響を見る','消すと、必要な動作まで<br>壊れない？','yellow'),('判断する','AIには報告と提案だけ。<br>人が確認してから変更。','pink')]),section=4,target='section-4-3',note='開発開始から30分を目安に点検する。機能が増えるほど良いわけではない。')
slide('止まったら、<mark>原因を切り分ける。</mark>',table(['確認すること','記録すること'],[['現在採用している条件','通る／通らない／未確認'],['止まる場所','どの操作で、何が起きた？'],['直す順番','AC1が通らなければ最優先'],['確認できないもの','推測で合格にせず、未確認と残す']]),section=4,target='section-4-4',note='AIにはまず切り分けと提案を依頼。実際の動作を自分たちでも確かめる。')
slide('流れを切らずに、<mark>小さくする。</mark>',table(['いまの状況','チームで決めること'],[['残り20分でAC1が通らない','AC2以降を外す。AC1の入力から結果までを優先'],['AC1は通ったが、AC2が重い','対象を減らす・画面をまとめる・固定データで試す'],['AC1自体が大きすぎる','流れを残して簡略化。模擬した範囲と限界を記録']]),section=4,target='section-4-5',note='シート・spec・plan・tasksを揃える。成果物テンプレート8・10にも変更と理由を残す。')
slide('4限の時間割｜<mark>確かめ、直し、伝える。</mark>',agenda('4',[
    ('実装の仕上げと動作確認',15,'他チームがすぐに触れる状態にする'),
    ('他チームと確かめる',10,'5分ずつ交代して、操作と観察'),
    ('対応を決めて直し、再確認する',10,'対応を決める3分 → 修正・再確認7分'),
    ('最終発表の準備',15,'資料を整理し、デモを一度通す'),
    ('最終発表・質疑',35,'5チーム × 発表4分・質疑2分 ＋ 切り替え5分'),
    ('個人の振り返り',5,'判断・学び・次の行動を自分の言葉で残す'),
    ('予備',10,'発表が延びたときの調整に使う')], '使ってもらい、<br>学びを次につなぐ。'),section=5,note='つくって終わりにしない。観察 → 判断 → 修正 → 再確認までを一周する。')
slide('触ってもらえる状態に、<mark>仕上げる。</mark>',exercise('15',[('採用した条件の未完了を確認', 'AC1の一連の流れを優先する'), ('初期データと開始画面を用意', '他チームがすぐに操作を始められる状態にする'), ('機能追加を止める', '新しい案は記録し、次の検討へ')],'操作できるプロトタイプ'),section=5,target='section-5',note='ここから4限。仕上げ → 相互確認 → 修正・再確認の順で進める。')
slide('相手が操作。<mark>つくった人が観察。</mark>',split('つくったチーム',['操作せず、行動と言葉を見る', '<a href="https://github.com/Creative-Cucumbers/solution-design-with-technology/blob/main/2026/7_case_study_solutioning_and_presentation/handout/review-sheet.md" target="_blank" rel="noopener">相互確認シートに記録 ↗</a>'],'相手のチーム',['実際に操作する', '思ったことを声に出す']),section=6,target='section-6-1',note='10分：5分ずつ交代。5チームのうち1チームは講師が相手をする。')
slide('売り込まず、<mark>仕事を渡して見守る。</mark>',quote('この人は＿＿です。<br>いま、＿＿を<br>しようとしています。','操作手順は教えない。<br>迷った様子も観察する。<br>「何を探していましたか？」'),section=6,target='section-6-2',note='「便利ですよね？」ではなく問いを返す。操作が伝わらないことと、価値がないことは別。')
slide('操作の問題と、<mark>価値の仮説を分ける。</mark>',split('操作が伝わる？',['「ボタンを探して止まった」は観察', '配置や言葉を変えて、もう一度試す'],'仕事に役立つ？',['「現場で便利そう」は学生の意見', '実務への適合は仮説。実ユーザーに確かめる']),section=6,target='section-6-3',note='操作できなかった＝価値がない、ではない。どちらの話か分けて記録する。')
slide('見たことと、<mark>解釈を分ける。</mark>',table(['順番','ホテルの仮想例'],[['① 事実：見た・聞いた','「絞り込みはどこ？」と言い、一覧を上から探した'],['② 解釈：どう考えた','ボタンに気づいていないのでは？'],['③ 判断：どうする','CHANGE：ボタンを一覧の上へ移す'],['QUESTION：未確認','繁忙時にも入力してもらえるかは、実ユーザーに確認']]),section=6,target='section-6-4',note='学生同士の操作確認で、実際の職場の需要や継続利用を証明したことにはならない。')
slide('直すこと・直さないことを、<mark>決める。</mark>',exercise('3',[('観察とCHANGEの根拠を読み直す', 'なぜそう考えた？ 指摘をそのまま修正リストにしない'), ('小さな修正を1〜2件選ぶ', '残り時間で修正・再確認できる範囲にする'), ('直さない判断も残す', '理由と、次にどう確かめるかを書く')],'対応方針と理由'),section=7,target='section-7-1',note='修正と確認は次の7分。すべての指摘に対応する必要はない。')
slide('直したら、<mark>もう一度確かめる。</mark>',exercise('7',[('選んだ箇所を小さく直す', '直前の大きな作り替えは避ける'), ('同じ操作をもう一度試す', '修正は効いた？ 採用した他の条件を壊していない？'), ('最後の2分は通し確認', 'コードを変更せず、デモの流れを最初から最後まで')],'修正・再確認の結果と未確認事項'),section=7,target='section-7-2',note='直したことと、直さなかった理由は成果物テンプレート11へ。')
slide('資料を整え、<mark>デモを一度通す。</mark>',exercise('15',[('テンプレート10・11を更新', '10：実現・未実装・模擬範囲。11：観察・解釈・判断と対応'), ('構成図と実装を揃える', '成果物テンプレート9の図を更新。価値の概算も必要に応じて見直す'), ('開始画面・入力値・役を決める', '誰が操作し、誰が話す？ デモを一度、最後まで通す')],'発表資料とデモの準備'),section=8,target='section-8-1',note='共有リンクとAIへの判断に関わる指示も用意する。')
slide('発表は4分。<mark>動くものを中心に。</mark>',table(['話すこと','伝える内容'],[['① 対象','誰の、どの仕事を変える？'],['② デモと構成','主要な流れを動かし、仕組みを示す'],['③ 検証と変更','見たこと・解釈・判断。何を変えた？'],['④ 限界／⑤ 次の問い','未実装と理由。使い続けてもらうために何を確かめる？']]),section=9,target='section-9-1',note='35分：5チーム×発表4分・質疑2分＋入れ替え・講評5分。聞く側は価値・前提・次の検証を問う。')
slide('自分の判断を、<mark>自分の言葉に。</mark>',exercise('5',[('判断が変わったところ', '第6回の案から、つくってみて何が変わった？'), ('自分の貢献', 'どの作業・判断に関わった？'), ('次に確かめたいこと', 'QUESTIONのまま残っていることを一つ')],'全員個別の振り返り3点'),section=10,target='section-10',note='AIと対話して整理しても、最後は自分の判断として書く。')
slide('評価するのは、<mark>動作と判断のつながり。</mark>',table(['観点','説明できること'],[['つながる','課題 → 解決策 → 動くもの → 確かめたこと'],['通る・説明できる','主要な流れが動く。構成と技術を選んだ理由が言える'],['区別できる','見た事実・解釈・判断・未確認を分け、削った理由を残す'],['次がある','観察から、次に変えること・確かめることを言える']]),section=10,target='rubric',note='AC1が通るのは動作面の最低条件。機能数・見栄え・速さ・AIの利用量では評価しない。')
slide('成果物と、<mark>判断の記録を届ける。</mark>',table(['提出するもの','形式・中身'],[['チーム：成果物テンプレート1〜11','PDFまたは共有リンク。絞り込みシートも添付'],['チーム：プロジェクトZIPの共有リンク','ソース・specs・初期データ・起動手順のREADME.txt'],['チーム：AIとのやり取り','共有リンク、または判断に関わった部分の抜粋'],['全員個別：振り返り3点','判断の変化・自分の貢献・次に確かめたいこと']]),section=10,note='授業終了後3日以内に、Slackの第7回提出用スレッドへ。他の人が動かせる形で出す。',target='submission')
slide('授業のあとも、<mark>一歩進めて確かめる。</mark>',split('① どちらかを選ぶ｜約3時間',['未実装の機能を一つ、条件を追加して実装', 'または確認例を増やし、壊れた箇所と修正を記録'],'② 全員が取り組む｜約2時間',['QUESTIONを一つ選び、検証方法を設計', '誰に何を聞く？ 何を観察する？ 実施は必須ではない']),section=10,target='homework',note='条件を追加するときはspec.mdとconstitution.mdも更新し、制約を変えたことを残す。')
slide('つくった先に、<mark>次の問いがある。</mark>',split('今回確かめたこと',['動作・操作の理解・構成との一致', '観察したことと判断したことを区別'],'これから確かめること',['実際の仕事に合うか', '使い続けてもらえるか']),section=10,note='課題 → 解決策 → 設計 → 試作 → 確認 → 更新。最初の一周を、次へ。',target='homework')
# Render all slide markup.
# Explicit work instructions and destinations; numbers refer to the original 36 slides.
work_specs = {
4: ('準備を確認する','準備／導入中',('準備','手元の資料とIDEを確認する'),''),
6: ('中間発表の指摘を3つに分ける','5分',('テンプレート 11','QUESTION欄へ未確認の問いを書く'),'KEEP・CHANGEと理由はメモにも残す'),
7: ('操作する人と見る人を決める','5分',('口頭で決める','10分ごと、またはACが一つ通ったら交代する'),''),
8: ('①〜⑥を、自分たちの言葉で埋める','8分',('絞り込みシート','前半①〜⑥'),'原本を手元に開く'),
11: ('AIに整理させ、3点を確かめる','7分',('絞り込みシート','後半（原本）'),'要約をテンプレート8へ'),
12: ('使い続ける障害を、2行で書く','整理の7分に含む',('絞り込みシート','末尾の2行'),'テンプレート11のQUESTIONへ'),
13: ('要約を貼り、全文で仕様書をつくる','5分',('テンプレート 8','要件定義の要約を貼る'),'シート全文 → specs/内のspec.md'),
14: ('2案を比べて、1案を選ぶ','5分',('メモ','構成案と比較・選択の理由'),'技術選択の理由はテンプレート9へ'),
15: ('図を描かせ、AC1を指でたどる','5分',('テンプレート 9','構成図を貼る'),'編集できる.drawioファイルも保存'),
16: ('技術選択の理由を3行で書く','2分',('テンプレート 9','技術・選んだ理由・採らなかったもの'),''),
17: ('計画をつくり、読んでからタスクへ','約10分',('specs/','plan.md・tasks.md'),'開発50分の内訳の目安'),
18: ('AC1だけ実装させ、自分で動かす','約40分',('コード','シートの確認例で自分たちが動作確認'),'完成後、テンプレート10に共有情報'),
23: ('他チームが触れる状態にする','15分',('テンプレート 10','プロトタイプの共有情報'),'ローカル実行ならZIPの共有リンクと起動手順'),
24: ('相手に操作してもらい、記録する','10分',('相互確認シート','つくったチームが行動と言葉を記録'),'5分ずつ交代する'),
28: ('直す1〜2件と、直さない理由を決める','3分',('相互確認シート','下部：対応方針と理由'),'テンプレート11へ転記'),
29: ('直して、同じ操作をもう一度試す','7分',('テンプレート 11','修正・再確認の結果と直さなかった理由'),'最後の2分は変更せず、通し確認'),
30: ('テンプレートを埋め、デモを通す','15分',('テンプレート 10・11','実現・未実装・観察・判断・対応'),'構成図9とビジネス価値7も更新'),
32: ('3点を自分の言葉で書く','5分',('Slack 個人投稿','判断の変化・貢献・次の問い'),'テンプレートではなく、全員が個別に提出'),
}
questions=[('① 今回確かめたいこと','この試作で、何が分かれば一歩前に進む？'),('② 今回扱う場面','誰が、いつ、何をする場面だけをつくる？'),('③ 最後にできてほしいこと','操作が終わったとき、何が分かる・できる？'),('④ 小さくする方法','人・画面・データ・処理を、どう減らす？'),('⑤ 今回の線引き','実際につくる／代わりの方法で試す／今回は扱わない、のどれ？'),('⑥ 合格の確かめ方','何を操作して、どうなれば予定どおり？')]
slides[7]['content']=table(['考える欄','問い'],questions)
slides[11]['content']=sheet([('障害は？','この人が使い続けるうえで、いちばん気になる障害は？'),('次の確認は？','今回確かめられる範囲と、実ユーザーに確かめたいことは？')],'')
slides[15]['content']=work('技術選択の理由を3行で書く','2分',[('選んだ技術','何を使い、どう組み合わせる？'),('選んだ理由','採用した条件にどう合う？'),('採らなかったもの','何を採らず、なぜそう判断した？')],('テンプレート 9','選択理由'))
slides[8]['title']='④⑤で迷ったら、<mark>目的から決める。</mark>'
slides[26]['content']=slides[26]['content'].replace('順番','相互確認シートの1→2→3→4')
slides[1]['content']+='<div class="s7-goal-strip">今日埋める：成果物テンプレート <b>8 → 9 → 10 → 11</b></div>'
for original, destinations in [(3,['準備','テンプレート8','テンプレート9','コード → 10','シート・仕様書']), (22,['テンプレート10','相互確認シート','テンプレート11','テンプレート10・11','発表','Slack個人投稿','時間調整'])]:
    values=iter(destinations)
    slides[original-1]['content']=re.sub(r'</li>',lambda m:'<em class="s7-agenda-dest">'+next(values)+'</em></li>',slides[original-1]['content'])
for n,d in enumerate(slides,1):
    d['tag']='困ったら' if n in (19,20,21) else '説明'
    if n in work_specs:
        do,minutes,dest,also=work_specs[n]
        work(do, minutes, [('確認', '内容と記録先を確認する')], dest, also)
        d.update(do=do,minutes=minutes,dest=dest,also=also,tag='WORK')
        d['note']='採用する内容と理由は、チームで判断しよう。'
        # Existing exercise body is retained; the shared frame owns its clock and destination.
        d['content']=re.sub(r'<div class="s4-clock">.*?</div>','',d['content'],flags=re.S)
        d['content']=re.sub(r'<div class="s4-output">.*?</div>','',d['content'],flags=re.S)
    elif n==21:
        d.update(dest=('テンプレート 8・10','変更・未実装とその理由'),also='シート・spec・plan・tasksも揃える')
        d['note']='流れを残した簡略化で、確かめたい価値を守ろう。'
    elif n!=1:
        d['note']=''
# Keep the constraints explanation immediately before the acceptance-condition example.
constraints=slides.pop(4); slides.insert(8,constraints)
map_slide=dict(title='今日の<mark>成果物マップ。</mark>',content=table(['作業の記録（原本）','成果物テンプレートへ'],[['絞り込みシート 前半①〜⑥ → 後半AC','8：要件定義（要約）'],['構成2案を比較 → draw.ioの図・技術選択','9：構成図と選んだ理由'],['コード・共有情報・落とした機能','10：プロトタイプ・実現／未実装'],['相互確認シート → 対応・再確認','11：観察・解釈・判断・次の問い'],['specs/内のspec → plan → tasks','シート全文から生成。実装と一致させる']]),kind='',section=1,note='',eyebrow='LECTURE 07 / OUTPUT MAP',tag='説明',target='record-map')
slides.insert(2,map_slide)
header='<header class="identity"><div>KYOTO UNIVERSITY OF THE ARTS<br>Department of Information Design</div><span class="identity-line"></span><div>Solution Design with Technology<br>2026 Spring</div></header>'
footer='<footer class="identity-bottom">PEOPLE<br>TECHNOLOGY<br>IDEAS<br>FOR A BETTER TOMORROW.</footer>'
total=len(slides); sections=[]
for i,d in enumerate(slides,1):
    title=re.sub('<[^>]+>','',d['title']).replace('&','＆')
    content=d['content'] if d['kind'] in ('chapter','cover') else '<div class="s4-content">'+d['content']+'</div>'
    note='<div class="takeaway">'+d['note']+'</div>' if d['note'] else ''
    if d.get('tag') and d['kind']!='cover':
        content+='<span class="s7-tag">'+d['tag']+'</span>'
    if d.get('do'):
        content+='<div class="s7-do">やること：'+d['do']+'</div><div class="s7-time">'+d['minutes']+'</div>'
        content+='<div class="s7-progress">'+''.join('<span class="'+('active' if str(n) in (d['dest'][0]+d['also']) else '')+'">'+str(n)+'</span>' for n in (8,9,10,11))+'</div>'
    if d.get('dest'): content+=destination(d['dest'],d.get('also',''))

    target=d.get('target') or f'section-{d["section"]}'
    sections.append(f'<section class="slide s4 s4-{d["kind"]}{" s7-work" if d.get("do") else ""}" data-title="{esc(title,quote=True)}" aria-label="{i}：{esc(title,quote=True)}"'+(' hidden' if i>1 else '')+'>'+header+f'<div class="page-tag">{i:02d} / {total}</div><div class="eyebrow">{d["eyebrow"]}</div><h1>{d["title"]}</h1>'+content+note+footer+f'<div class="s4-foot"><span>LECTURE 07 · {"3限" if d["section"]<5 else "4限"}</span><a href="workbook.html#{target}" target="_blank" rel="noopener">資料・プロンプト ↗</a></div></section>')
nav=f'<nav aria-label="スライド操作"><button id="prev" aria-label="前のスライド">← 前へ</button><label><input id="page" type="number" min="1" max="{total}" value="1" aria-label="スライド番号"> / {total}</label><button id="next" aria-label="次のスライド">次へ →</button><button id="fullscreen">全画面</button><a href="workbook.html">資料</a><span class="help">← → / Space：移動 · F：全画面 · H：操作バー</span></nav>'
(ROOT/'index.html').write_text('<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第7回 ケーススタディ：ソリューショニングと成果発表</title><link rel="stylesheet" href="styles.css"></head><body><main id="stage" aria-label="第7回の講義スライド"><div id="deck">'+ '\n'.join(sections)+'</div></main>'+nav+'<span id="status" class="sr-only" aria-live="polite"></span><noscript>JavaScriptを有効にしてください。</noscript><script src="viewer.js"></script></body></html>')
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
        out.append('<div class="code"><button type="button" class="copy">コピー</button><pre>'+esc(code)+'</pre></div>')
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
        h=min(len(m[1])+1,4)
        n=re.match(r'^(\d+(?:\.\d+)?)(?:\.\s|\s)',m[2])
        special={'課題と評価':'assignment','提出物':'submission','到達の目安':'rubric','事後学習':'homework','参考':'references'}
        anchor='section-'+n[1].replace('.','-') if n else special.get(m[2])
        attr=f' id="{anchor}"' if anchor else ''
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
workcss+=' .course-diagram{margin:24px 0;padding:16px;background:#fff}.course-diagram svg{width:100%;height:auto;display:block}.course-diagram text{font-family:system-ui,sans-serif;fill:#151515}.course-diagram .node-title{font-size:27px;font-weight:900}.course-diagram .node-sub{font-size:21px}.course-diagram .edge-label{font-size:19px;paint-order:stroke;stroke:#f5f4ef;stroke-width:8px}.course-diagram .edge{fill:none;stroke:#151515;stroke-width:3}.course-diagram .node{stroke:#151515;stroke-width:2}h3,h4{scroll-margin-top:24px}'
script="""document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',async()=>{const t=b.nextElementSibling.textContent;try{await navigator.clipboard.writeText(t);b.textContent='コピーしました';}catch{const r=document.createRange();r.selectNodeContents(b.nextElementSibling);const s=window.getSelection();s.removeAllRanges();s.addRange(r);b.textContent='選択しました（Ctrl/Cmd+C）';}}));"""
(ROOT/'workbook.html').write_text('<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第7回 資料・コピー用プロンプト</title><style>'+workcss+'</style><body><header><h1>第7回 · 資料とプロンプト</h1><a href="index.html">スライドへ</a><p>プロンプトはボタンからコピーできます。講義本文から生成した資料です。</p></header>'+''.join(out)+'<script>'+script+'</script></body></html>')
(ROOT/'slide-map.md').write_text('# スライドと講義本文の対応\n\n| 枚 | タイトル | 本文の節 |\n| --- | --- | --- |\n'+''.join(f'| {i:02d} | {re.sub("<[^>]+>","",d["title"])} | {d["section"]} |\n' for i,d in enumerate(slides,1)))
print(f'Built {total} slides and workbook.html')
