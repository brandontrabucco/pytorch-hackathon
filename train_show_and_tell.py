import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as dsts
from torchvision.datasets.coco import CocoCaptions

if __name__ == "__main__":
    
    dataset = CocoCaptions(
        root="images/",
        annFile='annotations.json',
        transform=transforms.ToTensor())
    
    print("Loaded.")