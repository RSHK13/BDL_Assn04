import subprocess
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ruamel.yaml import YAML

def download_url(base_url, year, output_file, max_files, threshold):
    subprocess.run(["curl", "-L", "-o", output_file, base_url + str(year)])
    
    with open(output_file, 'r') as file:
        data = file.read()
    
    parse_file = BeautifulSoup(data, 'html.parser')
    
    df_with_memory = []
    for row in parse_file.find_all('tr')[2:]:
        columns = row.find_all('td')
        if columns and columns[2].text.strip().endswith('M'):
            csv_link = urljoin(base_url + str(year) + '/', columns[0].text.strip())
            memory = float(columns[2].text.strip().replace('M', ''))
            df_with_memory.append((csv_link, memory))
    
    filtered_csv_files = [link for link, memory in df_with_memory if memory > threshold][:max_files]
    
    print(filtered_csv_files)
    index = 0
    for link in filtered_csv_files:
        index = index + 1
        res = requests.get(link)
        if res.status_code == 200:
            file_name = link.split('/')[-1]
            file_path = f"data/csv_{index}.csv"
            with open(file_path, "wb") as f:
                for chunk in res.iter_content(chunk_size=1024):
                    f.write(chunk)
            

if __name__ == '__main__':
    yaml = YAML(typ="safe")
    params = yaml.load(open("params.yaml", encoding="utf-8"))
    download_url(base_url=params['download']['base_url'],  year = params['download']['year'], output_file='rand.txt', max_files=params['download']['num_files'], threshold= params['download']['threshold'])