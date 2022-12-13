import os, requests
from bs4 import BeautifulSoup

def get_images(topic_slug, current_working_dir, num_images = 10):
    
    # This is the URL for the Unsplash search page
    url = "https://unsplash.com/s/photos/" + topic_slug

    # Send an HTTP request to the URL and store the response
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the images on the page using the img tag
    images = soup.find_all("img")
    images.pop(0) # This is a garbage file and we don't want it.

    # Iterate over the images and download each one
    for i in range(num_images):
        image = images[i]
        
        # Get the image URL and download it
        image_url = image["src"]
        response = requests.get(image_url)
        
        # Save the image to disk
        # The image file name is the last part of the image URL
        # For example, the image file name for https://example.com/images/image.jpg is image.jpg
        # We use the split() method to get the last part of the URL
        # and the replace() method to remove the query string from the file name
        # 

        file_name = topic_slug + str(i) + ".jpg"
        file_path = os.path.join(current_working_dir + '/images', file_name)
        with open(file_path, "wb") as f:
            f.write(response.content)
            print("Downloaded", file_name)
        
    return images



    