num = input()
num = num.split()
int_num = list(map(int, num))

squ_num = []

for i in range(len(int_num)):
  squ_num.append(int_num[i] ** 2)

squ_num_sum = sum(squ_num)
rest = squ_num_sum % 10
print(rest) # 검증수