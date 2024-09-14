from module_name.utils.build import Builder

LOSS_BUILDER = Builder("LOSS")
LOSS_BUILDER.register_index("BaseLoss", "module_name.loss.base", "BaseLoss")
LOSS_BUILDER.register_index("LossName", "module_name.loss.loss_name", "LossName")