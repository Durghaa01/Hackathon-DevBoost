# services/openai_service.py
import httpx
import asyncio

print(">>> LM Studio AI Service Loaded <<<")

# LM Studio local API URL (OpenAI-compatible)
LMSTUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"

# Model name (make sure it's already downloaded and loaded in LM Studio)
MODEL_NAME = "liquid/lfm2-1.2b"

async def generate_docs(code: str):
    """
    Generate Markdown documentation for Python code using LM Studio.
    """
    prompt = f"Generate clear Markdown documentation for this Python code:\n\n{code}"
    data = {}  # fallback in case of error

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                LMSTUDIO_API_URL,
                json={
                    "model": MODEL_NAME,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0
                }
            )
            response.raise_for_status()  # Raise exception for non-2xx responses
            data = response.json()
            print(">>> LM Studio Response (Docs):", data)

            # Extract content
            if "choices" in data and len(data["choices"]) > 0:
                choice = data["choices"][0]
                if "message" in choice and "content" in choice["message"]:
                    return choice["message"]["content"]
                elif "text" in choice:  # fallback for text-only responses
                    return choice["text"]

    except httpx.RequestError as e:
        print(">>> LM Studio Request Error (Docs):", str(e))
        return f"Error: Request failed: {str(e)}"
    except httpx.HTTPStatusError as e:
        print(">>> LM Studio HTTP Error (Docs):", str(e))
        return f"Error: HTTP error: {str(e)}"
    except Exception as e:
        print(">>> LM Studio General Error (Docs):", str(e))
        return f"Error: Unexpected error: {str(e)}"

    return f"Error: Unexpected response from LM Studio: {data}"


async def generate_tests(code: str):
    """
    Generate Python unit tests (PyTest style) for Python code using LM Studio.
    """
    prompt = f"Generate Python unit tests (PyTest style) for this function:\n\n{code}"
    data = {}

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                LMSTUDIO_API_URL,
                json={
                    "model": MODEL_NAME,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0
                }
            )
            response.raise_for_status()
            data = response.json()
            print(">>> LM Studio Response (Tests):", data)

            # Extract content
            if "choices" in data and len(data["choices"]) > 0:
                choice = data["choices"][0]
                if "message" in choice and "content" in choice["message"]:
                    return choice["message"]["content"]
                elif "text" in choice:
                    return choice["text"]

    except httpx.RequestError as e:
        print(">>> LM Studio Request Error (Tests):", str(e))
        return f"Error: Request failed: {str(e)}"
    except httpx.HTTPStatusError as e:
        print(">>> LM Studio HTTP Error (Tests):", str(e))
        return f"Error: HTTP error: {str(e)}"
    except Exception as e:
        print(">>> LM Studio General Error (Tests):", str(e))
        return f"Error: Unexpected error: {str(e)}"

    return f"Error: Unexpected response from LM Studio: {data}"
