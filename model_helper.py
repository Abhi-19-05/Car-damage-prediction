import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image
import os
from collections import OrderedDict


trained_model = None

class_names = [
    'Front Breakage',
    'Front Crushed',
    'Front Normal',
    'Rear Breakage',
    'Rear Crushed',
    'Rear Normal'
]


class CarClassifierResNet(nn.Module):

    def __init__(self, num_classes=6):
        super().__init__()

        self.model = models.resnet50(weights=None)

        for param in self.model.parameters():
            param.requires_grad = False

        for param in self.model.layer4.parameters():
            param.requires_grad = True

        self.model.fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(self.model.fc.in_features, num_classes)
        )


    def forward(self, x):
        return self.model(x)



transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])


def predict(image_input):

    global trained_model


    # Handle Streamlit uploaded image
    if isinstance(image_input, str):
        image = Image.open(image_input)

    else:
        image = Image.open(image_input)


    # Ensure RGB format
    image = image.convert("RGB")


    image_tensor = transform(image).unsqueeze(0)



    if trained_model is None:

        trained_model = CarClassifierResNet()

        model_path = os.path.join(
            os.path.dirname(__file__),
            "model",
            "saved_model.pth"
        )


        state_dict = torch.load(
            model_path,
            map_location=torch.device("cpu")
        )


        if any(k.startswith("module.") for k in state_dict.keys()):

            new_state_dict = OrderedDict()

            for k,v in state_dict.items():
                new_state_dict[
                    k.replace("module.","")
                ] = v

            state_dict = new_state_dict



        trained_model.load_state_dict(state_dict)

        trained_model.eval()



    with torch.no_grad():

        output = trained_model(image_tensor)

        _, predicted_class = torch.max(
            output,
            1
        )


    return class_names[predicted_class.item()]
