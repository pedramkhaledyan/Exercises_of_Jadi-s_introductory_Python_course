won_the_game=0
points=0
for _ in range(30):
    # we can use '_' in for loop When we need to repeat only a certain number of loops and it is not needed inside the loop body
    game_point=int(input())
    points+=game_point
    if game_point==3:
        won_the_game+=1

print(points,won_the_game)