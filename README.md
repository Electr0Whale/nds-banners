# NDS Banner Tools

[中文](#中文说明) · [English](#english)

## 中文说明

一组用于读取和批量修改 Nintendo DS ROM banner 标题的 Python 工具。脚本直接处理 `.nds` 文件中的 banner 数据，因此运行前必须保留原始 ROM 备份。

### 工具

- `extract_banner.py`：扫描目录中的 `.nds` 文件，提取各语言标题并写入 `banners.xml`。
- `nds_banner_editor.py`：根据 ROM 文件名生成两行标题，写入可用语言槽并重新计算 banner CRC16。
- `nds_banner_editor-V2.py`：扩展文件名解析规则和地区标签处理的版本，同样生成错误报告并修复 CRC16。

编辑器预期的文件名结构为：

```text
GameName(Region)(Translator)(Size).nds
```

例如：

```text
Mario Party(JP)(ACG-Hans)(512Mb).nds
```

### 使用

需要 Python 3；脚本只使用 Python 标准库。

```powershell
git clone https://github.com/Electr0Whale/nds-banner-tools.git
cd nds-banner-tools
python .\extract_banner.py
python .\nds_banner_editor-V2.py
```

脚本会通过对话提示选择或输入目标目录。批量修改前请复制一份 ROM，并在模拟器或校验工具中验证结果。

### 历史说明

本仓库曾误提交一个与 banner 工具无关的个人 3DS 存档压缩包。该文件已迁移到私有备份仓库，并从本仓库全部可达 Git 历史中清除。已有克隆需要重新克隆，不能继续基于旧历史拉取。

## English

Python utilities for extracting and batch-editing title strings in Nintendo DS ROM banners.

- `extract_banner.py` exports all available language titles to `banners.xml`.
- `nds_banner_editor.py` creates a two-line title from the ROM filename and recalculates the banner CRC16.
- `nds_banner_editor-V2.py` expands filename and region parsing while retaining the same validation and CRC repair behavior.

Back up every ROM before editing. These scripts modify binary data in place, and a valid CRC does not guarantee that every ROM or flashcart will accept the result.
