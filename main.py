# import sys
# import importlib.util
# import os
# import tkinter as tk

# def import_pyc(name, pyc_path):
#     spec = importlib.util.spec_from_file_location(name, pyc_path)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     return module

# # Path ke folder build/
# build_dir = os.path.join(os.path.dirname(__file__), "build")

# # Masukkan 'build/' ke sys.path agar import di dalam .pyc bisa temukan module lain
# sys.path.insert(0, build_dir)

# # Import dari file .pyc
# app = import_pyc("app", os.path.join(build_dir, "app.pyc"))
# gui = import_pyc("gui", os.path.join(build_dir, "gui.pyc"))

# # Jalankan GUI
# if __name__ == "__main__":
#     root = tk.Tk()
#     gui.KipappGUI(root)
#     root.mainloop()
import importlib.util
import os
import sys

def run_pyc(path_to_pyc):
    try:
        # Tambahkan folder build ke sys.path agar .pyc lain bisa diimpor
        build_dir = os.path.dirname(path_to_pyc)
        if build_dir not in sys.path:
            sys.path.insert(0, build_dir)

        spec = importlib.util.spec_from_file_location("__main__", path_to_pyc)
        module = importlib.util.module_from_spec(spec)
        sys.modules["__main__"] = module
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"❌ Gagal menjalankan '{path_to_pyc}': {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pyc_path = os.path.join(base_dir, "build", "gui.pyc")

    if os.path.exists(pyc_path):
        run_pyc(pyc_path)
    else:
        print(f"❌ File '{pyc_path}' tidak ditemukan.")
