from dataclasses import dataclass


@dataclass
class Config:
    device: str
    EPOCHS: int
    TIMESTEPS: int
    INPUT_FEATURES: int
    BATCH_SIZE: int
    LEARNING_RATE: float
