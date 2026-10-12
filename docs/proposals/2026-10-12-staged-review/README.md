# RFC：面向 AI / Agent 开发游戏的分阶段审查

日期：2026-10-12。状态：**提案，待维护者与独立 Agent review；不是已经生效的 skill 规则。**

审阅基线：`game-design-review 0.6.0`，commit `ce2ec9bfa5b2cc753181656a813d2f701c753f51`，`report_schema=2`，`critic_scale=1`。

本 PR 只增加设计与评审交接文档，不改 `SKILL.md`、现行附件、校验器、VERSION、CHANGELOG，不发布新版本，不改历史报告，也不代表已经完成跨游戏实测。合并提案不等于批准全部实施方案。

## 1. 要解决什么

目标使用者是个人创作者，以及不熟悉游戏设计、开发流程或代码、主要依靠 AI / Agent 制作游戏的人。目标对象是新游戏、机制样机、应用式交互原型、MVP 和开发中版本；不是以成熟商业游戏评论为主要服务。这里的 AI 驱动指开发方式，不要求游戏运行时使用 AI。

问题不只是“好不好玩”，而是：开发 Agent 交付的东西，是否漏了当前玩家任务必需的能力？设计是否自洽？按钮是否真正接入规则？陌生玩家能否独立进入？达到什么条件后，才值得继续做深度试玩、同类成熟度分析和评论员反馈？下一轮开发应做什么，如何复验？

这些是用户明确提出的使用情境与风险，不是对所有 AI 开发项目缺陷发生率的统计结论。OPC / 个人创作者用于描述目标使用者，不作为游戏品质或判级依据。

## 2. 本次讨论的最终对齐

| 讨论中的方向 | 本提案如何处理 |
|---|---|
| skill 应适配广泛游戏类型 | 保留；通用的是早期开发审查方法，不能把经营玩法当所有游戏的模板 |
| 优先找必要设计与功能遗漏 | 提升为首次评审前置主线，不等作者先提出需求 |
| 检查设计是否合理 | 在设计材料阶段识别矛盾与风险，能操作时再以行为取证；不把设计推演冒充实玩 |
| 模拟玩家、模拟测评员、成熟游戏参照 | 全部保留，但按准备程度和问题安排；不是在前置检查之后被取消 |
| 证据、公平替代、反例、亮点保护 | 保留；严格审查不等于强迫功能齐全或制造问题 |
| 给其他 Agent 执行 | 增加最小任务卡、依赖、复验条件与实施路线，独立 review 后再改正式协议 |

核心顺序：**定靶 → 必要能力与设计合理性审查 → 最小可玩核验 → 深度试玩与成熟度评审 → 开发交接与独立复验。**

这不是“先补完所有功能才能玩”的瀑布流程。前置阶段允许有目的的短探测；门槛只限制依赖缺口的活动；任何阶段都可输出局部结论、补测或开发任务。没有存档可能阻止跨日成长验证，但不自动阻止镜头测试。

## 3. 阅读顺序与产物

| 文档 | 用途 |
|---|---|
| [01-workflow.md](01-workflow.md) | 阶段、输入输出、推进门槛、证据边界、与 Phase / R 轮次的映射 |
| [02-capability-contracts.md](02-capability-contracts.md) | 条件化能力清单、设计合理性、跨品类适配、公平对照与成熟度字段 |
| [03-implementation-plan.md](03-implementation-plan.md) | Agent 分工、任务卡示例、文件级实施路线、兼容迁移与不做事项 |
| [04-evaluation-plan.md](04-evaluation-plan.md) | 30 个待执行验收场景、行为评测、度量与发布证据要求 |
| [05-agent-review-prompt.md](05-agent-review-prompt.md) | 可直接交给下一位 Agent 的独立 review prompt |

建议先评审流程与边界，再评审字段和实现。不要从“再加几个游戏类型附件”开始，以免在未理顺的流程上继续堆规则。

## 4. 对 0.6.0 的判断与变更理由

0.6.0 已有能力对照、同类必要但未宣称能力的检查、差距与损害分流、隔离首访、原始证据、唯一台账和条件专项。不是从零重做，也不应把这些能力描述成当前全部缺失。[B1]、[B2]、[B3]

主要建议是重排优先级并把隐含条件显式化：首次评审先识别必要能力与阶段风险；区分“设计材料审查”和“实际体验裁决”；把可继续哪些验证写清；让报告能直接形成适合个人项目的下一步任务。跨品类判据、实时执行、矩阵维度与渐进加载属于配套改进，而非取消早期项目的具体检查清单。

成熟作品有两个角色：早期提供解决玩家任务的候选做法；后期支持更深入的能力与体验对照。它们不是本项目必须复制的规格，也不是本 skill 的主要受审对象。[B2]、[B5]

## 5. 依据与事实边界

以下是固定基线的仓库来源；未重新做外部行业调研。实施提议、合成案例和验收门槛均是设计建议，不是论文结论或实测结果。原讨论中的媒体链接、数值建议或“行业常见”表述不作为未经核验的事实自动带入。

[B1]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/SKILL.md
[B2]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/references/capability-review.md
[B3]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/references/orchestration.md
[B4]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/references/adjudication.md
[B5]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/references/management-baseline.md
[B6]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/tests/acceptance.md
[B7]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/scripts/validate.py
[B8]: https://github.com/liuyejinghong/game-design-review/blob/ce2ec9bfa5b2cc753181656a813d2f701c753f51/VERSIONING.md

- 主线与判据：[B1]；能力矩阵与替代验证：[B2]；编排、隔离与范围：[B3]；唯一台账与严重度：[B4]。
- 条件基准：[B5]；现有合成场景：[B6]；静态验证器：[B7]；版本与历史报告边界：[B8]。
- 对“是否已有效泛化”的回答仍需执行证据。已有合成场景和静态检查不能代替真实宿主试玩或真人反馈。

## 6. 独立 review 最需要作出的决定

流程是否同时避免“只查缺项、不评玩法”和“直接长测、漏掉基础设计”？阶段门槛能否限制范围而不滥用全局阻断？设计材料结论与实玩结论是否分开？具体检查清单是否足够可执行且不过度设计？新增字段是否可以依附原台账而非制造第二套事实？实施顺序是否适合渐进迁移？

接受、修改、延期、拒绝须逐项说明。不要把本提案的存在当成路线已批准，也不要仅凭篇幅完整或静态检查通过就宣布新 skill 已验证。
