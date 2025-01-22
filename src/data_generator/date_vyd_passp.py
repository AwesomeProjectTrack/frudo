import locale
from datetime import datetime, timedelta

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.date import DateGenerator

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


class DateVydPasspGenerator(BaseDataGenerator):
    """ """
    @staticmethod
    def generate(birth_date=datetime(1980, 1, 1, 0, 0, 0)) -> datetime:
        """
        

        Parameters
        ----------
        birth_date :
             (Default value = datetime(1980)
        1 :
            
        0 :
            
        0) :
            

        Returns
        -------

        """
        start_date = birth_date + timedelta(days=14 * 365)

        return DateGenerator.generate(start_date=start_date)
