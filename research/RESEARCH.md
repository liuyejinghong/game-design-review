# 调研记录（2026-09-20）

本文件记录 skill v0.1–v0.2 背后的调研过程：查了什么、核实了什么、采纳了什么、放弃了什么。供后续迭代（以及外部模型定向优化）理解设计意图。

## 1. 问题起源

用户发现：让 AI 反复测试游戏，它始终测不出"整个游戏是整页切换式导航，不像个游戏"这类问题。原因不是模型不行，而是**验收缺基准**——bug 测试的隐含标准是"能跑、无报错"，而"打开背包应该是弹窗"是范式错误，只能用显式的范式基准去抓。结论：先立尺子（范式清单 + 可玩性启发式 + 核心循环），再固化成规范流程与 skill。

## 2. 现成 skill / 工具生态扫描

**skills.sh 注册表**（`npx skills find`，关键词：playtest / game qa / game acceptance / gamedev / game testing）：

- 游戏验收类：最高的是 `donchitos/claude-code-game-studios@playtest-report`（450 装机）。实读其内容后弃用：绑死该仓库私有的 `production/` 目录结构与 director-gates 体系，非通用。其余（playtest-review、game-qa、game-demo-feedback-triage 等）装机量 1–300，来源不明，按"低于 100 装机要警惕"标准视为噪音。
- 游戏开发类：`gamedev-skills/awesome-gamedev-agent-skills` 合集最成体系（单 skill 3–4.4K 装机），但条目全是 Unity / Unreal / Godot / Three.js 引擎向；`higgsfield-game-generation`（26.7K）是平台自己的 AI 资产生成，无关。
- 结论：**无成熟通用的"游戏策划验收" skill → 自建。**

**GitHub**（gh search，关键词：playtest / game design review / games user research / game ux）：

- playtest 相关仓库均为工具性质（遥测、录制、引擎内 MCP：robloxstudio-mcp 242★、godot-mcp 166★、Viewback 48★ 等），无方法论级仓库。
- "game design review" 直接命中的仓库全部 0–1★。
- 收进资源库：`Roobyx/awesome-game-design`（650★，经典 GDD 存档 + postmortem 大全）。

## 3. 直接借鉴的开源工作

`Shupianmaka/codex-game-ux-skills`（游戏交互易用性评估，中文，实读其 SKILL.md 与 evaluation-framework.md）。借鉴四点：

1. **观察先于判断**：先客观描述"看到了什么"，再写"可能导致什么体验影响"。
2. **置信度标签**（确认/疑似/待确认）：静态素材证明不了动效、音效是否存在，不能从截图断言"没有反馈"。
3. **玩家阶段差异**（新手/中度/硬核）：三者关注点不同，分析"设计偏向服务谁、哪类玩家损耗最大"。
4. **亮点保留**：只报问题的报告会让后续改动误伤好设计。

其十大评估维度、P0–P3 分级、实现难度标注亦作为对照参考（本 skill 采用 P0/P1/P2 三级 + 低/中/高实现难度）。

## 4. 方法论来源（一手核实）

| 框架 | 出处 | 落点 |
|---|---|---|
| PLAY 可玩性启发式 | Desurvire & Wiberg, 2009 | 尺子二（取对网页/原型期适用的子集） |
| MDA 框架 | Hunicke, LeBlanc & Zubek, 2004 | 尺子四骨架（机制→动态→体验）+ 八类 Aesthetics 体验清单 |
| A Theory of Fun | Raph Koster, 2004（好玩=学会新模式的快感） | 尺子三"好玩三问" |
| GameFlow | Sweetser & Wyeth, 2005（经 OpenAlex/Crossref 核实存在） | 尺子三心流检查 |
| 游戏 UI 四类型（diegetic/non-diegetic/spatial/meta） | 游戏 UI 通用框架 | 尺子一 |
| Games User Research 方法 | gamesuserresearch.com（GUR 行业社区） | 铁律"行为优先于观点"（玩家说的≠玩家做的）、无偏提问 → Phase 1 预期日志 |

## 5. 参照游戏（对照基准，详见 benchmarks.md）

- **Evennia web client**（最流行的开源 MUD 框架，官方文档核实）：单页结构——主文字流+输入行常驻，信息面板是可停靠窗口/标签，设置用弹窗，全程无页面跳转。MUD 形态的交互范式锚点。
- **A Dark Room**（开源 HTML5，多来源核实）：纯文字但有节奏、渐进揭示、流动感——证明"文字"不等于"静态"。
- Kittens Game（无图形的数值深度）、Universal Paperclips（阶段跃迁）、Candy Box（发现感）、Progress Quest（零决策反例）。
- 像素期体裁参照：RimWorld / Factorio / Oxygen Not Included / Dwarf Fortress / Stardew Valley / Fallout Shelter。

## 6. 放弃的路径

- 采用现成 playtest/QA skill：无可用的（见第 2 节）。
- 给 skill 挂 Jev/小模型做自动分诊：评审判断本身是主模型职责，额外分诊层是过度设计。
- 全文照抄 PLAY 43 条：条目过半对网页原型期不适用，整体载入会稀释执行质量；取子集并标注来源。

## 7. 已知空白 / 下一步

1. PLAY 完整条目只取了子集；GameFlow 八元素未逐条化。
2. 增量/放置/经营玩法专属检查（时间墙、数字外显、加速器经济、离线收益体验）尚薄。
3. 文字游戏专属启发式（文字流节奏、信息密度、空间感的文字营造、交互词一致性）尚薄。
4. 红队模式的对抗深度可再加强（多评审员视角、persona 分轮试玩）。
5. LLM 评审员的防漂移机制（越评越温和、忘记证据要求）可再加自查钩子。

→ 以上为外部模型定向优化的输入方向。
