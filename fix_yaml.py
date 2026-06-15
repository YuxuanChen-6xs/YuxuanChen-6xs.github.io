import os
import re

# 如果你的文章在其他文件夹，请修改这里的路径
POSTS_DIR = '.'

def standardize_front_matter(front_matter):
    """
    按标准格式重构 YAML 头部信息
    """
    lines = front_matter.strip().split('\n')
    new_lines = []

    for line in lines:
        # 正则匹配顶层的键值对，例如 "title: xxx"
        # ^([a-z]+) 匹配行首的小写英文字母键名
        match = re.match(r'^([a-z]+):\s*(.*)$', line)
        
        if match:
            key = match.group(1)
            value = match.group(2).strip()

            # 1. 文本类字段：强制加双引号
            if key in ['title', 'linktitle', 'author']:
                if value and not ((value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'"))):
                    # 转义内部可能存在的双引号
                    safe_value = value.replace('"', '\\"')
                    new_lines.append(f'{key}: "{safe_value}"')
                else:
                    new_lines.append(f'{key}: {value}')
            
            # 2. 常规字段：确保冒号后只有一个空格
            elif key in ['date', 'weight', 'next', 'prev', 'tags']:
                new_lines.append(f'{key}: {value}')
            
            # 3. 带有子层级的字段（如 menu）
            else:
                if value:
                    new_lines.append(f'{key}: {value}')
                else:
                    new_lines.append(f'{key}:')
        else:
            # 4. 保留嵌套的层级结构（如 menu 下的 main 和 parent）及空行
            new_lines.append(line)

    return '\n'.join(new_lines) + '\n'

def main():
    count = 0
    print("🔍 开始扫描并标准化 Markdown 文件格式...")
    
    for root, dirs, files in os.walk(POSTS_DIR):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)

                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 分割出 Front Matter 区域 (通常在两个 --- 之间)
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    original_fm = parts[1]
                    body = parts[2]

                    # 执行标准化格式化
                    standardized_fm = standardize_front_matter(original_fm)
                    
                    # 只有当格式真正发生改变时，才写入文件
                    if standardized_fm != original_fm:
                        new_content = f"---{standardized_fm}---{body}"
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        print(f"✅ 已修正: {filepath}")

    print(f"\n🎉 批量格式化完成！共规范了 {count} 篇文章。")

if __name__ == '__main__':
    main()