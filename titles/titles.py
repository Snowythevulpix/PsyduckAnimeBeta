import re
import json

# File paths
input_file = r'C:\Users\Hayle\Psyduckanimev4\titles\titles.txt'
output_file = r'C:\Users\Hayle\Psyduckanimev4\titles\titles.json'

# Read content from titles.txt
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process lines and create JSON data
formatted_data = []
for line in lines:
    # Splitting by '|' and handling different cases in line format
    data = line.strip().split('|')
    episode_id = data[1]
    english_title = data[2]
    
    # Check if the translated title is empty or not in the expected format
    translated_title = data[3] if len(data) > 4 else ""
    if not translated_title.startswith('{{'):
        translated_title = data[-3]

    # Replace "Pokémon" in both English and Translated titles
    english_title = english_title.replace("Pokémon", "pokemon")
    translated_title = translated_title.replace("Pokémon", "pokemon")

    air_date_us = data[-2]
    air_date_jp = data[-1].rstrip('}}')

    formatted_entry = {
        "EpisodeID": episode_id,
        "EnglishTitle": english_title,
        "TranslatedTitle": translated_title,
        "AirDateUS": air_date_us,
        "AirDateJP": air_date_jp
    }
    formatted_data.append(formatted_entry)

# Write formatted data to titles.json
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(formatted_data, json_file, ensure_ascii=False, indent=2)
