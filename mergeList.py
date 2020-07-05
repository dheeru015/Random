import time
def fun(list1,list2):
    list1=sorted(list1,reverse=True)
    list2=sorted(list2,reverse=True)
    one_len=len(list1)-1
    two_len=len(list2)-1
    new_list=[]
    while one_len>=0 and two_len>=0:
        if list1[one_len]>list2[two_len]:
            new_list.append(list2[two_len])
            two_len-=1
        else:
            new_list.append(list1[one_len])
            one_len-=1
    while one_len>=0:
         new_list.append(list1[one_len])
         one_len-=1
    while two_len>=0:
         new_list.append(list2[two_len])
         two_len-=1     
    return new_list
if __name__=='__main__':
    list1=[81,62,11,17,13,19,2661,118,69,91,19,19,1895,97,97]
    list2=[100,91,42,99594,562,9,92,99,299,8,8,5,9,8,6,9,4]
    start=time.time()
    li=fun(list1,list2)
    print(li[::-1])
    end=time.time()
    print("time Taken",end-start)    