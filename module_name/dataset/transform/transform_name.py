from module_name.dataset.transform import TRANSFORM_BUILDER
from module_name.dataset.transform.base import BaseTransform


@TRANSFORM_BUILDER.register("TransformName")
class TransformName(BaseTransform):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __call__(self, data):
        # implement your transform here
        raise NotImplemented
