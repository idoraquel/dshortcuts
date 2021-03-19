import pickle
import geopandas as gpd


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


def geo_data_frame(dataframe, lat_col, lon_col):
    """
    Makes a geopandas.GeoDataFrame given pandas.DataFrame
    CRS is hardcoded to GPS (EPSG:4326)    

    Parameters
    ----------
    dataframe : pandas dataframe
    lat_col : a NAME of a column which holds the lattitude in given dataframe
    lon_col : a NAME of a column which holds the longtitude in given dataframe

    Returns
    -------
    geopandas.GeoDataFrame
    """
    _geoDataFrame = gpd.GeoDataFrame(
        dataframe, 
        geometry=gpd.points_from_xy(dataframe[lon_col], dataframe[lat_col]))

    # Set the coordinate reference system (CRS)
    _geoDataFrame.crs = {'init': 'epsg:4326'}

    return _geoDataFrame

