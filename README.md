# Natural Language Document Service

This service allows for the storage, retrieval, and search of natural language documents, similar to a simplified Google search functionality. It also features an endpoint that utilizes a large language model (LLM) to generate direct answers to queries based on the documents' content.

## Technologies

- **FastAPI**: For the web framework.
- **Elasticsearch**: For storing and searching documents.
- **Docker**: For containerization and easy deployment.
- **OpenAI API**: For generating answers using LLM.

## Setup Instructions

1. **Clone the repository**
   - `git clone https://github.com/alizarch-10p/10p-code-challenge.git`
   - Navigate to the project directory: `cd 10p-code-challenge`

2. **Build the Image**
   - Run `docker-compose --build`

3. **Run the Docker containers**
   - Run `docker-compose up`
   - This will start the FastAPI application and Elasticsearch service.

4. **Accessing the Application**
   - The FastAPI application will be available at `http://localhost:8001`
   - To Run API you can access FastAPI docs at 'http://localhost:8001/docs'
   - Elasticsearch will be accessible at `http://localhost:9200`


## API Documentation

### Endpoints

- `POST /documents/`
  - **Description**: Store a document and return a unique document ID.
  - **Request Body**: `{"content": "Your document content"}`
  - **Response**: `{"document_id": "unique-document-id"}`

- `GET /documents/{document_id}`
  - **Description**: Retrieve a document by its ID.
  - **URL Parameters**: `document_id` (string)
  - **Response**: `{"content": "Stored document content"}`

- `GET /search/`
  - **Description**: Search documents by free text query.
  - **Query Parameters**:
    - `query`: Text to search for.
    - `top_k`: Number of top documents to return (default 10).
  - **Response**: `{"results": ["list", "of", "matching", "documents"]}`

- `GET /answer/`
  - **Description**: Generate an answer to a query based on the context of stored documents.
  - **Query Parameters**: `query`: Query for which the answer is generated.
  - **Response**: `{"query": "Your query", "answer": "Generated answer"}`


## Running Tests with Docker

- To run the test cases using Docker, you need to first run main app. then need to run test service. Run these commands one by one:
  - `docker-compose up`
  - `docker-compose -f docker-compose.test.yml --build`
  - `docker-compose -f docker-compose.test.yml up`
- This command builds the test environment and executes the tests defined in the `tests/` directory.

## Additional Information

- Ensure that the `OPENAI_API_KEY` is set in your environment variables or a `.env` file for the LLM to function properly. You need to place .env file in app folder. 
- The Docker setup ensures that dependencies and environments are consistent across different setups.
