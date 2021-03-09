"""Module to create exe file."""
from distutils.core import setup
import py2exe
import scrabble_randomiser

console = [
    {
        "script": "main.py",  ### Main Python script
        "dest_base": "scrabble_trainer"
    }]
options = {
    'py2exe': {
        'bundle_files': 1,
        'compressed': True,
        'dist_dir': "scrabble_trainer",
    }
}
setup(
    console=console,
    options=options,
    zipfile=None
)
