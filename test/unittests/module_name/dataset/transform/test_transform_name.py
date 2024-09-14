import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestTransformName(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.dataset.transform import TRANSFORM_BUILDER
        config = {
            "name": "TransformName",
            "args": {},
        }
        name = config["name"]
        args = config["args"]
        transform = TRANSFORM_BUILDER.build(name, **args)
        from module_name.dataset.transform.transform_name import TransformName
        self.assertIsInstance(transform, TransformName)

    def test_build(self):
        from module_name.dataset.transform.transform_name import TransformName
        transform = TransformName()
        self.assertIsInstance(transform, TransformName)


if __name__ == "__main__":
    unittest.main()