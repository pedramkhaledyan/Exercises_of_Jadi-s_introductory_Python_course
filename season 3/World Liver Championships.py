number_of_player = int(input())
count_of_games = input().split()
player = 0
for n in count_of_games:
    n=int(n)
    if n <= 2 :
        player += 1
print(player//3) 