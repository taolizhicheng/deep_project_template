from module_name.scheduler import SCHEDULER_BUILDER
from module_name.scheduler.base import BaseScheduler



@SCHEDULER_BUILDER.register("SchedulerName")
class SchedulerName(BaseScheduler):
    def __init__(self, optimizer, **kwargs):
        super().__init__(optimizer)
        self.kwargs = kwargs
    
    def _step(self):
        # implement the logic of the scheduler according to the kwargs and current_step
        pass