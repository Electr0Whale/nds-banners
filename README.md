# NDS Banners (`nds-banners`)

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Nintendo%20DS-e60012.svg?style=flat-square" alt="Platform">
  <img src="https://img.shields.io/badge/Language-Python%203-3776ab.svg?style=flat-square" alt="Python 3">
  <img src="https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-brightgreen.svg?style=flat-square" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/Status-Maintained-blue.svg?style=flat-square" alt="Status">
</p>

[中文说明](#中文说明) · [English](#english)

---

## 中文说明

一组用于读取、提取与批量修改 Nintendo DS ROM Banner 标题与元数据的 Python 工具集。工具直接操作 `.nds` 二进制文件中的 Banner 数据区并自动校验/修复 CRC16，无需任何第三方外部依赖。

> [!WARNING]
> 脚本直接原地修改 `.nds` 文件的二进制数据。在批量运行修改前，**请务必为原始 ROM 制作完整副本备份**。

### 目录与文件结构

```text
nds-banners/
├── src/
│   ├── extract_banner.py          # 提取 ROM Banner 标题至 banners.xml
│   ├── nds_banner_editor.py       # 基础版：按规则写入双行标题并重算 CRC16
│   └── nds_banner_editor_v2.py    # 增强版：扩充地区标签解析与报错校验
├── nds_banner_cli.py              # 统一命令行交互式快速启动入口
└── README.md
```

### 工具说明

- **`src/extract_banner.py`**：递归扫描指定目录下的所有 `.nds` 文件，提取包含日语、英语、法语、德语、意大利语、西班牙语等各语言槽位的 Banner 标题，统一导出为 `banners.xml`。
- **`src/nds_banner_editor.py`**：根据 ROM 文件名自动生成规范的双行标题，写入可用语言槽并自动重新计算写入 Banner CRC16 校验码。
- **`src/nds_banner_editor_v2.py`**：增强版解析器，扩展对文件名、地区代码（`JP`, `US`, `EU`, `CN` 等）与汉化组标签的处理，生成详细处理报告并校验数据完整性。
- **`nds_banner_cli.py`**：集成式命令行菜单，快速调用上述任一工具。

### 命名预期规范

编辑器默认支持且推荐的标准 ROM 命名结构：

```text
GameName(Region)(Translator)(Size).nds
```

示例：
```text
Mario Party(JP)(ACG-Hans)(512Mb).nds
```

### 快速开始

仅需 Python 3 环境（仅依赖 Python 标准库）：

```powershell
# 1. 克隆仓库
git clone https://github.com/Electr0Whale/nds-banners.git
cd nds-banners

# 2. 通过交互式菜单启动
python nds_banner_cli.py

# 或直接运行特定工具
python src/extract_banner.py
python src/nds_banner_editor_v2.py
```

---

## English

A suite of standalone Python utilities for extracting, inspecting, and batch-editing title strings in Nintendo DS ROM banners with automatic CRC16 recalculation.

### Key Features
- **Zero Third-party Dependencies**: Built purely on the Python 3 standard library (`struct`, `os`, `xml.etree`).
- **Batch Processing**: Scans directories for `.nds` files and extracts/patches titles in bulk.
- **CRC16 Verification & Repair**: Automatically fixes the Banner checksum to ensure ROM integrity.
- **Structured Layout**: Core engines organized under `src/` with a unified launcher `nds_banner_cli.py`.

### Quickstart

```powershell
git clone https://github.com/Electr0Whale/nds-banners.git
cd nds-banners
python nds_banner_cli.py
```

### Disclaimer
Always create backups before running batch modifications. These utilities directly modify binary segments of `.nds` ROM files.
