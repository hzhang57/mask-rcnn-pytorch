import torch.nn as nn
import torch.nn.functional as F
from libs.model.fpn import FPN101


class ResNet_101_FPN(nn.Module):
    """ResNet 101 FPN backbone feature map extractor.
    
    """
    def __init__(self, pretrained=None):
        super(ResNet_101_FPN, self).__init__()
        self.fpn = FPN101()

    def forward(self, x):
        """
        Args:
            x(Variable): input image 
        Returns:
            feature_pyramid(list): feature pyramid contains 5 feature maps.
        """
        p2, p3, p4, p5 = self.fpn(x)
        # Detectron style, use max pooling to simulate stride 2 subsampling
        p6 = F.max_pool2d(p5, kernel_size=1, stride=2)
        feature_pyramid = [p2, p3, p4, p5, p6]

        return feature_pyramid
