from fastapi import APIRouter, HTTPException
from app.models.document import Document
from app.utils.elasticsearch import get_elasticsearch
from uuid import uuid4
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

es = get_elasticsearch()


@router.post("/documents/")
async def create_document(document: Document):
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
    except Exception as e:
        logger.error(f"Error retrieving document from Elasticsearch: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))