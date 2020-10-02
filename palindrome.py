lst_nums = []
num = int(input('Enter a number: '))
print()
lst_nums.append(num)

for value in lst_nums:
    a = value
    while True:
        n = str(a)

        a += 1
        if str(n[::-1]) == str(n):
            print('The next palindrome of {0} is "{1}"'.format(value, n))
            print()
            break
