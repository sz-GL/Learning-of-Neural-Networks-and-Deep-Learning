import torch
#演示点乘
def demo1():
    t1=torch.tensor([[1,2,3],[3,4,5]])
    print(t1)
    t2=torch.tensor([[1,2,3],[3,4,5]])
    print(t2)
    t3 = t1 * t2
    print(t3)

#演示矩阵乘法
def demo2():
    t1=torch.tensor([[1,2,4],[3,4,5]])#两行三列
    t2=torch.tensor([[1,2],[3,4],[5,6]])#三行两列
    t3=t1@t2
    print(t3)






if __name__ == '__main__':
    #demo1()
    demo2()