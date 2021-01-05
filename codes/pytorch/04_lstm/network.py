import torch
from torch import nn, optim
from torch.nn import functional as F


class Model(nn.Module):
    def __init__(
        self,
        input_size=28,
        hidden_size=256,
        num_layers=3,
        num_classes=10,
        init_weight="he",
        init_bias="zero",
        device="cpu",
    ):
        super(Model, self).__init__()

        self.init_weight = init_weight
        self.init_bias = init_bias

        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, num_classes)

        self.init_params()

        self.device = device

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

    def forward(self, x):
        # Set initial hidden and cell states
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)

        out, _ = self.lstm(x, (h0, c0))

        out = self.linear(out[:, -1, :])
        return out
