from dataclasses import dataclass


@dataclass
class Config:
    device: str
    EPOCHS: int
    LATENT_SIZE: int
    BATCH_SIZE: int
    LEARNING_RATE: float
