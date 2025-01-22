from abc import ABCMeta
from pathlib import Path


class BaseAugmentation(metaclass=ABCMeta):
    """ """
    def __init__(self, **kwargs):
        pass

    def apply(self, dataset_path) -> Path | str:
        """
        

        Parameters
        ----------
        dataset_path :
            

        Returns
        -------

        """
        pass
