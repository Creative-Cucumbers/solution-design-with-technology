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
    add(title,content,kind,section,note,eyebrow='LECTURE 06 / '+('RESEARCH & DEFINE' if section<7 else 'IDEATE & SHARE'))
    if target: slides[-1]['target']=target
slide('現実に向き合い、<br><mark>考え抜き、形にする。</mark>',
    '<div class="cover-sub">ユーザーの仕事を知り、<br>使い続けてもらえるソリューションを考え抜く。<br><br><span style="font-size:23px;font-weight:500">第6回 ／ ケーススタディ：デザインと演習問題</span></div><div class="research-board"><svg viewBox="0 0 90 500" aria-hidden="true"><path d="M70 30 Q0 100 60 210 M45 190 L60 210 L72 185 M65 255 Q0 330 65 415 M48 401 L65 415 L74 393" fill="none" stroke="#222" stroke-width="4"/></svg><div class="scrap">RESEARCH<b>誰の、どんな仕事？</b>資料を開く。根拠を残す。</div><div class="scrap">DEFINE<b>何に困っている？</b>分かったこと／まだ仮説。</div><div class="scrap">IDEATE<b>どう変えられる？</b>使い続けてもらえる？</div></div>',kind='cover',target='section-1-4')
route_names=[('ソリューション<br>基礎','考え方'),('開発方法論と<br>アジャイル','進め方'),('ユーザー中心の<br>デザイン','誰のため？'),('ソリューション<br>設計と試作','どうつなぐ？'),('対話と問いで<br>価値を考える','何が大切？'),('ケーススタディ<br>デザインと演習','調べる・考える'),('ケーススタディ<br>実装と発表','つくる・確かめる')]
road='<p class="roadmap-lead">これまでの学びを、チームで一つの提案へ。<br>第6・7回の400分で、調べる・考える・つくる。</p><aside class="roadmap-note">今日は第6回。<br>仮説を、理由と一緒に。</aside><div class="route-line"></div>'
for n,(name,desc) in enumerate(route_names,1):
    road+=f'<article class="route r{n}">'+('<span class="you-are">TODAY ↓</span>' if n==6 else '')+f'<b>0{n}</b><h3>{name}</h3><span class="hand">{desc}</span></article>'
slide('これまでを、<mark>自分たちの判断に。</mark>',road,kind='roadmap',target='section-1-1')
slide('今日は、<mark>理由を持って一案へ。</mark>',split('3限：対象と課題を定める',['第3・5回：ユーザーを理解する','事実・仮説・未確認を分ける','誰の、どの課題かを一つに絞る'],'4限：解決策を決める',['複数の案を同じ基準で比べる','仕事の流れに合い、使い続けられるか','要件・アーキテクチャ・試作は第7回へ']),note='ペルソナ＝仮説を含むユーザー像。新しい用語より、学んだ考え方を使おう。',target='section-1-2')
slide('今日の200分を、<mark>一本の資料に。</mark>',split('3限：調べる・絞る',['導入10 → テーマ10 → 調査25分','ペルソナ20 → 課題20 → 確認5分','予備10分：調査か課題検討へ'],'4限：比べる・伝える',['案出し15 → 比較20 → ラフ15分','準備10 → 中間発表30分','予備10分：案の比較などへ']),note='11名→5チーム（2名×4・3名×1）。テンプレートを複製し、表紙にチーム名・全員の氏名と学籍番号。',target='section-1-5')
themes=[('01 大学職員','教務・学生支援','申請／問い合わせ／日程調整'),('02 医療従事者','看護師・薬剤師・医療事務','記録／引き継ぎ／予約'),('03 宿泊施設','フロント・清掃担当','部屋の状態共有／依頼対応'),('04 小売業','店長・販売員・バイヤー','在庫／発注／接客準備'),('05 製造業','設計・生産管理・品質管理','検索／工程調整／不具合共有'),('06 物流','倉庫・配車・配送管理','入出荷／配送計画／遅延対応'),('07 自治体職員','窓口・施設管理・観光振興','申請／住民への案内／施設管理'),('08 クリエイティブ制作','制作進行・ディレクター','素材／修正・承認／見積もり'),('09 建設・設備管理','現場監督・点検員・保守担当','進捗／点検記録／修理手配'),('10 農業','作業リーダー・出荷担当','作業計画／人員配置／出荷')]
slide('どの仕事を、<mark>見てみたい？ ①</mark>',table(['テーマ','職種の例','探索する場面'],themes[:5],True),2,note='テーマ5：第3回の「金属加工工場の生産管理担当」と同じ人物・課題をそのまま使わない。')
slide('どの仕事を、<mark>見てみたい？ ②</mark>',table(['テーマ','職種の例','探索する場面'],themes[5:],True),2,note='技術が何を肩代わりできるだろう？ まずは対象の仕事を知るところから。')
slide('テーマを選び、<mark>場面を一つに。</mark>',exercise('10',[('チームで第1〜第3希望｜まず2分','Slackへチーム名＋第1希望の番号・テーマ名。投稿時刻順に確定'),('重複したら、次の希望を投稿','1チーム1テーマ。決まったら、職種と場面を一つに絞る'),('対象と選んだ理由を書く','例：ホテル全般 → フロントがチェックイン前に清掃状況を確認する場面')],'成果物テンプレートのスライド3：背景と目的'),2,note='調べる手がかりがあり、次回に主要な体験を動かせる範囲か。迷ったら講師へ。')
slide('AIには、<mark>読むべき資料を探させる。</mark>',timeline([('FIND','資料を探す','求人票・業務紹介・業界資料'),('OPEN','自分で読む','URLを開き、本文を確認'),('RECORD','根拠を残す','確認した記述＋出典URL')]),3,note='AIの回答だけではFACTにならない。資料で確認できる範囲と、自分たちの推測を分ける。')
slide('事実・仮説・未確認を、<mark>分ける。</mark>',table(['言葉と意味','記入のしかた'],[['FACT：確認できた事実','読んだ資料の記述＋実際に開いた出典URL'],['ASSUMPTION：補った仮説','「清掃完了は内線で伝わるのでは？」〔仮想例〕'],['QUESTION：まだ分からないこと','「1日に何回、部屋の状態を確認する？」〔仮想例〕']]),3,note='資料が示す職場・条件を超えて一般化しない。QUESTIONの数ではなく、区別と次の確認が大切。')
slide('調査｜<mark>一件は、自分で開いて読む。</mark>',exercise('25',[('AIに資料を探させる｜5分','対象の職種・場面を伝える。求人票や公開資料のURLを探す'),('URLを開き、本文を確認｜10分','最低1件は読む。何が書かれ、どこまで言えるかを確認'),('根拠・仮説・未確認を整理｜10分','FACTにはURL。推測はASSUMPTION、分からない点はQUESTION')],'成果物テンプレートのスライド4：ユーザリサーチ'),3,note='公開情報で分かる一般的な業務と、特定の現場の実態は同じではない。限界も残そう。')
slide('ペルソナは、<mark>考えるための仮説。</mark>',table(['5項目','ホテルのフロント担当・田中さん〔すべて仮想例〕'],[['属性・役割：どんな人？','34歳、60室のホテルで予約・受付を担当〔仮説〕'],['行動：どう働く？','予約管理システムと内線を行き来する〔仮説〕'],['思考：何を考える？','早く着いた客を待たせたくない〔仮説〕'],['目的・Need：何を達成したい？','聞かずに、いま入れる部屋を知りたい〔仮説〕'],['困りごと・制約：何が阻む？','繁忙時に連絡がつながらないのか？〔未確認〕']],True),4,note='年齢や客室数も仮の設定。自分たちの成果物では、確認した記述だけに出典付きFACTを付ける。')
slide('ペルソナ｜<mark>調べたことから人物像へ。</mark>',exercise('20',[('調査から、5項目を書き出す','属性・役割／行動／思考／目的・Need／困りごと・制約'),('各項目の根拠を確かめる','FACT・ASSUMPTION・QUESTIONを付ける。混ざる文は分ける'),('チームで一人の姿を説明する','どんな場面で、何をしたい人？ 分からない点も一緒に残す')],'成果物テンプレートのスライド5：ペルソナ'),4,note='人物紹介を埋めることが目的ではない。何を根拠に、その人の仕事を考えるか。')
slide('「したい」を、<mark>何が邪魔している？</mark>',split('INSIGHT：背景にある思いの解釈',['田中さんは本当は、聞かなくても','いま入れる部屋が分かる状態でいたい','目的・Needから考える'],'PROBLEM：解くべき課題の仮説',['しかし、清掃完了が内線でしか伝わらず','繁忙時に確認が滞るため、難しい','この障害は本当にある？ 根拠は？']),5,note='ホテルの説明用の仮説。Data＝事実、Insight＝解釈、Problem＝仮説を区別する。')
slide('課題設定｜<mark>3つ以上から、一つへ。</mark>',exercise('20',[('課題の候補を3つ以上出す','AIも使える。最初の候補をそのまま採用せず、並べて見る'),('この人に大切な課題を一つ選ぶ','何をしたい人か、その障害は何か。選ばなかった候補も残す'),('Problem Hypothesis：課題の仮説を一文に','「私たちは＿＿というProblemを解く。なぜなら＿＿」')],'成果物テンプレートのスライド6：課題と根拠'),5,note='既存の解決方法も確認する。大きな製品を作り直すより、対象場面を絞ろう。')
slide('チェックイン｜<mark>誰の、何を変えたい？</mark>',exercise('5',[('5チーム、各1分で共有','対象の人を一言で → 着目した課題を説明する'),('作成中の資料を見せる','専用資料は不要。困っている点も講師へ伝える'),('3限の到達を確認','テンプレート3〜6。URL付きFACT・ペルソナ・一つの課題がつながるか')],'講師と共有した進捗・次に進めること'),6,note='予備10分は調査か課題検討へ。押したら、項目を埋めきるよりURL付きFACTを1件残す。')
slide('ここからは、<mark>解決策を選ぶ。</mark>',timeline([('IDEATE','案を広げる','15分：個人→チーム＋AI'),('CHOOSE','比べて決める','20分：理由を残す'),('SKETCH','利用の流れ','15分：一本を描く'),('SHARE','中間発表','準備10分＋発表30分')]),7,note='4限100分（予備10分を含む）。思いついた案を、ペルソナと課題に照らして考える。')
slide('案出し｜<mark>最初の5分は、自分で。</mark>',exercise('15',[('個人で書く｜5分・NO AI','全員が書く。1アイデア＝1枚。文字でも絵でも。まずは数を出す'),('共有し、AIで広げる｜残り10分','USER・PROBLEM・USER VALUEと自分たちの案を渡す'),('案を並べる','別の方向性は？ 技術が何を肩代わりする？ 自分たちの案と比べる')],'次に比較する複数の解決策案'),7,note='発散では実現可能性を急いで判定しない。AIへのプロンプト全文は右下の資料へ。')
slide('好き嫌いではなく、<mark>この人への価値で。</mark>',cards([('User Value','ユーザーへの価値<br>この人の仕事は、<br>どう良くなる？','yellow'),('Originality','体験の新しさ<br>これまでと違う、<br>嬉しい体験は？','blue'),('Feasibility','実現の見通し<br>どうすれば実現できる？<br>次回、どこまで作れる？','pink')]),8,note='同じ基準で複数案を比べる。多数決だけで決めず、ペルソナを根拠に話そう。')
slide('比較・選択｜<mark>一案と、その理由を。</mark>',exercise('20',[('複数案を3つの基準で比較','User Value・Originality・Feasibility。案ごとの良さと負担を残す'),('一案を選び、理由を話し合う','このUSERには何が大切？ 選ばなかった案の理由も書く'),('Solution Hypothesis：解決策の仮説を書く','「このUSERが＿＿できるように、＿＿を試したい。なぜなら＿＿」')],'成果物テンプレートのスライド7：案の比較・選択理由'),8,note='20分で終わらなければ予備10分を活用。結論だけでなく、どう判断したかを残す。')
slide('価値を、<mark>前提付きの数字にも。</mark>',split('一人・一店舗・一社で考える',['誰が使い、誰が予算を出す？','現在のやり方と比べ、何が変わる？','必須ではない。未検討でもよい'],'仮定で計算してみる',['1日20分 × 月20日＝月約6.7時間','時給1,500円と仮定 → 約1万円相当','作業時間の換算。価格や現金削減ではない']),8,note='数字には出典か仮定を必ず書く。今回は事業計画や市場規模の予測を求めません。',target='section-8-3')
slide('全部ではなく、<mark>主要な流れを一本。</mark>',timeline([('01','清掃担当が操作','「502号室 清掃完了」を押す'),('02','状態が伝わる','フロントの表示が完了へ'),('03','田中さんが確認','入れる部屋を見て案内する')]),9,note='仮想例。表示は色だけでなく「清掃完了」の文字も。誰が何をして、次にどう変わるかを描こう。')
slide('ラフ作成｜<mark>使う場面を見える形に。</mark>',exercise('15',[('主要な利用の流れを一本選ぶ','誰が、何を始めて、どんな結果にたどり着くか'),('画面のラフか、操作の順番を描く','紙でも図でもよい。操作する人と、変化する内容を示す'),('チームでたどってみる','選んだ課題につながるか。次回に動かす範囲は広すぎないか')],'発表資料に追加するラフ1枚'),9,note='テンプレートの必須枠とは別に1枚追加。次回の開発は75分。きれいさより、流れが伝わること。')
slide('発表準備｜<mark>根拠から案へ、つながる？</mark>',table(['10分で確認','成果物テンプレート・追加資料'],[['出典を示せる','スライド4：URL付きFACTが1件以上'],['仮説と区別できる','スライド5：各項目にFACT／ASSUMPTION／QUESTION'],['課題を絞れている','スライド6：一つの課題と「なぜなら」'],['選んだ理由を説明できる','スライド7：複数案の比較とUser Value'],['使う場面を伝えられる','追加のラフ1枚：主要な流れが一本']],True),10,note='テンプレート3〜7を整え、ラフを追加。新しく発表専用の資料を作る必要はありません。')
slide('中間発表｜<mark>課題と選択理由を中心に。</mark>',split('発表3分：ここを伝える',['対象の職種と場面・ペルソナ','課題と根拠 → 案の比較と選択理由','利用の流れ。価値の概算は書けた範囲で'],'全体30分の進め方',['5チーム × 5分（発表3＋質疑2）','入れ替え・講評で5分','③課題と根拠、④比較と理由に時間を使う']),11,note='全項目を同じ長さで読まない。何を調べ、どう考え、この一案になったのか。')
slide('感想より、<mark>次につながる問いを。</mark>',table(['聞く側の問い','確かめたいこと'],[['User Valueは？','この解決策で、仕事や行動はどう良くなる？'],['Assumptionは？','まだ確かめていない前提は何？'],['何を確かめたい？','次に聞くこと・試すことは何？']]),11,note='受けた指摘はそのまま修正リストにしない。理由を考え、変えるかどうかをチームで決める。',target='section-11-2')
slide('提出｜<mark>判断のつながりを残す。</mark>',table(['チームで提出するもの','内容'],[['成果物テンプレート1〜7','PDFまたは共有リンク。表紙・背景・調査・人物像・課題・案'],['調査と選択の根拠','スライド4：事実／仮説／未確認。スライド7：比較と選択理由'],['追加のラフ1枚','主要な利用の流れを一本にした図']]),11,note='第7回の前日までに、Slackの第6回提出用スレッドへ。個人の投稿も全員が行います。',target='submission')
slide('個人の振り返り｜<mark>自分の判断を言葉に。</mark>',sheet([('担当した部分','チームの中で何をやったか'),('判断と根拠','何を選び、何を根拠にしたか'),('次に確かめたいこと','QUESTIONのままのことを一つ')],'各2〜3行。<br>全員が個別に<br>Slackへ投稿。'),11,note='チームの結論と違う考えも、理由と一緒に書いてよい。AIの文章をそのまま貼るだけにしない。',target='submission')
slide('到達の目安は、<mark>この3つ。</mark>',cards([('絞れている','どの職種の、どの場面？<br>課題が一つに<br>決まっている。','blue'),('区別できている','確認できた事実、<br>補った仮説、未確認が<br>分かれている。','yellow'),('説明できる','同じ基準で案を比べ、<br>この一案にした理由を<br>ユーザーから説明できる。','pink')]),11,note='資料の枚数・見栄え・AIの利用量では評価しない。QUESTIONが残っていることは減点ではない。',target='rubric')
slide('次回は、<mark>一本の体験を動かす。</mark>',split('事後学習：範囲と判断を整える',['約2時間：何を動かすか・優先順位を決める','約1時間：受けた問いへの対応を考える','変えないことにも、その理由を残す'],'第7回：つくる・確かめる',['要件定義 → アーキテクチャ → 実装','受け入れ条件で動作を確認 → 最終発表','開発75分。授業内で到達できる範囲にする']),11,note='全機能ではなく、主要な流れ一本。第2回の受け入れ条件と、第4回の設計を使います。',target='homework')
slide('その人の仕事は、<mark>どう変わる？</mark>',quote('調べたことから課題へ。<br>課題から、解決策へ。<br>その筋を、自分たちで。','資料を開く ↗<br><a href="workbook.html">資料・プロンプト</a><br><a href="../template-review/index.html">成果物テンプレート</a><br><br>次回、動くもので<br>確かめよう。'),11,note='同じテンプレートを第7回まで育てる。仮説は、確かめた結果から更新していい。',target='references')
assert len(slides)==30

# Render all slide markup.
header='<header class="identity"><div>KYOTO UNIVERSITY OF THE ARTS<br>Department of Information Design</div><span class="identity-line"></span><div>Solution Design with Technology<br>2026 Spring</div></header>'
footer='<footer class="identity-bottom">PEOPLE<br>TECHNOLOGY<br>IDEAS<br>FOR A BETTER TOMORROW.</footer>'
total=len(slides); sections=[]
for i,d in enumerate(slides,1):
    title=re.sub('<[^>]+>','',d['title']).replace('&','＆')
    content=d['content'] if d['kind'] in ('chapter','cover') else '<div class="s4-content">'+d['content']+'</div>'
    note='<div class="takeaway">'+d['note']+'</div>' if d['note'] else ''
    target=d.get('target') or f'section-{d["section"]}'
    sections.append(f'<section class="slide s4 s4-{d["kind"]}" data-title="{esc(title,quote=True)}" aria-label="{i}：{esc(title,quote=True)}"'+(' hidden' if i>1 else '')+'>'+header+f'<div class="page-tag">{i:02d} / {total}</div><div class="eyebrow">{d["eyebrow"]}</div><h1>{d["title"]}</h1>'+content+note+footer+f'<div class="s4-foot"><span>LECTURE 06 · {"3限" if d["section"]<7 else "4限"}</span><a href="workbook.html#{target}" target="_blank" rel="noopener">資料・プロンプト ↗</a></div></section>')
nav=f'<nav aria-label="スライド操作"><button id="prev" aria-label="前のスライド">← 前へ</button><label><input id="page" type="number" min="1" max="{total}" value="1" aria-label="スライド番号"> / {total}</label><button id="next" aria-label="次のスライド">次へ →</button><button id="fullscreen">全画面</button><a href="review.html">一覧</a><span class="help">← → / Space：移動 · F：全画面 · H：操作バー</span></nav>'
(ROOT/'index.html').write_text('<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第6回 ケーススタディ：デザインと演習問題</title><link rel="stylesheet" href="styles.css"></head><body><main id="stage" aria-label="第6回の講義スライド"><div id="deck">'+ '\n'.join(sections)+'</div></main>'+nav+'<span id="status" class="sr-only" aria-live="polite"></span><noscript><a href="review.html">画像一覧を開く</a></noscript><script src="viewer.js"></script></body></html>')
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
(ROOT/'workbook.html').write_text('<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第6回 資料・コピー用プロンプト</title><style>'+workcss+'</style><body><header><h1>第6回 · 資料とプロンプト</h1><a href="index.html">スライドへ</a> ／ <a href="review.html">一覧へ</a><p>プロンプトはボタンからコピーできます。講義本文から生成した資料です。</p></header>'+''.join(out)+'<script>'+script+'</script></body></html>')
(ROOT/'slide-map.md').write_text('# スライドと講義本文の対応\n\n| 枚 | タイトル | 本文の節 |\n| --- | --- | --- |\n'+''.join(f'| {i:02d} | {re.sub("<[^>]+>","",d["title"])} | {d["section"]} |\n' for i,d in enumerate(slides,1)))
print(f'Built {total} slides and workbook.html')
