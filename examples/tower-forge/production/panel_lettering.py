"""Keep dialogue, display text and sound effects independent in art prompts."""

def normalize_panel(panel):
    panel=dict(panel)
    panel['sounds']=[dict(x) for x in panel.get('sounds',[])]
    panel['ui']=[dict(x,lines=list(x['lines'])) for x in panel.get('ui',[])]
    if panel.get('voice')=='効果音':
        if not panel['sounds']:
            panel['sounds']=[dict(text=panel['text'],cause=panel['art'],placement='動作の発生源の近く。顔・手・接触点を避ける',design='素材と重さに合う描き文字。会話の吹き出しと尾は付けない')]
        panel.update(speaker='',text='',columns=[],voice='発話なし')
    return panel

def make_panel(art,speaker='',text='',columns=None,voice='普通の声',sounds=None,quiet_reason='',ui=None):
    return normalize_panel(dict(art=art,speaker=speaker,text=text,columns=columns or ([text] if text else []),voice=voice,sounds=sounds or [],quiet_reason=quiet_reason,ui=ui or []))

def render_panel_lettering(panel):
    panel=normalize_panel(panel)
    lines=[]
    if panel['text']:
        if panel['voice']=='画面の横書き':
            lines.append(f"In-world display only, not speech. EXACT text: {panel['text']}. Horizontal lettering; no balloon or tail.")
        else:
            lines.append(f"Dialogue/thought only, speaker {panel['speaker']}, voice {panel['voice']}. EXACT text: {panel['text']}. Vertical columns RIGHT to LEFT: {' / '.join(panel['columns'])}.")
    else:
        lines.append('Dialogue: none. No speech or thought balloons. This does not prohibit separately specified interface text or sound effects.')
    for window in panel['ui']:
        lines.append(f"Player interface, visible to {window['owner']} in their own view. Action: {window['action']}. Placement: {window['placement']}. EXACT horizontal rows top to bottom: {' | '.join(window['lines'])}. Restrained translucent dark navy field, thin cyan borders, softly glowing white/cyan Japanese gothic, generous spacing. No gold ornament, no balloon or tail; do not cover face, hands, blade or vent. These interface rows are independent of dialogue and sound effects.")
    for sound in panel['sounds']:
        lines.append(f"Sound effect EXACT text: {sound['text']}. Cause: {sound['cause']}. Placement: {sound['placement']}. Drawn lettering: {sound['design']}. Outside every speech/thought balloon, no tail. Orientation follows the action, independently of vertical dialogue.")
    for sound in panel.get('sound_continuations',[]):
        lines.append(f"Continuing sound from moment {sound['origin']}: {sound['text']}. {sound['placement']} This is the SAME inscription crossing the panel boundary and gutter, not a new sound or a duplicate complete word. Keep it outside balloons and off faces, hands and dialogue.")
    if not panel['sounds'] and not panel.get('sound_continuations'):
        lines.append('Sound effects: none. '+(panel.get('quiet_reason') or 'Keep this beat focused on the stated perception, dialogue or reaction.'))
    lines.append('No unlisted words or sound effects.')
    return '\n'.join(lines)+'\n'

def panel_board(panel):
    panel=normalize_panel(panel)
    lines=[f"   - 発話：{panel['speaker'] or 'なし'}。全文：{panel['text'] or 'なし'}。声：{panel['voice']}。縦列（右→左）：{' / '.join(panel['columns']) or 'なし'}。"]
    for window in panel['ui']:
        lines.append(f"   - HUD：{window['owner']}本人の視界。操作：{window['action']}。横書きの行（上→下）：{' / '.join(window['lines'])}。位置：{window['placement']}。セリフ・効果音と別指定。")
    if panel['sounds']:
        for sound in panel['sounds']:
            lines.append(f"   - 効果音：{sound['text']}。原因：{sound['cause']}。位置：{sound['placement']}。字形：{sound['design']}。会話の吹き出しへ入れない。")
    elif not panel.get('sound_continuations'):
        lines.append('   - 効果音：なし。'+(panel.get('quiet_reason') or '今回の知覚・会話・感情を優先する。'))
    for sound in panel.get('sound_continuations',[]):
        lines.append(f"   - 継続する効果音：{sound['text']}。開始：{sound['origin']}。位置：{sound['placement']}。同じ一つの音がコマと余白を跨ぐ。新しい音・全文の重複ではない。")
    return '\n'.join(lines)+'\n'
