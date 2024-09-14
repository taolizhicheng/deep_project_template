from module_name.scheduler import SCHEDULER_BUILDER


@SCHEDULER_BUILDER.register("BaseScheduler")
class BaseScheduler:
    def __init__(self, optimizer):
        self.optimizer = optimizer
        self.current_step = -1
    
    def step(self):
        self.current_step += 1
        # 此处根据current_step进行学习率的调整
        self._step()

    def _step(self):
        raise NotImplemented
