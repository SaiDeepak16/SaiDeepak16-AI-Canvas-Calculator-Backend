# AI Canvas Calculator Backend

This backend service powers the **AI Canvas Calculator**, handling requests for mathematical expression analysis and LaTeX rendering from image inputs. The backend is built using **FastAPI** and interfaces with the **Google Gemini API** to perform image analysis on user-drawn inputs.

## Quick Start Guide

1. **Start the Server**: Run the backend locally or access the deployed version using the provided API endpoint.
2. **Send a Request**: Make a POST request to `/calculate` with an image of the mathematical expression.
3. **Receive LaTeX Output**: The server processes the image, recognizes the expression, and returns a LaTeX-rendered result.

---

## Developer Setup

#### Prerequisites

- **Python 3.8+** and **pip**
- A **Google Gemini API Key** (set up as an environment variable)

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SaiDeepak16/AI-Canvas-Calculator-Backend.git
   cd AI-Canvas-Calculator-Backend
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:

   ```bash
   SERVER_URL="0.0.0.0"
   PORT="8000"
   GEMINI_API_KEY="your_api_key_here"
   ENV="dev"  # or "prod" for production mode
   ```

4. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `localhost:8000`.

---

## Code Overview

### Project Structure

- **main.py**: Configures the FastAPI app, CORS settings, and routes.
- **apps/calculator/route.py**: Defines the main `/calculate` endpoint, which processes image inputs.
- **apps/calculator/utils.py**: Contains the `analyze_image` function that interfaces with the Google Gemini API.
- **schema.py**: Defines Pydantic models used for request validation and response serialization.
- **constants.py**: Stores server configuration constants and loads environment variables.

---

### Core Functionality

#### CORS Middleware

To allow cross-origin requests, especially for frontend interactions, **CORS** is enabled globally.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### `/calculate` Endpoint

- **URL**: `/calculate`
- **Method**: `POST`
- **Request**: Expects a base64-encoded image of the drawn expression.
- **Response**: Returns LaTeX-formatted output based on the analysis.

   ```python
   @router.post("/calculate")
   async def calculate_route(image_data: ImageData):
       # Decode image, send to analyze_image(), return LaTeX result
       ...
   ```

### Utilities for Image Processing

In `utils.py`, the `analyze_image` function communicates with Google Gemini API to interpret the mathematical expressions from the drawn image.

- **analyze_image**: Accepts image data, generates prompts for the Gemini API, and processes the response to return LaTeX output.

  ```python
  def analyze_image(image: str) -> str:
      response = requests.post(
          GEMINI_API_ENDPOINT,
          headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
          json={"image_data": image},
      )
      ...
      return latex_expression
  ```

### Environmental Configuration

The `constants.py` file loads configuration settings and API keys from environment variables.

```python
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERVER_URL = os.getenv("SERVER_URL")
PORT = os.getenv("PORT")
```

### Schema and Validation

The `ImageData` model in `schema.py` validates incoming image data to ensure compatibility with the API requirements.

---

## Libraries Used

- **FastAPI**: High-performance API framework for Python.
- **Pydantic**: For data validation and settings management.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **dotenv**: For loading environment variables.
- **requests**: Handles HTTP requests to external APIs.

## Usage Notes

- **API Calls**: Ensure the correct API endpoint is used (`/calculate`) with valid image data.
- **Error Handling**: Returns detailed error messages on request validation and API connection issues.

--- 

Feel free to extend or modify this setup as needed!
