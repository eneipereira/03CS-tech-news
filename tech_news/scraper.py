from requests import get, ReadTimeout, HTTPError
from ratelimiter import RateLimiter


# Requisito 1
@RateLimiter(max_calls=1, period=1)
def fetch(url):
    """Seu código deve vir aqui"""
    SECONDS = 3

    try:
        header = {"user-agent": "Fake user-agent"}
        response = get(url, headers=header, timeout=SECONDS)
        response.raise_for_status()
    except (ReadTimeout, HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
