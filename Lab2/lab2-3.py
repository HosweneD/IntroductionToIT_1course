def is_prime(number): #является ли число простым
    cnt = 0
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
    if cnt > 2:
        return "false"
    else:
        return "true"
