from pathlib import Path
from typing import Union

from PIL import ImageFont

from src.data_generator.base_data_generator import BaseDataGenerator


class BboxTins(BaseDataGenerator):
    """ """
    @staticmethod
    def generate(
        text: str,
        old_coords: Union[list, tuple],
        font: Path = None,
        font_size: int = 25,
        is_new_tin: bool = True,
        old_tin_number: bool = False,
    ):
        """
        

        Parameters
        ----------
        text: str :
            
        old_coords: Union[list :
            
        tuple] :
            
        font: Path :
             (Default value = None)
        font_size: int :
             (Default value = 25)
        is_new_tin: bool :
             (Default value = True)
        old_tin_number: bool :
             (Default value = False)

        Returns
        -------

        """
        if is_new_tin:
            if font is None:
                font = ImageFont.truetype("src/templates/tins/timesnewromanpsmt.ttf", font_size)
            width = font.getlength(text)
            height = 50
            return (old_coords[0], old_coords[1], old_coords[0] + width, old_coords[1] + height)
        else:
            if font is None:
                font = ImageFont.truetype("src/templates/tins/timesnewromanpsmt.ttf", 15)
            width = font.getlength(text)
            height = 16
            return (old_coords[0], old_coords[1], old_coords[0] + width, old_coords[1] + height)
