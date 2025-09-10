# batch_narration.py
import os
import re
import requests
from pathlib import Path
import argparse

DEFAULT_PROMPT = """Rewrite the following text into smooth, narration-ready prose.
- Remove OCR artifacts, page numbers, and figure references.
- Keep section headings and concept checks.
- Make sentences flow naturally for an AI narrator.
- Do not shorten content, just clean and smooth it."""

def call_openrouter(text: str, model: str, api_key: str, prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "OCR Narration Cleaner",
    }
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a text rewriter that produces clean narration style."},
                {"role": "user", "content": prompt + "\n\n" + text},
            ],
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunk-dir", default="chunks")
    ap.add_argument("--out", default="build/final.txt")
    ap.add_argument("--model", default="openai/gpt-5-nano")
    ap.add_argument("--prompt-file", default=None)
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY not set")

    prompt = Path(args.prompt_file).read_text(encoding="utf-8") if args.prompt_file else DEFAULT_PROMPT

    def chunk_index(p: Path):
        m = re.search(r"chunk_(\d+)\.txt$", p.name)
        return int(m.group(1)) if m else 0

    chunk_files = sorted(Path(args.chunk_dir).glob("chunk_*.txt"), key=chunk_index)
    if not chunk_files:
        raise SystemExit("No chunks found. Run precleaning first.")

    merged = []
    for i, cf in enumerate(chunk_files, 1):
        raw = cf.read_text(encoding="utf-8")
        print(f"Processing {cf.name} ({len(raw)} chars)")
        rewritten = call_openrouter(raw, args.model, api_key, prompt)
        merged.append(rewritten)
        Path(f"{args.chunk_dir}/out_{i}.txt").write_text(rewritten, encoding="utf-8")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n\n".join(merged), encoding="utf-8")
    print(f"Narration -> {args.out}")

if __name__ == "__main__":
    main()
