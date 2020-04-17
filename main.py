# Project 10.

# This program works with XML file which contains information about books.

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
    book_number = 1
    for book in root:
        data_books[book_number] = book.attrib
        for feature in book:
            try:
                value = int(str(feature.text).strip())
            except ValueError:
                try:
                    value = float(str(feature.text).strip())
                except ValueError:
                    value = str(feature.text).strip()
            data_books[book_number][feature.tag] = value
        book_number += 1
    return data_books


def find_book_by(key, value, data_books):
    """
    Find book by selected parameter.
    :param key: selected parameter
    :param value: value of selected parameter
    :param data_books: dictionary with data about library
    :return: None
    """
    for book_number in data_books:
        book_i = data_books[book_number][key]
        if book_i == value:
            print_data(key, data_books[book_number])
            return
    print(lc.TXT_FIND_BOOK_BY.format(key, value))


def print_data(exception, data_book):
    """
    Printing data about book
    :param exception: key that mustn't be output
    :param data_book: dictionary with data about books
    :return: None
    """
    for key in data_book:
        if key != exception:
            print('{}: {}'.format(key, data_book[key]))


def count_book_by_year(year, data_books):
    """
    Counting book by selected year.
    :param year: year
    :param data_books: dictionary with data about books
    :return: number of books written in selected year
    """
    counter = 0
    for book_number in data_books:
        book_year = data_books[book_number]['Year_of_publishing']
        if book_year == year:
            counter += 1
    print(lc.TXT_COUNT_BOOK_BY_YEAR.format(year, counter))


def average_price(data_books):
    """
    Finding the total price of all books and their number for each publisher.
    :param data_books: dictionary with data about books
    :return: None
    """
    data_publishers = {}
    for book_number in data_books:
        publisher = data_books[book_number]['Publisher']
        price = float(data_books[book_number]['Price'])
        if publisher not in data_publishers:
            data_publishers[publisher] = {}
            data_publishers[publisher]['Count'] = 1
            data_publishers[publisher]['Price'] = price
        else:
            data_publishers[publisher]['Count'] += 1
            data_publishers[publisher]['Price'] += price

    print_average_price(data_publishers)


def print_average_price(data_publishers):
    """
    Counting and printing average price of all books for each publisher.
    :param data_publishers: dictionary with data about prices for each publisher
    :return: None
    """
    for publisher in data_publishers:
        price = data_publishers[publisher]['Price']
        count = data_publishers[publisher]['Count']
        average = price / count
        print('{}: {:.2f}'.format(publisher, average))


def most_expensive(publisher, year, data_books):
    """
    Finding the most expensive book.
    :param publisher: selected publisher
    :param year: selected year
    :param data_books: dictionary with data about books
    :return: None
    """
    expensive_books = []
    for book_number in data_books:
        if data_books[book_number]['Publisher'].lower() == publisher.lower() \
                and data_books[book_number]['Year_of_publishing'] == year:
            price = float(data_books[book_number]['Price'])
            if not expensive_books:
                expensive_books.append(data_books[book_number])

            elif price > expensive_books[0]['Price']:
                expensive_books = [data_books[book_number]]

            elif price == expensive_books[0]['Price']:
                expensive_books.append(data_books[book_number])

    if print_most_expensive(expensive_books):
        print(lc.TXT_NO_INFORMATION.format(publisher, year))


def print_most_expensive(expensive_books):
    """
    Printing information about the most expensive books.
    :param expensive_books: list of the most expensive books
    :return: None
    """
    if expensive_books:
        for book in expensive_books:
            print()
            for key in book:
                if key != 'Publisher' and key != 'Year_of_publishing':
                    print('{}: {}'.format(key, book[key]))
        return False
    else:
        return True


def main():
    data_books = reading_data()
    while True:
        while True:
            print(lc.TXT_CHOOSE)
            print(lc.TXT_MENU)
            answer = input()
            print('-' * 100)
            if answer == '1':
                print(lc.TXT_ID, end=' ')
                book_id = input()
                find_book_by('id', book_id, data_books)
                break

            elif answer == '2':
                print(lc.TXT_ISBN, end=' ')
                book_ISBN = input()
                find_book_by('ISBN', book_ISBN, data_books)
                break

            elif answer == '3':
                print(lc.TXT_YEAR, end=' ')
                year = int(input())
                count_book_by_year(year, data_books)
                break

            elif answer == '4':
                average_price(data_books)
                break

            elif answer == '5':
                print(lc.TXT_PUBLISHER, end=' ')
                publisher = input()
                print(lc.TXT_YEAR, end=' ')
                year = int(input())
                most_expensive(publisher, year, data_books)
                break

            else:
                print(lc.TXT_ERROR)
                print('-' * 100)

        print('-' * 100)
        print(lc.TXT_EXIT)

        answer = input()
        print('-' * 100)
        if answer == '1':
            pass

        else:
            break


language = input('Choose your language:\n1. English\n2. Russian\n').lower()
while True:
    if language == 'english' or language == 'eng' or \
            language == 'e' or language == '1':
        import lc_eng as lc
        break

    elif language == 'russian' or language == 'rus' or \
            language == 'r' or language == '2':
        import lc_rus as lc
        break
    language = input('Please, choose language from proposed: ')
print()

main()
