import pandas as pd
import faker
import random

numero_de_pessoas = 500

fake = faker.Faker()


df = pd.DataFrame()
for _ in range(numero_de_pessoas):
    df = pd.concat([df, pd.DataFrame([[fake.name(), fake.random_int(min=1, max=20), fake.boolean()]], columns=["name", "zone", "infected"])])

df.to_csv("fake_data.csv", index=False)


names = df['name'].tolist()
friend_pairs = set()
friend_list = []

for name in names:
    num_friends = random.randint(1, 20)
    for _ in range(num_friends):
        friend = random.choice(names)
        while friend == name or (name, friend) in friend_pairs or (friend, name) in friend_pairs:
            friend = random.choice(names)
        friend_pairs.add((name, friend))
        friend_list.append([name, friend])


df_friends = pd.DataFrame(columns=['pessoa1', 'pessoa2'])
for pair in friend_list:
    df_friends = pd.concat([df_friends, pd.DataFrame([pair], columns=['pessoa1', 'pessoa2'])])

df_friends.to_csv('friendship_data.csv', index=False)
