"""
Модуль содержит функции для работы в обычном, последовательном режиме
"""
from parallel_utils.fetch import fetch_file, my_time


@my_time
def download_consistent(url_list, path_to_save):
    """
    Функция скачивает список файлов в определенный каталог
    :param url_list: список файлов
    :param path_to_save: каталог для сохранения
    :return:
    """
    for url in url_list:
        fetch_file(url, path_to_save)
