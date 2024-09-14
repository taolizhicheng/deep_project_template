from torch.optim import SGD

from module_name.optimizer import OPTIMIZER_BUILDER

OPTIMIZER_BUILDER.register('SGD', SGD)
