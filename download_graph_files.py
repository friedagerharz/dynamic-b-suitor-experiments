#!/usr/bin/env python3

import os
import tarfile
import urllib.request

def download(group, graph):
    url = f'https://suitesparse-collection-website.herokuapp.com/MM/{group}/{graph}.tar.gz'
    input_dir = 'instances'
    os.makedirs(input_dir, exist_ok=True)

    tar_filename = os.path.join(input_dir, f"{graph}.tar.gz")
    dest_path = os.path.join(input_dir, f"{graph}.mtx")

    if os.path.exists(dest_path):
        print(f"{graph} already exists.")
        return

    urllib.request.urlretrieve(url, tar_filename)

    with tarfile.open(tar_filename, 'r:gz') as tar:
        try:
            member = tar.getmembers()[0]
            member.path = member.path.split('/', 1)[-1] 
            tar.extractall(path=input_dir, members=[member])


        except KeyError:
            print(f"File '{graph}.mtx' not found.")

    os.remove(tar_filename)

if __name__ == "__main__":
    graph_file = 'graphs.txt'
    with open(graph_file, 'r') as file:
        instances = file.read().splitlines()

    for instance in instances:
        if not instance.startswith('#') and instance.strip():
            group, graph = instance.split('/')
            download(group, graph)
