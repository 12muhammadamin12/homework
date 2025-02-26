def apply_discount_and_sort(prices: list) -> list:
    # Apply discount and sort prices in descending order
    discounted_prices = [price * 0.85 for price in prices if price > 0]
    return sorted(discounted_prices, reverse=True)
