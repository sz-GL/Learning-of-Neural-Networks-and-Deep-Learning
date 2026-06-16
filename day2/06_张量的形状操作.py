""""
涉及到的api：
   reshape()：改变数组的形状
   transpose()：转置数组
   squeeze()：去掉数组中维度为1的轴
    unsqueeze()：在指定位置插入一个维度为1的轴
    permute()：改变数组的维度顺序
    view()：改变数组的形状，但不改变数据的存储方式
    contiguous()：返回一个内存连续的数组
    is_contiguous()：检查数组是否是内存连续的

"""
import torch
torch.manual_seed(24)
#1.演示reshape()函数
def demo1():
    t1=torch.randint(1,10,size=(2,3))
    print(t1,t1.shape,t1.shape[0])
    t2=t1.reshape(3,2)
    print(t2,t2.shape)

#2.演示transpose()函数，一次交换两个维度
def demo2():
    t1=torch.randint(1,10,size=(2,3,4))
    print(t1,t1.shape)
    t2=t1.transpose(0,1)
    print(t2,t2.shape)

#3.演示squeeze()函数
#4.演示unsqueeze()函数
def demo4():
    t1=torch.randint(1,10,size=(2,3))
    print(t1,t1.shape)
    t2=t1.unsqueeze(0)
    print(t2,t2.shape)
    t3=t1.unsqueeze(1)
    print(t3,t3.shape)
    t4=t1.unsqueeze(2)
    print(t4,t4.shape)
    t5=torch.randint(1,10,size=(2,1,3,1,1))
    print(t5,t5.shape)
    t6=t5.squeeze()
    print(t6,t6.shape)
#5.演示permute()函数，一次可以交换多个维度
def demo5():
    t1=torch.randint(1,10,size=(2,3,4))
    print(t1,t1.shape)
    t2=t1.permute(2,0,1)
    print(t2,t2.shape)

#6.演示view()函数,只能修改连续的张量的形状
def demo6():
    t1=torch.randint(1,10,size=(2,3))
    print(t1,t1.shape)
    #print(t1.is_contiguous())
    t2=t1.view(3,2)
    print(t2,t2.shape)
    print(t2.is_contiguous())
    t3=t1.transpose(0,1)
    print(t3,t3.shape)
    print(t3.is_contiguous())
    #t4=t3.view(2,3),不可以,因为t3不连续
    t5= t3.contiguous().view(2,3)
    print(t5,t5.shape)
#7.演示contiguous()函数，把不连续张量变成连续的，
#8.演示is_contiguous()函数，判断张量是否连续
#测试
if __name__=="__main__":
      #demo1()
    #demo2()
    # demo4()
    #demo5()
    demo6()

