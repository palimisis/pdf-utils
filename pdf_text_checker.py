import argparse
import os
import shutil

import fitz  # PyMuPDF


def check_pdfs_for_text(source_dir, destination_dir, min_text_length=100, excluded_directories=None):
    """
    Checks all PDF files in the source directory for text content.
    Copies PDF files with text length less than `min_text_length` to the destination directory.

    :param source_dir: The root directory to search for PDF files.
    :param destination_dir: The directory to copy PDFs with minimal text to.
    :param min_text_length: The minimum length of text required to consider a PDF as containing text.
    """
    if not os.path.exists(source_dir):
        print(f"The source directory '{source_dir}' does not exist.")
        return

    os.makedirs(destination_dir, exist_ok=True)

    found_files = []

    for root, _, files in os.walk(source_dir):
        if excluded_directories and any([d in root for d in excluded_directories]):
            continue
        
        for file in files:
            if file.lower().endswith(".pdf") and not file.startswith("."):
                text = ""
                pdf_path = os.path.join(root, file)
                try:
                    with fitz.open(pdf_path) as pdf_file:
                        for page in pdf_file:
                            text += page.get_text()

                    if len(text) < min_text_length:
                        print(f"File with minimal text: {pdf_path}")
                        found_files.append(pdf_path)

                except Exception as e:
                    print(f"Error reading {pdf_path}: {e}")

    # Copy identified files to the destination directory
    for file in found_files:
        shutil.copy(file, destination_dir)
        print(f"Copied: {file} to {destination_dir}")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--source_directory", required=True, help="The root directory to search for PDF files.")
    args.add_argument("--destination_directory", required=True, help="The directory to copy PDFs with minimal text to.")
    args.add_argument("--min_text_length", type=int, default=100, help="The minimum length of text required to consider a PDF as containing text.")
    args.add_argument("--excluded_directories", nargs="+", help="Directories to exclude from the search.")
    args = args.parse_args()

    check_pdfs_for_text(args.source_directory, args.destination_directory, args.min_text_length, args.excluded_directories)