"""Describe the story separately from artwork generation instructions."""


def narrative_alt_text(description, panels):
    if not isinstance(description, str) or not description.strip():
        raise ValueError("A reader-facing narrative description is required")
    dialogue = []
    for panel in panels:
        for line in panel['lines']:
            speaker = {'HUD': '画面', '音': '音'}.get(line['speaker'], line['speaker'])
            dialogue.append(speaker + '「' + line['text'] + '」')
    return description.strip() + ('　' + ' / '.join(dialogue) if dialogue else '')
