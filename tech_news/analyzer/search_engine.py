from tech_news.database import search_news
from datetime import datetime as dt


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    matched_news = search_news({"title": {"$regex": title, "$options": "i"}})

    tuple_list = [(news["title"], news["url"]) for news in matched_news]

    return tuple_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        formatted_date = dt.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

        matched_news = search_news({"timestamp": formatted_date})

        tuple_list = [(news["title"], news["url"]) for news in matched_news]
    except Exception:
        raise ValueError("Data inválida")
    else:
        return tuple_list


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    matched_news = search_news({"tags": {"$regex": tag, "$options": "i"}})

    tuple_list = [(news["title"], news["url"]) for news in matched_news]

    return tuple_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
