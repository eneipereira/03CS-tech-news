from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = find_news()

    sorted_news = sorted(
        all_news, key=lambda x: (-x["comments_count"], x["title"])
    )

    top_5_news = [(news["title"], news["url"]) for news in sorted_news][:5]

    return top_5_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    all_news = find_news()

    categories = [news["category"] for news in all_news]

    sorted_categories = sorted(categories, key=lambda x: x)

    top_5_categories = [
        category[0] for category in Counter(sorted_categories).most_common(5)
    ]

    return top_5_categories
