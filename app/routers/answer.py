import re
from fastapi import APIRouter, HTTPException
from app.utils.elasticsearch import get_elasticsearch
from elasticsearch_dsl import Search
import openai
from decouple import config
import logging

OPENAI_API_KEY = config('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

router = APIRouter()

logger = logging.getLogger(__name__)

es = get_elasticsearch()

special_characters_pattern = re.compile(r'[^a-zA-Z0-9\s]')

@router.get("/search/")
async def search_documents(query: str, top_k: int = 10):
    if special_characters_pattern.search(query):
        logger.error("422: Search query contains special characters")
        raise HTTPException(status_code=422, detail="Search query contains special characters")

    try:
        search = Search(using=es, index="documents").query("match", content=query)[:top_k]
        response = search.execute()
        return {"results": [hit.content for hit in response]}
    except Exception as e:
        logger.error(f"Error searching documents in Elasticsearch: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/answer/")
async def get_answer(query: str):
    if special_characters_pattern.search(query):
        logger.error("422: Query contains special characters")
        raise HTTPException(status_code=422, detail="Query contains special characters")

    try:
        search = Search(using=es, index="documents").query("match", content=query)[:5]
        response = search.execute()
        if response:
            context = " ".join([doc.content for doc in response.hits])
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Given the following information: {context}\n\nQ: {query}\nA:"},
            ]

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            answer = completion.choices[0].message['content']
            return {"query": query, "answer": answer}
        else:
            return {"query": query, "answer": "No relevant documents found to provide context."}
    except Exception as e:
        logger.error(f"Error generating direct answer: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))