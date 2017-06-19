"""
Script updates sakha {{Нэдиэлэ тылбааһа}} template according to Translate of
the Week project.

Usage:
    python tow.py
"""

import re
import pywikibot

def main():
    """Main script function."""
    meta = pywikibot.Site("meta", "meta")
    template = pywikibot.Page(meta, "Template:TOWThisweek")
    match = re.search(r"\[\[:([a-z\-]+):(.*?)\]\]", template.text, flags=re.I)
    original = match.group(0)
    lang = match.group(1)
    link = match.group(2)

    sahwiki = pywikibot.Site()
    orwiki = pywikibot.Site(lang)
    try:
        sakha = pywikibot.ItemPage.fromPage(pywikibot.Page(orwiki, link)).getSitelink(sahwiki)
    except Exception:
        sakha = "'''[[Халыып:Нэдиэлэ тылбааһа|Ыстатыйа сахалыы аатын суруй]]'''"

    template = pywikibot.Page(sahwiki, "Халыып:Нэдиэлэ тылбааһа")
    result = template.text
    result = re.sub(r"(<span id=\"sakha\">).*?(</span>)", "\\1" + sakha + "\\2", result)
    result = re.sub(r"(<span id=\"original\">).*?(</span>)", "\\1" + original + "\\2", result)
    template.text = result
    template.save("Нэдиэлэ тылбааһын саҥардыы.", minor=False)

if __name__ == "__main__":
    main()
