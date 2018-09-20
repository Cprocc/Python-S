import  string
# print (s.count('s[i]'))
s = input( ).split(' ')
len =int(s[0])
quCount = int(s[1])
strings = input()
question=[]
for i in range(quCount):
    question.append(int(input()))
for i in range(quCount):
    print(strings[0:i+1].count(strings[int(question[i]-1)],0,i+1))

# for j in range(quCount):
#     print(strings.count(strings[question[j]],0,j+1))
