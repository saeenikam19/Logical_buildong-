import matplotlib.pyplot as m

a=input("Enter a sentence ")
count=0

for i in a:
    if i != " ":
        count=count+1
print("total characters: ",count)

word=a.split()
count1=len(word)
print("total word: ",count1)

a="I love python"
word=a.split()
word.reverse()
print(word)

for i in range(1,51):
    if i%2==0:
        print(i)