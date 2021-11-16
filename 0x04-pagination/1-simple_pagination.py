#!/usr/bin/env python3
"""Write a function named index_range"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """index range"""
    a = (page - 1) * page_size
    b = page * page_size
    return (a, b)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init method"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        if page * page_size > len(self.dataset()) or page * page_size < 0:
            return []
        else:
            index_start = index_range(page, page_size)[0]
            index_end = index_range(page, page_size)[1]
            return (self.__dataset[index_start:index_end])
