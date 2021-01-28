from typing import List, Dict
from ...main import id_nlp


def get_entities(sentence) -> List[Dict]:
    doc = id_nlp(sentence)
    return [(ent.text, ent.label_) for ent in doc.ents]