import shutil
from pathlib import Path

from src.augmentations import BaseAugmentation


class BasicAugmentation(BaseAugmentation):
    """ """
    def apply(self, dataset_path: Path) -> Path | str:
        """
        

        Parameters
        ----------
        dataset_path: Path :
            

        Returns
        -------

        """
        shutil.copytree(dataset_path, dataset_path.parents[0] / "basic")
        return dataset_path.parents[0] / "basic"
