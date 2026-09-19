# game-design-review

游戏策划视角的试玩评审 skill（ZCode / Claude Code 兼容格式）。

**解决什么问题**：AI 测游戏时天然退化成"找 bug"——能跑、无报错就算通过，永远测不出"打开背包是整页跳转而不是弹窗"这类范式错误。那不是 bug，是设计错误；设计错误要用设计基准去抓。本 skill 把"先立尺子 → 黑盒试玩 → 对照评审 → 分级报告"固化成可反复执行的流程，专评：**设计对不对、好不好玩、机制是否成立**。

## 组成

- [`SKILL.md`](SKILL.md) — 主文件：
  - **四把尺子**：游戏交互范式（像不像个游戏）/ 可玩性启发式（PLAY 子集）/ 核心循环与节奏（含"好玩三问"、心流检查、失败压力）/ 机制还原与数值体检（MDA 骨架）
  - **阶段校准**：文字原型期 → 像素表现期。设计级问题标"保留"优先修；表现级临时方案标"重做"记入临时决策台账；"现在只是文字版"不能当借口
  - **三种模式**：迭代评审（1 轮）/ 里程碑评审（3 轮）/ 红队模式（指控→取证→裁决，专治评审太客气）
  - **评审技术**：预期日志、置信度标签、玩家阶段透镜、行为优先于观点、亮点保留
- [`references/benchmarks.md`](references/benchmarks.md) — 参照游戏库（文字期/MUD/像素期）+ 方法论来源表 + 社区资源
- [`research/RESEARCH.md`](research/RESEARCH.md) — 调研记录：现有生态扫描、借鉴来源、方法论核实、已知空白

## 安装

复制到 skill 目录即可（ZCode：`~/.zcode/skills/game-design-review/`；Claude Code：`~/.claude/skills/game-design-review/`）。

## 触发

对 agent 说"游戏验收 / 试玩评审 / 好不好玩 / 像不像个游戏 / 策划视角评估"，或直接点名 `/game-design-review`。明确不适用于纯 bug 测试与代码审查。

## 方法论依据

PLAY（Desurvire & Wiberg 2009）· MDA（Hunicke/LeBlanc/Zubek 2004）· A Theory of Fun（Koster）· GameFlow（Sweetser & Wyeth 2005）· Games User Research 行业方法 · 游戏 UI 四类型框架。详见 benchmarks.md 附一。

## 状态

v0.2（2026-09-20）。已知空白与下一步见 RESEARCH.md 第 7 节。
