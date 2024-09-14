from module_name.postprocessor import POSTPROCESSOR_BUILDER


@POSTPROCESSOR_BUILDER.register("BasePostprocessor")
class BasePostprocessor:
    def __init__(self):
        pass

    def __call__(self, data):
        raise NotImplemented
