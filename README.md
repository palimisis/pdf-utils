# pdf-utils

A Python utility for checking PDF files.

## Description

This repository contains a script that scans a directory for PDF files, checks their text content, and copies files with minimal text to a specified destination directory. It's useful for identifying PDFs that might be scanned images or have very little textual content.

## Features

- Recursively scans directories for PDF files
- Checks the text content of each PDF
- Copies PDFs with text content below a specified threshold to a destination directory
- Allows exclusion of specific directories from the search

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/palimisis/pdf-utils.git
   cd pdf-utils
   ```

2. Install the required dependencies:
   ```
    conda env create -f environment.yml
   ```

## Usage

Run the script from the command line with the following arguments:

```
python pdf_text_checker.py --source_directory <source_dir> --destination_directory <dest_dir> [--min_text_length <length>] [--excluded_directories <dir1> <dir2> ...]
```

Arguments:
- `--source_directory`: The root directory to search for PDF files.
- `--destination_directory`: The directory to copy PDFs with minimal text to.
- `--min_text_length`: (Optional) The minimum length of text required to consider a PDF as containing text. Default is 100.
- `--excluded_directories`: (Optional) Directories to exclude from the search.

## Example

```
python pdf_text_checker.py --source_directory /path/to/pdfs --destination_directory /path/to/output --min_text_length 50 --excluded_directories temp archive
```

This command will search for PDFs in `/path/to/pdfs`, excluding the `temp` and `archive` subdirectories. It will copy any PDFs with less than 50 characters of text to `/path/to/output`.
