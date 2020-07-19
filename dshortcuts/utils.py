import pickle


def open_pickle(path):
    """
    Shortcut to open a pickle file

    Parameters
    ----------
    path : path to a xxxx.pickle file to open

    Raises
    -------
    FileNotFoundError
    PermissionError

    Returns
    -------
    object : unserialised python object

    Examples
    -------
    dtypes = utils.open_pickle('trainDtypes.pickle')
    train = pandas.read_csv('train.csv', dtype=dtypes)

    """
    with open(path, 'rb') as h:
        return pickle.load(h)


def save_pickle(obj, path):
    """
    Shortcut to save python object to a pickle file

    Parameters
    ----------
    obj : python object to save as a pickle
    path : where to save this pickle file

    Raises
    -------
    FileNotFoundError
    PermissionError

    Examples
    -------
    dtypes = {'feat1': 'int8', 'feat2': 'float16'}
    utils.save_pickle(dtypes, 'trainDtypes.pickle')
    """
    with open(path, 'wb') as h:
        pickle.dump(obj, h, protocol=pickle.HIGHEST_PROTOCOL)

