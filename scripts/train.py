import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


from module_name.trainer.trainer import Trainer
from module_name.utils.load_config import load_config

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python train.py <config_file>")

    config_file = sys.argv[1]
    config = load_config(config_file)

    trainer = Trainer(config)
    trainer.train()


if __name__ == "__main__":
    main()
