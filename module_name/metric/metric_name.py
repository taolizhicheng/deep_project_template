from module_name.metric import METRIC_BUILDER
from module_name.metric.base import BaseMetric


@METRIC_BUILDER.register("MetricName")
class MetricName(BaseMetric):
    def __init__(self, **kwargs):
        super(MetricName, self).__init__()

    def reset(self):
        # clear cache and reset the metric
        pass
    
    def accumulate(self, preds, labels):
        # accumulate result to the cache
        pass
    
    def compute(self):
        # compute the metric
        pass

    @property
    def name(self):
        return "MetricName"

    