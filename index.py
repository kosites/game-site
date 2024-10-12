import json
import os

# Load the games.json file
input_file = 'games.json'
output_file = 'games_output.html'

# Check if games.json exists
if not os.path.exists(input_file):
    print(f"{input_file} not found in the current directory.")
    exit()

# Read the JSON data
with open(input_file, 'r') as file:
    games = json.load(file)

# Open the output HTML file for writing
with open(output_file, 'w') as file:
    # Write a basic HTML header
    file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    file.write('<meta charset="UTF-8">\n')
    file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    file.write('<title>Games</title>\n</head>\n<body>\n')

    # Convert each game entry to the desired HTML format and write it to the file
    for game in games:
        link = game['link']
        imgSrc = game['imgSrc']
        title = game['title']
        
        # Format the entry as an HTML card
        game_html = f"""
        <a href="{link}" class="game-card">
            <img src="{imgSrc}" alt="{title}">
            <div class="info">
                <h3>{title}</h3>
                <p>Click to Play!</p>
            </div>
        </a>
        """
        file.write(game_html + '\n')

    # Write the closing HTML tags
    file.write('</body>\n</html>')

print(f"HTML output successfully written to {output_file}")
