import requests
import os

def download_logo():
    # URL of the logo you provided
    # Using the logo from the BITS Pilani website
    url = "https://www.bits-pilani.ac.in/wp-content/uploads/Logo-Colour.png"
    
    # Destination file path
    destination = os.path.join(os.getcwd(), "bits_logo.png")
    
    try:
        # Send HTTP GET request
        response = requests.get(url, stream=True)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the image to file
            with open(destination, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            
            print(f"Logo successfully downloaded to {destination}")
            return True
        else:
            print(f"Failed to download logo. Status code: {response.status_code}")
            return False
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    download_logo() 