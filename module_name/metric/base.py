from module_name.metric import METRIC_BUILDER


@METRIC_BUILDER.register("BaseMetric")
class BaseMetric(object):
    def __init__(self):
        pass

    def reset(self):
        raise NotImplemented

    def accumulate(self, preds, labels):
        raise NotImplemented

    def compute(self):
        raise NotImplemented

    @property
    def name(self):
        raise NotImplemented