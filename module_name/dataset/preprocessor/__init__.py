from module_name.utils.build import Builder


PREPROCESSOR_BUILDER = Builder('PREPROCESSOR')
PREPROCESSOR_BUILDER.register_index('BasePreprocessor', "module_name.dataset.preprocessor.base", "BasePreprocessor")
PREPROCESSOR_BUILDER.register_index('PreprocessorName', "module_name.dataset.preprocessor.preprocessor_name", "PreprocessorName")