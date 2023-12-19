import random

def secret_santa(names):
    # Shuffling the list of names
    shuffled_names = names[:]
    random.shuffle(shuffled_names)

    # Assigning Secret Santa pairs in a circular fashion
    pairs = {}
    for i in range(len(shuffled_names)):
        if i == len(shuffled_names) - 1:
            pairs[shuffled_names[i]] = shuffled_names[0]
        else:
            pairs[shuffled_names[i]] = shuffled_names[i + 1]

    return pairs

# Example usage
participants = ["Make", "Kaitsu", "Mazzeri", "Niklas", "Emil", "Dänk"]
pairs = secret_santa(participants)
for giver, receiver in pairs.items():
    print(f"{giver} -> {receiver}")
