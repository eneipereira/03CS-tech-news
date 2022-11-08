from requests import get, ReadTimeout, HTTPError
from ratelimiter import RateLimiter
from parsel import Selector


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
    selector = Selector(text=html_content)

    urls = selector.css(".archive-main article h2 a::attr(href)").getall()

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    next_page_url = selector.css(".nav-links .next::attr(href)").get()

    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
