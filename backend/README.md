## Running the FastAPI Application

> Make sure to add a `.env` file with the following : 
```py
GROQ_API_KEY = "API_KEY" 
GROQ_LLama = "llama3-groq-70b-8192-tool-use-preview" 
GITHUB_TOKEN = "TOKEN"
```

To run the FastAPI application in `main.py`, follow these steps:

### Prerequisites

- Ensure you have Python installed (version 3.7 or higher is recommended).
- Install FastAPI and Uvicorn, which is an ASGI server compatible with FastAPI.

```bash
pip install fastapi uvicorn
```

### Running the Application

1. Open your terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the application using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   - `main` refers to the filename `main.py` (exclude the `.py` extension).
   - `app` refers to the FastAPI app instance inside `main.py`.
   - `--reload` enables auto-reload, so changes to your code will automatically restart the server (useful for development).

4. Once the server is running, access the API documentation in your browser at:

   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Stopping the Server

- Press `CTRL + C` in the terminal to stop the server when needed.

--- 

This will start the FastAPI application and allow you to test and explore the API endpoints.