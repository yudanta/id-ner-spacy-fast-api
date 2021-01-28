from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

class NerQuery(BaseModel):
    sentence: str


from ..apis.nlp.ner import get_entities

router = APIRouter(
    prefix='/nlp/id',
    tags=['nlp'],
    responses={
        404: {'description': 'Not Found'}
    }
)

@router.post('/ner')
async def api_ner(query: NerQuery):
    result = get_entities(query.sentence)
    return result