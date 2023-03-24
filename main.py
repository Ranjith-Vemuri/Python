# Divisible by 2
def is_div2(n):
    j = int(n[-1])
    if j in [0, 2, 4, 6, 8]:
        return True


# Divisible By 3
def is_div3(n):
    s = 0
    for i in n:
        s = s + int(i)
    if s >= 10:
        k = str(s)
        return is_div3(k)
    else:
        if s in [3, 6, 9]:
            return True


# Divisible by 4
def is_div4(n):
    s = "0"+n
    j = int(s[-2])
    k = int(s[-1])
    if j in [0, 2, 4, 6, 8] and k in [0, 4, 8]:
        return True
    elif j in [1, 3, 5, 7, 9] and k in [2, 6]:
        return True
    else:
        return False


# Divisible By 5
def is_div5(n):
    if int(n) > 0:
        for i in n:
            j = int(i[-1])
            if j == 0 or j == 5:
                return True


# Divisible by 6
def is_div6(n):
    if int(n) >= 6:
        s = 0
        for i in n:
            s = s + int(i)
        if s >= 10:
            k = str(s)
            return is_div6(k)
        elif s in [0, 2, 4, 8, 3] and s in [3, 6, 9]:
            return True


# Divisible by 7
def is_div7(n):
    n = str(n)
    while len(n) != 1:
        a = int(n[-1])
        b = int(n[0:len(n) - 1])
        n = b + (5 * a)
        n = str(n)
        if n == '49':
            return True
    return True if n == '7' else False


# Divisible by 8
def is_div8(n):
    n = str(n)
    while len(n) >= 3:
        a = int(n[len(n) - 1])
        b = int(n[len(n) - 2])
        c = int(n[len(n) - 3])
        n = 4 * c + 2 * b + a
        n = str(n)
    while len(n) == 2:
        a = int(n[len(n) - 1])
        b = int(n[len(n) - 2])
        n = 2 * b + a
        n = str(n)
    return True if n == '8' else False


# Divisible by 9
def is_div9(n):
    s = 0
    for i in n:
        s = s + int(i)
    if s >= 10:
        k = str(s)
        return is_div9(k)
    else:
        if s == 9:
            return True


if __name__ == "__main__":
    try:
        numbers = list(input('Enter the numbers:\n').split(','))
        fl = []
        for num in numbers:
            if num.isdigit():
                fl.append(num)
            elif num == '':
                raise Exception(f'Number Missed Enter valid Number')
            else:
                raise Exception(f"{num} is not an integer enter valid number")

        for num in fl:
            divisible_by_2 = is_div2(num)
            divisible_by_3 = is_div3(num)
            divisible_by_4 = is_div4(num)
            divisible_by_5 = is_div5(num)
            divisible_by_6 = is_div6(num)
            divisible_by_7 = is_div7(num)
            divisible_by_8 = is_div8(num)
            divisible_by_9 = is_div9(num)

            res = []
            if divisible_by_2:
                res.append(2)
            if divisible_by_3:
                res.append(3)
            if divisible_by_4:
                res.append(4)
            if divisible_by_5:
                res.append(5)
            if divisible_by_6:
                res.append(6)
            if divisible_by_7:
                res.append(7)
            if divisible_by_8:
                res.append(8)
            if divisible_by_9:
                res.append(9)
                
            result = ','.join(str(i) for i in res)
            if len(result) == 0:
                print(f"{num}: is not divisible")
            else:
                print(f"{num}: is divisible by {result}")
    except Exception as e:
        print(f"Error: {e}")
