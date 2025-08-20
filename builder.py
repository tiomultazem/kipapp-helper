# builder.py
import os
import shutil
import py_compile

SRC_DIR = "src"
BUILD_DIR = "build"

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

def compile_semua_py():
    for filename in os.listdir(SRC_DIR):
        if filename.endswith(".py") and not filename.startswith("_"):
            source_path = os.path.join(SRC_DIR, filename)
            target_filename = filename.replace(".py", ".pyc")
            target_path = os.path.join(BUILD_DIR, target_filename)
            try:
                py_compile.compile(source_path, cfile=target_path, doraise=True)
                print(f"✅ {filename} -> build/{target_filename}")
            except py_compile.PyCompileError as e:
                print(f"❌ Gagal compile {filename}: {e}")

if __name__ == "__main__":
    bersihkan_build()
    hapus_semua_pycache(SRC_DIR)
    compile_semua_py()
    print("🔥 Build selesai. Semua .pyc berdiri sendiri di /build.")
