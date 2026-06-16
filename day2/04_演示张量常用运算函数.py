import torch

t1=torch.tensor([
    [1,2,3],
    [4,5,6]
])
print(t1)

print(t1.sum(dim=0))#列求和
print(t1.sum(dim=1))#行求和
print(t1.sum())#全局求和
print("------------------")

print(t1.max(dim=0))#按列相加，求最大
print(t1.max(dim=1))#按行相加求最大
print(t1.max())#求矩阵内最大值
print("--------------------")

print(t1.mean(dim=0))#按列求平均
print(t1.mean(dim=1))#按行求平均
print(t1.mean())#整体求平均
print("*******************")

print(t1.pow(2))#每个数的平方
print(t1.sqrt())#每个数的开方
print(t1.log())#每个数的对数
print(t1.exp())#每个数的e的次方
print(t1.sin())#每个数的正弦
print(t1.log2())#每个数的对数