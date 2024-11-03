from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    """
    Process the image data received in the request.
    
    Args:
        data (ImageData): The image data sent in the request body.
        
    Returns:
        dict: A response message indicating the status and processed data.
    """
    image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    # Convert the decoded bytes into a BytesIO object for image processing
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    # Analyze the image and retrieve responses
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    data = []
    for response in responses:
        data.append(response)
    print('response in route: ', response)
    # Return a JSON response containing the status and processed data
    return {"message": "Image processed", "data": data, "status": "success"}
