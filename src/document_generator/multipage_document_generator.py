from src.document_generator.base_document_generator import BaseDocumentGenerator
from pathlib import Path
import random
import shutil
from collections import defaultdict
from pprint import pprint
from copy import deepcopy
from PIL import Image

class MultiPageDocumentGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        p = Path('dataset')
        doc_types = [item for item in list(p.iterdir()) if item != Path('dataset/multipage_docs')]
        self.random_elements = random.sample(doc_types, 3)
        self._doc_type = 'multipage_docs'
    def _generate_one_sample(self):
        images_list_path = []
        for el in self.random_elements:
            files = list(Path(el / 'images' / 'clean').iterdir())
            selected = random.choice(files)
            if not selected.is_dir():
                images_list_path.append(selected)
            else:
                 images_list_path.extend(sorted(Path(selected).iterdir()))
        original = deepcopy(images_list_path)
        random.shuffle(original)
        annotations = defaultdict(list)
        for u in original:
            annotations[u.parts[1]].append(images_list_path.index(u)+1)
        return [Image.open(u) for u in original], annotations

if __name__=="__main__":
    y = MultiPageDocumentGenerator()
    y.generate(10)



        










        