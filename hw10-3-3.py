def three_letter_words(lst):
    total = 0 
    length = 0 
    again = 0
    time = 0
    while again < len(lst):
        if len(lst[length]) == 3:
            total += 1 
        again += 1

    return(total)

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
