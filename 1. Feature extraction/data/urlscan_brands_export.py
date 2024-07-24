"""
SKRYPT DO EKSPORTU UNIKALNYCH DOMEN Z PLIKU JSON, ZAWIERAJĄCEGO DANE ŚLEDZONYCH MAREK Z URLSCAN.IO
"""


import json


def extract_unique_domains(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    unique_domains = set()
    for kit in data['kits']:
        domains = kit['terms'].get('domains', [])
        if domains:
            unique_domains.add(domains[0])

    return list(unique_domains)


def save_domains_to_file(domains, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for domain in domains:
            file.write(f"https://{domain}\n")


# Path to the input JSON file
input_file_path = '../out.json'

# Path to the output text file
output_file_path = '../URLSCAN_legit_domains.csv'

# Extract unique domains
unique_domains = extract_unique_domains(input_file_path)

# Save unique domains to file
save_domains_to_file(unique_domains, output_file_path)

print(f"Unique domains have been saved to {output_file_path}")
