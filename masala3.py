print("three")
def apply_discount_and_sort(prices: list) -> list:
    # Apply discount and sort prices in descending order
    discounted_prices = [price * 0.85 for price in prices if price > 0]
    return sorted(discounted_prices, reverse=True)

prices1 = [100, 250, 75, 150, 300]
prices2 = []
prices3 = [150.5, 200, 99.9, 50.25]
prices4 = [0, 300, -200, 150, 50]

print(apply_discount_and_sort(prices1))
print(apply_discount_and_sort(prices2))
print(apply_discount_and_sort(prices3))
print(apply_discount_and_sort(prices4))
