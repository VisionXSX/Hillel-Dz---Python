import re

with open("draft.html", 'r', encoding='utf-8') as infile:
    html = infile.read()
cleaned_text = re.sub(r'<[^>]+>','', html)
with open("cleaned.txt", 'w', encoding='utf-8') as outfile:
    outfile.write(cleaned_text)