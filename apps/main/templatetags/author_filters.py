from django import template

register = template.Library()

@register.filter
def author_names_only(authors_string):
    """
    Extracts only the names before the first ' - ' in each line of the authors string.
    """
    lines = authors_string.strip().splitlines()
    names = [line.split(' - ')[0].strip() for line in lines if ' - ' in line]
    return ', '.join(names)

@register.filter
def bold_names_with_designation(authors_string):
    """
    Bolds the name (before the dash) and appends the designation after it.
    Each line becomes its own <p> element.
    """
    if not authors_string:
        return ""

    lines = authors_string.strip().splitlines()
    formatted = ''
    for line in lines:
        if ' - ' in line:
            name, designation = line.split(' - ', 1)
            formatted += f"<p><strong>{name.strip()}</strong> – {designation.strip()}</p>"
        else:
            formatted += f"<p>{line.strip()}</p>"
    return formatted
