"""
Программа скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует
названию изображения в URL-адресе.
- Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
- Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
- Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем
времени выполнения программы.
"""

import parallel_utils as pu
import argparse
import os

url_list = []

if __name__ == '__main__':

    # Работаем с командной строкой
    parser = argparse.ArgumentParser(description='Asynchronous, threads and multiprocessor url downloader')
    parser.add_argument('-url', '--url-list',
                        metavar='url1 url2 url3 ... url(n)',
                        help='enter list of url\'s',
                        nargs='+',
                        default=[])
    parser.add_argument('-f', '--file',
                        metavar='<name of file with list urls>',
                        help='enter path to file\'s',
                        type=str,
                        default='')
    args = parser.parse_args()

    if args.url_list:
        url_list = args.url_list.copy()
    else:
        if os.path.isfile(args.file):
            with open(args.file, 'r', encoding='utf-8') as f:
                url_list = f.read().splitlines()

    if url_list:
        print('Скачиваем файлы последовательно')
        pu.download_consistent(url_list, 'consistent')

        print('\nСкачиваем файлы с помощью потоков')
        pu.download_threads(url_list, 'threads')

        print('\nСкачиваем файлы с помощью процессов')
        pu.download_multiprocessor(url_list, 'multiprocessor')

        print('\nСкачиваем файлы асинхронно')
        pu.download_asynchronous(url_list, 'async')
    else:
        print('Список url для скачивания пуст!')
