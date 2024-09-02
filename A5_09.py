my_tuple = tuple(input("Enter comma-separated numbers: ").split(","))
sum_num=0
for i in my_tuple:
    sum_num=sum_num+i
mean = sum_num / len(my_tuple)
print("Mean:", mean)
