from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from confidential import cfdt

def read_image(image_address):
    with open(image_address, "rb") as f:
        image_data = f.read()
        return image_data

def get_captions(image_data):
    client = ImageAnalysisClient(
        endpoint=cfdt('endpoint'),
        credential=AzureKeyCredential(cfdt('key'))
    )

    # Get a caption for the image. This will be a synchronously (blocking) call.
    result = client.analyze(
        image_url=image_data,
        visual_features=[VisualFeatures.CAPTION],
        gender_neutral_caption=True,  # Optional (default is False)
    )
    if result.caption is not None:
        print("Caption: ")
        return result.caption.text

def get_tags(image_data):
    client = ImageAnalysisClient(
        endpoint=cfdt('endpoint'),
        credential=AzureKeyCredential(cfdt('key'))
    )

    result = client.analyze(
        image_url=image_data,
        visual_features=[VisualFeatures.TAGS],
        gender_neutral_caption=True,  # Optional (default is False)
    )

    if result.tags is not None:
        print(" Tags:")
        for tag in result.tags.list:
            return tag.name

