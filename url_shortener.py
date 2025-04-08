import pyshorteners
import validators

def shortenurl():
    while True:
        url = input('Enter the URL to shorten: ')
        
        if not validators.url(url):
            print("Invalid URL. Please enter a valid URL.")
            continue  # Ask again
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(url)
            print("Shortened URL:", short_url)
            break  # Exit loop after successful shortening
        except Exception as e:
            print("An error occurred while shortening the URL.")
            print("Error details:", e)
            break  # Exit loop on error (you can change this if needed)

# Call the function
shortenurl()
