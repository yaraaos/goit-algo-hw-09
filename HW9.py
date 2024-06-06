def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)  # Сортуємо монети в порядку спадання
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins):
    # Ініціалізація таблиці для зберігання мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_count = [0] * (amount + 1)
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for higher_amount in range(coin, amount + 1):
            if min_coins[higher_amount - coin] + 1 < min_coins[higher_amount]:
                min_coins[higher_amount] = min_coins[higher_amount - coin] + 1
                coin_used[higher_amount] = coin

    if min_coins[amount] == float('inf'):
        return {}  # Немає рішення

    # Визначення кількості кожного номіналу монет
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

# Приклад використання
coins = [50, 25, 10, 5, 2, 1]
amount = 113

print("Greedy algorithm result:", find_coins_greedy(amount, coins))
print("Dynamic programming result:", find_min_coins(amount, coins))
