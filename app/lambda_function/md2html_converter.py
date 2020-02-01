import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'packages'))
import codecs

import markdown

import html_template


MD_EXTENSION = 'gfm'
CSS_FILE = 'github.css'

def convert(original_md):
    sanitized_md, page_title = sanitize(original_md)
    html_body = md2html(sanitized_md)
    html = merge_html_css(page_title, html_body)

    byte_html = html.encode('utf-8')
    return byte_html.decode('utf-8')


def sanitize(original_md):
    sanitized_md = []

    rows = original_md.split('\n')
    for i, row in enumerate(rows):
        if '```' not in row:
            sanitized_md.extend([ row ])
            continue

        sanitized_md.extend(separate_option(row))

    page_title = rows[1][7:]

    return '\n'.join(sanitized_md), page_title


def separate_option(row):
    row.strip()
    option = row.split('```')[1]
    if option == '':
        return ['```', '\n']
    else:
        file_name = None
        language = None

        options = option.split(':')
        if len(options) == 1:
            if '.' in options[0]:
                file_name = options[0]
            else:
                language = options[0]

        elif len(options) == 2:
            language = options[0]
            file_name = options[1]

        ex_option = []
        if file_name is not None:
            ex_option.append(f'**{ file_name }**')
        ex_option.extend([f'```{ language }', '\n'])

        return ex_option


def md2html(md_body):
    md = markdown.Markdown(extensions=[ MD_EXTENSION ])
    html_body = md.convert(md_body)
    return html_body


def get_css():
    current_dir = os.path.dirname(__file__)
    css_file_path = f'{ current_dir }/resources/{ CSS_FILE }'
    css = codecs.open(css_file_path, encoding='utf-8', mode='r')
    return css.read()


def merge_html_css(page_title, html_body):
    css = get_css()
    template = html_template.template

    html = template.format_map({
        'page_title': page_title,
        'css': css,
        'html_body': html_body
    })
    return html