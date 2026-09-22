"""读取并校验共享领域资料。"""

import json
from pathlib import Path

REQUIRED = {"domain", "version", "sample_id", "record_types", "workflow_states", "facts", "sample"}

def load_domain(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not REQUIRED.issubset(value) or value["version"] < 1:
        raise ValueError("领域资料缺少必要内容")
    if len(value["record_types"]) < 4 or len(value["workflow_states"]) < 4:
        raise ValueError("领域资料的记录或状态不完整")
    return value
