import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned = re.sub(r'<[^>]+>', '', html)

    lines = cleaned.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        for line in non_empty_lines:
            file.write(line + '\n')

delete_html_tags('draft.html', 'cleaned.txt')