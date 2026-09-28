def Q(tag, topic, stem, opts, expl, img=None, difficulty="medium", why=None, table=None):
    """opts[0] is the correct answer.
    why: reasons each distractor is wrong — either a list aligned with opts[1:],
         or a dict {unique prefix of distractor text: reason}.
    table: a dict(title, cols, rows[, highlight]) or a list of them."""
    images = [img] if isinstance(img, str) else (img or [])
    tables = [table] if isinstance(table, dict) else (table or [])
    return dict(tag=tag, topic=topic, stem=stem, opts=opts, expl=expl, images=images,
                difficulty=difficulty, why=why, tables=tables)

def T(title, cols, rows, highlight=None):
    return dict(title=title, cols=cols, rows=rows, highlight=highlight or [])
