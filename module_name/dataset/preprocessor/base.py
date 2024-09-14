from module_name.dataset.preprocessor import PREPROCESSOR_BUILDER


@PREPROCESSOR_BUILDER.register("BasePreprocessor")
class BasePreprocessor:
    def __init__(self, **kwargs):
        pass

    def __call__(self, data):
        raise NotImplemented
