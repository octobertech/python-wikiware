# -*- coding: utf-8 -*-

import re

from fetcher import WikiwareFetch
from parser import WikiwareAPIParseSummary

def get_wiki_summary(title):

    summary = None
    f = WikiwareFetch()
    html = f.fetch_api_parse(title=title, section="0")
    if html:
        p = WikiwareAPIParseSummary(content=html)
        summary = p.get_summary()
    return summary


