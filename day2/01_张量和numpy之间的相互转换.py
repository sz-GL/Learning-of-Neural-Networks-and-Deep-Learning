"""
演示张量和numpy之间如何相互转换，以及如何从标量张量中提取其内容

涉及到的api:
场景1：张量-numpy nd数组对象
张量对象.numpy()    共享内存
张量对象.numpy().copy()    不共享内存

场景2：numpy nd数组对象-张量
from_numpy()   共享内存
torch.tensor(nd数组)        不共享内存

场景3：从标量张量中提取其内容
标量张量.item()
"""

import torch
import numpy as np
#1.定义函数，演示：张量转numpy
def demo1():
    t1 = torch.tensor([1, 2, 3])
    print(t1,type(t1))
    n1 = t1.numpy()
    print(n1,type(n1))
    n1[0] = 100
    print(n1)
    print(t1)

#2.定义函数，演示：numpy转张量
def demo2():
    n1 = np.array([1, 2, 3])
    print(n1,type(n1))
    t1 = torch.from_numpy(n1)
    print(t1,type(t1))
    t2 = t1.type(torch.float32)
    print(t2,type(t2))


#3.定义函数，演示提取
def demo3():
    t1 = torch.tensor(100.3)
    print(t1,type(t1))
    value= t1.item()
    print(value,type(value))




#4.测试
if __name__ == '__main__':
    # demo1()
    # demo2()
    demo3()

