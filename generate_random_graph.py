#!/usr/bin/env python3

import networkit as nk
import os
import random

def generate(n, prob):
    format = nk.Format.GraphToolBinary

    input_dir = 'instances'
    os.makedirs(input_dir, exist_ok=True)
    file_name = f"er-{len(str(n)) - 1}.gt"
    dest_path = os.path.join(input_dir, file_name)
    
    G = nk.generators.ErdosRenyiGenerator(n, prob).generate()
    # nk.graphtools.randomizeWeights(G) # edge weights cannot be handled by GraphToolBinaryReader?
    nk.graphio.writeGraph(G, dest_path, format)    

if __name__ == "__main__":
    prob = 0.5
    num_nodes = [10**3, 10**4, 10**5, 10**6, 10**7]
    seed = 1
    nk.setSeed(seed, False)
    random.seed(seed)

    for n in num_nodes:
        generate(n,prob)
