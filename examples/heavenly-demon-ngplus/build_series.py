#!/usr/bin/env python3
"""Build the adopted full rewrite."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent/'production/build_rebuild.py'),run_name='__main__')
