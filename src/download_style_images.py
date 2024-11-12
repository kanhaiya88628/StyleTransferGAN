import os
import requests

def download_unsplash_style_images(query, output_folder, num_images=100, access_key='YOUR_UNSPLASH_ACCESS_KEY'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    url = "https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {access_key}"}
    params = {
        "query": query,
        "per_page": 30,  # Maximum number of images per request
        "page": 1
    }

    count = 0
    while count < num_images:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        for photo in data['results']:
            if count >= num_images:
                break
            img_url = photo['urls']['regular']
            try:
                img_data = requests.get(img_url).content
                with open(os.path.join(output_folder, f'style_image_{count}.jpg'), 'wb') as img_file:
                    img_file.write(img_data)
                count += 1
                print(f'Downloaded {count}/{num_images} images')
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")

        params['page'] += 1  # Move to the next page for more images

# Replace 'YOUR_UNSPLASH_ACCESS_KEY' with your actual Unsplash Access Key
download_unsplash_style_images('famous paintings', '../data/style', num_images=100, access_key='b1tXFlrMFTQv76eI_1h0lVR4wyQ5CiJDpj4HXns-Lfw')
