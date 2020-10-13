#Bartosz Wrobel, 302940
import unittest
from collections import Counter

from servers import Server, ListServer, Product, Client, MapServer, TooManyProductsFoundError, NoProductsFoundError

server_types = (ListServer, MapServer)

class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))

    def test_get_entries_sorts(self):
        products = [Product('PP12', 39), Product('PP234', 22), Product('PP235', 13)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual([products[2], products[1], products[0]], entries)

    def test_if_get_entries_raises_exception(self):
        products = [Product('PP12', 39), Product('PP234', 22), Product('PP235', 13), Product('PP236', 21)]
        for server_type in server_types:
            server = server_type(products)
            with self.assertRaises(TooManyProductsFoundError):
                entries = server.get_entries(2)

    def test_if_get_entries_returns_empty_list(self):
        products = [Product('PP12', 39), Product('PP234', 22), Product('PP235', 13)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(5)
            self.assertEqual([], entries)


class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    def test_total_price_for_exception_list(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 32), Product('PP237', 4)]
        server = ListServer(products)
        client = Client(server)
        price = client.get_total_price(2)
        self.assertEqual(price, None)

    def test_total_price_for_exception_map(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 32), Product('PP237', 4)]
        server = MapServer(products)
        client = Client(server)
        price = client.get_total_price(2)
        self.assertEqual(price, None)


if __name__ == '__main__':
    unittest.main()