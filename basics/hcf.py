# Find HCF of 2 numbers

num1 = 14
num2 = 49


# step1 : find factors function
def find_factors(num):
    fact_num = []
    for n in range(1, num + 1):
        if num % n == 0:
            fact_num.append(n)
    return fact_num


fact_num1 = find_factors(num1)
fact_num2 = find_factors(num2)
print(fact_num1)
print(fact_num2)


def find_hcf(fact1, fact2):
    hcf = None
    for x in fact1:
        if fact2.__contains__(x):
            hcf = x
    return hcf


print("HCF of %d and %d is: %d" % (num1, num2, find_hcf(fact_num1, fact_num1)))
