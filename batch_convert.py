# 2026-9-14  batch_convert.py

import subprocess
from pathlib import Path

# -------- 配置 --------
INPUT_DIR = r"svg"
OUTPUT_DIR = r"png"
TARGET_WIDTH = 1680
BACKGROUND = "none"  # 填写颜色名；"none" 透明背景
IGNORE_FILES = {
    "bilibili-raw.svg",
    "haskell-raw.svg",
}

def main():
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)

    output_path.mkdir(parents=True, exist_ok=True)

    svg_files = list(input_path.glob("*.svg"))

    if not svg_files:
        print("未在输入文件夹中找到 SVG 文件。")
        return

    print(f"共发现 {len(svg_files)} 个 SVG 文件。开始处理……")

    success_count = 0
    fail_count = 0
    skip_count = 0

    for file in svg_files:
        if file.name in IGNORE_FILES:
            print(f"- 跳过文件: {file.name}")
            skip_count += 1
            continue

        output_file = output_path / f"{file.stem}.png"

        cmd = [
            "magick",
            "-background", BACKGROUND,
            str(file),
            "-resize", f"{TARGET_WIDTH}x",
            str(output_file),
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"- 成功转换: {file.name}\n    -> {output_file.name}")
            success_count += 1
        except subprocess.CalledProcessError as e:
            print(f"- 转换失败: {file.name}\n    - 错误信息: {e.stderr.decode('utf-8', errors='ignore').strip()}")
            fail_count += 1
        except FileNotFoundError:
            print("未找到 ImageMagick。请确保系统已安装 'magick' 并配置了环境变量。")
            return

    print(f"处理完成。成功 {success_count} 个，失败 {fail_count} 个，跳过 {skip_count} 个。")

if __name__ == "__main__":
    main()
