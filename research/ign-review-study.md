# IGN 评分方法与评测样本研究

核查日期：2026-09-20。用途：为本仓库的非官方 AI 游戏评论员建立方法参照，不代表 IGN、不是训练完成的评分预测器，也不宣称穷尽其历史评测。
本研究区分三件事：IGN 官方公开规则；个别评论员在所列版本中的判断；我们为文字 MUD/代理执行做的工程化改编。

## 一、核查方式与资料限制

尝试网页检索及直接访问后，部分 IGN 主站页面被读取工具拒绝；改用 Exa 读取官方页面、官方分站及原文存档。下表如实标出全文、正文片段或结论的读取范围。
评分交叉核对官方游戏条目中带评论员署名的编辑评分卡，不读取邻近的用户平均分、游戏发行日期或统计游玩时长来冒充评测数据。
遇到标题/正文/结论不同步时不拼接成一篇“已核验全文”；原作、最终剪辑版、抢先体验、正式版、移植版和新平台版分开。
只保存出处、简短转述及方法推导，不在仓库镜像整篇有版权的文章。来源变动时追加核验记录，不静默改历史样本分数。

## 二、IGN 官方规则：可借鉴什么

出处：[IGN Review Practices](https://corp.ign.com/review-practices)，本次读取完整正文；页面未给出可据以确认的正文更新日期，以下是核查时可读版本。
- 评分服务于是否值得投入时间/金钱的判断；评论有具体评论员立场，不是客观测量“乐趣”。
- 自 2020 年 1 月采用 1–10 整数档，历史分数保留；总分不是分项加权，也不从固定起点加减。
- 10 是最高推荐，不表示完美无缺；评论依据实际体验、同类比较和编辑复核。
- 早期访问可能采用进行中评测及当前暂分；未完成作品也必须明确其被评范围。

英文档位：10 Masterpiece；9 Amazing；8 Great；7 Good；6 Okay；5 Mediocre；4 Bad；3 Awful；2 Painful；1 Unbearable。
本仓库把这些语义档位改写成可执行证据门槛，详见 [评分模块](../references/critic-scoring.md)。七个观察角度、相邻档位问题、原型评分标签和反漂移流程均为我们新增，不是声称找到了 IGN 内部算法。

## 三、重点样本与版本

| 样本 | 原评日期与评论员 | 编辑评分 | 本次实际读取范围 | 版本/误读风险 |
|---|---|---|---|---|
| Baldur's Gate 3 | 2023-08-18；当前原页署名 Len Hafer | 10 | 主站开头、官方分站正文与结论、主站编辑评分卡 | 首发 PC 评测；分站当地日期为 8 月 19 日，不混同后续平台 |
| The Legend of Zelda: Tears of the Kingdom | 2023-05-11；Tom Marks | 10 | 原文存档主要正文段落、官方结论及编辑评分卡 | 原 Switch 版，不是 Switch 2 版重新评分 |
| Disco Elysium: The Final Cut | 2021-03-31；Simon Cardy | 10 | 主站正文节选和最终结论、编辑评分卡；另检查分站异常 | 更新后的 Final Cut；不能用仍显示 9.6 的旧版结论替代 |
| Celeste | 2018-01-25；Tom Marks | 10 | 官方分站正文、主站开头及编辑评分卡 | 2020 年前的历史原评，按原值记录，不据此重算新量表 |
| Hades | 2020-09-17；Nick Limon | 9 | 主站开头/编辑评分卡、分站部分机制正文；排除混存的早期访问结论 | 原作正式版，不是 Hades II，也不是早期访问评分 |
| Starfield | 2023-08-31；Dan Stapleton | 7 | 原评开头、官方视频页面的文字结论及主站编辑评分卡 | PC/Xbox Series X 原评；不外推其他版本或当下完整状态 |

日期按原评条目而非搜索抓取日；分站时区/更新日差异不当成新的一次评测。选择四篇满分、两篇非满分用于方法对照，不据六篇样本总结评分分布或推断任何作品应得分数。

## 四、满分文章具体看什么

### 1. Baldur's Gate 3：行动自由、世界回应、遭遇变化与整体密度

文章用具体解决问题的行动解释自由度：环境互动、绕过冲突、不同战术以及较早选择在后续得到回应；肯定角色与任务写作。它也写到教学不足、早期脆弱及后段性能问题，并非把缺点藏起来才给 10。
我们推导的 MUD 检查：对同一目标尝试不同办法；离开再返回看世界记忆；跨阶段看策略是否变化。不能要求文字原型复制它的制作规模，也不能借该文给自己的阻断 bug 免责。
出处：[原评](https://www.ign.com/articles/baldurs-gate-3-review)｜[官方分站正文](https://pk.ign.com/baldurs-gate-iii/213256/review/baldurs-gate-3-review)｜[编辑评分卡](https://www.ign.com/games/baldurs-gate-iii/reviews)。

### 2. Tears of the Kingdom：系统组合使探索产生自主目标

正文通过地图探索、临时改变目的地和组合工具解决障碍说明价值，而不是只用地图大小论证好玩；评价新能力、区域与遭遇如何扩展原有体验，也保留对叙事组织形式的批评。
我们推导的 MUD 检查：没有任务箭头时能否依据文本线索自定目标？已有工具能否形成多种解法？地图/资源/事件是否相互作用？不照搬开放世界规模或建造系统。
出处：[原评与结论](https://www.ign.com/articles/the-legend-of-zelda-tears-of-the-kingdom-review)｜[原文存档](https://web.archive.org/web/20230511120332/https://www.ign.com/articles/the-legend-of-zelda-tears-of-the-kingdom-review)｜[编辑评分卡](https://www.ign.com/games/the-legend-of-zelda-tears-of-the-kingdom/reviews)。

### 3. Disco Elysium: The Final Cut：文本、角色与机制共同承载体验

主站可读部分把对话写作、世界、独特心理技能与选择联系起来；最终结论特别说明新增任务和配音如何增强原作，编辑评分卡确认为 10。
我们推导的 MUD 检查：文本是否支持选择和人物/世界变化，而不只是篇幅多？玩家如何利用信息行动？不能据该文要求所有文字原型全配音，更不能把真实共情假写成 AI 亲身感受。
出处：[Final Cut 原评](https://www.ign.com/articles/disco-elysium-the-final-cut-review)｜[编辑评分卡](https://www.ign.com/games/disco-elysium-the-final-cut/reviews)。

### 4. Celeste：少量核心动作、持续变化、低成本重试与表达一致

正文从移动控制讲到关卡如何反复挖掘简单动作，说明快速重试、支线挑战及技能进步；还讨论音乐、叙事与关卡节奏如何协同，以及不同偏好玩家可采用的辅助/跳过选项。
我们推导的 MUD 检查：三五个核心动词能否在新约束下产生新选择？失败后能否学到并快速再试？文字、机制和主题是否互相支持？不是模仿其平台跳跃操作。
出处：[原评](https://www.ign.com/articles/2018/01/25/celeste-review)｜[官方分站正文](https://me.ign.com/en/celeste/142686/celeste-review)｜[编辑评分卡](https://www.ign.com/games/celeste/reviews)。

## 五、非满分对照：避免只学会夸奖

### Hades：9 分同样可以高度赞扬体验协同

主站编辑卡肯定快节奏动作与持续叙事的结合；机制正文讨论不同构筑、角色记住失败、重复尝试仍能带来新内容。不能因为看到“独特、优秀、值得玩”就自动归到 10，也不能自行发明一个具体扣一分的原因。
迁移到 MUD：重复循环/失败/回访是否仍推进关系、策略或目标？把“又来一遍”变成“带着变化再来”，但有叙事并不强制升一档。
出处：[原评](https://www.ign.com/articles/hades-review)｜[编辑评分卡](https://www.ign.com/games/hades/reviews)｜[官方分站正文，结论未采](https://me.ign.com/en/hades/177346/review/hades-review)。

### Starfield：7 分不是全盘否定，好内容也不能抹去进入成本

原评及官方视频文字结论同时保留角色扮演任务/战斗的吸引力和慢热开头、导航、旅行割裂、物品管理的损耗；据此给出有保留的推荐。
迁移到 MUD：熟练后仍要回看首访证据；“后面才有趣”不能撤销前期损耗。这里只说明如何论证取舍，不把这些问题机械绑定到 7 分。
出处：[原评](https://www.ign.com/articles/starfield-review)｜[原评视频页面文字结论](https://za.ign.com/video/181609/starfield-video-review)｜[编辑评分卡](https://www.ign.com/games/starfield/reviews)。

## 六、资料校验中实际遇到的陷阱

1. [印度分站 Final Cut 页面](https://in.ign.com/no-truce-with-the-furies/156904/review/disco-elysium-the-final-cut-review)同时出现更新说明与旧 9.6/旧结论；本研究以主站 Final Cut 编辑卡与最终结论判定样本版本，不把两版混用。
2. Hades 部分分站正文描述了完整推进，末尾却仍推荐等待正式版前的早期访问体验；其结论不作为正式版评分依据。
3. 官方游戏页面同时出现编辑评分与用户平均分，数值不同不代表评论员改分；游戏初始发行日也不是文章日期。
4. 只读搜索摘要不能声称完成全文分析；这里明确记录读取范围，不从遗漏段落断言“IGN 没提某问题”。

## 七、落地决定

采用整体语义档位、具体体验片段、目标人群、同约束对照、最强反证与编辑复核；不要构造“玩法 40% + 画面 20%”并称之为 IGN 算法。
单独输出原型暂评/完整版本评分；保留设计诊断十节和全部未解决 P0。先自由首访封存，再深玩，再评分，避免盲玩者为了某一分数收集证据。
七个观察角度详见 [评分模块](../references/critic-scoring.md)。真人校准见 [真人试玩](../references/human-playtest.md)，评分变化需要 [体验回归](../references/experience-regression.md) 的新版本证据。
本次完成的是评审方法与提示协议，未进行模型训练、统计验证或对当前 MUD 的实机评分。没有游戏入口和合格试玩证据时必须不评分。
