from module_name.model import MODEL_BUILDER
from module_name.model.base import BaseModel


@MODEL_BUILDER.register("ModelName")
class ModelName(BaseModel):
    def __init__(self, *args, **kwargs):
        super(ModelName, self).__init__(*args, **kwargs)
    
    def forward(self, data):
        # implement forward function
        return data
