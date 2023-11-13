# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.

# returns an list with both scores, alice first
def define_scores(list_alice_values, list_bob_values) -> int:
    score_alice = 0
    score_bob = 0

    for position in range(len(list_alice_values)):
        print('POSITION', position)
        if list_alice_values[position] > list_bob_values[position]:
            score_alice += 1
            print(f'POINT ALICE {list_alice_values[position]} - {list_bob_values[position]}')
        elif list_alice_values[position] < list_bob_values[position]:
            score_bob += 1
            print(f'POINT BOB {list_alice_values[position]} - {list_bob_values[position]}')
        else:
            pass
    

    return score_alice, score_bob


# Given a and b, determine their respective comparison points.


# First line has 3 value separated by space
list_alice = list(map(int, input().split()))
print('list Alice', list_alice)

list_bob = list(map(int, input().split()))
print('list bob', list_bob)

# put the lists on function define_scores
score_alice, score_bob = define_scores(list_alice_values=list_alice, list_bob_values=list_bob)


# print the scores joined by space
print(f'{score_alice} {score_bob}')

