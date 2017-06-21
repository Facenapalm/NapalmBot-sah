"""
Sandbox cleaner for Sakha Wikipedia.

Usage:
    python sandbox.py
"""

import pywikibot

SANDBOXES = [
    ("Бикипиэдьийэ:Эрчиллэр сир", "{{/Мантан аллара суруй}} <!-- Бука диэн, бу суругу сотума. Мантан аллара суруй/эрчилин -->\n")
]

def delayed_edit(page, text, delay=15):
    """
    Replace text of the page (first parameter) with given one (second parameter)
    only if last edit was made more than 15 (can be changed via third parameter)
    minutes ago.
    """
    delta = pywikibot.Timestamp.utcnow() - page.editTime()
    if delta.total_seconds() >= 60 * delay:
        page.text = text
        page.save("Эрчиллэр хонууну ыраастааһын.", force=True)

def main():
    """Main script function."""
    site = pywikibot.Site()
    for (title, text) in SANDBOXES:
        page = pywikibot.Page(site, title)
        delayed_edit(page, text)

if __name__ == "__main__":
    main()
 