import gradio as gr
from accounts import Account, get_share_price

account = None

def create_account(username: str, initial_deposit: float):
    global account
    account = Account(username, initial_deposit)
    return f"Account created for {username} with an initial deposit of ${initial_deposit}"

def deposit(amount: float):
    global account
    if account is None:
        return "No account found. Please create an account first."
    new_balance = account.deposit(amount)
    return f"New balance: ${new_balance}"

def withdraw(amount: float):
    global account
    if account is None:
        return "No account found. Please create an account first."
    new_balance = account.withdraw(amount)
    return f"New balance: ${new_balance}"

def buy_shares(symbol: str, quantity: int):
    global account
    if account is None:
        return "No account found. Please create an account first."
    account.buy_shares(symbol, quantity)
    return f"Bought {quantity} shares of {symbol}."

def sell_shares(symbol: str, quantity: int):
    global account
    if account is None:
        return "No account found. Please create an account first."
    account.sell_shares(symbol, quantity)
    return f"Sold {quantity} shares of {symbol}."

def portfolio_value():
    global account
    if account is None:
        return "No account found. Please create an account first."
    return f"Portfolio value: ${account.calculate_portfolio_value()}"

def profit_loss():
    global account
    if account is None:
        return "No account found. Please create an account first."
    return f"Profit/Loss: ${account.calculate_profit_loss()}"

def holdings():
    global account
    if account is None:
        return "No account found. Please create an account first."
    return f"Holdings: {account.get_holdings()}"

def transactions():
    global account
    if account is None:
        return "No account found. Please create an account first."
    return f"Transactions: {account.get_transactions()}"

with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation Account Management")
    status = gr.Textbox(label="Status", interactive=False)
    
    with gr.Row():
        username = gr.Textbox(label="Username")
        initial_deposit = gr.Number(label="Initial Deposit", value=1000)
        create_btn = gr.Button("Create Account")
        create_btn.click(create_account, inputs=[username, initial_deposit], outputs=status)
    
    with gr.Row():
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_btn = gr.Button("Deposit")
        deposit_btn.click(deposit, inputs=deposit_amount, outputs=status)

    with gr.Row():
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_btn = gr.Button("Withdraw")
        withdraw_btn.click(withdraw, inputs=withdraw_amount, outputs=status)

    with gr.Row():
        buy_symbol = gr.Textbox(label="Symbol to Buy")
        buy_quantity = gr.Number(label="Quantity to Buy")
        buy_btn = gr.Button("Buy Shares")
        buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=status)

    with gr.Row():
        sell_symbol = gr.Textbox(label="Symbol to Sell")
        sell_quantity = gr.Number(label="Quantity to Sell")
        sell_btn = gr.Button("Sell Shares")
        sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=status)

    with gr.Row():
        portfolio_btn = gr.Button("Calculate Portfolio Value")
        portfolio_output = gr.Textbox()
        portfolio_btn.click(portfolio_value, outputs=portfolio_output)

    with gr.Row():
        profit_loss_btn = gr.Button("Calculate Profit/Loss")
        profit_loss_output = gr.Textbox()
        profit_loss_btn.click(profit_loss, outputs=profit_loss_output)

    with gr.Row():
        holdings_btn = gr.Button("Get Holdings")
        holdings_output = gr.Textbox()
        holdings_btn.click(holdings, outputs=holdings_output)

    with gr.Row():
        transactions_btn = gr.Button("Get Transactions")
        transactions_output = gr.Textbox()
        transactions_btn.click(transactions, outputs=transactions_output)

demo.launch()