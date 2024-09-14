import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestBaseTransform(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.dataset.transform import TRANSFORM_BUILDER
        config = {
            "name": "BaseTransform",
            "args": {},
        }
        name = config["name"]
        args = config["args"]
        transform = TRANSFORM_BUILDER.build(name, **args)
        
        from module_name.dataset.transform.base import BaseTransform
        self.assertIsInstance(transform, BaseTransform)
    
    def test_build(self):
        from module_name.dataset.transform.base import BaseTransform
        transform = BaseTransform()
        self.assertIsInstance(transform, BaseTransform)


if __name__ == "__main__":
    unittest.main()
