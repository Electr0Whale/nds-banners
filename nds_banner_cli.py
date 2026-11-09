#!/usr/bin/env python3
"""
NDS Banners - Unified CLI Entrypoint
"""
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

def main():
    print("=" * 60)
    print("  NDS Banner Tools - CLI Launcher")
    print("=" * 60)
    print("1. 提取所有 ROM Banner 标题至 XML (extract_banner)")
    print("2. 批量格式化并写入 Banner 标题 - 基础版 (nds_banner_editor)")
    print("3. 批量格式化并写入 Banner 标题 - 增强版 V2 (nds_banner_editor_v2)")
    print("0. 退出 (Exit)")
    print("-" * 60)
    
    choice = input("请选择操作 (Select an option) [0-3]: ").strip()
    
    if choice == "1":
        script = SRC_DIR / "extract_banner.py"
        subprocess.run([sys.executable, str(script)])
    elif choice == "2":
        script = SRC_DIR / "nds_banner_editor.py"
        subprocess.run([sys.executable, str(script)])
    elif choice == "3":
        script = SRC_DIR / "nds_banner_editor_v2.py"
        subprocess.run([sys.executable, str(script)])
    elif choice in ("0", "q", "exit"):
        print("已退出。")
        sys.exit(0)
    else:
        print("无效选项。")
        sys.exit(1)

if __name__ == "__main__":
    main()
