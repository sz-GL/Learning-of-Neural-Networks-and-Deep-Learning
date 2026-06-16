'''涉及的api：
    cat()：不改变维度数，拼接张量，除了拼接的维度之外，其他维度必须相同
    stack()：会改变维度数，拼接张量，所有维度都必须相同
'''

import torch
t1 = torch.randint(1,10,(2,3))
print(t1)
t2 = torch.randint(1,10,(2,3))
print(t2)

