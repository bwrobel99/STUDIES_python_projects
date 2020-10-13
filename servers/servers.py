#Bartosz Wrobel, 302940
from typing import List, Tuple, Dict, Optional
from abc import ABC, abstractmethod
import re

class TooManyProductsFoundError(Exception):
    pass

class Product:
    def __init__(self, name_: str, price_: float):
        self.name = name_
        self.price = price_

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

class Server(ABC):
    def __init__(self, product_list_: List[Product]):
        self.product_list = product_list_

    def list_to_dict(self) -> Dict[str, Product]:
        product_dict = {}
        for product in self.product_list:
            product_dict[product.name] = product
        return product_dict

    n_max_returned_entries = 3

    @abstractmethod
    def get_entries(self, n_letters: int = 1):
        pass

class ListServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = self.product_list

    def get_entries(self, n_letters: int) -> List[Product]:
        products_found = []
        for product in self.products:
            letters = re.split('(\d+)',product.name)[0]
            numbers = re.split('(\d+)',product.name)[1]
            if len(letters) == n_letters and 2<=len(numbers)<=3:
                products_found.append(product)
        if len(products_found) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()
        if not products_found:
            return products_found
        return sorted(products_found, key = lambda product: product.price)

class MapServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = self.list_to_dict()

    def get_entries(self, n_letters: int) -> List[Product]:
        products_found = []
        for name in self.products.keys():
            letters = re.split('(\d+)', name)[0]
            numbers = re.split('(\d+)', name)[1]
            if len(letters) == n_letters and 2<=len(numbers)<=3:
                products_found.append(self.products[name])
        if len(products_found) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        if not products_found:
            return products_found
        return sorted(products_found, key = lambda product: product.price)

class Client:
    def __init__(self, server_: Server):
        self.server = server_
    def get_total_price(self, n: Optional[int]) -> Optional[float]:
        try:
            entries = self.server.get_entries(n)
        except TooManyProductsFoundError:
            return None
        if not entries:
            return None
        total_price = 0
        for entry in entries:
            total_price += entry.price
        return total_price