from requests import get, ReadTimeout, HTTPError
from ratelimiter import RateLimiter
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)

    news = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get()
        or selector.css("p.post-modified-info::text").get()[:9],
        "writer": selector.css(".author > a::text").get(),
        "comments_count": len(selector.css(".comment-body").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
            ).strip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css("span.label::text").get()
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url_to_scrape = "https://blog.betrybe.com"

    all_news = []

    while len(all_news) <= amount:
        html_content = fetch(url_to_scrape)
        page_urls = scrape_novidades(html_content)

        for url in page_urls:
            curr_html_content = fetch(url)
            news = scrape_noticia(curr_html_content)
            all_news.append(news)

        url_to_scrape = scrape_next_page_link(html_content)

    all_news = all_news[:amount]

    create_news(all_news)

    return all_news
