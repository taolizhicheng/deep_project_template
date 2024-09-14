import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestLossName(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.loss import LOSS_BUILDER
        config = {
            "name": "LossName",
            "args": {},
        }
        name = config["name"]
        args = config["args"]
        loss = LOSS_BUILDER.build(name, **args)
        
        from module_name.loss.loss_name import LossName
        self.assertIsInstance(loss, LossName)

    def test_build(self):
        from module_name.loss.loss_name import LossName
        loss = LossName()
        self.assertIsInstance(loss, LossName)


if __name__ == "__main__":
    unittest.main()