import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestPostprocessorName(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.postprocessor import POSTPROCESSOR_BUILDER

        config = {
            "name": "PostprocessorName",
            "args": {},
        }
        
        name = config["name"]
        args = config["args"]
        postprocessor = POSTPROCESSOR_BUILDER.build(name, **args)

        from module_name.postprocessor.postprocessor_name import PostprocessorName
        self.assertIsInstance(postprocessor, PostprocessorName)
    
    def test_build(self):
        from module_name.postprocessor.postprocessor_name import PostprocessorName
        postprocessor = PostprocessorName()
        self.assertIsInstance(postprocessor, PostprocessorName)


if __name__ == "__main__":
    unittest.main()