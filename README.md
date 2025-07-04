Name:Tanmaya Hodawadekar
Company:CODTECH IT SOLUTION
ID:CT04DF2359
Domain:Cyber Security & Ethical Hacking 
Duration: 5May to 5June 2025
Mentor: Neela Santosh Kumar


Task 1: File Integrity Checker

This is a Python-based **File Integrity Checker** that monitors changes in files by calculating and comparing their hash values. 
It helps detect if any files have been modified, tampered with, or deleted.
## Features
- ✅ Calculates SHA256 hash values of files
- ✅ Stores file paths and their hashes in a `baseline.txt`
- ✅ Detects changes, missing files, or tampering
- ✅ Prints changed or missing files clearly
## Requirements

- Python 3.6 or higher

> No external libraries are needed — uses built-in modules (`hashlib`, `os`)

## File Structure

file_integrity_checker/
├── file_integrity_checker.py
└── baseline.txt
## How to Run

### 🔹 Step 1: Save the current state (baseline)

Edit the last lines in `file_integrity_checker.py`:
if __name__ == "__main__":
    save_baseline("C:/Users/YourName/Desktop/test_folder")
Then run:
python file_integrity_checker.py

### 🔹 Step 2: Check file integrity later

Change the bottom code to:
if __name__ == "__main__":
    check_integrity()
Then run again:
python file_integrity_checker.py

## Example Output

✅ Baseline saved to `baseline.txt`  
✅ All files are unchanged.
Or if something changed:
⚠️ Changed files detected:
 - C:/path/to/changed_file.txt
❌ File missing: C:/path/to/missing_file.txt

##  Use Case

- Track file changes in important directories (e.g., configuration files, logs)
- Detect tampering or accidental overwrites

#output:
![Screenshot 2025-07-03 190524](https://github.com/user-attachments/assets/1df56e64-0326-4952-93ca-c4752fa457e9)

