import random
number_of_sequences = 0
double_sequences = 0
triple_sequences = 0
for i in range(100000):
    # Creating a random list of heads and tails
    result = [random.choice("HT") for i in range(100)]
    count = 1
    # Evaluating the amout of sequences of 6 consecutive heads or tails
    for j in range(1, 100):
        if result[j] == result[j-1]:
            count += 1
        else:
            count = 1
        if count % 6 == 0:
            number_of_sequences += 1
            double_sequences += 1 if count % 12 == 0 else 0
            triple_sequences += 1 if count % 18 == 0 else 0


print(f"The number of sequences of 6 heads or tails was: {number_of_sequences}")
print(f"The number of sequences of 12 heads or tails was: {double_sequences}")
print(f"The number of sequences of 18 heads or tails was: {triple_sequences}")