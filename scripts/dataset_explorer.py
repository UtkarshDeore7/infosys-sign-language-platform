import os
import json
from pathlib import Path

# Auto-detect project root (no hardcoded paths)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASL_PATH = PROJECT_ROOT / "ml" / "datasets" / "asl-alphabet" / "asl_alphabet_train" / "asl_alphabet_train"
WLASL_JSON = PROJECT_ROOT / "ml" / "datasets" / "wlasl" / "wlasl-complete" / "WLASL_v0.3.json"

def explore_asl():
    print("=" * 50)
    print("ASL ALPHABET DATASET")
    print("=" * 50)

    classes = sorted(os.listdir(ASL_PATH))
    print(f"Total Classes: {len(classes)}")
    print(f"Classes (alphabetical): {classes}")

    total_images = 0
    for cls in classes:
        count = len(os.listdir(ASL_PATH / cls))
        total_images += count
        print(f"  {cls}: {count} images")

    print(f"Total Images: {total_images}")

def explore_wlasl():
    print("\n" + "=" * 50)
    print("WLASL DATASET")
    print("=" * 50)

    with open(WLASL_JSON, "r") as f:
        data = json.load(f)

    print(f"Annotation File: {WLASL_JSON}")
    print(f"Unique Signs: {len(data)}")
    print("\n5 Sample Entries:")
    for entry in data[:5]:
        print(f"  Sign: {entry['gloss']} | Instances: {len(entry['instances'])}")

if __name__ == "__main__":
    explore_asl()
    explore_wlasl()