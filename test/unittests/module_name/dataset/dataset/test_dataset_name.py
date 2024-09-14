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
            "name": "DatasetName",
            "args": {
            },
        }
        name = config["name"]
        args = config["args"]
        
        dataset = DATASET_BUILDER.build(name, **args)

        from module_name.dataset.dataset.dataset_name import DatasetName
        self.assertIsInstance(dataset, DatasetName)

    def test_build(self):
        from module_name.dataset.dataset.dataset_name import DatasetName

        dataset = DatasetName()
        self.assertIsInstance(dataset, DatasetName)


if __name__ == '__main__':
    unittest.main()