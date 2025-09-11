import os
import glob
import sys

def combine_md_files(input_folder, output_file="combined.md"):
    """
    Combines all .md files in the input_folder into a single Markdown file.
    
    Args:
        input_folder (str): Path to the folder containing .md files.
        output_file (str): Name of the output file (default: 'combined.md').
    
    Returns:
        None
    """
    
    # Normalise the input folder path
    input_folder = os.path.abspath(input_folder)

    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' does not exist.")
        return
    
    # Find all .md files in the folder
    md_files = glob.glob(os.path.join(input_folder, "*.md"))

    if not md_files:
        print(f"Error: no .md files found in '{input_folder}'")
        return

    # Sort alphabetically
    md_files.sort()

    print(f"Found {len(md_files)} .md files. Combining...")

    # Read and combine contents
    combined_content = []

    for file_path in md_files:
        filename = os.path.basename(file_path)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Add a sepeartor with the filename
            seperator = f"\n\n---\n\n**Source: {filename}**\n\n---\n\n"
            combined_content.append(seperator + content)

            print(f"  Added: {filename}")

        except Exception as e:
            print(f"Error reading {file_path}: {e}")    
    
    # Write to output file
    output_path = os.path.join(input_folder, output_file)
    try:
        with open(output_path, 'w', encoding="utf-8") as f:
            f.write("# Combined Markdown Files\n\n")
            f.writelines(combined_content)

        print(f"\nCombined file saved as: {output_path}")
        print(f"Total files processed: {len(md_files)}")

    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python combine_md.py <input_folder_path>")
        sys.exit(1)

    input_folder = sys.argv[1]
    combine_md_files(input_folder)