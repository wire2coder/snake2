length = 10
what1 = length -1

# 'start at 0' index
x=[1,2,3,4,5,6,7,8,9,10]

# tell me why it's length-1 ?
# don't over-think, the answer is simple
for index in range(length-1, 0, -1):
    in2 = index-1
    x[index] = x[in2]

for index in range(0,5):
    asdf = index

print('debug wait')