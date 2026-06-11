import os
import sys

# 현재 활성화된 conda 환경 경로를 자동으로 찾음
env_path = sys.prefix
docling_parse_path = os.path.join(env_path, "Lib", "site-packages", "docling_parse")
sitecustomize_path = os.path.join(env_path, "sitecustomize.py")

with open(sitecustomize_path, "w", encoding="utf-8") as f:
    f.write("import os\n")
    f.write(f'os.add_dll_directory(r"{docling_parse_path}")\n')