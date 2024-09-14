from typing import List

from torch.utils.data import Dataset
from module_name.dataset.dataset import DATASET_BUILDER
from module_name.dataset.preprocessor import PREPROCESSOR_BUILDER
from module_name.dataset.transform import TRANSFORM_BUILDER


@DATASET_BUILDER.register("BaseDataset")
class BaseDataset(Dataset):
    def __init__(self, **kwargs):
        super().__init__()
        
        preprocessor = kwargs.get("preprocessor", None)
        transforms = kwargs.get("transforms", None)
        self.preprocessor = self._build_preprocessor(preprocessor)
        self.transforms = self._build_transforms(transforms)

        self._build_data(**kwargs)

    def __len__(self):
        raise NotImplemented

    def __getitem__(self, index):
        data, label = self._get_data(index)
        if self.preprocessor is not None:
            data = self.preprocessor(data)
        if self.transforms is not None:
            for transform in self.transforms:
                data = transform(data)
        return data, label

    def _build_preprocessor(self, preprocessor: dict):
        if preprocessor is None:
            return None

        name = preprocessor.get("name")
        args = preprocessor.get("args")
        return PREPROCESSOR_BUILDER.build(name, **args)

    def _build_transforms(self, transforms: List[dict]):
        if transforms is None:
            return []

        transform_list = []
        for transform in transforms:
            name = transform.get("name")
            args = transform.get("args", {})
            transform_list.append(TRANSFORM_BUILDER.build(name, **args))
        return transform_list

    def _build_data(self, **kwargs):
        pass

    def _get_data(self, index):
        raise NotImplemented
