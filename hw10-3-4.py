def your_function_name(wordy,var):
    times_there = 0 
    times = 0
    chang = 0 
    while times < len(wordy):
        if wordy[times] == var:
            times_there += 1
        times += 1
    return(times_there)




print(your_function_name("cat", "t") == 1)
print(your_function_name("apple", "p") == 2)
print(your_function_name("supercalifragilisticexpialidocious", "i")== 7)