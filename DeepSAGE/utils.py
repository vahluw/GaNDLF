import numpy as np
def one_hot(segmask_array, largest_class):
    '''
    Encodes the mask voxels in a stacked numpy array for segmentation
    '''
    tum_mask = []
    
    # create a range from 0 to largest class and find if it is present in current mask
    # do not consider background
    for idx, j in enumerate(np.arange(largest_class)):
        if j != 0:
            tum_mask.append((segmask_array == j).astype(np.float32))

    bag_mask = (segmask_array == 0).astype(np.float32)
    tum_mask.append(bag_mask)
    onehot_stack = np.asarray(tum_mask)
    return onehot_stack
