#学号：202410111420
#登陆邮箱：15181957072@163.com
#姓名：王庭宝
def Change(x: list) -> list:
    a = []
    for i in range(len(x) - 1):
        a.append(((x[i] + x[i+1]) % 10))
    return a
a=[1,2,3,4,5,]
if len(a) == 1:
    print(a[0])
else:
    for _ in range(len(a)-1):
        a=Change(a)
print(a)
