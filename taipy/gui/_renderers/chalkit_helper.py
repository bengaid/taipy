import io
import base64

# Function to convert an image to base64
def image_to_base64(image):
    # Create a BytesIO buffer to save the image
    buffered = io.BytesIO()
    # Save the image to the buffer in JPEG format
    image.save(buffered, format="JPEG")
    # Get the byte data from the buffer
    img_byte = buffered.getvalue()
    # Encode the bytes to base64
    img_base64 = base64.b64encode(img_byte)
    # Convert bytes to string for HTML use
    img_base64_str = img_base64.decode('utf-8')
    html_img_str = f'data:image/jpeg;base64,{img_base64_str}'

    return html_img_str