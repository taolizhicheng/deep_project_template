from module_name.utils.build import Builder


TRANSFORM_BUILDER = Builder('TRANSFORM')
TRANSFORM_BUILDER.register_index('BaseTransform', "module_name.dataset.transform.base", "BaseTransform")
TRANSFORM_BUILDER.register_index('TransformName', "module_name.dataset.transform.transform_name", "TransformName")