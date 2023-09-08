from parallel_utils.asynchronous import download_asynchronous
from parallel_utils.consistent import download_consistent
from parallel_utils.multiprocessor import download_multiprocessor
from parallel_utils.thread import download_threads
from parallel_utils.fetch import fetch_file, my_time

__all__ = ['download_asynchronous', 'download_consistent', 'download_multiprocessor', 'download_threads',
           'fetch_file', 'my_time']
