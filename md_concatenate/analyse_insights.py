import os
import sys
import requests
import json

def analyse_document(file_path, api_key, model="meta-llama/llama-3.3-8b-instruct:free",
num_insights=15):
    """
    Reads a Markdown file and uses OpenRouter API to extract top insights.
    
    Args:
        file_path (str): Path to the combined Markdown file.
        api_key (str): OpenRouter API key.
        model (str): OpenRouter model name (default: "meta-llama/llama-3.3-8b-instruct:free").
        num_insights (int): Number of top insights to extract (default: 15).
    
    Returns:
        str: The LLM's response (insights) (print to console).
    """

    # 1: Read document
    if not os.path.exists(file_path):
        raise ValueError(f"File '{file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as f:
        document_content = f.read()

    print(f"Document loaded: {len(document_content.split())} words (~{len(document_content)/4} tokens estimated)")

    # 2: Construct the prompt
    prompt = f"""
    You are an expert analyst. Analyze the following document and extract the {num_insights} best insights.
    
    An "insight" is a concise, valuable takeaway, key lesson, pattern, or piece of information that stands out as important, actionable, or thought-provoking. 
    Focus on depth over breadth—prioritize novel, non-obvious, or high-impact ideas. Ignore fluff, repetitions, or administrative content.
    
    For each insight:
    - Write it out, verbatim, as it occurs in the document
    - Reference the relevant section(s) or source file(s) from the document (e.g., "From file1.md"). Do not include any further explanation.
    
    Output only a numbered list of the top {num_insights} insights, ranked by importance. No introduction or conclusion—just the list.
    
    Document Content:
    {document_content}
    """

    # 3: Prepare API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 3000, # Output limit
        "temperature": 0.3, # Low for focussed, consistent output
    }

    # 4: Make API call
    api_url = "https://openrouter.ai/api/v1/chat/completions"

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status() # Raise error for bad status

        result = response.json()
        insights = result["choices"][0]["message"]["content"].strip()

        print("API call successful! Insights extracted.")
        print("\n" + "="*50)
        print(insights)
        print("\n" + "="*50)

    except requests.exceptions.RequestException as e:
        error_msg = response.json().get("error", {}).get("message", str(e) if "response" in locals() else str(e))
        raise RuntimeError(f"API request failed: {error_msg}")
    except KeyError as e:
        raise RuntimeError(f"Unexpected API response format: {e}")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyse_insights.py <file_path> [model] [num_insights]")

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY not set")
    file_path = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else "meta-llama/llama-3.3-8b-instruct:free"
    num_insights = int(sys.argv[3]) if len(sys.argv) > 3 else 15

    try:
        analyse_document(file_path, api_key, model, num_insights)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
