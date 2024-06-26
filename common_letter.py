def common_letter():
    user1, user2 = input("enter the str:"), input("enter the str:")
    x, y = set(user1), set(user2)
    res = lambda x, y: x & y
    print(res(x, y))

common_letter()

def common_letter_word():
    try:
        user1,user2=input("enter the str"), input("enter the str")
        if not user1.isalpha() or not user2.isalpha():
            raise ValueError("enter input must be string")
        x,y=set(user1),set(user2)
        res=lambda x, y:x & y
        print(res(x,y))

    except ValueError as e:
        print("error is",e)

common_letter_word()


def common_word():
    try:
        user1, user2=input("enter str word:"), input("enter str word:")
        if not user1.isalpha() or not user2.isalpha():
            raise ValueError("enter input must be string")
        x, y=set(user1), set(user2)
        res = lambda x, y: x & y
        print(res(x, y))
    except ValueError as e:
        print("error is ", e)
common_word()

lst_items=[1,2,5,6,9,10]
def avereg_lst(lst_items):
    total=sum(lst_items)
    sum_el=len(lst_items)
    averge=total/sum_el
    return averge

result=avereg_lst(lst_items)
print(result,"RESULT IS")