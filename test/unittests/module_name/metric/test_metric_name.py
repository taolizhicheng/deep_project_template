import os
import sys
import unittest


sys.dont_write_bytecode = True

MODULE_DIR = os.environ.get('MODULE_DIR', None)
if MODULE_DIR is not None:
    sys.path = [MODULE_DIR] + sys.path
else:
    raise ValueError("MODULE_DIR environment variable not set!")


class TestMetricName(unittest.TestCase):
    def test_build_by_config(self):
        from module_name.metric import METRIC_BUILDER

        config = {
            "name": "MetricName",
            "args": {},
        }
        name = config["name"]
        args = config["args"]
        metric = METRIC_BUILDER.build(name, **args)

        from module_name.metric.metric_name import MetricName
        self.assertIsInstance(metric, MetricName)

    def test_build(self):
        from module_name.metric.metric_name import MetricName

        metric = MetricName()
        self.assertIsInstance(metric, MetricName)


if __name__ == "__main__":
    unittest.main()
