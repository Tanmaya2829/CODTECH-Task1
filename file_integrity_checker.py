
import hashlib
import os

def calculate_hash(file_path, algo='sha256'):
    """Calculate the hash of a file using the selected algorithm."""
    hash_func = getattr(hashlib, algo)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def save_baseline(directory, output_file='baseline.txt'):
    """Generate hash values for all files in a directory and save them."""
    with open(output_file, 'w') as out:
        for root, _, files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)
                hash_val = calculate_hash(path)
                out.write(f"{path}|{hash_val}\n")
    print(f"✅ Baseline saved to {output_file}")

def check_integrity(baseline_file='baseline.txt'):
    """Check file hashes against the saved baseline."""
    with open(baseline_file, 'r') as f:
        lines = f.readlines()

    changed = []
    for line in lines:
        path, old_hash = line.strip().split('|')
        if not os.path.exists(path):
            print(f"❌ File missing: {path}")
            continue
        new_hash = calculate_hash(path)
        if new_hash != old_hash:
            changed.append(path)

    if changed:
        print("⚠️ Changed files detected:")
        for file in changed:
            print(f" - {file}")
    else:
        print("✅ All files are unchanged.")

# Usage example:
# save_baseline("your_folder_path")
# check_integrity()
# Usage example:
# save_baseline("your_folder_path")
# check_integrity()

if __name__ == "__main__":
    #save_baseline("C:/Users/91940/Desktop/test_folder")
    check_integrity()
