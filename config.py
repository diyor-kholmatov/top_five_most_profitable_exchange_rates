from dataclasses import dataclass

@dataclass()
class Config:
    with open('config_tokens.txt', 'r') as file:
        value = file.read().strip()
    token: str = value