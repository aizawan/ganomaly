import os
import numpy as np
from PIL import Image
import glob

import torch
import torchvision
import torchvision.transforms as transforms


class MVTecAD(torchvision.datasets.MNIST):
    def __init__(self, root, category, train, transform=None):
        self.root = root
        self.category = category
        self.train = train
        self.transform = transform
        
        self.train_dir = os.path.join(root, category, 'train')
        self.test_dir = os.path.join(root, category, 'test')
        
        self.normal_class = ['good']
        self.abnormal_class = os.listdir(self.test_dir)
        self.abnormal_class.remove(self.normal_class[0])
        
        if train:
            img_paths = glob.glob(os.path.join(
                self.train_dir, self.normal_class[0], '*.png'))
            self.img_paths = sorted(img_paths)
            self.labels = len(self.img_paths) * [1]
        else:
            img_paths = []
            labels = []
            for c in os.listdir(self.test_dir):
                paths = glob.glob(os.path.join(
                    self.test_dir, c, '*.png'))
                img_paths.extend(sorted(paths))
                if c == self.normal_class[0]:
                    labels.extend(len(paths) * [1])
                else:
                    labels.extend(len(paths) * [0])
            
            self.img_paths = img_paths
            self.labels = labels     

    def __getitem__(self, index):
        img_path, target = self.img_paths[index], self.labels[index]

        img = Image.open(img_path).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)

        return img, target

    def __len__(self):
        return len(self.img_paths)
    
    

def main(isize=32, batchsize=49):
    transform = transforms.Compose([
        transforms.Resize(isize),
        transforms.CenterCrop(isize),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), ])
    
    dataset = MVTecAD(
        root='data/mvtec',
        category='metal_nut',
        train=True,
        transform=transform)
    
    loader = torch.utils.data.DataLoader(
        dataset=dataset,
        batch_size=batchsize,
        shuffle=False,
        num_workers=4,
        drop_last=True)
    
    for i, batch in enumerate(loader):
        imgs, labels = batch
        torchvision.utils.save_image(imgs, '{}-batch-{}.png'.format(category, i), nrow=7, normalize=True)
        print(imgs.shape, labels.shape)
    
    

if __name__ == '__main__':
    main()
    