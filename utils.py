import requests

def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Sorry, I couldn't fetch a joke at the moment."
    
def get_random_meme():
    response = requests.get("https://meme-api.com/gimme")
    if response.status_code == 200:
        meme_data = response.json()
        return meme_data['url']
    else:
        return None