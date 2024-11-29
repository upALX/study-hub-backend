# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

def breakingRecords(scores):
    list_score_verified = []
    value_biggest_score = 0
    value_lowest_score = 0
    counter_minor = 0
    counter_biggest = 0
    counter = 0
    for score in scores:
        if list_score_verified.__len__() == 0:
            list_score_verified.append(score)
            value_biggest_score = score
            value_lowest_score = score
        else:
            if score > value_biggest_score:
                print('biggest: ', value_biggest_score)
                print(score)
                value_biggest_score = score
                counter_biggest += 1
                list_score_verified.append(score)
            elif score < value_lowest_score:
                value_lowest_score = score
                counter_minor += 1
                list_score_verified.append(score)
            else:
                list_score_verified.append(score)

        counter +=1

        print(counter)
        print(list_score_verified)

    return f'{counter_biggest} {counter_minor}'

n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(result)

