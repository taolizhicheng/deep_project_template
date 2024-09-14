from module_name.utils.build import Builder


OPTIMIZER_BUILDER = Builder('OPTIMIZER')
OPTIMIZER_BUILDER.register_index('SGD', "module_name.optimizer.sgd", "SGD")