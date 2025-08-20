import os
import shutil
from pathlib import Path
import fnmatch

ROOT = Path(__file__).resolve().parent
DEST = ROOT.parent / "public"
GITIGNORE = ROOT / ".gitignore"

# ==========================
# 1. Baca daftar ignore
# ==========================

ignore_patterns = []

if GITIGNORE.exists():
    with GITIGNORE.open() as f:
        for line in f:
            rule = line.strip()
            if not rule or rule.startswith("#"):
                continue
            ignore_patterns.append(rule)

# Tambahan manual (untuk menghindari gagal match)
ignore_patterns += [
    ".git",
    "src", "src/"

]

def is_ignored(path: Path):
    rel_path = path.relative_to(ROOT).as_posix()
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(rel_path, pattern) or rel_path.startswith(pattern.rstrip("/") + "/"):
            return True
    return False

# ==========================
# 2. Hapus semua isi ../public kecuali .git
# ==========================

print("🧹 Menghapus isi folder /public (kecuali .git)...")
for item in DEST.iterdir():
    if item.name == ".git":
        continue
    if item.is_dir():
        shutil.rmtree(item)
    else:
        item.unlink()

# ==========================
# 3. Salin file yang tidak di-ignore
# ==========================

print("📁 Menyalin file ke /public...")

for root_dir, dirs, files in os.walk(ROOT):
    root_path = Path(root_dir)
    rel_root = root_path.relative_to(ROOT)

    if is_ignored(root_path):
        dirs[:] = []
        continue

    dest_root = DEST / rel_root
    dest_root.mkdir(parents=True, exist_ok=True)

    for file in files:
        src_file = root_path / file
        if is_ignored(src_file):
            continue
        shutil.copy2(src_file, dest_root / file)

print("✅ Selesai. Folder /public sudah diperbarui.")
