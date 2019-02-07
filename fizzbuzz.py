for i in range(100):
    i += 1
    is_divisible = False
    exit_str = ''
    
    if i % 3 == 0:
        is_divisible = True
        exit_str += 'Fizz'
        
    if i % 5 == 0:
        is_divisible = True
        exit_str += 'Buzz'
        
    if not is_divisible:
        exit_str += str(i)
        
    print(exit_str)
