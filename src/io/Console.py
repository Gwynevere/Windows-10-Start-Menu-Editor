from sty import fg, bg, ef, rs
from sty import Style, RgbFg


def out(text, text_color=None, builder=False):
    if text_color is None:
        text_color = (255, 255, 255)

    colored_text = get_colored_fg(text, text_color)

    if builder:
        return colored_text

    print(colored_text, sep='\n')


def out_bg(text, text_color, bg_color=None, builder=False):
    if bg_color is None:
        if sum(list(text_color)) <= 125:
            bg_color = (255, 255, 255)
        else:
            bg_color = (text_color[2], text_color[1], text_color[0])

    background_colored_text = get_colored_bg(text, text_color, bg_color)

    if builder:
        return background_colored_text

    print(background_colored_text, sep='\n')


def out_multi(sequences=None, builder=False):
    if sequences is None:
        sequences = ['']

    full_text = ' '.join(sequences)

    if builder:
        return full_text

    print(full_text)


def get_colored_fg(text, fg_color):
    fg.text_color = Style(RgbFg(fg_color[0], fg_color[1], fg_color[2]))
    return fg.text_color + text + fg.rs


def get_colored_bg(text, fg_color, bg_color):
    fg.text_color = Style(RgbFg(fg_color[0], fg_color[1], fg_color[2]))
    colored_text = fg.text_color + text + fg.rs

    return bg(bg_color[0], bg_color[1], bg_color[2]) + colored_text + rs.bg
