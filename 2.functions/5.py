# setting by optional field
def increment(number, by=1):
    return number+by


print(increment(3))  # print 4

# increment(number, by=1, another_number) This is wrong because optional parameter should be last
