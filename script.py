from bs4 import BeautifulSoup
import requests

def print_grid_from_google_doc(url):
    # Fetch the Google Doc content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the table data
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip header row
    
    # Parse the data and find grid dimensions
    grid_data = []
    max_x = max_y = 0
    for row in rows:
        cells = row.find_all('td')
        x = int(cells[0].text.strip())
        char = cells[1].text.strip()
        y = int(cells[2].text.strip())
        grid_data.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    # Create the grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill the grid with characters
    for x, y, char in grid_data:
        grid[y][x] = char
    
    # Print the grid
    for row in grid:
        print(''.join(row))

# Example usage
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
print_grid_from_google_doc(url)