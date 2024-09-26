import h5py, pdb

path = 'file_demo/demo.h5'

def print_group_structure(group, indent=0):
    for key in group.keys():
        print('  ' * indent + key)
        subgroup = group[key]
        if isinstance(subgroup, h5py.Group):
            print_group_structure(subgroup, indent + 1)

def read_dataset(group, dataset_name):
    dataset = group[dataset_name]
    print(f"Reading dataset: {dataset_name}")
    print(dataset.shape, dataset.dtype)
    data = dataset[:]
    return data

with h5py.File(path, 'r') as file:
    print("Root group contents:")
    print_group_structure(file)
    
    dataset_name = 'your_dataset_name'
    if dataset_name in file:
        data = read_dataset(file, dataset_name)
    else:
        print(f"Dataset {dataset_name} not found in the file.")

    for key in file.keys():
        if isinstance(file[key], h5py.Dataset):
            print(f"Reading dataset: {key}")
            data = file[key][:]
            print(data.shape, data.dtype)