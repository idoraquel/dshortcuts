import pickle

def open_pickle(path):
    with open(path, 'rb') as h:
        return pickle.load(h)
