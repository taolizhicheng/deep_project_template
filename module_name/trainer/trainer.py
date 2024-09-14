import torch
from torch.utils.tensorboard import SummaryWriter

from module_name.dataset.dataset import DATASET_BUILDER
from module_name.model import MODEL_BUILDER
from module_name.loss import LOSS_BUILDER
from module_name.optimizer import OPTIMIZER_BUILDER
from module_name.scheduler import SCHEDULER_BUILDER


class Trainer:
    def __init__(self, config: dict):
        self.config = config
        self.device = torch.device(config["HYPER_PARAMETERS"]["DEVICE"])
        self.train_dataloader = self._build_train_dataloader()
        self.test_dataloader = self._build_test_dataloader()
        self.model = self._build_model()
        self.loss = self._build_loss()
        self.optimizer = self._build_optimizer()
        self.scheduler = self._build_scheduler()
        self.postprocessor = self._build_postprocessor()
        self.metric = self._build_metric()

        self.summary_writer = SummaryWriter(self.config["HYPER_PARAMETERS"]["SUMMARY_DIR"])

    def train(self):
        epochs = self.config["HYPER_PARAMETERS"]["TRAIN"]["EPOCHS"]
        for epoch in range(epochs):
            self.model.train()
            for idx, (datas, labels) in enumerate(self.train_dataloader):
                datas = datas.to(self.device)
                labels = labels.to(self.device)
                outputs = self.model(datas)
                loss = self.loss(outputs, labels)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                self.scheduler.step()

                self.summary_writer.add_scalar("loss", loss.item(), epoch * len(self.train_dataloader) + idx)
            
            test_epochs = self.config["HYPER_PARAMETERS"]["TEST"]["TEST_EPOCHS"]
            if epoch % test_epochs == test_epochs - 1:
                self.test(epoch)

    def test(self, epoch):
        self.metric.reset()
        self.model.eval()
        with torch.no_grad():
            for idx, (datas, labels) in enumerate(self.test_dataloader):
                datas = datas.to(self.device)
                labels = labels.to(self.device)
                outputs = self.model(datas)
                outputs = self.postprocessor(outputs)
                self.metric.accumulate(outputs, labels)
        self.metric.compute()
        self.summary_writer.add_scalar("metric", self.metric.value, epoch)

    def _build_train_dataloader(self):
        train_dataset_config = self.config["DATASET"]["TRAIN"]
        name = train_dataset_config["NAME"]
        args = train_dataset_config["ARGS"]
        dataset = DATASET_BUILDER.build(name, args)

        batch_size = self.config["HYPER_PARAMETERS"]["TRAIN"]["BATCH_SIZE"]
        shuffle = self.config["HYPER_PARAMETERS"]["TRAIN"]["SHUFFLE"]
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
        return dataloader


    def _build_test_dataloader(self):
        test_dataset_config = self.config["DATASET"]["TEST"]
        name = test_dataset_config["NAME"]
        args = test_dataset_config["ARGS"]
        dataset = DATASET_BUILDER.build(name, args)

        batch_size = self.config["HYPER_PARAMETERS"]["TEST"]["BATCH_SIZE"]
        shuffle = self.config["HYPER_PARAMETERS"]["TEST"]["SHUFFLE"]
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
        return dataloader

    def _build_model(self):
        model_config = self.config["MODEL"]
        name = model_config["NAME"]
        args = model_config["ARGS"]
        model = MODEL_BUILDER.build(name, args)
        model.to(self.device)
        return model
    
    def _build_loss(self):
        loss_config = self.config["LOSS"]
        name = loss_config["NAME"]
        args = loss_config["ARGS"]
        loss = LOSS_BUILDER.build(name, args)
        return loss
    
    def _build_optimizer(self):
        optimizer_config = self.config["OPTIMIZER"]
        name = optimizer_config["NAME"]
        args = optimizer_config["ARGS"]
        optimizer = OPTIMIZER_BUILDER.build(name, args)
        return optimizer
    
    def _build_scheduler(self):
        scheduler_config = self.config["SCHEDULER"]
        name = scheduler_config["NAME"]
        args = scheduler_config["ARGS"]
        args["optimizer"] = self.optimizer
        scheduler = SCHEDULER_BUILDER.build(name, args)
        return scheduler

    def _build_postprocessor(self):
        postprocessor_config = self.config["POSTPROCESSOR"]
        name = postprocessor_config["NAME"]
        args = postprocessor_config["ARGS"]
        postprocessor = POSTPROCESSOR_BUILDER.build(name, args)
        return postprocessor

    def _build_metric(self):
        metric_config = self.config["METRIC"]
        name = metric_config["NAME"]
        args = metric_config["ARGS"]
        metric = METRIC_BUILDER.build(name, args)
        return metric

