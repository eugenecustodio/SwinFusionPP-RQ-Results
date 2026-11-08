"""Replace a whole B('...') paragraph call (located by its opening words) with new text, in a content file."""
import re
def wrap(text, indent='               '):
    words, lines, cur = text.split(' '), [], ''
    for w in words:
        if len(cur) + len(w) + 1 > 104:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return ("'" + (" '\n" + indent + "'").join(l.replace("'", "’") for l in lines) + "'")
def replace_par(src, start, new_text, extra=''):
    i = src.index("x.append(B('" + start)
    assert src.count("x.append(B('" + start) == 1, start
    j = src.index("))", i)
    # the call may contain '))' only at its end; check we end at a line end
    tail = src[j:j+3]
    assert tail.startswith("))"), tail
    return src[:i] + "x.append(B(" + wrap(new_text) + extra + "))" + src[j+2:]
