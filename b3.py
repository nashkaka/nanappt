a=[]
b=[]
c=[]
d=[]
def string(x):
    for i in x:
        if i.isdigit():
           a.append(i)
        elif i.isupper():
           b.append(i)
        elif i.islower():
            c.append(i)
        else:
           d.append(i)
    return a,b,c,d
n=input('请输入一个字符串：')
q,w,e,r=string(n)
print('大写字母的个数：{}'.format(len(q)))
print('小写字母的个数：{}'.format(len(w)))
print('数字的个数：{}'.format(len(e)))
print('其他数字的个数：{}'.format(len(r)))
q=tuple(q)
w=tuple(w)
e=tuple(e)
r=tuple(r)
print(q,w,e,r)

