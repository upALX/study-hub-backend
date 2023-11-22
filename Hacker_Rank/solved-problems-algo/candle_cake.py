# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are talles


def birthdayCakeCandles(candles_height):

    most_biggest = max(candles_height)

    all_max_values = [item for item in candles_height if item == most_biggest]

    return all_max_values.__len__()

candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)

print(result)
