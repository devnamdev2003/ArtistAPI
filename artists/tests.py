import requests

# Replace with your API URL and token
BASE_URL = 'http://127.0.0.1:8000/api'
TOKEN = '44e65ac63dec1471a8d930757588dbed879e609f'

def add_token(headers):
    headers['Authorization'] = f'Token {TOKEN}'
    return headers

def get_works():
    url = f'{BASE_URL}/works/'
    headers = add_token({})
    response = requests.get(url, headers=headers)
    return response.json()

def create_work(data):
    url = f'{BASE_URL}/works/'
    headers = add_token({'Content-Type': 'application/json'})
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def update_work(work_id, data):
    url = f'{BASE_URL}/works/{work_id}/'
    headers = add_token({'Content-Type': 'application/json'})
    response = requests.put(url, json=data, headers=headers)
    return response.json()

def delete_work(work_id):
    url = f'{BASE_URL}/works/{work_id}/'
    headers = add_token({})
    response = requests.delete(url, headers=headers)
    return response.status_code

def get_artists():
    url = f'{BASE_URL}/artists/'
    headers = add_token({})
    response = requests.get(url, headers=headers)
    return response.json()

def create_artist(data):
    url = f'{BASE_URL}/artists/'
    headers = add_token({'Content-Type': 'application/json'})
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def update_artist(artist_id, data):
    url = f'{BASE_URL}/artists/{artist_id}/'
    headers = add_token({'Content-Type': 'application/json'})
    response = requests.put(url, json=data, headers=headers)
    return response.json()

def delete_artist(artist_id):
    url = f'{BASE_URL}/artists/{artist_id}/'
    headers = add_token({})
    response = requests.delete(url, headers=headers)
    return response.status_code

# Example usage
if __name__ == '__main__':
    works_list = get_works()
    print("List of works:", works_list)
    
    new_work_data = {
        'link': 'https://example.com/new_video',
        'work_type': 'YT',
    }
    created_work = create_work(new_work_data)
    print("Created work:", created_work)
    
    artists_list = get_artists()
    print("List of artists:", artists_list)

    # Create a new artist
    new_artist_data = {
        'name': 'ishu',
        'user': 3,  # Replace with the appropriate user ID
        'works': [1, 2],  # Replace with the appropriate work IDs
    }
    created_artist = create_artist(new_artist_data)
    print("Created artist:", created_artist)

    # Update the created artist
    artist_id_to_update = created_artist['id']
    updated_artist_data = {
        'name': 'Jane Doe',
        'user': 2,  # Replace with the appropriate user ID
        'works': [3, 4],  # Replace with the appropriate work IDs
    }
    updated_artist = update_artist(artist_id_to_update, updated_artist_data)
    print("Updated artist:", updated_artist)

    # Delete the created artist
    delete_status_code = delete_artist(artist_id_to_update)
    if delete_status_code == 204:
        print("Artist deleted successfully.")
    else:
        print("Failed to delete artist.")


