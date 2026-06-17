# File Date Renamer

A simple Python tool for renaming files based on their last modification date.

## Features
- Rename files to the format: `YYYY-MM-DD.ext`
- Automatically avoids overwriting files by adding a counter
- Supports any file extension (e.g. `.png`, `.jpg`, `.pdf`)
- Includes preview mode to see changes before applying

## Scripts

### Rename files (applies changes)
```bash
file-date-renamer.py
```

### Preview renaming (no changes)
```bash
preview-file-date-renamer.py
```

## Example

Before:
```
IMG_1234.jpg
holiday.png
report.pdf
```

After:
```
2024-06-15.jpg
2024-06-16.png
2024-06-17.pdf
```

## Use case
Useful for organizing folders with many files where naming is inconsistent.
