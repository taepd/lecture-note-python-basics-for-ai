import torch
from torch import nn, optim
from torch.nn import functional as F


class Generator(nn.Module):
    def __init__(
        self, latent_size=100, output_size=784, init_weight="he", init_bias="zero"
    ):
        super(Generator, self).__init__()

        self.init_weight = init_weight
        self.init_bias = init_bias

        self.linear1 = nn.Linear(latent_size, 256)
        self.bnorm1 = nn.BatchNorm1d(256)
        self.linear2 = nn.Linear(256, 512)
        self.bnorm2 = nn.BatchNorm1d(512)
        self.linear3 = nn.Linear(512, output_size)

        self.init_params()

    def init_params(self):

        init_weight_method = {
            "he": nn.init.kaiming_normal_,
            "xavier": nn.init.xavier_normal_,
        }
        assert (
            self.init_weight in init_weight_method.keys()
        ), f"Select the weight initialization method in {list(init_weight_method.keys())}"

        init_bias_method = {"zero": nn.init.zeros_, "uniform": nn.init.uniform_}
        assert (
            self.init_bias in init_bias_method.keys()
        ), f"Select the bias initialization method in {list(init_bias_method.keys())}"

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                init_weight_method[self.init_weight](m.weight)
                init_bias_method[self.init_bias](m.bias)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, X):
        X = F.relu(self.bnorm1(self.linear1(X)))
        X = F.relu(self.bnorm2(self.linear2(X)))
        X = torch.tanh(self.linear3(X))
        return X


class Discriminator(nn.Module):
    def __init__(self, input_size=784, init_weight="he", init_bias="zero"):
        super(Discriminator, self).__init__()

        self.init_weight = init_weight
        self.init_bias = init_bias

        self.linear1 = nn.Linear(784, 256)
        self.linear2 = nn.Linear(256, 64)
        self.linear3 = nn.Linear(64, 1)

        self.init_params()

    def init_params(self):

        init_weight_method = {
            "he": nn.init.kaiming_normal_,
            "xavier": nn.init.xavier_normal_,
        }
        assert (
            self.init_weight in init_weight_method.keys()
        ), f"Select the weight initialization method in {list(init_weight_method.keys())}"

        init_bias_method = {"zero": nn.init.zeros_, "uniform": nn.init.uniform_}
        assert (
            self.init_bias in init_bias_method.keys()
        ), f"Select the bias initialization method in {list(init_bias_method.keys())}"

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                init_weight_method[self.init_weight](m.weight)
                init_bias_method[self.init_bias](m.bias)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, X):
        X = F.leaky_relu(self.linear1(X), 0.002)
        X = F.leaky_relu(self.linear2(X), 0.002)
        X = torch.sigmoid(self.linear3(X))
        return X
