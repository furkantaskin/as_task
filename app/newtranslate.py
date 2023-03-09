from bs4 import BeautifulSoup
import translators as ts
import translators.server as tss
import time

# Load the HTML file
with open('../docs-copy/index.html', 'r') as f:
    html = f.read()

# Parse the HTML file
soup = BeautifulSoup(html, 'html.parser')

# Initialize the translator

# Find all the elements located in the body


string_list = [x.strip(" ") for x in [*set(soup.get_text().split("\n"))] if x.replace(" ", "")]
string_list_hi = []
for s in string_list:
    print("\n\033[0;96m Translating \033[0m", s)
    x = tss.google(s, to_language="hi")
    print("\033[0;96m Translated \033[0m", x)
    string_list_hi.append(x)
    time.sleep(2)

print(len(string_list_hi), len(string_list))

