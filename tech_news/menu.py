import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_tag, search_by_category
    )


def insert_news_by_amount():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(amount)


def get_by_title():
    title = input("Digite o título: ")
    print(search_by_title(title))


def get_by_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(date))


def get_by_tag():
    tag = input("Digite a tag: ")
    print(search_by_tag(tag))


def get_by_category():
    category = input("Digite a categoria: ")
    print(search_by_category(category))


def get_top_5_news():
    print(top_5_news())


def get_top_5_categories():
    print(top_5_categories())


def exit_menu():
    print("Encerrando script")


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    options_menu = input(
        """
 Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """
    )

    menu = {
            "0": insert_news_by_amount,
            "1": get_by_title,
            "2": get_by_date,
            "3": get_by_tag,
            "4": get_by_category,
            "5": get_top_5_news,
            "6": get_top_5_categories,
            "7": exit_menu
        }
    try:
        menu[options_menu]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
