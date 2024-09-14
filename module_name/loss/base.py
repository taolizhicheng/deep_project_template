import torch.nn as nn

from module_name.loss import LOSS_BUILDER


@LOSS_BUILDER.register("BaseLoss")
class BaseLoss(nn.Module):
    def __init__(self, **kwargs):
        super().__init__()

    def forward(self, preds, labels):
        raise NotImplemented
