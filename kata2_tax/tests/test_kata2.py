import unittest
from kata2_tax.kata2_tax import get_total

class TestTax(unittest.TestCase):
    def test_buy_two_out_of_three_items(self):
        costs = {'socks':5, 'shoes':60, 'sweater':30}
        items_bought = ['socks', 'shoes']
        tax = 0.09
        self.assertEqual(get_total(costs, items_bought, tax), 70.85)

    def test_buy_on_empty_cost_list(self):
        costs = {}
        item_bought = ['socks', 'shoes']
        tax = 0.09
        self.assertEqual(get_total(costs, item_bought, tax), 0)

    def test_buy_only_missing_items_from_costs(self):
        costs = {'socks':5, 'shoes':60, 'sweater':30}
        item_bought = ['shirt', 'football']
        tax = 0.12
        self.assertEqual(get_total(costs, item_bought, tax), 0)

    def test_negative_tax(self):
        costs = {'socks':5, 'shoes':60, 'sweater':30}
        item_bought = ['socks', 'shoes']
        tax = -0.01
        self.assertEqual(get_total(costs, item_bought, tax), 65)

    def test_all_empty_parameters(self):
        costs = 0
        item_bought = []
        tax = 0
        self.assertEqual(get_total(costs, item_bought, tax), 0)

if __name__ == "__main__":
    unittest.main()