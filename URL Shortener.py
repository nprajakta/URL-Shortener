import string
import random
import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url, length=8):
        url_hash = self._generate_hash(long_url)
        short_url = url_hash[:length]
        self.url_mapping[short_url] = long_url

        return short_url

    def _generate_hash(self, long_url):
        hash_object = hashlib.sha256(long_url.encode())
        hash_hex = hash_object.hexdigest()

        return hash_hex

    def expand_url(self, short_url):
        long_url = self.url_mapping.get(short_url)

        return long_url


url_shortener = URLShortener()

while True:
    print("\nURL Shortener Application")
    print("1. Shorten URL")
    print("2. Expand URL")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        long_url = input("Enter the long URL to shorten: ")
        short_url = url_shortener.shorten_url(long_url)
        print(f"Short URL: {short_url}")

    elif choice == '2':
        short_url = input("Enter the short URL to expand: ")
        long_url = url_shortener.expand_url(short_url)

        if long_url:
            print(f"Expanded URL: {long_url}")
        else:
            print("Invalid short URL.")

    elif choice == '3':
        print("Exiting the URL Shortener Application.")
        break

    else:
        print("Invalid choice. Please try again.")

