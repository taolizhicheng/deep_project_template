import torch.nn as nn


from module_name.model import MODEL_BUILDER


@MODEL_BUILDER.register("BaseModel")
class BaseModel(nn.Module):
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__()
    
    def forward(self, *args, **kwargs):
        raise NotImplemented

