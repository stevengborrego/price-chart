import math

MIN_COST = 10.00
MAX_COST = 50.00


def calculate_price(cost):
    return math.floor((cost * 1.4) + 1) + 0.99


def mark_up():
    # find number of prices to be calculated
    min_price_int = math.floor(calculate_price(MIN_COST))
    max_price_int = math.floor(calculate_price(MAX_COST))
    num_prices = max_price_int - min_price_int

    # initialize dictionary with empty arrays
    price_dict = {}
    price_key = calculate_price(MIN_COST)  # set to the lowest price
    for i in range(num_prices):
        price_dict[price_key] = []
        price_key = round(price_key + 1, 2)

    # calculate prices
    cost = MIN_COST
    while cost < MAX_COST:
        cost = round(cost, 2)
        price = calculate_price(cost)
        price_dict[price].append(cost)
        cost += 0.01

    # print results
    for price in price_dict:
        print(str(min(price_dict[price])) + ' - ' + str(max(price_dict[price])) + ' = ' + str(price))


if __name__ == '__main__':
    mark_up()
