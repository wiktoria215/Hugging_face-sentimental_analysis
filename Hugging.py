import requests


def sprawdz_sentyment(tekst_uzytkownika):
    API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    MOJ_TOKEN = "YOUR_HUGGING_FACE_TOKEN_HERE"

    naglowki = {"Authorization": f"Bearer {MOJ_TOKEN}"}
    paczka_z_danymi = {"inputs": tekst_uzytkownika}


    try:
        odpowiedz = requests.post(API_URL, headers=naglowki, json=paczka_z_danymi)

        odpowiedz.raise_for_status()

        wynik = odpowiedz.json()
        return wynik

    except Exception as e:
        return f"Wystąpił błąd komunikacji: {e}"




print("Analizuję zdanie nr 1...")
print(sprawdz_sentyment("I absolutely love this new cloud architecture!"))

print("\nAnalizuję zdanie nr 2...")
print(sprawdz_sentyment("This network error is making me very frustrated."))