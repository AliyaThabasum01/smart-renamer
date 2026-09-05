# 🔄 Smart Renamer

A lightweight Python CLI tool for renaming multiple files with a custom prefix and automatic numbering.

## Features

- Rename files in bulk
- Custom filename prefix
- Automatic numbering
- Preserve file extensions
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
Enter folder path: ./photos
Enter new filename prefix: vacation

✅ Renamed 5 files successfully.
```

The files become:

```text
vacation_1.jpg
vacation_2.jpg
vacation_3.png
vacation_4.jpg
vacation_5.png
```

## Built With

- Python
- os
