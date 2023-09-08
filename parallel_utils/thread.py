"""
Модуль содержит функции для работы в многопоточном режиме
"""
from parallel_utils.fetch import fetch_file, my_time
import threading


@my_time
def download_threads(url_list, path_to_save):
    """
    Функция скачивает список файлов в определенный каталог
    :param url_list: список файлов
    :param path_to_save: каталог для сохранения
    :return:
    """

    threads = []

    for url in url_list:
        # fetch_file(url, path_to_save)
        thread = threading.Thread(target=fetch_file, args=[url, path_to_save])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
