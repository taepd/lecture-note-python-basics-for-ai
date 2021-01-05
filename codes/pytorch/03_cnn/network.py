from torch import nn, optim
from torch.nn import functional as F


class Model(nn.Module):
    def __init__(
        self,
        input_size=[1, 28, 28],
        hidden_size=[32, 64],
        num_classes=10,
        init_weight="he",
        init_bias="zero",
    ):
        super(Model, self).__init__()

        self.init_weight = init_weight
        self.init_bias = init_bias

        layer_list = []
        prev_channel = input_size[0]

        for idx in range(len(hidden_size)):
            layer_list.append(
                nn.Conv2d(
                    prev_channel, hidden_size[idx], kernel_size=3, stride=1, padding=1
                )
            )
            layer_list.append(nn.BatchNorm2d(hidden_size[idx]))
            layer_list.append(nn.ReLU(True))
            layer_list.append(nn.MaxPool2d(kernel_size=2, stride=2))
            prev_channel = hidden_size[idx]

        layer_list.append(nn.Flatten())
        feature_size = int(input_size[1] / 2 ** len(hidden_size))
        layer_list.append(nn.Linear(feature_size * feature_size * prev_channel, 10))

        self.net = nn.Sequential(*layer_list)

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
        return self.net(X)
