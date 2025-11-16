import importlib.util
import os
import sys

def pilih_folder_build():
    """Mengembalikan folder build sesuai versi Python yang sedang aktif."""
    major = sys.version_info.major
    minor = sys.version_info.minor

    versi = f"{major}.{minor}"

    # Mapping folder build berdasarkan versi Python
    mapping = {
        "3.12": "build12",
        "3.13": "build13",
        "3.14": "build14",   # opsional, siap kalau nanti ada
    }

    if versi in mapping:
        return mapping[versi]

    raise RuntimeError(f"Tidak ada folder build untuk Python {versi}")

def run_pyc(pyc_path):
    try:
        build_dir = os.path.dirname(pyc_path)
        if build_dir not in sys.path:
            sys.path.insert(0, build_dir)

        spec = importlib.util.spec_from_file_location("__main__", pyc_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules["__main__"] = module
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"❌ Gagal menjalankan '{pyc_path}': {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        folder_build = pilih_folder_build()
    except RuntimeError as e:
        print(f"❌ {e}")
        sys.exit(1)

    pyc_path = os.path.join(base_dir, folder_build, "gui.pyc")

    if os.path.exists(pyc_path):
        print(f"▶️ Menjalankan {pyc_path} dengan Python {sys.version.split()[0]}")
        run_pyc(pyc_path)
    else:
        print(f"❌ File '{pyc_path}' tidak ditemukan.")
