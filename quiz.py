players=input("do you want play? ")

if players!="yes":
    quit()


print("okay lets play")
score=0

ans=input("what does cpu stand for? ")
if ans.lower() =="central processing unit":
    print('correct')
    score+=1
else:
    print('incorrect')

ans=input("what is gpu? ")
if ans.lower() =="graphics processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got " + str(score) + " queations correct")
print("you got " + str(score / 2 * 100) + "%.")