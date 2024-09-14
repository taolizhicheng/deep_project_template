import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestSchedulerName(unittest.TestCase):
    def test_build_by_config(self):
        import torch
        from module_name.scheduler import SCHEDULER_BUILDER

        model = torch.nn.Linear(10, 10)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
        config = {
            "name": "SchedulerName",
            "args": {
                "optimizer": optimizer,
            },
        }
        name = config["name"]
        args = config["args"]
        scheduler = SCHEDULER_BUILDER.build(name, **args)
        from module_name.scheduler.scheduler_name import SchedulerName
        self.assertIsInstance(scheduler, SchedulerName)
        scheduler.step()
        self.assertEqual(scheduler.current_step, 0)
    
    def test_build(self):
        import torch
        from module_name.scheduler.scheduler_name import SchedulerName

        model = torch.nn.Linear(10, 10)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
        scheduler = SchedulerName(optimizer)
        self.assertIsInstance(scheduler, SchedulerName)
        scheduler.step()
        self.assertEqual(scheduler.current_step, 0)
    

if __name__ == "__main__":
    unittest.main()