from module_name.loss import LOSS_BUILDER
from module_name.loss.base import BaseLoss


@LOSS_BUILDER.register("LossName")
class LossName(BaseLoss):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def forward(self, preds, labels):
        # TODO: implement loss function here
        raise NotImplemented
