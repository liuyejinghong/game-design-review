#!/usr/bin/env python3
"""本仓库静态契约检查；仅用标准库，不执行游戏，不写仓库。"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

REQUIRED = (
    'SKILL.md', 'VERSION', 'VERSIONING.md', 'CHANGELOG.md', 'README.md',
    'references/orchestration.md', 'references/adjudication.md',
    'references/first-visit.md', 'references/critic-scoring.md',
    'references/human-playtest.md', 'references/experience-regression.md',
    'references/benchmarks.md', 'agents/blind-player.md', 'tests/acceptance.md',
)
TRIGGERS = ('游戏验收', '试玩评审', '好不好玩', '像不像个游戏', '策划视角评估', '游戏感评审')


def check(root: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'缺文件：{name}')
    if errors:
        return errors
    try:
        texts = {p: p.read_text(encoding='utf-8') for p in root.rglob('*.md')}
        version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    except (OSError, UnicodeError) as exc:
        return [f'读取失败：{exc}']
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', version):
        errors.append('VERSION 必须为三段非负整数且无前导零')
    skill = texts[root / 'SKILL.md']
    parts = skill.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append('缺 YAML frontmatter 边界')
        front = ''
    else:
        front = parts[1]
    if not re.search(r'^name: game-design-review$', front, re.M):
        errors.append('skill 名称改变或缺失')
    if not re.search(r'^metadata:\n  version: "' + re.escape(version) + r'"\n', front, re.M):
        errors.append('metadata.version 与 VERSION 不一致')
    if '  report-schema: "1"' not in front:
        errors.append('report-schema 与当前校验器契约不一致；升级时须同步校验器')
    match = re.search(r'^description: (.+)$', front, re.M)
    description = match.group(1) if match else ''
    if not 1 <= len(description) <= 1024 or any(t not in description for t in TRIGGERS):
        errors.append('description 超界或缩窄旧触发场景')
    if len(skill.splitlines()) > 420:
        errors.append('SKILL.md 超过 420 行')
    for n in range(6):
        if len(re.findall(r'^### Phase ' + str(n) + r' · ', skill, re.M)) != 1:
            errors.append(f'Phase {n} 缺失或重复')
    for n in '一二三四':
        if len(re.findall(r'^### 尺子' + n + ':?', skill, re.M)) != 1:
            errors.append(f'尺子{n}缺失或重复')
    phase5 = skill.split('### Phase 5 · 报告', 1)[-1].split('## 五、', 1)[0]
    numbers = re.findall(r'^(\d+)\. \*\*', phase5, re.M)
    if numbers != [str(i) for i in range(1, 11)]:
        errors.append('总报告不再是固定十节')
    for name in ('references/orchestration.md', 'references/adjudication.md'):
        if f']({name})' not in skill:
            errors.append(f'主入口未直接连接：{name}')
    if f'**{version}**' not in texts[root / 'README.md']:
        errors.append('README 当前版本不一致')
    if f'## [{version}]' not in texts[root / 'CHANGELOG.md']:
        errors.append('CHANGELOG 缺当前版本')
    for path, text in texts.items():
        # 只校验普通 Markdown 内联相对文件链接，不爬外网，不校验标题锚点。
        outside_code = re.sub(r'```.*?```', '', text, flags=re.S)
        for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', outside_code):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root):
                errors.append(f'{path.relative_to(root)}：链接越出整包：{link}')
            elif not target.exists():
                errors.append(f'{path.relative_to(root)}：相对链接缺失：{link}')
    return errors


def self_test(root: Path) -> int:
    """在临时副本破坏五种契约，验证不会错误放行。"""
    mutations = {
        '版本失配': lambda p: (p / 'VERSION').write_text('9.9.9\n'),
        '核心附件缺失': lambda p: (p / 'references/adjudication.md').unlink(),
        '悬空链接': lambda p: (p / 'README.md').write_text(
            (p / 'README.md').read_text() + '\n[错误](absent-file.md)\n'),
        '主入口过长': lambda p: (p / 'SKILL.md').write_text(
            (p / 'SKILL.md').read_text() + '\n' * 421),
        '十节结构损坏': lambda p: (p / 'SKILL.md').write_text(
            (p / 'SKILL.md').read_text().replace('10. **顺手记录的 bug**', '11. **顺手记录的 bug**')),
    }
    for label, mutate in mutations.items():
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / root.name
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            mutate(copy)
            if not check(copy.resolve()):
                print(f'失败：负向样例被放行：{label}')
                return 1
            print(f'负向自测通过：{label}')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    errors = check(root)
    if errors:
        print('\n'.join(f'失败：{e}' for e in errors))
        return 1
    print('静态契约检查通过（不代表游戏或多代理端到端通过）')
    return self_test(root) if args.self_test else 0


if __name__ == '__main__':
    raise SystemExit(main())
