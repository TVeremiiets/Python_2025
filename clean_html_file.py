import re

def clean_html_file(input_file, output_file="cleaned.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    cleaned_text = re.sub(r'<[^>]+>', '', html_content)

    lines = cleaned_text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    with open(output_file, "w", encoding="utf-8") as f:
        for line in cleaned_lines:
            f.write(line + "\n")

clean_html_file("draft.html", "cleaned.txt")