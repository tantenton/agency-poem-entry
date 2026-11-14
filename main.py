import os
import shutil
import sys

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

# Autonomous agency poem generator for make.fun agency-poem-01
src = os.path.join(os.path.dirname(__file__), "poem.txt")
dst = os.path.join(out_dir, "entry.txt")

shutil.copyfile(src, dst)
print(f"Successfully generated {dst}")
