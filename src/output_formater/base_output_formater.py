from abc import ABCMeta, abstractmethod
from pathlib import Path

from PIL import Image

from src.document_data_generator.dataclasses import Entity


class BaseOutputFormater(metaclass=ABCMeta):
    """ """
    @abstractmethod
    def format(self, dataset_path, output_dataset_path) -> Path | str:
        """
        

        Parameters
        ----------
        dataset_path :
            
        output_dataset_path :
            

        Returns
        -------

        """
        pass
