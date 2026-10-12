# 参照游戏库（对照评审用）

用法：基准由 primary 来源驱动——Phase 0 按目标玩家任务选 2–4 个成熟样本，条目按 [能力对照协议](capability-review.md) 的模块格式写：玩家任务、典型实现、版本/平台/核查日期、source 类型、确切声明、已核验或待核查。下列游戏表是**选材线索，不是已查机制**：未核验前不得把表中行为写成事实。评审时做**同约束对比**——同样的约束下它做到了什么、我们差在哪；对比要具体到模块与条目，不写“感觉不如 XX”。少样本只写“在已查样本中出现”，不宣称行业普遍性。
使用每个参照前补记：**平台/版本与核查日期｜匹配约束｜对应模块与条款｜触发路径｜来源/证据｜已核验或待核查**。未核验的机制、动画或离线行为不能写成事实；官方声明只证明“提供了”，不证明深度或手感。
类型不限表现形态：文字、2D、3D、灰盒按玩家任务匹配选样，不以像素或界面路由限定类型。模拟经营（样本类型，FPS 等可换）另读 [经营基准](management-baseline.md)（候选 source 池，不是硬清单）与两份研究记录：[经营能力研究](../research/management-capability-study.md)、[类型基准迁移](../research/genre-baseline-transfer.md)——FPS 部分只是通用方法的有限迁移验证，不是完整 FPS 标准。

表现/转段请求另见 [R09](presentation-transition.md) 及 [表现与工具研究](../research/presentation-engine-notes.md)：借鉴信息关系与操作流程，不把画风或引擎当质量分。

## 一、文字/极简网页游戏（文字原型期直接对照）

| 游戏 | 学什么 | 对照问题 |
|---|---|---|
| **A Dark Room** | 节奏与渐进揭示、氛围、事件流 | 新内容是渐进出现还是一次性摊开？文字流有“正在发生什么”的推进感吗？ |
| **Kittens Game** | 无图形也能有数值深度：资源链、转换、瓶颈 | 资源之间有转换与制约关系吗，还是一堆互不相干的计数器？ |
| **Universal Paperclips** | 阶段跃迁与惊喜，行为曲线设计 | 中后期有形态/玩法的阶段转变吗，还是从头到尾一个节奏？ |
| **Candy Box** | 秘密与发现感 | 有值得探索的内容吗？玩家会出于好奇做实验吗？不强制所有“发现”都必须隐藏。 |
| **Progress Quest**（边界参照） | 自动化与消遣体验的边界 | 减少主动操作之后，项目承诺的体验还剩什么？不把“零决策”单独当作所有体裁不好玩的证明。 |

## 二、传统 MUD（文字形态的成熟工艺）

| 参照 | 学什么 | 对照问题 |
|---|---|---|
| **Evennia 系 MUD / Discworld MUD** | 世界持续性、命令感、空间感 | 改变世界后回来能看出后果吗？行动有分量和可理解反馈吗？具体离线行为须按游戏核验。 |
| 经典 MUD 客户端范式 | 主文字流、输入行、可停靠面板的连续性 | 管理操作之后能否接续原地点、输入和阅读？不以 URL 或页签变化本身定罪。 |

## 三、基地/经营/生存（跨表现形态，文字/2D/3D 都可对照）

| 游戏 | 学什么 | 对照问题 |
|---|---|---|
| **RimWorld** | 事件叙事、节奏调控（讲故事而非倒计时） | 事件是编好的脚本，还是会互相作用生成故事？ |
| **Factorio** | 自动化循环、吞吐优化 | 有可优化的生产链吗？优化有可见回报吗？ |
| **Oxygen Not Included** | 系统性互相施压（资源、温度、人） | 各系统会互相制造麻烦吗，还是各自独立打卡？ |
| **Dwarf Fortress** | 涌现叙事：失败也能产出故事 | 失败会产出“故事”还是只是惩罚？ |
| **Stardew Valley** | 日循环节奏、能量经济 | 一天/一局有明确的节奏曲线吗？ |
| **Fallout Shelter** | 移动端基地调度、计时互动 | 调度决策有趣吗（谁去做什么）？等待是否可感知？ |

经营/放置按主 SKILL 的 I1–I9 对照：记录时间墙、升级前后净速率、瓶颈迁移、自动化后剩余决策、离线结算和重置。参照本身不适配时只能标“不可对照”，不能因此替目标判不适用；目标的适用性由玩家任务判，不编造参照做法。

## 四、表现转型参照（Phase 0 判为转段/表现评审时用）

| 参照 | 学什么 | 对照问题 |
|---|---|---|
| Stardew / RimWorld 的界面骨架 | 信息架构与屏幕分区 | 现在的面板结构能映射成屏幕布局吗？改变表现后，旧行动和信息是否仍可找到？ |
| A Dark Room 跨平台适配（待核验） | 比较不同版本保留和改变的表达 | 未核验具体版本前，不把 iOS 版当“文字转像素”的事实案例；先记录真正发生的表现变化。 |

## 附一：方法论来源（评审框架的出处）

| 框架 | 来源 | 在 skill 中的用途 |
|---|---|---|
| HEP 与 PLAY | HEP（2004）提供四分组历史；PLAY（Desurvire & Wiberg，2009）是后续版本 | 尺子二保留四分组便于使用，但不混称“PLAY 四类 43 条”；具体采纳/合并/条件适用见主 SKILL |
| MDA 框架（Mechanics→Dynamics→Aesthetics） | Hunicke, LeBlanc & Zubek, 2004 | 尺子四骨架 + 八类体验清单 |
| A Theory of Fun | Raph Koster, 2004 | 尺子三“好玩三问”的模式学习视角，不是唯一乐趣定义 |
| GameFlow | Sweetser & Wyeth, 2005 | 尺子三八元素的可观察条件，不冒充真实心流测量 |
| 游戏 UI 四类型（diegetic/non-diegetic/spatial/meta） | 游戏 UI 通用框架 | 描述信息与世界的关系，不直接规定路由技术 |
| Games User Research 方法 | gamesuserresearch.com / GUR 社区 | 行为与陈述分开、预期日志、真实用户研究 |
| 游戏交互易用性评估 | Shupianmaka/codex-game-ux-skills（开源 skill） | 观察先于判断、置信度标签、玩家阶段及亮点保留 |
| IGN 官方量表与评测样本 | [独立调研记录](../research/ign-review-study.md) | 仅为 [非官方媒体评分](critic-scoring.md) 提供方法参照，不是游戏验收官方标准 |

## 附二：社区与持续学习资源（需要深挖某一项时查）

**试玩/用户研究方法**
- [Games User Research](https://www.gamesuserresearch.com/) — 试玩、观察与无偏提问
- [NN/g：任务场景](https://www.nngroup.com/articles/task-scenarios-usability-testing/) — 不把正确操作写进任务
- [Player Research：游戏可用性测试](https://www.playerresearch.com/learn/getting-more-from-usability-testing-your-game/) — 用行为检验学习目标
- GDC 历年 playtesting / user research 演讲（YouTube @Gdconf）

**设计理论**
- [Raph Koster's Blog](https://www.raphkoster.com/) — 好玩理论延续讨论
- [Game Maker's Toolkit](https://www.youtube.com/@GMTK) — 设计原则视频分析
- [The Level Design Book](https://book.leveldesignbook.com/) — 关卡设计理论
- [GDKeys](https://gdkeys.com/) — 经济系统、技能树、成长曲线实战分析
- [Game UI Database](https://www.gameuidatabase.com/) — 游戏界面参照
- [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/) — 无障碍清单

**复盘与文档**
- [awesome-game-design](https://github.com/Roobyx/awesome-game-design) — GDD 与复盘选材
- gamedocs.org / VGHF Digital Archive — 文档存档线索，使用前核验访问与具体内容

## 附三：按任务使用的本仓库协议

[首访盲玩](first-visit.md)｜[真人校准](human-playtest.md)｜[体验回归](experience-regression.md)｜[非官方评分](critic-scoring.md)。
以上是执行协议，不是新增参照游戏；仅在相关任务加载，不能把库中商业游戏的媒体分数当成当前 MUD 的得分。
