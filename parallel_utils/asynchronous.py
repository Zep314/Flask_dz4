"""
Модуль содержит функции для работы в асинхронном режиме
"""
from parallel_utils.fetch import my_time
import asyncio
import aiofiles
import aiohttp
import os
from urllib.parse import urlparse


async def async_fetch_file(url, path_to_save):
    """
    Функция скачивает один файл по-указанному url, и сохраняет его в указанном каталоге.
    Позволяет запускать асинхронно другие функции
    :param url: список файлов
    :param path_to_save: каталог для сохранения
    :return:
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    if not os.path.exists(path_to_save):
                        os.mkdir(path_to_save)
                    filename = path_to_save + os.sep + os.path.basename(urlparse(url).path)
                    async with aiofiles.open(filename, 'wb') as f:
                        await f.write(await response.read())
        except aiohttp.ClientError:
            pass


async def run(url_list, path_to_save):
    """
    Запускаем задачи скачивания файлов асинхронно
    :param url_list: список файлов
    :param path_to_save: каталог для сохранения
    :return:
    """
    tasks = []
    for url in url_list:
        task = asyncio.ensure_future(async_fetch_file(url, path_to_save))
        tasks.append(task)
    await asyncio.gather(*tasks)


@my_time
def download_asynchronous(url_list, path_to_save):
    """
    Функция скачивает список файлов в определенный каталог
    :param url_list: список файлов
    :param path_to_save: каталог для сохранения
    :return:
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(url_list, path_to_save))
