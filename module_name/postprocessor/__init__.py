from module_name.utils.build import Builder


POSTPROCESSOR_BUILDER = Builder("POSTPROCESSOR")
POSTPROCESSOR_BUILDER.register_index("BasePostprocessor", "module_name.postprocessor.base", "BasePostprocessor")
POSTPROCESSOR_BUILDER.register_index("PostprocessorName", "module_name.postprocessor.postprocessor_name", "PostprocessorName")