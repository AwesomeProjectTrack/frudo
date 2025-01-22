import locale
import random
from datetime import datetime, timedelta

from src.data_generator.base_data_generator import BaseDataGenerator

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


class DateGenerator(BaseDataGenerator):
    """ """
    @staticmethod
    def generate(
        start_date=datetime(1950, 1, 1, 0, 0, 0),
        end_date=datetime.now(),
    ) -> datetime:
        """
        

        Parameters
        ----------
        start_date :
             (Default value = datetime(1950)
        1 :
            
        0 :
            
        0) :
            
        end_date :
             (Default value = datetime.now())

        Returns
        -------

        """
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return start_date + timedelta(days=random_days)
