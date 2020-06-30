import torch
# what is Tensor
# Tensor 可以看作是一个多维数组
# 标量是0维向量，向量是1维，矩阵是2维
x1 = torch.empty(5, 3) # 创建5行3列的未初始化Tensor
x2 = torch.rand(5, 3) # 创建5行3列的随机Tensor
x3 = torch.ones(5, 3) # 看代码即可知
x4 = torch.tensor([5.5, 4])
x5 = torch.ones_like(x3,dtype=torch.long)
x6 = x3 + x3
x3.add_(x6) # add in place pytorch 的inplace 版本都有后缀_
# index 索引
print(x3)
x = x3[0, :]
x += 1
print(x3[0, :])
# 改变Tensor的size
y = x3.view(15)
z = x3.view(-1, 3)
print(z)
x = torch.randn(1)
print(x)
print(x.item())


