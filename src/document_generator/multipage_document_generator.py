import random
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

from PIL import Image

from src.document_generator.base_document_generator import BaseDocumentGenerator


class MultiPageDocumentGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        p = Path("dataset")
        self.doc_types = [item for item in list(p.iterdir()) if item != Path("dataset/multipage_docs")]
        self._doc_type = "multipage_docs"

    def _generate_one_sample(self):
        images_list_path = []
        random_elements = random.sample(self.doc_types, 3)
        for el in random_elements:
            files = list(Path(el / "images" / "clean").iterdir())
            selected = random.choice(files)
            if not selected.is_dir():
                images_list_path.append(selected)
            else:
                images_list_path.extend(sorted(Path(selected).iterdir()))
        original = deepcopy(images_list_path)
        random.shuffle(original)
        annotations = defaultdict(list)
        shuffled_index_map = {path: idx for idx, path in enumerate(original)}

        for u in images_list_path:
            annotations[u.parts[1]].append(shuffled_index_map[u])
        return [Image.open(u) for u in original], annotations


if __name__ == "__main__":
    y = MultiPageDocumentGenerator()
    y.generate(10)
