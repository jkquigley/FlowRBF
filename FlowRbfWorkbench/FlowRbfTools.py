import os


def getModulePath():
    """
    Returns the current Cfd module path.
    Determines where this file is running from, so works regardless of whether
    the module is installed in the app's module directory or the user's app data folder.
    (The second overrides the first.)
    """
    return os.path.normpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
