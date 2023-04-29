def prime_num_generator(value):
    for i in range(value):
        yield i+1
 
for i in prime_num_generator(10):
    print(i)