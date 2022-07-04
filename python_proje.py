katList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatList=[]

def flatten(n):
    for index in n:
        if isinstance(index,list):
            flatten(index)
        else:
            flatList.append(index)

flatten(katList)

print(flatList)