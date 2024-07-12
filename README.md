# Natural Language Document Service

This service allows for the storage, retrieval, and search of natural language documents, similar to a simplified Google search functionality. It also features an endpoint that utilizes a large language model (LLM) to generate direct answers to queries based on the documents' content.

## Technologies

- **FastAPI**: For the web framework.
- **Elasticsearch**: For storing and searching documents.
- **Docker**: For containerization and easy deployment.
- **OpenAI API**: For generating answers using LLM.

## Running the Application Locally with Docker

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

### Important Note
In all API form data, the characters `=`, `<`, and `>` are not allowed.

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


## Running the Application Locally without Docker

If you prefer not to use Docker, you can run the application directly on your local machine. Follow these steps to set up and run the application with a virtual environment and set up Elasticsearch.

### Prerequisites

- Python 3.8 or higher
- Elasticsearch 7.x or higher
- pip (Python package installer)
- virtualenv (to create isolated Python environments)

### Setting Up the Virtual Environment

1. **Clone the Repository**
   - `git clone https://github.com/alizarch-10p/10p-code-challenge.git`
   - Navigate to the project directory: `cd 10p-code-challenge`

2. **Create a Virtual Environment**
   - Navigate to the `app` directory: `cd app`
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**
   - Ensure you are in the `app` directory and the virtual environment is activated.
   - Install the required packages: `pip install -r requirements.txt`

### Setting Up Elasticsearch

1. **Download and Install Elasticsearch**

   Follow the instructions to download and install Elasticsearch from the [official Elasticsearch website](https://www.elastic.co/downloads/elasticsearch).

2. **Start Elasticsearch**

   - On Windows: Run `bin\elasticsearch.bat` from the Elasticsearch directory.
   - On macOS/Linux: Run `bin/elasticsearch` from the Elasticsearch directory.

3. **Verify Elasticsearch is Running**

   - Open a browser and navigate to `http://localhost:9200`.
   - You should see a JSON response indicating the Elasticsearch service is running.


### Running the Application

1. **Start the FastAPI Application**

   - Ensure the virtual environment is activated and you are in the `app` directory.
   - Run the FastAPI application: `uvicorn main:app --host 127.0.0.1 --port 8001`

2. **Access the Application**

   - Open a browser and navigate to `http://127.0.0.1:8001/docs` to access the FastAPI documentation and test the endpoints.

### Running Tests Locally

1. **Run Tests**

   - Ensure the virtual environment is activated and you are in the `app` directory.
   - Use the following command to run the tests:

     ```bash
     pytest ../tests
     ```

### Additional Information

- Ensure that the `OPENAI_API_KEY` and `ELASTICSEARCH_HOSTS` is set in your environment variables.
- The virtual environment setup ensures that dependencies and environments are consistent across different setups.

By following these steps, you should be able to set up and run the application locally without Docker. This setup provides a flexible and isolated environment for development and testing.
