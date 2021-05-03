def add_it_up(number):
    if type(number) != int:
        return 0
    else:
        # return sum(range(0,number+1))
        return int(number * (number + 1) / 2)


print(add_it_up('aca'))
print(add_it_up(3))
