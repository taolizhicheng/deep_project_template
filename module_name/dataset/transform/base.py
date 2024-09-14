from module_name.dataset.transform import TRANSFORM_BUILDER


@TRANSFORM_BUILDER.register("BaseTransform")
class BaseTransform:
    def __init__(self, **kwargs):
        pass

    def __call__(self, data):
        raise NotImplemented
