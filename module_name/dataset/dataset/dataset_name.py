from module_name.dataset.dataset import DATASET_BUILDER
from module_name.dataset.dataset.base import BaseDataset



@DATASET_BUILDER.register("DatasetName")
class DatasetName(BaseDataset):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __len__(self):
        # finish this function
        raise NotImplemented

    def _build_data(self, **kwargs):
        # finish this function
        pass

    def _get_data(self, index):
        # finish this function
        raise NotImplemented