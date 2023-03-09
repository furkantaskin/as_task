from bs4 import BeautifulSoup
import translators as ts
import translators.server as tss
import time
import json
import os

string_list_hi = []
custom_list = ["../docs-copy/index.html", "../docs-copy/contact.html"]


def write_to_json(data=None):
    if data is None:
        data = {}
    with open("../l10n/en-hi.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
        f.close()
    merged_data = {**json_data, **data}

    with open("../l10n/en-hi.json", "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)
        f.close()


def read_from_json() -> dict:
    with open("../l10n/en-hi.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
        f.close()
    return json_data


def convert_file(arg_file="../docs-copy/index.html"):
    en_text = read_from_json().keys()
    with open(arg_file, 'r', encoding="utf-8") as html_file:
        html = html_file.read()
        html_file.close()

    soup = BeautifulSoup(html, 'html.parser')
    for inner_text in [*set(soup.get_text().split("\n"))]:
        if inner_text in en_text:
            continue
        else:
            write_to_json({inner_text: tss.google(inner_text, to_language="hi")})
            print(f"Translated {inner_text} to {tss.google(inner_text, to_language='hi')} and added to the JSON")
    with open(arg_file, 'w+', encoding="utf-8") as html_file:

        html_file.write(str(soup))
        html_file.close()

# Load the HTML file


# Parse the HTML file

# print(read_from_json())



# string_list = [x.strip(" ") for x in [*set(soup.get_text().split("\n"))] if x.replace(" ", "")]

#
#
#
#
# json.dump(dict.fromkeys(string_list), local_file, indent=4, ensure_ascii=False)
#
# local_file.close()

