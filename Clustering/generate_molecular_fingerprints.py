import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import PandasTools

def sdf_to_fingerprints(sdf_file):
    # Read the sdf file
    molecules = PandasTools.LoadSDF(sdf_file)
    # Generate the fingerprints
    fingerprints = [AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024) for m in molecules.ROMol]
    # Convert the fingerprints to an array
    fingerprints_array = np.array(fingerprints)

    return fingerprints_array