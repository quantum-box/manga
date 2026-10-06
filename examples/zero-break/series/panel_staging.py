"""Panel-level staging for the existing fifty-episode plot; no new story events."""
import re

# Ordered quoted spans per episode. Signs/records are not assigned speech tails.
VOICES = {
 11:['ノア','レン'],12:['ノア','レン','監視者'],13:['住民','レン'],
 14:['ノア','管理局の使者'],15:['レン','レン','炎術士'],16:['依頼板','娘の父'],
 17:['ノア'],18:['ミラ','ルーク','記録の声'],19:['ルーク','署名'],
 20:['書名','アラタ'],21:[],22:['レン','ミラ'],23:['施設の通信'],24:['ミラ'],
 25:['王','ミラ'],26:['ノア','ミラ','レン'],27:['ミラ','記録のレン'],
 28:['地上の住民'],29:['アラタ'],30:['レン','レン','署名'],31:[],32:[],
 33:['アラタ'],34:['住人','レン'],35:['レン','アラタ'],36:[],
 37:['レン'],38:['初代核'],39:['レン','日誌'],40:['アラタ'],41:[],42:[],43:[],
 44:['レン','初代核'],45:['過去の願い'],46:[],47:['ノア'],48:['ミラ'],
 49:['レン'],50:['博物館の札','ミラ','レン','レン'],
}
PRINTED={'依頼板','署名','書名','日誌','過去の願い','博物館の札'}
NOTES = {
 11:'足場と救助網の上下関係を先に一度見せる。「三秒」は距離測定の後。未完成の脚部を完成フォームとして描かない。',
 12:'子供を一人抱いた状態を次の塔まで保つ。導線への接触と旋回を別コマへ。スプリント全身は青い足元の後に初公開。',
 13:'行き止まり、台車の幅、修理扉の位置を順に示す。出口を開く前に住民を安全側へ描かない。',
 14:'脚部の冷却と洪水現場へ移る間に道具と時間の接続を置く。三台の排水機は低出力が揃ってから動く。',
 15:'試合のルールと核の不発を説明してから延焼へ。炎術士の迷いを挟み、消火と搬送を役割ごとに見せる。',
 16:'消えたランキング欄と増えた依頼板は別の小コマ。娘が工房へ走る動線を置き、父の証言を救助前に出さない。',
 17:'門の入口と未知の出口を混同しない。空気・地面の測定、観測映像、希望の反応の順。地上へ人はまだ通さない。',
 18:'夢は同じ赤い布と手で接続し、事故の結末をまだ明かさない。現在の子供の救助はルークの行動として見せる。',
 19:'署名しかけた手で止め、救助記録を見る視線を挟む。家族の避難と公開証言の二地点は切替えの全景を置く。アラタの名は最後の原本で初めて読める。',
 20:'19話の署名から同じ名の伝記へ接続。破れた頁を小コマにし、燃える書庫の出口を先に示す。三百年の声は最後に置く。',
 21:'二つの診療所は外観と位置を区別。射線、受けた腕、床の亀裂を分ける。患者が無傷と分かるのは避難後。',
 22:'地上支点と冷却器を見せてから盾を拡大。ガーディアンの全身と盾を大きくし、直前は核と足元だけを見せる。',
 23:'貯水庫から盾の内側へ流れる水の方向を示す。ノアを覆う小盾と広場の薄い盾を別々に見せ、全域防御と誤解させない。',
 24:'去った車を現在の避難所に描かない。空の毛布で不在を見せる。報告と実際の名簿の違いを小コマで比較する。',
 25:'承認紙、父の返答、ミラの反応を分ける。少数と全員の違いを確認してから要求へ進め、返答を一画面に詰めない。',
 26:'王家の鍵を置いた前話から質素な寝床へ接続。作業着への衣服変更を飛ばさない。住民の布と道具を少人数ずつ見せる。',
 27:'18話と同じ横断歩道の断片を使う。ミラが手を離す間を置き、記録再生を先へ強制しない。子供の顔はまだ不鮮明。',
 28:'降下前、雲の中、地面への到着を分ける。谷の空気・水・畑を観察してから避難可能と判断する。',
 29:'模型の落下とミラの指を小コマで因果接続。通信中のアラタと現場のレンは場所を切替えて描く。一施設だけの移行を全都市成功にしない。',
 30:'横断歩道の足、引き返す手、子供を受け止める通行人、暗転を順番に見せる。泣くレンへの返答を急がず、ミラが座る無言の間を長く。',
 31:'投げられた石と投げ返さない手を分ける。外側のレンと院内の医師を位置で区別し、回復の確認前に支持へ転換しない。',
 32:'優先地図、各地の端子、中央のレンを順に紹介。接続音の後にリンクを初公開。病院→給水→避難所の復旧は別コマ。',
 33:'照合用の三資料は一つずつ見せる。本人の名と証言を先に確認。動けないレンと記録を運ぶルークの切替えに位置を置く。',
 34:'残り浮力と代替案は隣り合う小コマで比較。支持者の危険を見せてからレンが入る。会談場所は最後に導入する。',
 35:'白い中枢室の二人を一度示し、その後は声・表情・設計図へ寄る。地球の音を聞く反応の後に転生者と理解させる。',
 36:'二施設と共通支持塔の配置を先に見せる。隊の分担、詰まった搬送台、再始動、二つの名簿を順番に描く。',
 37:'装甲の色、名札、生存者の目を別々に見せる。全員死亡と先に結論しない。「戦わなくていい」の後に青年の反応を置く。',
 38:'外殻を開ける手から青い回路へ。1話の0と9話の軸は比較コマ。停止装置を引き抜く直前で止まり、複製作成へ接続する。',
 39:'一日の期限を確認した後に役割を分ける。変身を失ったレンは住民の台車で運ばれる。感謝の短い声に反応の間を置く。',
 40:'白い巨大装甲と街の支持構造を長い縦構図で紹介。「倒せば落ちる」を聞く反応から攻撃を止める手へ。ゲートはまだ試験段階。',
 41:'空の街の名簿、降下籠、地上の受入場所を別々に紹介。先行避難者の到着確認の後に次の列が動く。',
 42:'実験する工房と地上の受取地点を先に示す。失敗した砂袋と人の転送を同時に描かない。固定具・再試験・同行者の順。',
 43:'入口の避難列と出口の青い旗を分ける。受入確認まで扉を開かず、輪と背中の光の後にゲート全身を大きく見せる。',
 44:'現在の砲撃と三百年前の記録は入口を区別。笑顔が消える表情に間を置き、共感の台詞の後も現在の救助を続ける。',
 45:'核の説明をレンの反応と短い返答へ分ける。元の体が戻らない答えを曖昧にしない。管理鍵の切離しと残量低下は順番を守る。',
 46:'決闘の二人と残る避難列を先に示す。フォーム変更は残量確認を挟む。武器の破壊を敵の死亡として見せない。',
 47:'病院名と人数を小コマで一組ずつ追う。王の承認は過去の赦しに置換しない。輸送経路を繋いでから名簿を地上へ移す。',
 48:'ケーブル、発電機、区域切替えを作業者ごとの小コマへ。青い線が揃った後にユナイト。千人の確認後にアラタの孤立を明かす。',
 49:'アラタを渡してから無人都市を着地。装甲が解けるレンと救助網の上下を先に見せる。最後は互いを見つける目と握る手。',
 50:'数カ月後の新街を広い導入で示す。裁判と復旧の現場を短く区別。猫の救助は梯子と支える足元を先に見せ、最後の夕方は枠なしで長く閉じる。',
}

ACTORS=('レン','ミラ','ノア','ルーク','アラタ')
OBJECTS=('救助網','脚部','導線','台車','修理扉','排水機','看板','地図','座標','観測機','マフラー','原本','名簿','設計図','呼吸器','支点','冷却器','毛布','承認紙','鍵','布','図面','記録','発信機','模型','回路','端子','遮断弁','日誌','浮力','降下籠','固定具','旗','ケーブル','発電機','梯子','猫','手')
REVEALS={(12,4),(22,4),(32,4),(43,3),(48,3)}

def units(scene):
    """Keep narration around a quote together, without dangling speaker prefixes."""
    sentences=[];buf='';inside=False
    for char in scene:
        if char=='「':inside=True
        elif char=='」':inside=False
        if char=='。' and not inside:
            if buf.strip():sentences.append(buf.strip())
            buf=''
        else:buf+=char
    if buf.strip('。 '):sentences.append(buf.strip('。 '))
    out=[]
    for sentence in sentences:
        quotes=re.findall('「([^」]*)」',sentence)
        narration=re.sub('「[^」]*」','',sentence).strip('。 、')
        if quotes:
            narration=re.sub(r'と(?:言う|答える|告げる)$','',narration).strip(' 、')
        if narration and narration not in ACTORS and narration not in ('完','札は','署名が','初代核の警告','アラタの最後の一言','ミラの通信へ声','ノア','レンは泣きながら'):
            # A remaining clause must describe a visible action, not a name alone.
            if not quotes or len(narration)>5:out.append(('action',narration))
        out.extend(('quote',quote) for quote in quotes)
    return out

def fragments(text):
    # Only divide at punctuation, never silently rewrite or remove a glyph.
    parts=re.findall(r'[^。、]+[。、]?|[。、]',text)
    return parts if len(text)>16 and len(parts)>1 else [text]

def stage_episode(number,scenes):
    voices=iter(VOICES[number]);result=[];last_actor='レン'
    for index,scene in enumerate(scenes,1):
        panels=[]
        for kind,text in units(scene):
            if kind=='quote':
                voice=next(voices)
                printed=voice in PRINTED
                pieces=fragments(text)
                for j,piece in enumerate(pieces):
                    balloon='枠付きの資料内表示・尻尾なし' if printed else '通常の楕円・口へつながる尻尾'
                    if not printed and ('！' in text or '火を消せ' in text):balloon='太い輪郭の叫び・連続する尻尾'
                    elif not printed and ('怖' in text or '逃げた' in text):balloon='少し揺れる弱い声・連続する尻尾'
                    elif not printed and voice in ('アラタ','王','管理局の使者'):balloon='落ち着いた角丸・連続する尻尾'
                    elif not printed and voice=='ミラ':balloon='細い青灰の角丸・口へつながる尻尾'
                    elif not printed and voice=='ノア':balloon='柔らかい橙の輪郭・口へつながる尻尾'
                    panels.append(dict(beat=piece,focus=(voice+'の資料だけ' if printed else voice+'の顔と口だけ'),frame='幅90%・右寄せ・中縦コマ',pause=55,voice=balloon,line=dict(speaker=voice,text=piece,type='caption' if printed else 'speech')))
                    if j==0:
                        receivers=[a for a in ACTORS if a in scene and a!=voice]
                        target=receivers[-1]+'の目' if receivers else ('資料を読む目' if printed else '直前から話を聞いている相手の目')
                        panels.append(dict(beat='直前の言葉を受け止める。場所と時間を進めない。',focus=target,frame='幅62%・左寄せ・浅い無言コマ',pause=70,voice='無言'))
                continue
            if text in ('と言う','と答える','と言う住人へ、レン','完'):continue
            actors=sorted((a for a in ACTORS if a in text),key=text.index)
            subject=actors[0] if actors else last_actor
            objects=[o for o in OBJECTS if o in text and not (o=='手' and '相手' in text and text.count('手')==1)]
            focus=objects[0]+'の状態・操作する手だけ' if objects and len(text)<38 else subject+'の一つの動作'
            if actors:last_actor=subject
            opening=not panels
            reveal=(number,index) in REVEALS and any(x in text for x in ('初めて','フォーム','ガーディアン','ユナイト','巨大な青い盾'))
            frame='幅100%・低い横コマで位置を確認' if opening else '幅72%・左寄せ・手元の小コマ' if objects and len(text)<38 else '幅84%・右寄せ・中コマ'
            if reveal:frame='幅100%・枠なし・長い縦コマ。直前は部分だけ、ここで初めて全身を公開'
            if number==28 and index==1:frame='幅100%・雲を抜ける長い縦コマ・無言'
            if number==50 and index==6:frame='幅100%・枠なし・夕方の背中を長く見せる'
            panels.append(dict(beat=text,focus=(('場所と安全側・危険側の関係。'+focus) if opening and index==1 else focus),frame=frame,pause=100 if reveal else 70 if opening else 45,voice='無言'))
        result.append(dict(scene=index,context=scene,panels=panels))
    try:next(voices)
    except StopIteration:pass
    else:raise ValueError('Unused voice assignment')
    return result
