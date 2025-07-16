import torch.nn as nn
import torch.nn.functional as F

class TumorClassification(nn.Module):
    def __init__(self):
        super().__init__()
        self.con1d = nn.Conv2d(1, 32, 3, padding=1)
        self.con2d = nn.Conv2d(32, 64, 3, padding=1)
        self.con3d = nn.Conv2d(64, 128, 3, padding=1)
        self.pool  = nn.MaxPool2d(2, 2)
        self.fc1   = nn.Linear(128 * 28 * 28, 512)
        self.fc2   = nn.Linear(512, 256)
        self.output= nn.Linear(256, 4)

    def forward(self, x):
        x = self.pool(F.relu(self.con1d(x)))
        x = self.pool(F.relu(self.con2d(x)))
        x = self.pool(F.relu(self.con3d(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.output(x)

class GliomaStageModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(9, 100)
        self.fc2 = nn.Linear(100, 50)
        self.fc3 = nn.Linear(50, 30)
        self.out = nn.Linear(30, 4)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return self.out(x)
