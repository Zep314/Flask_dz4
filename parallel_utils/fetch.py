"""
В модуле содержатся функции для скачивания файлов ихз интернета,
а так же - декоратор для измерения времени работы функций
"""
import parallel_utils.constants as c
import requests
import os
import time
from urllib.parse import urlparse


def fetch_file(url, path):
    """
    Функция скачивает файл из интернета и пытается его сохранить в указанном каталоге
    :param url: url файла, который надо скачать
    :param path: путь к папке для сохранения файла
    :return: код завершения
    """
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        response = requests.get(url)
        if response.ok:
            filename = path + os.sep + os.path.basename(urlparse(url).path)
            with open(filename, 'wb') as f:
                f.write(response.content)
            return c.OK
        else:
            return c.URL_NOT_FOUND
    except IOError:
        return c.URL_NOT_FOUND


def my_time(func):
    """
    Декоратор для замера времени выполнения функции
    :param func: Декорируемая функция
    :return: Результат выполнения декорируемой функции
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Время выполнения: {time.time() - start_time:.3f} сек")
        return result

    return wrapper
