from module_name.utils.build import Builder


METRIC_BUILDER = Builder('METRIC')

METRIC_BUILDER.register_index("BaseMetric", "module_name.metric.base", "BaseMetric")
METRIC_BUILDER.register_index("MetricName", "module_name.metric.metric_name", "MetricName")