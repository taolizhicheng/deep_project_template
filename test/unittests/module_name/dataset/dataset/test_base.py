import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestDatasetName(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.dataset.dataset import DATASET_BUILDER
        config = {
            "name": "BaseDataset",
            "args": {
            },
        }
        name = config["name"]
        args = config["args"]

        dataset = DATASET_BUILDER.build(name, **args)

        from module_name.dataset.dataset.base import BaseDataset
        self.assertIsInstance(dataset, BaseDataset)
        self.assertRaises(Exception, dataset.__len__)
        self.assertRaises(Exception, dataset.__getitem__)

    def test_build(self):
        from module_name.dataset.dataset.base import BaseDataset
        dataset = BaseDataset()
        self.assertIsInstance(dataset, BaseDataset)
        self.assertRaises(Exception, dataset.__len__)
        self.assertRaises(Exception, dataset.__getitem__)


if __name__ == '__main__':
    unittest.main()
