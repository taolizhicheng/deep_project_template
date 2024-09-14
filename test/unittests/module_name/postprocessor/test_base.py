import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")



class TestBasePostprocessor(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.postprocessor import POSTPROCESSOR_BUILDER

        config = {
            "name": "BasePostprocessor",
            "args": {},
        }
        
        name = config["name"]
        args = config["args"]
        postprocessor = POSTPROCESSOR_BUILDER.build(name, **args)

        from module_name.postprocessor.base import BasePostprocessor
        self.assertIsInstance(postprocessor, BasePostprocessor)
    
    def test_build(self):
        from module_name.postprocessor.base import BasePostprocessor

        postprocessor = BasePostprocessor()
        self.assertIsInstance(postprocessor, BasePostprocessor)


if __name__ == "__main__":
    unittest.main()
