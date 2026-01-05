class Account:
    def __init__(self, username: str, initial_deposit: float):
        self.username = username
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})
        return self.balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.balance -= amount
        self.transactions.append({'type': 'withdraw', 'amount': amount})
        return self.balance

    def buy_shares(self, symbol: str, quantity: int):
        price = get_share_price(symbol)
        total_cost = price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price})

    def sell_shares(self, symbol: str, quantity: int):
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        price = get_share_price(symbol)
        self.balance += price * quantity
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price})

    def calculate_portfolio_value(self) -> float:
        total_value = 0.0
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value + self.balance

    def calculate_profit_loss(self) -> float:
        current_value = self.calculate_portfolio_value()
        return current_value - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings.copy()

    def get_transactions(self) -> list:
        return self.transactions.copy()


def get_share_price(symbol: str) -> float:
    prices = {'AAPL': 150.0, 'TSLA': 750.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)

# Test implementation
account1 = Account(username='traderJoe', initial_deposit=10000)
print(account1.deposit(500))
account1.buy_shares('AAPL', 10)
print(account1.get_holdings())
print(account1.calculate_portfolio_value())
print(account1.calculate_profit_loss())
print(account1.get_transactions())