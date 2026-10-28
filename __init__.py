"""
ComfyUI MiniMax M3 SongPlanner
==============================

Turn a creative idea into MiniMax Music 3 caption + lyrics using a LOCAL VLM.
No API keys, no external services. Uses ComfyUI's native CLIP text-generation stack.

Pipeline:
    idea → [VLM: caption generation] → caption STRING
    idea + caption → [VLM: lyrics generation] → lyrics STRING

Wire both outputs to MiniMaxMusic3TextEncode.

Pair with ethanfel's MiniMax Music 3 workflow or any Music 3 ComfyUI pipeline.
"""

import sys
import os

_current_dir = os.path.dirname(os.path.abspath(__file__))
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

from .py.nodes import M3SongPlanner

NODE_CLASS_MAPPINGS = {
    "M3SongPlanner": M3SongPlanner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "M3SongPlanner": "🎵 M3 Song Planner (Local VLM)",
}

__version__ = "1.0.0"
