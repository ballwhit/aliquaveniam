if to_symbol == 'LPT':
    # Long position trade
    trade_type = 'long'
    entry_price = ask_price
    stop_loss_price = entry_price - stop_loss_amount
    take_profit_price = entry_price + take_profit_amount
