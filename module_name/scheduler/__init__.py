from module_name.utils.build import Builder


SCHEDULER_BUILDER = Builder('SCHEDULER')
SCHEDULER_BUILDER.register_index("BaseScheduler", "module_name.scheduler.base", "BaseScheduler")
SCHEDULER_BUILDER.register_index("SchedulerName", "module_name.scheduler.scheduler_name", "SchedulerName")