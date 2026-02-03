from django import template

register = template.Library()

@register.filter
def split_references(value):
    """
    Splits references based on newlines and wraps each in a <li> tag.
    """
    if not value:
        return ""
    lines = value.strip().splitlines()
    items = ''.join(f'<li>{line.strip()}</li>' for line in lines if line.strip())
    return f'<ul>{items}</ul>'
