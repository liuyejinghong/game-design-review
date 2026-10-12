# 经营/管理类能力基准研究（文档证据）

面向通用经营评审的“来源—经验”映射。所有条目为**文档证据（read, not played）**，核查日 2026-10-12；未实测执行时延、稳定性与玩家满意度。默认基准是**有限几款经营游戏、跨原版/重制/续作的文档样本之工程归纳，不是行业普查或学术标准**；不因某能力非惯例、或某样本走另一路线而判坏。结论回到厂商一手（官方博客/开发者日志/更新说明/官方手册/官方 FAQ）；官方托管社区 wiki 单列并标注。

例外类别先定义，但按“该类下的玩家任务”重设检查口径，不自动免检、也不自动要求同一种实现：
- 在线持久世界：无单人读档语义 → 改查崩溃/断线后的恢复摩擦、回滚策略与玩家成果损失；
- 刻意永久死亡：回档被设计性移除 → 仍查失去成果的补偿与恢复摩擦是否与游戏承诺一致；
- 短单局：存档粒度低 → 仍查中断恢复是否顺畅；
- 无历史“live save”路线（S07）：属替代路线样本 → 需对照目标玩家任务验证；若失去成果、恢复摩擦大，仍是问题。

## 1. 来源台账（S01–S16）

| 编号 | 游戏/版本与平台 | 文章日期 | 作者身份/类型 | 链接（核查日 2026-10-12） | 确切支持什么 |
|---|---|---|---|---|---|
| S01 | Surviving Mars: Relaunched，PC/主机 | 2025-09-02 | Paradox 官方新闻，游戏内人设署名“Lina，lead QA and assistant game designer”；官网正文为 JS 渲染（直接抓取为空），本文读取 Wayback replay 快照全文（同时间戳的 id_ 原样抓取是不含正文的约 37KB 外壳，核查勿用 id_ 变体） | 原文 https://www.paradoxinteractive.com/games/surviving-mars-relaunched/news/logistics-and-resources ｜可读快照 https://web.archive.org/web/20260813012226/https://www.paradoxinteractive.com/games/surviving-mars-relaunched/news/logistics-and-resources | 无人机指挥范围（可在 info panel 调整）、仓库“期望数量”、火车纳入 global resource management/环线/轨道导电、移除流体运输（自称可能有争议）、穿梭机全局调度 |
| S02 | Surviving Mars（原版，2018 发行），PC | 2017-11-15 | Boian Spasov，Haemimont Games 开发者（官方论坛开发日志；论坛现被 bot 防护拦截，正文经 Wayback 读取） | 原文 https://forum.paradoxplaza.com/forum/index.php?threads/dev-diary-2-resources-by-boian-spasov-from-haemimont-games.1054807/ ｜读取快照 https://web.archive.org/web/20181206051408id_/https://forum.paradoxplaza.com/forum/index.php?threads/dev-diary-2-resources-by-boian-spasov-from-haemimont-games.1054807/ | 三条设计目标（资源彼此不同/稀缺/位置性）；运输大部分自动、紧急可手动指定；隧道；电力/燃料短缺会中断运输；可拆解救急 |
| S03 | Anno 1800（PC；博文为发售前），蓝图模式 | 2018-10-05 | Anno Union（Ubisoft/Blue Byte）官方博客，未署名 | https://www.anno-union.com/x-marks-the-spot/ | 蓝图=幽灵轮廓、零成本、施工升级工具可单击或拖拽建成、缺料自动留蓝图、仅限已解锁建筑、可关闭；“建筑空间本身就是资源” |
| S04 | Anno 1800，视觉反馈 | 2018-01-18 | Carsten Eckhardt，Ubisoft Blue Byte Mainz 高级 3D 美术师 | https://www.anno-union.com/devblog-visual-feedback/ | 建筑有“生产中/闲置”动画状态、火灾等事件反馈；“看到”比翻菜单更快理解；3D 选择区保证鼠标可点中建筑 |
| S05 | Anno 1800，UI/UX | 2018-06-07 | Khajag Jabaghchourian，Anno 1800 UI 设计师 | https://www.anno-union.com/devblog-user-interface-2/ | 功能优先；HUD 用暗色、通知弹窗用亮色；以最少点击建产线、避免玩家“翻一堆窗口找连接关系”；wireframe→原型测试流程 |
| S06 | Anno 1800，Game Update 6（PC） | 2019-12-10 | Anno Union/Ubisoft 官方更新说明 | https://www.anno-union.com/updates/game-update-6-december-10-2019/ | 统计功能“作为主界面的一部分实现”（原文：as part of the main game interface），入口=顶部财务/人口按钮、任一生产建筑、Ctrl+Q/W/E/R 快捷键（非“页面常驻显示”）；通知过滤器+错过通知在切换回对应游戏内区域 session 时补发（session=游戏内区域切换，非退出重进后的持久通知）；Shift 拖拽多重复制；小键盘切 session 可重绑定 |
| S07 | Anno 117: Pax Romana（PC/PS5/XSX） | 2025-10-15 | Anno Union 官方博客 | https://www.anno-union.com/devblog-multiplayer-and-co-op/ | co-op live savegame：云端只存最新状态、不保留历史；可单人续玩后再邀人；active pause；多人无加速 |
| S08 | Anno 1800 Console Edition（PS5/Xbox Series X\|S） | 2023-01-17 | Anno Union 官方公告（含官方账号 Ubi-Thorlof 回复） | https://www.anno-union.com/revealing-anno-1800-console-edition/ | 手柄替代键鼠：建造菜单改径向、区域地图放大、自动围街区修路、Annopedia；官方回复“控制与 UI 调整≠简化” |
| S09 | Anno 117（PC/主机） | 2025-06-12 | Anno Union 官方 FAQ | https://www.anno-union.com/union-update-june-faq/ | PS5/XSX 支持鼠标键盘；PC 支持手柄；跨平台 cross-save |
| S10 | Factorio（PC），教程/NPE | 2018-05-04 | V453000、Abregado、Twinsen，Wube 开发者（FFF） | https://www.factorio.com/blog/post/fff-241 | 旧教程 30–45 分钟才到自动化；约束过多教会“怎么解教程”；信息散在三个通道；目标：首关教装配机与电、以实验代替任务清单、科技树给目标 |
| S11 | Factorio，教程测试复盘 | 2018-09-21 | kovarex，Wube 创始人（FFF） | https://www.factorio.com/blog/post/fff-261 | 旧式教程约 22 个弹窗打断；“什么都不免费”，放开探索也会出现卡住挫败；错误提示移到光标附近；建造时高亮相关实体以看懂连接 |
| S12 | Factorio，NPE 退役复盘 | 2020-04-10 | Abregado，Wube 开发者（FFF） | https://www.factorio.com/blog/post/fff-342 | NPE 确实扩大了受众、末期反馈正面，但因与愿景不符被撤换回重制版 First Steps；给信息通道定用途（目标栏必须可独立完成）；内部测试专抓卡死角落用例 |
| S13 | Factorio（2.0/Space Age 期，PC） | 2024-04-26 | Klonan、raiguard，Wube 开发者（FFF） | https://www.factorio.com/blog/post/fff-408 | 蓄电池 charge 图用于判断容量是否够过夜；分星球统计+全局开关；考虑产能加成后的“最终科技产量”口径；按物品品质等级（Space Age 的 normal/uncommon 等）拆分产量统计。异步保存：fork 后台存档（只 mac/Linux、隐藏设置、耗内存、仍有未解问题） |
| S14 | Factorio 官方 wiki（**Wube 托管、社区维护**，非开发者亲述） | 页面无日期；读取版本 2026-10-12 | 社区编辑 | https://wiki.factorio.com/Settings ｜ https://wiki.factorio.com/Controls | 隐藏设置 autosave-slots 默认 3（滚动保留）；non-blocking-saving 仅 mac/Linux；控件表：Shift+左键“建造蓝图/ghost”、Q“清空光标”（取消接线/铁轨规划）、R 旋转**手持物品/实体**（非相机）、滚轮缩放；控件表无相机旋转/俯仰项 |
| S15 | Cities: Skylines 官方用户手册（PC，PDF，随 Steam 商店页发布） | 手册无日期（游戏 2015 年发行，版本未知） | Paradox/Colossal Order 官方手册 | https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/255710/manuals/CitiesSkylines-UserManual_EN.pdf | 鼠标控制表与键位（PDF 第 5–6 页，见 B）；Free Camera 模式隐藏 UI；SAVE GAME 覆盖旧档或命名新档、LOAD GAME 列表（PDF 第 12 页）；Info Views 按图层高亮服务/资源问题与覆盖，供跟踪与预判需求（手册第 10 页，PDF 第 11 页）；Chirper 作为城内反馈来源提示问题 |
| S16 | Cities: Skylines II 开发日记（**文中未注明发布平台**；仅区分键鼠/手柄两种输入） | 2023-10-22 | Colossal Order 官方站点开发日记 | https://colossalorder.fi/news/behind-the-scenes-6-tutorials-advisor/ | 教学可选、前期任务不可跳过、完成后可跳；Camera Controls 教学按键鼠/手柄显示不同内容；快捷键 Options→Input 可改可重置；Advisor 收纳全部教学可随时回看；提示（hint）无需动作 |

未取得正文（只记录尝试，不作结论）：Klei ONI “Quality of Life Mk1/2024 QoL Copy Settings”官方帖（kleiforums.com 为 JS 渲染、旧域返回 bot 校验页）；Coffee Stain Satisfactory Update 7 Blueprint Designer 官方补丁说明（Steam 抓取超时/SSL 失败，搜索摘要不足以外推）。Surviving Mars 无公开官方手册正文，存档层面仅核到 S01/S02 与 Paradox 官方支持文章（存档路径按平台/商店区分）。

## 2. 模块观察

### A. 会话/存档/读档/自动保存/槽位/中断恢复

| 任务 | 文档证据 | 成熟样本行为 | 条件/替代与“不能推出” |
|---|---|---|---|
| 手动留档与回读 | S15 | 暂停菜单内覆盖旧档或命名新档；读档列表 | 这是 2015 城市建造样本的一条路线，不能推出“所有经营游戏必备命名槽” |
| 自动保存不丢进度 | S14（社区 wiki） | 默认滚动保留 3 个 autosave，隐藏设置可调 | 数值来自社区维护 wiki，未在游戏 UI 逐一复核；**单一样本默认值，不代表普遍做法**；出现频率/触发点未核验 |
| 保存不打断体验 | S13 | fork 后台保存（mac/Linux），仍隐藏、耗内存且有未解 bug | 是工程取舍样本，不是标配；Windows 未提供同能力 |
| 在线/共玩持续会话 | S07 | 云端只存最新状态、无历史；可单人续玩再邀人；active pause | 取舍路线，不可据此说“无历史=不好”或“必须有历史”；但需按玩家任务验证：失去成果、恢复摩擦大仍是问题，有回滚需求时以其评缺口 |
| 存档恢复失败处理 | S06 | 更新说明曾修“读档崩溃”类问题 | 只能证明该产品出现过该类缺陷并修复，不能证明现状稳定性 |

### B. 镜头/输入：观察、选择、取消、预览

| 能力（玩家任务） | 文档证据（能力存在） | 成熟样本默认行为 | 键位与条件 |
|---|---|---|---|
| 平移/边滚 | S15 | 鼠标贴边或 W/A/S/D | 默认键位因游戏而异 |
| 旋转/俯仰 | S15 | 按住中键拖动=旋转；同一手势上下=俯仰；键盘另有 Q/E 与 HOME/END（笔记本 FN+方向） | “存在旋转/俯仰能力”与“必须同键绑定”分开判；S16 证明快捷键可改可重置，S06 证明小键盘切 session 可重绑定 |
| 缩放 | S15、S14 | 滚轮（CS 另有 Z/X；Factorio 滚轮，含小地图缩放） | 2D 固定俯视样本（Factorio）控件表无相机旋转/俯仰项、但有实体旋转 R——**按文档边界记录“未见该项”，不推导所有 2D 游戏都无需旋转** |
| 选择/确认 | S15、S14 | 左键选择/建造；Factorio Shift+左键先放 ghost 预览 | 预览（ghost）与直接建造是两种实现 |
| 取消/清空 | S15、S14 | 右键取消当前选择；Factorio Q 清空光标（含取消接线/铁轨规划） | 防误触能力=可取消预览，具体键位非判分项 |
| 点中对象可靠性 | S04 | 显式划 3D 选择区/命中盒 | 支持“点得到”这一能力，不规定实现 |
| 键鼠 vs 手柄 | S08、S09 | 主机版径向菜单、自动修路、Annopedia；官方称调整≠简化；PS5/XSX 也支持键鼠、PC 支持手柄 | 输入设备与平台已解耦；具体主机键位映射未核验 |
| 教学承载输入 | S16 | 相机控制教学卡按键鼠/手柄显示不同文本，完成后变绿 | 可抽“输入自适应教学”能力；键位清单进入 Options 可查改 |

### C. 总览/产销/容量/瓶颈/警报/计划/教学/规模

| 能力（玩家任务） | 文档证据 | 成熟样本行为 | 条件/替代与“不能推出” |
|---|---|---|---|
| 经营总览 | S06 | 统计功能嵌入主界面（入口：顶部财务/人口按钮、任一生产建筑、热键 Ctrl+Q/W/E/R）：生产力/消耗/库存/人口/财务分页 | “库存 vs 净产量 vs 容量”是三种口径；S06 提供分页，S13 提供“容量够不够”的图（蓄电池 charge）与“计入加成后的最终产量”口径——评目标时检查三者是否可辨 |
| 就近警报不漏 | S06、S16 | 通知过滤器防刷屏；错过通知在切换回对应游戏内区域 session 时补发（非退出重进持久通知的证据）；CS2 教学/通知分组进 Advisor | 区域内补发是成熟行为之一；不能推出必须用同类信道 |
| 计划/蓝图与取消 | S03、S14 | Anno 幽灵蓝图零成本、缺料自动留蓝图、施工工具单击/拖拽；Factorio ghost 预览 | “先计划后施工”“缺料不阻塞规划”是能力；实现方式（模式切换/ghost）不必相同 |
| 防误触与重复劳动 | S06、S14 | Shift 拖拽多重复制（含模块）；Q 清空取消；对比：slots 覆盖需谨慎（S15 覆盖旧档为显式选择） | 复制/批量是“规模成长”样本；不能推出必须有撤销栈 |
| 物流与上下游可见 | S01、S02 | 原版：资源位置性、自动运输+紧急手动、隧道、电/燃料短缺会停运；Relaunched：无人机服务范围可在 info panel 调、仓库期望数量、火车环线+轨道导电、穿梭机全局调度、移除流体运输（自称有争议） | 服务范围/覆盖率与“物流自动化程度”是两代不同取舍；移除一项是设计决定，评目标时不把“功能更多”自动当更好 |
| 量产状态不翻窗 | S04 | 生产/闲置动画状态、事件特效；官方理由：“看到”比菜单快 | 视觉反馈是替代“只看数字面板”的实现；不能推出所有状态都必须动画化 |
| 教学可重访与迁移运用 | S10、S11、S12、S16 | Factorio：少用打断弹窗、以实验教概念、科技树给目标、通道定用途、内部测试抓卡死；CS2：Advisor 收纳全部教学可随时重看（“可关闭/可跳过”是可选做法而非必备能力） | 能力口径=学习者可随时重访教程、并能在非教学语境独立运用；两样本路线相反（喂给 vs 实验），S11 明确“什么都不免费”，S12 证明面向大众的教学也可能被撤换——不因风格差异单方面判坏 |
| 统计/规模工具随规模成长 | S13、S06 | 分星球统计+全局开关、按物品品质等级（normal/uncommon 等）拆分；Anno 统计下钻到货品/建筑 | 规模工具是“成长后仍可管”的样本；不设统一数值阈值 |

## 3. 可提炼的通用审查步骤建议（默认基准=有限参照的待验起点）

1. 先写玩家任务，再查能力：每项记三层——“能力是否存在 / 实现到什么水平（用样本作参照系）/ 默认入口与键位”。键位相同性单列，不并入能力判定。
2. 证据分级标注：`同类中常见（待验，不证明普遍）`（≥2 个不同子类样本，如统计页 S06+S13）、`单样本`（如 live save S07）、`替代路线`（与常见不同但完成任务）。不用票数决定好坏。
3. 例外先行但非免检：先声明属于哪类（在线持久/永久死亡/短单局/无历史 live-save），再把检查口径换成该类真实玩家任务——恢复摩擦、成果损失与补偿、回滚策略；不能因“它是例外/替代”跳过验证。
4. 断点清单走查：存档/恢复失败提示；取消与预览（防误触）；警报能否定位到对象；库存/净产/容量三口径可分；计划与施工分离；教学可重访且可脱离教学语境使用；规模化后的重复操作是否有批量工具。
5. 对每个“缺失”先列替代实现与成熟样本，并核其覆盖范围、成本与成熟度：替代充分且成本可接受→不写差距；替代存在但范围/成本/成熟度不足→仍写差距与建议。
6. 拿不到正文的来源标“未核验”，用标题/摘要推 UI 或教学效果均禁止；未实测的时延、稳定性、满意度一律留空（本文件即如此）。

## 4. 仍未核验项

- Klei ONI（Copy Settings 扩张）与 Satisfactory（Blueprint Designer）官方正文未取得（bot 校验/JS 渲染/网络超时），未做任何结论；两子类样本暂缺。
- Surviving Mars 官方手册正文未取得；其存档语义仅按 S01–S02（开发日志）层面记录，不评其存档实现。
- 所有游戏的默认键位未在实机核对；主机具体按键映射未核验（仅“支持手柄/支持键鼠”层面）。
- S14 为社区维护 wiki；“滚动 3 槽”等数值未与游戏 UI 二次核对。
- 各能力的玩家使用率、满意度、教学效果（如 S12 所述受众扩大）均属开发者自述，无独立度量。
- 本文只回答“同类做到过什么、边界在哪”；目标游戏相对这些样本的分数、优先级与验收阈值由主评审另定。
