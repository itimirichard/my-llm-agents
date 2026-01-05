import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(username='traderJoe', initial_deposit=10000)

    def test_initial_deposit(self):
        self.assertEqual(self.account.balance, 10000)
        self.assertEqual(self.account.username, 'traderJoe')

    def test_deposit_positive(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 10500)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdrawal_success(self):
        self.account.withdraw(2000)
        self.assertEqual(self.account.balance, 8000)

    def test_withdrawal_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(15000)

    def test_withdrawal_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_buy_shares_success(self):
        self.account.buy_shares('AAPL', 10)
        self.assertEqual(self.account.holdings['AAPL'], 10)
        self.assertEqual(self.account.balance, 8500)

    def test_buy_shares_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 100)

    def test_sell_shares_success(self):
        self.account.buy_shares('AAPL', 10)
        self.account.sell_shares('AAPL', 10)
        self.assertNotIn('AAPL', self.account.holdings)
        self.assertEqual(self.account.balance, 10000)

    def test_sell_shares_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 1)

    def test_calculate_portfolio_value(self):
        self.account.buy_shares('AAPL', 10)
        self.assertEqual(self.account.calculate_portfolio_value(), 8500 + 1500)

    def test_calculate_profit_loss(self):
        self.account.buy_shares('AAPL', 10)
        self.assertEqual(self.account.calculate_profit_loss(), 1500)

    def test_get_transactions(self):
        self.account.deposit(500)
        self.account.withdraw(2000)
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 3)  # deposit + withdraw + buy_shares

if __name__ == '__main__':
    unittest.main()