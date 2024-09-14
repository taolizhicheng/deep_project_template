import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestBaseModel(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.model import MODEL_BUILDER
        config = {
            "name": "BaseModel",
            "args": {},
        }
        name = config["name"]
        args = config["args"]
        model = MODEL_BUILDER.build(name, **args)

        from module_name.model.base import BaseModel
        self.assertIsInstance(model, BaseModel)
    
    def test_build(self):
        from module_name.model.base import BaseModel
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)


if __name__ == "__main__":
    unittest.main()