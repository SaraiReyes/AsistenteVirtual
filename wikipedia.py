import wikipediaapi
import sys


wiki = wikipediaapi.Wikipedia(language='es')

page_ostrava = wiki.page('pandemia')
print(page_ostrava.summary)