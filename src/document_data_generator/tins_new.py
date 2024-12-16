import json
from pathlib import Path
import locale

from src.data_generator import (
    DateGenerator,
    FullNameGenerator,
    Gender,
    GeoPlace,
    TinsNumber, 
    BboxTins,
    StartCoords
)
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import Entity, NewTinsData


class NewTinsDocumentDataGenerator(BaseDocumentDataGenerator):
    @staticmethod
    def generate() -> NewTinsData:
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        gender = Gender.generate()
        name = FullNameGenerator.generate(gender)
        full_name = name.last_name + ' ' + name.first_name + ' ' + name.middle_name
        place = GeoPlace.generate()
        full_place = place.region + ' ' + place.city
        birth_date = DateGenerator.generate()
        birth_date = birth_date.strftime("%d.%m.%Y года")
        registration_date = DateGenerator.generate()
        registration_date = registration_date.strftime("%d.%m.%Y года")
        tins_number = TinsNumber.generate()
        
        annotations_path = Path('src/templates/tins/data.json')
        
        with open(annotations_path) as file:
            anno = json.load(file)
        
        start_coords_new = StartCoords.generate(width=anno['new']['width'], 
                                            height=anno['new']['heigth'])
                    
        anno['new']['name']['value'] = full_name
        anno['new']['name']['x'] = start_coords_new['name'][0]
        anno['new']['name']['y'] = start_coords_new['name'][1]
        anno['new']['name']['bbox'] =  BboxTins().generate(text= full_name, 
                                                                    old_coords= [anno['new']['name']['x'], 
                                                                                  anno['new']['name']['y']])        
        anno['new']['birth_date']['value'] = birth_date
        anno['new']['birth_date']['x'] = start_coords_new['birth_date'][0]
        anno['new']['birth_date']['y'] = start_coords_new['birth_date'][1]
        anno['new']['birth_date']['bbox'] = BboxTins().generate(text= birth_date, 
                                                                       old_coords= [anno['new']['birth_date']['x'], 
                                                                                  anno['new']['birth_date']['y']])
        
        anno['new']['sex']['value'] = gender
        anno['new']['sex']['x'] = start_coords_new['sex'][0]
        anno['new']['sex']['y'] = start_coords_new['sex'][1]
        anno['new']['sex']['bbox'] = BboxTins().generate(text=gender, 
                                                               old_coords= [anno['new']['sex']['x'], 
                                                                                  anno['new']['sex']['y']])
        
        anno['new']['place_of_birth']['value'] = full_place
        anno['new']['place_of_birth']['x'] = start_coords_new['place_of_birth'][0]
        anno['new']['place_of_birth']['y'] = start_coords_new['place_of_birth'][1]
        anno['new']['place_of_birth']['bbox'] = BboxTins().generate(text=full_place, 
                                                                           old_coords= [anno['new']['place_of_birth']['x'], 
                                                                                anno['new']['place_of_birth']['y']])
                
        anno['new']['issued']['value'] = registration_date
        anno['new']['issued']['x'] = start_coords_new['issued'][0]
        anno['new']['issued']['y'] = start_coords_new['issued'][1]
        anno['new']['issued']['bbox'] = BboxTins().generate(text= registration_date, 
                                                                   old_coords= [anno['new']['issued']['x'], 
                                                                                  anno['new']['issued']['y']])
        
        
        anno['new']['tin']['value'] = tins_number
        anno['new']['tin']['x'] = start_coords_new['tin'][0]
        anno['new']['tin']['y'] = start_coords_new['tin'][1]
        anno['new']['tin']['bbox'] = BboxTins().generate(text=tins_number, 
                                                                   old_coords= [anno['new']['tin']['x'], 
                                                                                  anno['new']['tin']['y']])
        return NewTinsData(
            tins_number= Entity(value=tins_number, bboxes=anno['new']['tin']['bbox']),
            family_name=Entity(value=name.last_name, bboxes=anno['new']['name']['bbox']),
            middle_name=Entity(value=name.middle_name, bboxes=anno['new']['name']['bbox']),
            first_name=Entity(value=name.first_name, bboxes=anno['new']['name']['bbox']),
            name = Entity(value = full_name, bboxes=anno['new']['name']['bbox']),
            birth_date=Entity(value=birth_date, bboxes=anno['new']['birth_date']['bbox']),
            reg_date=Entity(value=registration_date, bboxes=anno['new']['issued']['bbox']),
            city= Entity(value=place, bboxes=anno['new']['place_of_birth']['bbox']),
            region = Entity(place.region, bboxes=anno['new']['place_of_birth']['bbox']),
            full_place = Entity(value=full_place, bboxes= anno['new']['place_of_birth']['bbox']),
            gender= Entity(value=gender, bboxes = anno['new']['sex']['bbox'])
        )
        


        
        
        