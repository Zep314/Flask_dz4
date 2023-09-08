"""
Модуль содержит функции для работы в многопроцессорном режиме
"""
from parallel_utils.fetch import fetch_file, my_time
from multiprocessing import Process


@my_time
def download_multiprocessor(url_list, path_to_save):
    """
    Функция скачивает список файлов в определенный каталог
    :param url_list: список файлов
    :param path_to_save: каталог для сохранения
    :return:
    """

    processes = []

    for url in url_list:
        fetch_file(url, path_to_save)
        process = Process(target=fetch_file, args=(url, path_to_save))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
