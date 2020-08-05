def shorten_text(text, length):
    short_text = text
    if len(short_text) > length:
        short_text = short_text[:length + 1]
        cut_index = max(short_text.rfind(' '), short_text.rfind('\n'))
        if cut_index != -1:
            short_text = short_text[:cut_index]
        short_text += '...'
    return short_text
