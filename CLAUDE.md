# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

本地维护 `game-design-review` 整包 skill 的源码仓库。产品是 Markdown 评审协议（SKILL.md、references/、agents/、tests/）加一个仅依赖 Python 标准库的静态契约校验器（scripts/validate.py），不是可运行的游戏或 Web 应用。当前没有 build/lint 服务，也没有 pytest 单例测试入口；现有自动化验证器只有 scripts/validate.py。README 和验收场景中的游戏入口、分数、URL 是任务模板，不代表本仓库已有实跑结果。

## 常用验证命令

```sh
python3 -I scripts/validate.py               # 仓库根：整包静态契约检查
python3 -I scripts/validate.py --self-test   # 同一检查加负向样例，数量随契约扩展
python3 -I scripts/validate.py --root /path/to/game-design-review  # 校验另一份安装/暂存副本
```

- `--root` 的实用用途：用当前校验器的契约检查另一份已安装或暂存中的整包副本，不必切换工作目录；校验过程只读，不写回目标目录。
- `-I` 为隔离模式：导入路径不含脚本目录与用户 site-packages，避免同名模块劫持，脚本本身只依赖标准库。
- 静态检查覆盖：VERSION 格式及与 metadata.version、README、CHANGELOG 的版本一致性，代码块外的普通 Markdown 内联相对文件链接存在性，SKILL.md frontmatter（name/description 触发词/report-schema 2），420 行上限，Phase 0–5 与四尺/十节结构，编排顺序与 R09 标记，通用能力对照与经营基准的必需文件、主入口直链、编排请求行与 pointer，两个专项附件的入口与编排路由，TD01–TD10/MG01–MG12 逐条查重与缺失。
- 它不爬外网、不校验标题锚点、不判断语义正确性；`--self-test` 在临时副本上做十八种破坏（缺附件、断链、改调度顺序、版本失配、通用入口断开、报告 schema 失配、专项条目重复或缺失等），确认失配不会被放行，不固定数量。
- tests/acceptance.md 是人工/合成的协议验收场景，不是已完成的客户端端到端测试；真实端到端需要宿主入口、授权测试存档和实际 run。

只报告实际跑过的命令输出，不用“应该通过”替代。静态通过不等于端到端通过；验证由独立验收方执行，可在同一会话中显式切换到 verifier 视角，实现者不自我验收。协议或编排改动需对照 tests/acceptance.md 的相关场景走查；只有实际执行宿主试玩才声称真实端到端通过，验证深度按变更范围选择。

## 架构与加载边界

- SKILL.md 是唯一入口和公开契约：四把尺子、Phase 0–5、固定十节总报告；结构被校验器锁定，改动须同步，主入口保持 420 行以内。它必须直接链接 references/orchestration.md、adjudication.md、presentation-transition.md（R09 协议，V01–V10 逐条受检）、capability-review.md、management-baseline.md 以及 3d-gameplay.md、management-simulation.md 两个专项附件，断开会导致校验失败。
- references/ 按相关任务加载，不自动全量注入：capability-review.md 是通用总控必读主线（Phase 0 能力模块画像、R02–R05 模块行、R07 第 5 节矩阵；不新增轮次/尺子/台账）；orchestration.md 管轮次计划、上下文隔离、状态交接与停止规则；adjudication.md 由 R07/主评审维护每个 run 唯一的 findings.md 台账，专项轮只提交候选，Cxx 行仅是矩阵定位；benchmarks.md 为选材线索，management-baseline.md 为经营基准候选 source（条件加载、不是硬清单）；first-visit、human-playtest、experience-regression、critic-scoring 按请求启用；3d-gameplay.md（R02/R03，必要处 R04/R05）与 management-simulation.md（R02/R03/R04）按实际表现、体裁、实际玩家任务/同类支撑能力及当前承诺加载，两者可叠加；research/ 只在查依据时读取（management-capability-study.md、genre-baseline-transfer.md 为两份类型研究）。
- agents/blind-player.md 是宿主读取的最小角色卡，不是本仓库自动注册的多代理服务；盲玩执行者只收角色卡与净化简报，与主评审的基线、正确路线、旧报告严格隔离。
- 流水线：定靶 → R01 → R02 → R03 → R04 → R05 → 按需 R09 → R06 → R07 →（可选 R08）。R09 在 R06/R07 前执行、不重排 R01–R08 编号；其路线决策（R09-Axx）留在轮次报告，不进入 P0/P1/P2。专项不新增轮次，也不能用路线方案替代当前缺陷。
- 各轮只交短报告（rounds/Rxx.md 固定六项），十节报告由 R07 在整次运行末尾出一份；评审保持游戏代码和配置只读，允许正常操作获授权的测试存档，不擅自清档、改时钟；未获归档授权时只在会话交付、不虚构证据文件。
- 证据体系：轮次候选 Rxx-Fxx、最终台账 D/B、亮点 L、回归卡 G、路线决策 R09-Axx、能力对照行 Cxx（仅第 5 节矩阵定位，不是 D，也不单列问题）；专项覆盖沿符合/违规/未测/不适用，候选同时标 TD/MG 与原尺，不改变候选/最终 ID 与报告章节；同一条证据可被多轮引用但不算重复复现，同根问题跨条款只计一次。

## 维护完成标准与版本事实

- 改公开契约或发行内容（调用入口、轮次输入输出、分级语义、报告字段、十节结构、报告与评分 schema）时，按 VERSIONING.md 同步 VERSION、SKILL.md 的 metadata.version、README 当前版本、CHANGELOG，以及相关校验器与协议；升级须整包同步安装，不混装新旧附件。
- 版本语义：修订号只做不改变裁决语义的修复，新增兼容视角走次版本，报告/评分 schema 独立于 skill 版本；已发布内容不原地改写，无 tag 时按合并 commit 定位，不伪造 SHA。
- 纯项目维护文档（含本文件）不改变发行内容，无需版本 bump，也不写临时版本号或提交 SHA；CLAUDE.md 同样在整包 Markdown 链接检查范围内，新增相对链接必须真实存在。
- 新增或改名协议附件时同步 README 能力表与各处链接：静态检查只能发现悬空引用，发现不了描述过期，内容一致性靠改完后按 tests/acceptance.md 复核。
- 报告、回归卡与玩家证据默认留在被评游戏项目（docs/reviews/<game-build>/<run-id>/），本仓库保存协议与校验器。
