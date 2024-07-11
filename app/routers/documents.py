import re
from fastapi import APIRouter, HTTPException
from app.models.document import Document
from app.utils.elasticsearch import get_elasticsearch
from uuid import uuid4
from elasticsearch.exceptions import NotFoundError
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

es = get_elasticsearch()

special_characters_pattern = re.compile(r'[^a-zA-Z0-9\s]')


@router.post("/documents/")
async def create_document(document: Document):
    if special_characters_pattern.search(document.content):
        logger.error("422: Document content contains special characters")
        raise HTTPException(status_code=422, detail="Document content contains special characters")

    if not document.content.strip():
        logger.error("422: Document content is empty")
        raise HTTPException(status_code=422, detail="Document content cannot be empty")

    try:
        doc_id = str(uuid4())
        result = es.index(index="documents", id=doc_id, body=document.dict())
        if result['result'] == 'created':
            return {"document_id": doc_id}
        else:
            logger.error(f"Unexpected result from Elasticsearch: {result}")
            raise HTTPException(status_code=500, detail="Failed to create document")
    except Exception as e:
        logger.error(f"Error creating document in Elasticsearch: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documents/{document_id}")
async def get_document(document_id: str):
    try:
        result = es.get(index="documents", id=document_id)
        if result['found']:
            return {"content": result['_source']}
        else:
            raise HTTPException(status_code=404, detail="Document not found")
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Document not found")
    except Exception as e:
        logger.error(f"Error retrieving document from Elasticsearch: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
