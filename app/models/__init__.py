import importlib
import os


def import_models():
    """
    Essa função importa automaticamente os models para que a migration possa reconhece-los.
    Pode se usar a função "__all__ = []" mas nesse caso teria que informar manualmente cada model.
    """

    IDENTIFICATION_FILES = "_model.py"
    MODEL_EXCLUDE_FILES = []

    for dirpath, dirnames, filenames in os.walk("."):
        for file in filenames:
            if file.endswith(IDENTIFICATION_FILES) and file not in MODEL_EXCLUDE_FILES:
                filename_no_ext, _ = os.path.splitext(os.path.join(dirpath, file))
                filename_no_ext = filename_no_ext[2:]
                module_path = filename_no_ext.replace(os.sep, ".")
                importlib.import_module(module_path)
