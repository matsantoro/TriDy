import pandas as pd
from pathlib import Path
import numpy as np

def gather_data(data_path):
    arrays = []
    names = []
    for elem in sorted(data_path.glob("*.npy")):
        array = np.load(elem, allow_pickle=True)
        if elem.stem=='cell_counts':
             array = [x if type(x) == list else [x] for x in array]
             mdim = np.max([len(x) for x in array])
             for i in range(mdim):
                  arrays.append(np.array([l[i] if i < len(l) else 0 for l in array]))
                  names.append(elem.stem + str(i))
        elif elem.stem=='conn_comps':
             array = np.array([x if type(x) == tuple else [0, 0] for x in array])
             array = array[:,0]
             arrays.append(array)
             names.append(elem.stem)
        else:
             arrays.append(array)
             names.append(elem.stem)
    pd.DataFrame(np.stack(arrays).T, columns=names).to_pickle(data_path / "df.pkl")
    
if __name__ == '__main__':
    gather_data(Path("./results_active_in_tribe_cc_fake_layer/individual_parameters/"))     
