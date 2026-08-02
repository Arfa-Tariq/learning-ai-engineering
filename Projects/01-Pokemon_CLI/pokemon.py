import requests
import json

def main():
    pokemon_name = input("Enter the name of a Pokemon: ").lower().strip()
    filename = f"{pokemon_name}.json"

    try:
        # Added timeout - 10 seconds max wait
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # Uncomment the following lines if you want to save the raw JSON response
            # with open(filename, "w") as f:
            #     json.dump(data, f, indent=4)
            # print(f"Raw JSON saved to {filename}")
            print(f"Pokemon Name: {data['name'].capitalize()}")
            print(f"Height(m): {data['height'] / 10}")
            print(f"Weight(kg): {data['weight'] / 10}")
        else:
            print(f"Error: Pokemon '{pokemon_name}' not found.")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection. Please check your network.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. PokeAPI is not responding.")

    except json.decoder.JSONDecodeError:
        print("Error: Received invalid JSON response from API.")

    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed - {e}")

    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} - {e}")
        
if __name__ == "__main__":
    main()
