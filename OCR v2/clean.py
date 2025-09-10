# clean.py
import re
from pathlib import Path
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="input_file", required=True)
    p.add_argument("--out", dest="output_file", default="build/preclean.txt")
    p.add_argument("--chunk-dir", default="chunks")
    p.add_argument("--chunk-size", type=int, default=4000)
    args = p.parse_args()

    raw = Path(args.input_file).read_text(encoding="utf-8", errors="ignore")

    clean = re.sub(r"Copyright ©.*?\n", " ", raw)
    clean = re.sub(r"Figure\s*\d+(\.\d+)?[^\n]*", " ", clean)
    clean = re.sub(r"V Figure.*", " ", clean)
    clean = re.sub(r"\bCHAPTER\s+\d+.*?\n", " ", clean)
    clean = re.sub(r"\n\s*\d{1,4}\s*\n", " ", clean)

    clean = clean.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'").replace("—", "-")
    clean = re.sub(r"\b[a-z]{1,2}\s+[A-Z][a-z]+\b", " ", clean)
    clean = re.sub(r"\n+", " ", clean)
    clean = re.sub(r"\s{2,}", " ", clean)

    clean = re.sub(r"(CONCEPT CHECK \d+\.\d+)", r"\n\n\1\n", clean)
    clean = re.sub(r"(CONCEPT \d+\.\d+)", r"\n\n\1\n", clean)
    clean = re.sub(r"(Key Concepts:)", r"\n\n\1\n", clean)
    clean = re.sub(r"(Chapter \d+\. .*?) ", r"\n\n\1\n", clean)

    Path(args.output_file).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output_file).write_text(clean, encoding="utf-8")

    Path(args.chunk_dir).mkdir(exist_ok=True)
    for i in range(0, len(clean), args.chunk_size):
        chunk = clean[i:i+args.chunk_size]
        Path(f"{args.chunk_dir}/chunk_{i//args.chunk_size+1}.txt").write_text(chunk, encoding="utf-8")

    print(f"Preclean -> {args.output_file}")
    print(f"Chunks -> {args.chunk_dir}")

if __name__ == "__main__":
    main()
