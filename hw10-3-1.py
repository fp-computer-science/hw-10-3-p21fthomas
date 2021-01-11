def sum_odds(lst):
    lst1 = 0
    time = 0
    while time < len(lst):
        if lst[time] % 2 != 0:
            lst1 += lst[time]
        time += 1
    return(lst1)

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)