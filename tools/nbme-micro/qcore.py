def Q(tag, topic, stem, opts, expl, img=None, difficulty="medium", why=None, table=None,
      fig=None, steps=None):
    """opts[0] is the correct answer.
    why: reasons each distractor is wrong — either a list aligned with opts[1:],
         or a dict {unique prefix of distractor text: reason}.
    table: a dict(title, cols, rows[, highlight]) or a list of them.
    fig: a teaching figure for the explanation - F(file, caption) or a list of them.
    steps: a list of strings walking through the process shown."""
    images = [img] if isinstance(img, str) else (img or [])
    tables = [table] if isinstance(table, dict) else (table or [])
    figs = [fig] if isinstance(fig, dict) else (fig or [])
    return dict(tag=tag, topic=topic, stem=stem, opts=opts, expl=expl, images=images,
                difficulty=difficulty, why=why, tables=tables, figs=figs, steps=list(steps or []))

def T(title, cols, rows, highlight=None):
    return dict(title=title, cols=cols, rows=rows, highlight=highlight or [])

def F(file, caption):
    """A figure shown with the explanation. `file` lives in assets/images/nbme/micro/."""
    return dict(file=file, caption=caption)
