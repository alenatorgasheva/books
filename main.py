# Project 10.

# This program ...

# Developed by Torgasheva A.


import xml.etree.ElementTree as ET


def reading_data():
    """
    Reading data about library.
    :return: dictionary with data about library
    """
    data_books = {}
    XML_FILE = 'books.xml'
    tree = ET.ElementTree(file=XML_FILE)
    root = tree.getroot()
    i = 1
    for book in root:
        data_books[i] = book.attrib
        for feature in book:
            data_books[i][feature.tag] = str(feature.text).strip()
        i += 1
    return data_books


def find_book_by(key, value, data_books):
    """
    Find book by selected parameter.
    :param key: selected parameter
    :param value: value of selected parameter
    :param data_books: dictionary with data about library
    :return: None
    """
    for i in range(1, len(data_books)):
        book_i = data_books[i][key]
        if book_i == value:
            print_data(data_books[i])


def print_data(data_book):
    """
    Printing data about book
    :param data_book: dictionary with data about book
    :return: None
    """
    for key in list(data_book.keys()):
        print('{0:}: {1:}'.format(key, data_book[key]))


def count_book_by_year(year, data_books):
    """
    Counting book by selected year.
    :param year: year
    :param data_books: dictionary with data about book
    :return: number of books written in selected year
    """
    counter = 0
    for i in range(1, len(data_books)):
        book_year = data_books[i]['Year_of_publishing']
        if book_year == year:
            counter += 1
    return counter


def main():
    data_books = reading_data()


main()
