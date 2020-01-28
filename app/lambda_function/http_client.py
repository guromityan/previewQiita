import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'packages'))

import requests

def get_original_md(url):
    md_url = f'{ url }.md'
    response = requests.get(md_url)
    src_md = response.text
    return src_md
