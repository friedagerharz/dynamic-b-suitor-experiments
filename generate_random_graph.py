#!/usr/bin/env python3

import networkit as nk
import os
import random

def generate(n, prob):
    input_dir = 'instances'
    os.makedirs(input_dir, exist_ok=True)
    file_name = f"er-{len(str(n)) - 1}.nkb"
    dest_path = os.path.join(input_dir, file_name)

    if os.path.isfile(dest_path):
        print(f"{file_name} already exists.")
        return
    
    G = nk.generators.ErdosRenyiGenerator(n, prob).generate()
    G.removeMultiEdges()
    G.removeSelfLoops()
    if G.isDirected():
        G = nk.graphtools.toUndirected(G)
    nk.graphtools.randomizeWeights(G)
    nk.graphio.NetworkitBinaryWriter().write(G, dest_path)

    # # remove:
    # GR = nk.graphio.NetworkitBinaryReader().read(dest_path)
    # print(f"nodes: {G.numberOfNodes()}")
    # print(f"edges: {G.numberOfEdges()}")

    # def printEdge(v, u, w, eid):
    #     print(f"({v},{u}) - {w}")
    # GR.forEdges(printEdge)

if __name__ == "__main__":
    prob = 0.2
    num_nodes = [10**3, 10**4, 10**5, 10**6, 10**7]
    seed = 1
    nk.setSeed(seed, False)
    random.seed(seed)

    for n in num_nodes:
        generate(n,prob)
