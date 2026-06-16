import torch

t1=torch.tensor([1,2,3])#演示加法
t2=t1.add(12)
print(t1)
print(t2)

#演示减法
t3=t1.sub(12)
#演示乘法
t4=t1.mul(12)
#演示除法
t5=t1.div(12)
print(t3)
print(t4)
print(t5)