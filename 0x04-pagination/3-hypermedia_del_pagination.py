#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """hyper index"""
        assert index > 0 and index < len(self.dataset())
        next_index = index + page_size
        data = self.get_page(int(index / page_size), page_size)
        dict = {}
        dict['index'] = index
        dict['next_index'] = next_index
        dict['page_size'] = int(index / page_size)
        dict['data'] = data
        return (dict)
