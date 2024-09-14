from module_name.dataset.preprocessor import PREPROCESSOR_BUILDER
from module_name.dataset.preprocessor.base import BasePreprocessor


@PREPROCESSOR_BUILDER.register("PreprocessorName")
class PreprocessorName(BasePreprocessor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __call__(self, data):
        # implement your preprocessor here
        return data
