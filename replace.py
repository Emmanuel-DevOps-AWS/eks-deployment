# replace.py
import os

placeholder = "CONTAINER_IMAGE"
image = os.environ["REGISTRY"] + "/" + os.environ["REPOSITORY"] + ":" + os.environ["IMAGE_TAG"]

with open('deployment.yaml', 'r') as file:
    filedata = file.read()

filedata = filedata.replace(placeholder, image)

with open('deployment.yaml', 'w') as file:
    file.write(filedata)

