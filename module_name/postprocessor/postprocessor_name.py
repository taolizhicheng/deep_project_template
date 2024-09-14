from module_name.postprocessor import POSTPROCESSOR_BUILDER
from module_name.postprocessor.base import BasePostprocessor


@POSTPROCESSOR_BUILDER.register("PostprocessorName")
class PostprocessorName(BasePostprocessor):
    def __init__(self, **kwargs):
        super(PostprocessorName, self).__init__(**kwargs)

    def __call__(self, data):
        # implement postprocessing logic here
        raise NotImplemented
