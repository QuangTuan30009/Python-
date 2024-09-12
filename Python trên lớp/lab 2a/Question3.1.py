
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
sum_result = recursive_sum(10)
print(sum_result)
def display(name,age):
    print(name,age)
    print(name,age)
    return
display("Emma",26)
i=list(range(4,30,2))
print(i)