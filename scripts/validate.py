#!/usr/bin/env python3
"""本仓库静态契约检查；仅用标准库，不执行游戏，不写仓库。"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

REQUIRED = (
    'SKILL.md', 'VERSION', 'VERSIONING.md', 'CHANGELOG.md', 'README.md',
    'references/orchestration.md', 'references/adjudication.md',
    'references/presentation-transition.md', 'research/presentation-engine-notes.md',
    'references/first-visit.md', 'references/critic-scoring.md',
    'references/human-playtest.md', 'references/experience-regression.md',
    'references/benchmarks.md', 'agents/blind-player.md', 'tests/acceptance.md',
    'references/3d-gameplay.md', 'references/management-simulation.md',
    'references/capability-review.md', 'references/management-baseline.md',
    'research/management-capability-study.md', 'research/genre-baseline-transfer.md',
    'references/development-readiness.md', 'references/developer-handoff.md',
    'tests/staged-review-cases.md',
    'references/system-architecture-pipeline.md', 'tests/system-architecture-cases.md',
)
TRIGGERS = ('游戏验收', '试玩评审', '好不好玩', '像不像个游戏', '策划视角评估', '游戏感评审',
            '3D 游戏', '模拟经营', '模块功能', '设计材料审查', '最小可玩核验',
            '系统架构', '内容生产管线', 'AI 扩展性')
# 工具工作区与缓存不属于整包内容：扫描 Markdown 与自测副本时整棵跳过。
SKIP_DIRS = frozenset(('.git', '.claude', '__pycache__'))


def markdown_files(root: Path) -> list[Path]:
    def fail(exc: OSError) -> None:
        raise exc

    found: list[Path] = []
    for directory, dirnames, filenames in os.walk(root, onerror=fail):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        found.extend(Path(directory, name) for name in filenames if name.endswith('.md'))
    return found


def check(root: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'缺文件：{name}')
    if errors:
        return errors
    try:
        texts = {p: p.read_text(encoding='utf-8') for p in markdown_files(root)}
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
    if '  report-schema: "3"' not in front:
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
    for name in ('references/orchestration.md', 'references/adjudication.md',
                 'references/presentation-transition.md',
                 'references/capability-review.md', 'references/management-baseline.md',
                 'references/3d-gameplay.md', 'references/management-simulation.md',
                 'references/development-readiness.md', 'references/developer-handoff.md',
                 'references/system-architecture-pipeline.md'):
        if f']({name})' not in skill:
            errors.append(f'主入口未直接连接：{name}')
    orchestration = texts[root / 'references/orchestration.md']
    presentation = texts[root / 'references/presentation-transition.md']
    adjudication = texts[root / 'references/adjudication.md']
    gameplay3d = texts[root / 'references/3d-gameplay.md']
    management = texts[root / 'references/management-simulation.md']
    readiness = texts[root / 'references/development-readiness.md']
    pipeline = texts[root / 'references/system-architecture-pipeline.md']
    for marker in ('| R09 表现适配与转段 |', '→ R05 → 按需 R09 → R06 → R07'):
        if marker not in orchestration:
            errors.append('R09 调用卡缺失或调度顺序改变')
    for label, marker in (('3D 空间与操控请求行', '| 3D 空间与操控 |'),
                          ('模拟经营请求行', '| 模拟经营 |'),
                          ('通用能力对照请求行', '| 同类成熟度 / 模块功能与机制差距 |'),
                          ('3D 附件指针', '](3d-gameplay.md)'),
                          ('经营附件指针', '](management-simulation.md)'),
                          ('能力对照指针', '](capability-review.md)'),
                          ('经营基准指针', '](management-baseline.md)'),
                          ('材料就绪指针', '](development-readiness.md)'),
                          ('交接指针', '](developer-handoff.md)'),
                          ('材料就绪请求行', '| 设计材料审查 / 最小可玩核验 |'),
                          ('系统架构请求行', '| 系统架构 / 内容生产管线 / AI 扩展性 |'),
                          ('系统架构指针', '](system-architecture-pipeline.md)'),
                          ('R09 统一承载路由', 'SA01–SA08 由 R09 统一承载')):
        if marker not in orchestration:
            errors.append(f'编排缺{label}')
    for n in range(1, 11):
        if len(re.findall(r'^- \*\*V' + f'{n:02}' + r' ', presentation, re.M)) != 1:
            errors.append(f'R09 V{n:02} 缺失或重复')
    for n in range(1, 11):
        if len(re.findall(r'^- \*\*TD' + f'{n:02}' + r' ', gameplay3d, re.M)) != 1:
            errors.append(f'TD{n:02} 缺失或重复')
    for n in range(1, 13):
        if len(re.findall(r'^- \*\*MG' + f'{n:02}' + r' ', management, re.M)) != 1:
            errors.append(f'MG{n:02} 缺失或重复')
    for n in range(1, 13):
        if len(re.findall(r'^- \*\*CAP-' + f'{n:02}' + r' ', readiness, re.M)) != 1:
            errors.append(f'CAP-{n:02} 缺失或重复')
    for n in range(1, 9):
        if len(re.findall(r'^- \*\*SA' + f'{n:02}' + r' ', pipeline, re.M)) != 1:
            errors.append(f'SA{n:02} 缺失或重复')
    for marker, label in (('本轮已启用的 R01–R05 黑盒证据封存后', '封存门控'),
                          ('纯静态 SA', '纯静态边界')):
        if marker not in pipeline:
            errors.append(f'系统架构附件缺{label}说明')
    if '路线建议不计入 P0/P1/P2' not in adjudication:
        errors.append('路线决策与缺陷的分流约定缺失')
    if 'E-SA-001' not in adjudication:
        errors.append('证据台账缺工程证据类 E-SA-001')
    if '不安装引擎' not in presentation or '没有图形/客户端产物只能交计划' not in orchestration:
        errors.append('R09 只读或未实测边界缺失')
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
    """在临时副本逐项破坏契约（种类数随契约扩展，此处不写死），验证不会错误放行。"""
    def replace_text(base: Path, name: str, old: str, new: str) -> None:
        target = base / name
        text = target.read_text(encoding='utf-8')
        if old not in text:
            raise LookupError(f'替换目标不存在：{name}')
        target.write_text(text.replace(old, new), encoding='utf-8')

    def append_text(base: Path, name: str, suffix: str) -> None:
        target = base / name
        target.write_text(target.read_text(encoding='utf-8') + suffix, encoding='utf-8')

    mutations = {
        '新视角附件缺失': lambda p: (p / 'references/presentation-transition.md').unlink(),
        '新视角入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/presentation-transition.md)', '](references/benchmarks.md)'),
        '轮次顺序损坏': lambda p: replace_text(p, 'references/orchestration.md',
            '→ R05 → 按需 R09 → R06 → R07', '→ R05 → R06 → R07 → R09'),
        '路线分流缺失': lambda p: replace_text(p, 'references/adjudication.md',
            '路线建议不计入 P0/P1/P2', '路线建议'),
        '版本失配': lambda p: (p / 'VERSION').write_text('9.9.9\n', encoding='utf-8'),
        '核心附件缺失': lambda p: (p / 'references/adjudication.md').unlink(),
        '悬空链接': lambda p: append_text(p, 'README.md', '\n[错误](absent-file.md)\n'),
        '主入口过长': lambda p: append_text(p, 'SKILL.md', '\n' * 421),
        '十节结构损坏': lambda p: replace_text(p, 'SKILL.md',
            '10. **顺手记录的 bug**', '11. **顺手记录的 bug**'),
        '3D 专项附件缺失': lambda p: (p / 'references/3d-gameplay.md').unlink(),
        '经营专项附件缺失': lambda p: (p / 'references/management-simulation.md').unlink(),
        '3D 专项入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/3d-gameplay.md)', '](references/benchmarks.md)'),
        '经营专项入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/management-simulation.md)', '](references/benchmarks.md)'),
        '通用协议附件缺失': lambda p: (p / 'references/capability-review.md').unlink(),
        '通用入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/capability-review.md)', '](references/benchmarks.md)'),
        '报告schema失配': lambda p: replace_text(p, 'SKILL.md',
            '  report-schema: "3"', '  report-schema: "2"'),
        'TD 条目重复': lambda p: append_text(p, 'references/3d-gameplay.md',
            '\n- **TD01 重复条目\n'),
        'MG 条目缺失': lambda p: replace_text(p, 'references/management-simulation.md',
            '- **MG05 ', '- **MGX05 '),
        '开发就绪附件缺失': lambda p: (p / 'references/development-readiness.md').unlink(),
        '开发交接附件缺失': lambda p: (p / 'references/developer-handoff.md').unlink(),
        '开发就绪入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/development-readiness.md)', '](references/benchmarks.md)'),
        '开发交接入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/developer-handoff.md)', '](references/benchmarks.md)'),
        'CAP07 条目缺失': lambda p: replace_text(p, 'references/development-readiness.md',
            '- **CAP-07 ', '- **CAP-X07 '),
        'SA 附件缺失': lambda p: (p / 'references/system-architecture-pipeline.md').unlink(),
        'SA 主入口断开': lambda p: replace_text(p, 'SKILL.md',
            '](references/system-architecture-pipeline.md)', '](references/benchmarks.md)'),
        'SA 请求行损坏': lambda p: replace_text(p, 'references/orchestration.md',
            '| 系统架构 / 内容生产管线 / AI 扩展性 |', '| 系统架构 |'),
        'SA 编排指针断开': lambda p: replace_text(p, 'references/orchestration.md',
            '](system-architecture-pipeline.md)', '](benchmarks.md)'),
        'R09 统一承载 marker 缺失': lambda p: replace_text(p, 'references/orchestration.md',
            'SA01–SA08 由 R09 统一承载', 'SA01–SA08 由 R09 承载'),
        'SA 条目重复': lambda p: append_text(p, 'references/system-architecture-pipeline.md',
            '\n- **SA01 重复条目\n'),
        'SA 条目缺失': lambda p: replace_text(p, 'references/system-architecture-pipeline.md',
            '- **SA05 ', '- **SAX05 '),
        'SA 封存门控 marker 缺失': lambda p: replace_text(p, 'references/system-architecture-pipeline.md',
            '本轮已启用的 R01–R05 黑盒证据封存后', '黑盒证据封存后'),
        'SA 纯静态 marker 缺失': lambda p: replace_text(p, 'references/system-architecture-pipeline.md',
            '纯静态 SA', '纯静态分析'),
        '工程证据类缺失': lambda p: replace_text(p, 'references/adjudication.md',
            'E-SA-001', 'E-SX-001'),
        'SA 输入附件缺失': lambda p: (p / 'tests/system-architecture-cases.md').unlink(),
    }
    for label, mutate in mutations.items():
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / root.name
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(*SKIP_DIRS))
            try:
                mutate(copy)
            except (LookupError, OSError) as exc:
                print(f'失败：负向样例无法施加：{label}（{exc}）')
                return 1
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
