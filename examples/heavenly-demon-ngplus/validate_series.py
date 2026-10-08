#!/usr/bin/env python3
"""Validate the adopted full rewrite at real phone viewports."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent/'production/validate_rebuild.py'),run_name='__main__')
