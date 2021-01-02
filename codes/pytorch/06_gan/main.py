import argparse

import numpy as np
import torch
from torch import nn, optim
from torchvision import datasets, transforms

from tqdm import tqdm
import matplotlib.pyplot as plt

from config import Config
from network import Generator, Discriminator

SEED = 42
torch.manual_seed(SEED)

# Config Parsing
def get_config():
    parser = argparse.ArgumentParser(description="Multi-layer perceptron")
    parser.add_argument("--epochs", default=10, type=int)
    parser.add_argument("--latent_size", default=100, type=int)
    parser.add_argument("--batch_size", default=256, type=int)
    parser.add_argument("--lr", default=0.001, type=float)

    args = parser.parse_args()

    config = Config(
        EPOCHS=args.epochs,
        LATENT_SIZE=args.latent_size,
        BATCH_SIZE=args.batch_size,
        LEARNING_RATE=args.lr,
        device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
    )

    return config


# MNIST dataset
def get_mnist(BATCH_SIZE: int):
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize(mean=[0.5], std=[0.5])]
    )

    mnist_train = datasets.MNIST(
        root="./data/", train=True, transform=transform, download=True
    )
    mnist_test = datasets.MNIST(
        root="./data/", train=False, transform=transform, download=True
    )

    train_iter = torch.utils.data.DataLoader(
        mnist_train, batch_size=BATCH_SIZE, shuffle=True, num_workers=1
    )
    test_iter = torch.utils.data.DataLoader(
        mnist_test, batch_size=BATCH_SIZE, shuffle=True, num_workers=1
    )

    return train_iter, test_iter


# Defining Model
def get_network(LEARNING_RATE: float, device: str):
    G = Generator().to(device)
    D = Discriminator().to(device)

    criterion = nn.BCELoss()
    d_optimizer = optim.Adam(D.parameters(), lr=LEARNING_RATE)
    g_optimizer = optim.Adam(G.parameters(), lr=LEARNING_RATE)

    return G, D, criterion, d_optimizer, g_optimizer


# Print Model Info
def print_modelinfo(G: nn.Module, D: nn.Module):
    G_params = 0
    for param_name, param in G.named_parameters():
        if param.requires_grad:
            G_params += len(param.reshape(-1))
    print(f"Number of Generator's Parameters: {G_params:,d}")

    D_params = 0
    for param_name, param in D.named_parameters():
        if param.requires_grad:
            D_params += len(param.reshape(-1))
    print(f"Number of Discriminator's Parameters: {D_params:,d}")


# Define help function
def plot_generator(
    gen_model: nn.Module, num: int = 10, latent_size: int = 100, device: str = "cpu"
):
    z = torch.randn(num, latent_size).to(device)

    gen_model.eval()
    test_g = gen_model.forward(z)
    gen_model.train()

    plt.figure(figsize=(8, 2))
    for i in range(num):
        plt.subplot(1, num, i + 1)
        plt.imshow(test_g[i].view(28, 28).data.cpu().numpy(), cmap=plt.cm.gray)
        plt.axis("off")
    plt.show()


# Train MLP Model
def train_model(
    G: nn.Module,
    D: nn.Module,
    train_iter,
    test_iter,
    EPOCHS: int,
    BATCH_SIZE: int,
    LATENT_SIZE: int,
    device: str,
):
    # Training Phase
    print_every = 1
    plot_every = 5
    print("Start training !")

    # Training loop
    for epoch in range(EPOCHS):
        total = 0
        g_loss_val_sum = 0
        d_loss_val_sum = 0
        for batch_img, _ in train_iter:

            X = batch_img.view(batch_img.size(0), -1).to(device)

            real_lab = torch.ones(batch_img.size(0), 1).to(device)

            fake_lab = torch.zeros(batch_img.size(0), 1).to(device)

            # Training Discriminator
            D_pred = D.forward(X)
            d_loss_real = criterion(D_pred, real_lab)

            z = torch.randn(batch_img.size(0), LATENT_SIZE).to(device)

            fake_images = G.forward(z)
            G_pred = D.forward(fake_images)
            d_loss_fake = criterion(G_pred, fake_lab)

            d_loss = (d_loss_real + d_loss_fake) / 2.0
            d_loss_val_sum += d_loss

            d_optimizer.zero_grad()
            d_loss.backward()
            d_optimizer.step()

            # Training Generator
            z = torch.randn(batch_img.size(0), LATENT_SIZE).to(device)
            fake_images = G.forward(z)
            G_pred = D.forward(fake_images)
            g_loss = criterion(G_pred, real_lab)
            g_loss_val_sum += g_loss

            g_optimizer.zero_grad()
            g_loss.backward()
            g_optimizer.step()

            total += X.size(0)

        if (((epoch + 1) % print_every) == 0) or ((epoch + 1) == (EPOCHS - 1)):
            print(
                f"Epoch: {epoch+1}, G_loss: {g_loss_val_sum/total}, D_loss: {d_loss_val_sum/total}"
            )
        if (((epoch + 1) % plot_every) == 0) or ((epoch + 1) == (EPOCHS - 1)):
            plot_generator(G, num=10, latent_size=LATENT_SIZE, device=device)
    print("Training Done !")


if __name__ == "__main__":
    print("PyTorch version:[%s]." % (torch.__version__))

    config = get_config()
    print("This code use [%s]." % (config.device))

    train_iter, test_iter = get_mnist(config.BATCH_SIZE)
    print("Preparing dataset done!")

    G, D, criterion, d_optimizer, g_optimizer = get_network(
        config.LEARNING_RATE, config.device
    )
    print_modelinfo(G, D)

    train_model(
        G,
        D,
        train_iter,
        test_iter,
        config.EPOCHS,
        config.BATCH_SIZE,
        config.LATENT_SIZE,
        config.device,
    )
