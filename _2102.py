# while True:
n,m = list(map(int, input().split()))

inp = []

for i in range(m):
    inp.append(list(map(int, input().split())))


strength = {}
start_dict = {}
trans_dict = {}
exc = 0


for i in range(1, n + 1):
    strength[i] = 0
    start_dict[i] = []

# print("input:", inp)


for i in range(m):
    start_dict[inp[i][0]].append(inp[i][1])


def dfs(current, visited, start):
    for neighbor in start_dict.get(current, []):
        # print(f"Current: {current}, Neighbor: {neighbor}, Visited: {visited}, Start: {start}")
        if neighbor == start:
            raise Exception("Loop detected")
        # print(f"Visiting {neighbor} from {current}")
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor, visited, start)

for player in start_dict:
    visited = set()
    # print(f"Player {player} has neighbors: {start_dict[player]}")
    try:
        dfs(player, visited, player)
        trans_dict[player] = list(visited)
    except Exception:
        exc = 1
        # print(f"Loop detected for player {player}")
        break
    # print("new trans dict:", trans_dict)


if exc == 0:
    for i in range(1, n + 1):
        if i not in strength:
            strength[i] = 0
        strength[i] = len(trans_dict[i])



# print("strength:", strength)
# print("start_dict:", start_dict)
# print(f"\nFINAL trans_dict:", trans_dict)

  



# Певерірка чи нема однозначного переможця чи виник цикл чи він не є повним переможцем
if list(strength.values()).count(max(strength.values())) > 1 or exc == 1 or len(trans_dict[max(strength, key=strength.get)]) != n - 1:
    # print("No winner")
    print("-1")
else:
    # print(f"Winner is {max(strength, key=strength.get)} with strength {strength[max(strength, key=strength.get)]}")
    print(max(strength, key=strength.get))