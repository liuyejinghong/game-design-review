# 参照游戏库（对照评审用）

用法：Phase 0 从这里挑 2–3 个与当前系统最相关的参照物；评审时做**同约束对比**——同样的约束下（文字形态、网页、单人、放置与否）它做到了什么，我们差在哪。对比要具体到条目（"A Dark Room 的每段文字都有推进感，我们的事件是静态列表"），不写"感觉不如 XX"。

## 一、文字/极简网页游戏（文字原型期直接对照）

| 游戏 | 学什么 | 对照问题 |
|---|---|---|
| **A Dark Room** | 节奏与渐进揭示、氛围、事件流 | 新内容是渐进出现还是一次性摊开？文字流有"正在发生什么"的推进感吗？ |
| **Kittens Game** | 无图形也能有数值深度：资源链、转换、瓶颈 | 资源之间有转换与制约关系吗，还是一堆互不相干的计数器？ |
| **Universal Paperclips** | 阶段跃迁与惊喜，行为曲线设计 | 中后期有形态/玩法的阶段转变吗，还是从头到尾一个节奏？ |
| **Candy Box** | 秘密与发现感 | 有值得探索的隐藏内容吗？玩家会出于好奇做实验吗？ |
| **Progress Quest**（反例） | 全自动、零决策的极端 | 如果把玩家所有操作删掉游戏照样跑，那玩家在玩什么？ |

## 二、传统 MUD（文字形态的成熟工艺）

| 参照 | 学什么 | 对照问题 |
|---|---|---|
| **Evennia 系 MUD / Discworld MUD** | 世界持续性、命令感、空间感 | 世界感觉在持续运转吗（离线也在发生事）？行动有分量和即时反馈吗？ |
| 经典 MUD 客户端范式 | 单页主文字流 + 常驻输入行 + 可停靠面板 | 交互是否保持了"游戏还在"的连续性？还是动辄整页切换？ |

## 三、基地/经营/生存（像素表现期的主要体裁，也用于校验文字期的骨架）

| 游戏 | 学什么 | 对照问题 |
|---|---|---|
| **RimWorld** | 事件叙事、节奏调控（讲故事而非倒计时） | 事件是编好的脚本，还是会互相作用生成故事？ |
| **Factorio** | 自动化循环、吞吐优化 | 有可优化的生产链吗？优化有可见回报吗？ |
| **Oxygen Not Included** | 系统性互相施压（资源、温度、人） | 各系统会互相制造麻烦吗，还是各自独立打卡？ |
| **Dwarf Fortress** | 涌现叙事：失败也能产出故事 | 失败会产出"故事"还是只是惩罚？ |
| **Stardew Valley** | 日循环节奏、能量经济 | 一天/一局有明确的节奏曲线吗？ |
| **Fallout Shelter** | 移动端基地调度、计时互动 | 调度决策有趣吗（谁去做什么）？等待是否可感知？ |

## 四、像素转型参照（Phase 0 判为转段评审时用）

| 参照 | 学什么 | 对照问题 |
|---|---|---|
| Stardew / RimWorld 的界面骨架 | 信息架构直接映射到屏幕分区 | 现在的面板结构（背包/状态/地图/任务）能直接映射成屏幕布局吗，还是需要重新设计？ |
| 文字→图形转型案例（A Dark Room 的 iOS 版） | 哪些文字承载的体验被图形强化，哪些被丢失 | 我们的核心体验里，有多少依赖"读文字"本身？转图形后会丢什么？ |

## 附一：方法论来源（评审框架的出处）

| 框架 | 来源 | 在 skill 中的用途 |
|---|---|---|
| PLAY 可玩性启发式 | Desurvire & Wiberg, 2009 | 尺子二 |
| MDA 框架（Mechanics→Dynamics→Aesthetics） | Hunicke, LeBlanc & Zubek, 2004 | 尺子四骨架 + 八类体验清单 |
| A Theory of Fun（好玩=学会新模式） | Raph Koster, 2004 | 尺子三"好玩三问" |
| GameFlow（心流条件引入游戏评估） | Sweetser & Wyeth, 2005 | 尺子三心流检查 |
| 游戏 UI 四类型（diegetic/non-diegetic/spatial/meta） | 游戏 UI 通用框架 | 尺子一 |
| Games User Research 方法（观察行为而非听取意见；无偏提问） | gamesuserresearch.com / GUR 社区 | 铁律 6/7、Phase 1 预期日志 |
| 游戏交互易用性评估（观察先于判断、置信度标签、玩家阶段、亮点保留） | Shupianmaka/codex-game-ux-skills（开源 skill） | 铁律 6/8/9、Phase 1 玩家阶段透镜、报告结构 |

## 附二：社区与持续学习资源（需要深挖某一项时查）

**试玩/用户研究方法**
- [Games User Research](https://www.gamesuserresearch.com/) — GUR 行业方法论：如何组织试玩、无偏提问、观察记录
- GDC 历年 playtesting / user research 演讲（YouTube @Gdconf）

**设计理论**
- [Raph Koster's Blog](https://www.raphkoster.com/) — 好玩理论延续讨论
- [Game Maker's Toolkit](https://www.youtube.com/@GMTK) — 设计原则视频分析
- [The Level Design Book](https://book.leveldesignbook.com/) — 关卡设计理论
- [GDKeys](https://gdkeys.com/) — 经济系统、技能树、成长曲线实战分析
- [Game UI Database](https://www.gameuidatabase.com/) — 可搜索的游戏界面参照库（做界面范式对照时极有用）
- [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/) — 无障碍清单

**复盘与文档**
- [awesome-game-design](https://github.com/Roobyx/awesome-game-design) — 经典 GDD 存档 + postmortem 大全（含大量失败复盘，做"教训对照"时查）
- gamedocs.org / VGHF Digital Archive — 真实商业游戏设计文档存档

