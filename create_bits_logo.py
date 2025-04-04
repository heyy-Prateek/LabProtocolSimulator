from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    # Create a new image with a white background
    width, height = 500, 500
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw a circle for the logo background
    circle_radius = 200
    circle_center = (width // 2, height // 2)
    circle_bbox = (
        circle_center[0] - circle_radius,
        circle_center[1] - circle_radius,
        circle_center[0] + circle_radius,
        circle_center[1] + circle_radius
    )
    draw.ellipse(circle_bbox, fill='#1E3F87')  # BITS Blue
    
    # Draw a gold ring
    ring_width = 20
    outer_radius = circle_radius
    inner_radius = outer_radius - ring_width
    draw.ellipse(
        (
            circle_center[0] - outer_radius,
            circle_center[1] - outer_radius,
            circle_center[0] + outer_radius,
            circle_center[1] + outer_radius
        ),
        fill='#1E3F87',
        outline='#FCBA03',  # Gold color
        width=10
    )
    
    # Try to add text
    try:
        # Check if a font is available
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()
        
        # Add "BITS PILANI" text
        text = "BITS PILANI"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = ((width - text_width) // 2, height // 2 - text_height - 20)
        draw.text(text_position, text, fill="white", font=font)
        
        # Add "INDIA" text
        india_text = "INDIA"
        india_bbox = draw.textbbox((0, 0), india_text, font=font)
        india_width = india_bbox[2] - india_bbox[0]
        india_position = ((width - india_width) // 2, height // 2 + 20)
        draw.text(india_position, india_text, fill="white", font=font)
    except Exception as e:
        print(f"Couldn't add text: {e}")
    
    # Save the image
    logo_path = os.path.join(os.getcwd(), "bits_logo.png")
    img.save(logo_path)
    print(f"Generated BITS logo at {logo_path}")
    return logo_path

if __name__ == "__main__":
    create_logo() 