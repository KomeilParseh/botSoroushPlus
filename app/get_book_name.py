#!/env/bin/python3
"""Module get_book_name"""
from bs4 import BeautifulSoup
from requests import get


def get_book_name(search_mark):
    """get book name at googdread"""

    good_reads = f'https://www.goodreads.com/search?q={search_mark}'

    data = get(good_reads).content
    soup = BeautifulSoup(data, features="html5lib")

    looppnum = 0
    names = ''
    for name in soup.select('.bookTitle span'):

        newname = str(name).replace("<spen>", "")
        if newname == name:
            newname = str(name).replace(
                """<span aria-level="4" itemprop="name" role="heading">""", "")
        name = newname
        looppnum += 1
        names += f'{name}\n'
        if looppnum == 10: # TODO: loopnum is hard code
            break
        return names
