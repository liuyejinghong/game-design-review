# FPS 迁移证据：通用方法在射击子类的有限验证

核查日期：2026-10-12。用途：验证通用评审方法（同类样本 → 模块能力 → 存在性/深度 → 差距改进/成功替代）能否落到 FPS，并给出一组可追踪的一手证据样例。**本文件不是 FPS 专属评分标准、不新增尺子、不替代实测**；不包含真人试玩，不比较手感、平衡或品质。

样本子类：单人 arena（DOOM 2016）、竞技战术（Counter-Strike 2）、战术英雄＋主机移植（VALORANT）、战役＋竞技多人（Halo Infinite）。平台与版本状态以文中来源为准。

## 0. 方法与证据纪律

四步与主协议同构，仅替换模块名：

1. **同类样本**：按相关模块需要补不同设计样本，不强制每轮凑齐所有样本；不同子类不直接横比"有没有某功能"。
2. **模块能力清单**：从"玩家在这类游戏里要完成什么行动"拆模块（示例：会话接续 / 移动与瞄准 / 交战与反馈 / 输入与可达性 / 教学）。模块是提问清单，不是必选功能表。
3. **存在性 / 深度两问**：存在性＝文档、界面或实机路径是否提供该能力或等效替代；深度＝它在多大程度上推进玩家目标。实现状态按能力对照协议记四态：具备／部分具备／已确认缺失／未核验（没找到只写未核验与补测，不推"完全没有"）。官方文档一般只能回答存在性与设计意图；深度必须由试玩取证另证。
4. **结论口径**（对齐能力对照协议五值：达到参照／部分达到／存在差距／替代成立／未能判定）：未核验不等于缺失；与成熟参照有可见差距但无真实体验损害记录 → 只进对照表与建议，不强行 P 级；有替代仍可写部分达到或存在差距；只有证据不足才记"未能判定"，已有负面证据或局部已能判定时照写部分达到/差距；"替代成立"须实测正证据；四尺确认真实损害才成候选（P0/P1/P2）。

证据纪律：

- 文档声明"提供某功能"≠该功能质量达标；不得由此推断手感、流畅度、真人体验或留存。
- 标题与检索摘要只作线索；本文件每条事实均来自可读正文，存档快照标注快照日期。
- 没有正证据不宣布"创新成功"；"刻意省略"与"省略得好"是两件事。
- 采样记录：本轮 6 条独立检索方向、10 份官方/开发者正文来源（含 2 份 Wayback 快照）；下文只写实际读到的正文事实。

**记录字段模板**（对每个样本的每条能力声明；Phase 0 参照物与后续轮次可直接照抄字段）：

- 游戏/版本/平台＋适用子类：
- 来源＝名称＋URL＋发布日（或快照日）＋本次核查日：
- 文档支持事实（短引文，仅必要范围）：
- 能力需求与样本实现（该模块想让玩家完成什么）：
- 替代等效/刻意省略（含适用条件）：
- 不能推出什么（文档≠品质；未证实的部分明确标注）：
- 深度状态：在有试玩证据前一律记"未测/待补"，不得由文档升级为结论。

**与主协议条款挂接**（模块名换掉，条款不动）：

- 会话接续 → 一A1 连续性、U9 中断与接续、G6 既得成果（回访核对边界）。
- 移动与瞄准 → U4 输入与术语、F4 控制感、M4 控制与干预（替代方案是否仍可达目标）。
- 交战与反馈 → 一B1/B2 受理与结果反馈、F6 反馈、M1 因果一致。
- 教学与可达性 → U1/U2 上手与教学、U8 防错，可达性设置按"存在即记录适用条件"。

## 1. 样本卡

### 卡 1 · DOOM（2016，PC/主机，单人战役，arena FPS）

- 来源：GDC Vault 官方演讲页《Embracing Push Forward Combat in 'DOOM'》，GDC 2018，讲者 Kurt Loudy、Jake Campbell（id Software）；正文核查 2026-10-12。
- 文档支持事实（原句节选）："stares down genre conventions like regenerating health, reload and cover, and instead puts the onus on the player to take what they need from adversaries."
- 能力需求与样本实现：开发者描述把传统换弹/回血/掩体列为被挑战的惯例，并把方向写成"从敌人处取得所需"；由此可形成**候选资源循环**（本文件推导，完整循环与深度需另源或实测，非摘要原句）。
- 适用子类：高强度单人 arena 射击。
- 替代/刻意省略：传统换弹、掩体回血被声明为被挑战的惯例；替代方向＝从敌人处取得所需（开发者描述，非实测）。
- 不能推出：不证明该循环实际好玩或平衡；"本作刻意省略"不等于其他射击游戏应省略，也不等于省略本身是优点；摘要不能证明完整资源循环。

### 卡 2 · Counter-Strike 2（PC，竞技战术 5v5）

- 来源：Valve 官方博文《Rush Hour》，Steam 官方新闻 2026-09-22；正文核查 2026-10-12（官方 RSS 全文）。
- 文档支持事实（原句节选）："Reloading can now be performed silently (by holding the reload key), but with a cost--silent reloads take quite a bit longer."；"Un-scoping a sniper weapon no longer produces a sound."；准星更新新增 "Crosshair/Scopes" 标签页，默认准星改为 "Dynamic Quad"，"better represents weapon accuracy"。
- 能力需求与样本实现：换弹是核心节奏与声音信息模块（新增"静音但更慢"的取舍）；开镜属于部分武器（scoped weapons／狙击）并配有独立设置；武器不准度被显式建模并反映到准星。
- 适用子类：竞技战术射击（枪械信息战）。
- 替代/刻意省略：本轮可核验三项存在——开镜武器类别与专属设置、换弹（含静音换弹）、准星反映不准度；是否存在全武器通用 ADS 没有可读官方证据，记未核验，不能由博文未提推出不存在。
- 不能推出：博文只声明功能存在与调整，不证明平衡、手感或公平性；也不能构成本轮缺陷判据。

### 卡 3 · VALORANT（PC；主机版 open beta 自 2024-07-26，战术英雄射击）

- 来源与日期：Riot《Peeking into VALORANT's Netcode》（2020-07-28）；官方补丁 1.0（2020-06-01）；官方补丁 3.0（2021-06-22）；官方支持页《Walking, Running, and Crouching》（2023-12-19）；Xbox Wire 官方文《…Open Beta Begins Today》（2024-07-26）。正文核查 2026-10-12。
- 文档支持事实（原句节选）：
  - "Weapon fire is inaccurate while a player is moving, forcing the peeker to either come to a stop before firing or fire while inaccurate..."（2020）
  - "Deadzone"＝开始不准的移动速度，30% → 27.5%；行走不准度 1.3 → 2.0 等逐武器调整（2021）
  - "Removed the 'freeze time' that would trigger when waiting for a player to reconnect at the start of the buy phase."（补丁 1.0，2020-06-01）——说明"断线后重连回同一局"是既有流程；重连失败与惩罚的具体边界本轮未核验。
  - Toggle Walk／Toggle Crouch 与默认移动模式设置（2023）
  - "On PC, Hip-Fire is the primary shooting mode, and Aim-Down-Sights is a secondary, supporting mode"；"Enter Focus, a new shooting mode that functions much like Hip-Fire, but with reduced sensitivity"；官方自述尝试多种手柄移植方案，"never found a combination they were completely happy with"（2024）。PC 与主机不跨平台对战（保控制公平），跨进度共享。
- 能力需求与样本实现：移动→射击精度是显式设计轴；瞄准输入按平台分化。
- 适用子类：战术射击（PC）与手柄主机移植。
- 替代/刻意省略：主机增设 Focus 以完成低灵敏度/精准瞄准任务；ADS 在实际操作中的全量映射本次未核验（不能推断主机完全没有 ADS）。
- 不能推出：均属设计声明与规则调整；不证明手感、平衡或主机版表现；"替代是否成立"须实测正证据，本次未判。

### 卡 4 · Halo Infinite（Xbox/PC，单人战役＋多人免费）

- 来源：Halo Support《Guide to Halo Infinite Menus》（正文；Wayback 2025-10-24 快照）；Halo Support《Accessibility features in Halo Infinite》（正文；Wayback 2022-01-25 快照）；Xbox Wire 官方文（2021-10-01，含 343 Industries 的 Paige Johnson 条目）。核查 2026-10-12。
- 文档支持事实（原句节选）：
  - Campaign："Continue: Continues most recently saved game."；"Load Game: Opens menu of saved check points to start from."
  - Multiplayer："Players who exit early will lose any stats/progress earned in the match and risk an automated or manual enforcement ban..."
  - Academy："contains Tutorial, Weapon Drills, and Training Mode options"（Weapon Drills＝全主武器三档计时靶场；Training Mode＝可调 bot 对战）
  - 无障碍：瞄准准星轮廓透明度/厚度可调；UI 播报（可调速，仅英文）；按键重映射、"change to taps and toggles versus holds"、Movement Assisted Steering（2021）。
- 能力需求与样本实现：单人＝检查点式接续；多人＝文档明示退出后损失与纪律边界（结算规则），是否支持重连/局内接续本轮未核验，不能以惩罚推断保存能力；教学＝教程＋分级靶场＋可调训练赛；输入＝可改键与 hold/toggle。
- 适用子类：单人战役＋竞技多人；FPS 可达性基准面。
- 替代/刻意省略：单人 checkpoint 与在线赛局是不同对象（审查方法上不等价，不能跨对象比"有没有存档"）；文档把"离开即损失进度"与纪律边界作为已知规则明示；在线赛局是否提供任何接续形式本次未核验。
- 不能推出：菜单与规则说明只证明入口与规则存在；不证明检查点频率合理、教学有效或无障碍覆盖完整——同一官方页也列出 UI 播报未覆盖部分位置，说明"已声明功能"清单不是全覆盖承诺。

### 卡组摘读（只记已取证项，不补缺口猜测）

- **会话接续**：Halo 单人检查点接续（具备）；Halo 多人文档只证退出后结算损失与纪律边界，是否支持重连未核验；VALORANT 有断线重连回局流程（文档证流程，替代/深度未测）。CS2、DOOM 本轮未取证此模块，记未核验，不写"没有"。
- **移动与瞄准**：VALORANT 把移动→射击不准写成显式设计轴，主机增设 Focus 承接低敏精准瞄准任务（替代是否成立待实测）；CS2 可证开镜武器类别/专属设置与准星不准度表示，是否存在跨武器通用 ADS 未核验；DOOM 本轮未取瞄准机制。
- **交战与反馈**：DOOM 开发者描述把资源方向指向"从敌人处取得所需"（候选替代，待实测或另源）；CS2 把换弹做成节奏与声音信息（静音取舍）；VALORANT 文档记录命中减速（hit tagging）服务于交战胜负设计。
- **教学与可达性**：仅有 Halo 样本足够细分（教程/分级靶场/可调训练赛；准星轮廓、播报、hold/toggle）。其他样本未取样，不做跨游戏优劣比较。

## 2. 合成示例：把经营模块换成 FPS 模块（协议建议，非实测结论）

同一条方法换模块名后如下。左侧为经营评审常见模块，右侧为 FPS 对应模块与检查写法；引用条款编号沿用主 SKILL。

| 经营模块 | FPS 对应模块 | 存在性检查（证据要求） | 深度实测检查（试玩动作） | 差距/改进/成功替代写法 |
|---|---|---|---|---|
| 存档/接续（U9、G6） | 会话接续 | 单人：检查点/存档文档与入口；多人：重连支持、退出后结算与纪律说明。（Halo＝检查点＋退出结算/纪律，重连未核验；VALORANT＝重连流程） | 单人中途退出，按原档回访核对边界与目标；多人重连/离场测试仅限获授权测试档或 private lobby，不接触真实玩家或竞技离场处罚，已有录像/录屏/日志等现成证据亦可采用 | 无单人存档不判错；在线赛局若确无恢复，记录结算/纪律说明与对象差异，不跨对象比"有没有存档"（Halo 本轮仅核到结算边界）；承诺可回访却无法接续→按原尺一A1/U9 |
| 镜头/观察（U3、F4） | 移动与瞄准 | 平台差异与替代方案文档：腰射/开镜/替代瞄准、灵敏度与输入设置。（CS2＝开镜武器与专属设置，本轮仅证存在；VALORANT 主机＝Focus 增设，ADS 映射未核验） | 同一射击任务分别用腰射、开镜/替代完成，比较可达精度与操作成本；检查切换与误触 | 没有 ADS/开镜不判错；"想精确命中是否仍可达"须有正证据；主打精准射击却无任何瞄准/反馈结构→按原尺指出 |
| 生产链/资源循环（I4、N1） | 交战与反馈 | 资源恢复路径文档：弹药/续航如何补充，换弹是否存在及取舍。（DOOM＝开发者描述"从敌人处取得所需"；CS2＝换弹与静音换弹） | 三圈交战记录受理、结果、资源增减与失败恢复；核对教学是否在首次需要前出现 | 契合候选替代（如从敌人处取得资源）：实测正证据才写"替代成立"；不足则记未能判定，已确认局部负证据照写差距/原尺影响；宣称行动循环而资源可恢复路径不可读且造成行动损害→按原尺判 |

示例读法：方法不预设"应有 ADS/reload/单人存档"，只要求把每个模块追到"存在性证据＋深度证据＋替代解释"；结论按五值写（达到参照/部分达到/存在差距/替代成立/未能判定），缺失不自动等于缺陷，替代成立需正证据。

## 3. 边界与反误用

1. **没有 ADS、没有 reload、没有单人存档，不自动好或坏**。判定前先核对所谓"没有"是否已核验（未核验≠缺失，不能从没提推出不存在）；判定只问：玩家目标是否被现有实现支持、是否有正证据；文档只证存在与意图，试玩证达成与否。
2. **主打行动链确实缺失仍要指出**：如宣称精准射击却没有任何可达的瞄准或反馈结构，或宣称行动循环而资源无恢复路径；不得以"子类不同""刻意省略"豁免。
3. **不把设计宣言当成绩**：GDC 摘要与官方博文证明"作者刻意这么做"，不证明做得好；"创新/省略成功"需试玩正证据，不能由文档推出。
4. **分开对象与平台**：单人 checkpoint 与在线赛局不是同一对象；PC 与主机版本需分别标注适用条件（如 VALORANT 的瞄准方案按平台分化）。
5. **本文范围**：只验证通用提问法与证据格式能落到 FPS；不是新子类 skill、不是完整 FPS 评分标准，未取样大逃杀、撤离射击、载具战等，也不比较手感与品质。

## 4. 来源清单（全部正文可读；快照标注日期）

1. GDC Vault，*Embracing Push Forward Combat in 'DOOM'*（GDC 2018，id Software 讲者与摘要）— https://www.gdcvault.com/play/1024940/Embracing-Push-Forward- （核查 2026-10-12）
2. Valve，*Rush Hour*（Steam 官方新闻，2026-09-22）— https://store.steampowered.com/news/app/730/view/711161056325533826 （核查 2026-10-12）
3. Riot Games，*Peeking into VALORANT's Netcode*（2020-07-28）— https://www.riotgames.com/en/news/peeking-valorants-netcode
4. VALORANT 官方补丁 3.0（2021-06-22）— https://playvalorant.com/en-us/news/game-updates/valorant-patch-notes-3-0/
5. Riot 支持，*Walking, Running, and Crouching*（2023-12-19）— https://support.riotgames.com/en-us/valorant/gameplay/walking-running-and-crouching
6. Xbox Wire，*Valorant's Xbox Series X|S Open Beta Begins Today*（2024-07-26）— https://news.xbox.com/en-us/2024/07/26/valorant-console-open-beta-xbox-series-x-s/
7. Halo Support，*Guide to Halo Infinite Menus*（Wayback 2025-10-24 快照全文）— https://web.archive.org/web/20251024234532/https://support.halowaypoint.com/hc/en-us/articles/4408368163348-Guide-to-Halo-Infinite-Menus （原页同路径，本次核查 2026-10-12）
8. Halo Support，*Accessibility features in Halo Infinite*（Wayback 2022-01-25 快照全文）— https://web.archive.org/web/20220125175337/https://support.halowaypoint.com/hc/en-us/articles/4408122295444-Accessibility-Features-in-Halo-Infinite （原页同路径，本次核查 2026-10-12）
9. Xbox Wire，*Xbox Celebrates the Disability Community with New Accessibility Updates*（2021-10-01，含 343 Industries 条目）— https://news.xbox.com/en-us/2021/10/01/Xbox-announces-accessibility-updates/
10. VALORANT 官方补丁 1.0（2020-06-01，含重连条目）— https://playvalorant.com/en-us/news/game-updates/valorant-patch-notes-1-0/

证据限制：WebFetch 在本环境被域名校验阻断，以上页面经 curl 抓取正文核对；Halo Support 直连返回 403，故引用 Wayback 快照并标注日期。所有引文为官方正文节选；本文件不声称任何游戏的手感、平衡或品质结论。
