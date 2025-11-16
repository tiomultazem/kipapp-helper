import os
import shutil
import json
import subprocess
from datetime import datetime

SRC_DIR = "src"
BUILD_DIR = "build3.13"
CONFIG_FILE = "config.json"
CHANGELOG_FILE = "changelog.json"
PYTHON313 = "py -3.13"

def bersihkan_build():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR, exist_ok=True)

def hapus_semua_pycache(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                full_path = os.path.join(root, dir_name)
                shutil.rmtree(full_path)
                print(f"🧹 Hapus: {full_path}")

def compile_dengan_python313():
    """Kompilasi semua .py menggunakan Python 3.13 → hasil ke build3.13"""
    os.makedirs(BUILD_DIR, exist_ok=True)
    for filename in os.listdir(SRC_DIR):
        if filename.endswith(".py") and not filename.startswith("_"):
            source_path = os.path.join(SRC_DIR, filename)
            target_path = os.path.join(BUILD_DIR, filename.replace(".py", ".pyc"))
            try:
                subprocess.run(
                    ["py", "-3.13", "-m", "py_compile", source_path],
                    check=True,
                )
                # Pindahkan hasil dari __pycache__ ke build3.13
                pycache_dir = os.path.join(SRC_DIR, "__pycache__")
                for f in os.listdir(pycache_dir):
                    if f.startswith(filename.replace(".py", "")) and f.endswith(".pyc"):
                        shutil.move(os.path.join(pycache_dir, f), target_path)
                        print(f"✅ {filename} -> {BUILD_DIR}/{os.path.basename(target_path)}")
                shutil.rmtree(pycache_dir)
            except subprocess.CalledProcessError:
                print(f"❌ Gagal compile {filename}")

def tulis_version_ke_config():
    today = datetime.now()
    version_str = today.strftime("2.%y%m%d")

    if not os.path.exists(CONFIG_FILE):
        print("⚠️ config.json tidak ditemukan, membuat baru...")
        config = {}
    else:
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            config = {}

    config["version"] = version_str

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print(f"📝 Versi diperbarui menjadi {version_str} di config.json")
    return version_str

def tulis_changelog(version_str):
    print("\n🪵 Masukkan changelog (maksimal 3 baris). Tekan ENTER tanpa isi untuk melewati baris.\n")
    changelog_entries = []
    for i in range(1, 4):
        line = input(f"changelog baris ke-{i}: ").strip()
        if line:
            changelog_entries.append(line)
        else:
            break

    if not changelog_entries:
        print("⚠️ Tidak ada changelog yang dimasukkan, dilewati.")
        return

    if os.path.exists(CHANGELOG_FILE):
        try:
            with open(CHANGELOG_FILE, "r", encoding="utf-8") as f:
                changelog = json.load(f)
        except json.JSONDecodeError:
            changelog = {}
    else:
        changelog = {}

    changelog[version_str] = changelog_entries

    with open(CHANGELOG_FILE, "w", encoding="utf-8") as f:
        json.dump(changelog, f, indent=4, ensure_ascii=False)

    print(f"📜 Changelog versi {version_str} berhasil ditulis ke {CHANGELOG_FILE}\n")

if __name__ == "__main__":
    version = tulis_version_ke_config()
    tulis_changelog(version)

    bersihkan_build()
    hapus_semua_pycache(SRC_DIR)
    compile_dengan_python313()

    print("🔥 Build selesai. Semua .pyc versi Python 3.13 tersimpan di /build3.13.")
