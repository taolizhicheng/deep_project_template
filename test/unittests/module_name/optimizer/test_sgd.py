import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestSGD(unittest.TestCase):
    def test_build_by_config(self):
        import torch
        from module_name.optimizer import OPTIMIZER_BUILDER

        model = torch.nn.Linear(10, 10)
        config = {
            "name": "SGD",
            "args": {
                "params": model.parameters(),
            },
        }
        name = config["name"]
        args = config["args"]
        optimizer = OPTIMIZER_BUILDER.build(name, **args)
        self.assertIsInstance(optimizer, torch.optim.SGD)
    
    def test_build(self):
        import torch
        from module_name.optimizer.sgd import SGD

        model = torch.nn.Linear(10, 10)
        optimizer = SGD(model.parameters(), lr=0.01)
        self.assertIsInstance(optimizer, SGD)

if __name__ == '__main__':
    unittest.main()
