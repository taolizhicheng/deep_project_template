import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestBasePreprocessor(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.dataset.preprocessor import PREPROCESSOR_BUILDER
        config = {
            "name": "BasePreprocessor",
            "args": {},
        }
        name = config["name"]
        args = config["args"]
        
        preprocessor = PREPROCESSOR_BUILDER.build(name, **args)
        
        from module_name.dataset.preprocessor.base import BasePreprocessor
        self.assertIsInstance(preprocessor, BasePreprocessor)
    
    def test_build(self):
        from module_name.dataset.preprocessor.base import BasePreprocessor
        preprocessor = BasePreprocessor()
        self.assertIsInstance(preprocessor, BasePreprocessor)


if __name__ == "__main__":
    unittest.main()
