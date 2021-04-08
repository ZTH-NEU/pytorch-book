import torch
import os

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.backends.cudnn.version())

name = 'checkpoints\\' + '1234.pth'
print(name)
torch.save([1,2],name)

#
# root = 'E:\\test_mini\\'
# imgs = [os.path.join(root, img) for img in os.listdir(root)]
# print(imgs)
# imgs = sorted(imgs, key=lambda x: int(x.split('.')[-2].split('/')[-1]))
# print(imgs)


a = 'E:\\test_mini\\1.jpg'
print(a)
b = int(a.split('.')[-2].split('\\')[-1])
print(b)
