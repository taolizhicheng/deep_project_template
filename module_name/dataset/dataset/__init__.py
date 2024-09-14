from module_name.utils.build import Builder


DATASET_BUILDER = Builder('DATASET')

DATASET_BUILDER.register_index('BaseDataset', "module_name.dataset.dataset.base", "BaseDataset")
DATASET_BUILDER.register_index('DatasetName', "module_name.dataset.dataset.dataset_name", "DatasetName")