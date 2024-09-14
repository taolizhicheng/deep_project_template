from module_name.utils.build import Builder

MODEL_BUILDER = Builder("MODEL")

MODEL_BUILDER.register_index("BaseModel", "module_name.model.base", "BaseModel")
MODEL_BUILDER.register_index("ModelName", "module_name.model.model_name", "ModelName")
