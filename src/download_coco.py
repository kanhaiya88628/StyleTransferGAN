import os
import requests

def download_pexels_images(query, output_folder, num_images=200, api_key='YOUR_PEXELS_API_KEY'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": api_key}
    per_page = 80  # Maximum images per request for Pexels API
    page = 1
    count = 0

    while count < num_images:
        params = {
            "query": query,
            "per_page": min(per_page, num_images - count),
            "page": page
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        for photo in data['photos']:
            if count >= num_images:
                break
            img_url = photo['src']['original']
            try:
                img_data = requests.get(img_url).content
                with open(os.path.join(output_folder, f'content_image_{count}.jpg'), 'wb') as img_file:
                    img_file.write(img_data)
                count += 1
                print(f'Downloaded {count}/{num_images} images')
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")

        page += 1  # Move to the next page for more images

# Replace 'YOUR_PEXELS_API_KEY' with your actual Pexels API key
download_pexels_images('nature', '../data/content', num_images=200, api_key='Ko2BmPu62KwtkvLp5VP5kUTZ6O50ZSSLpI8Uo8OzGGJEUPcC6QDzHBx2')
