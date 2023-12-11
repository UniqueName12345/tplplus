import subprocess
import pkg_resources

def check_and_install_library(library_name, import_name=None):
    """Check if a library is installed, and install it if it's not present."""
    try:
        pkg_resources.require(import_name or library_name)
    except pkg_resources.DistributionNotFound:
        subprocess.run(
            ["pip", "install", library_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

check_and_install_library("lark_parser", "lark")

