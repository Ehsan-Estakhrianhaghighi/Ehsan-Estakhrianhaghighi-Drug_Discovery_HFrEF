import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import PandasTools


def ClusterFps(fps,cutoff=0.2):
    from rdkit import DataStructs
    from rdkit.ML.Cluster import Butina

    # first generate the distance matrix:
    dists = []
    nfps = len(fps)
    for i in range(1,nfps):
        sims = DataStructs.BulkTanimotoSimilarity(fps[i],fps[:i])
        dists.extend([1-x for x in sims])

    # now cluster the data:
    cs = Butina.ClusterData(dists,nfps,cutoff,isDistData=True)
    return cs


def clusters_to_images(clusters, mols_rdchem):
    pics = []
    for cluster in clusters[:5]:
        pics.append([Draw.MolToImage(mols_rdchem[x]) for x in cluster])
        print(len(cluster))
        for molecule in cluster:
            # turn the molecule into a mol object
            mol = mols_rdchem[molecule]