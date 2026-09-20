# 版本管理与复现

本仓库按整包版本管理，不给每个附件单独发号。当前版本以 [VERSION](VERSION) 为源，主 [SKILL.md](SKILL.md) 的 metadata.version、README 和 CHANGELOG 必须一致。
格式采用主.次.修订；依据 [SemVer 2.0.0](https://semver.org/lang/zh-CN/)，并把“调用入口、轮次输入输出、分级语义、报告字段”定义为本项目的公开契约。

## 一、升级规则

- 修订号：文字纠错、链接修复、没有改变裁决语义的澄清；仍记录变更。
- 次版本：增加兼容视角、调用模式或检查项；在 0.x 开发期若有不兼容变更也递增次版本，但必须写迁移说明。
- 主版本：1.0 之后破坏公开契约或改变既有严重度/报告语义时升级；0.x 不承诺完整兼容。
- 发布内容不可原地改写：修复已发布版本必须发新版本，不移动旧标签。

报告契约独立标 `report_schema: 1`；非官方媒体量表标 `critic_scale: 1`。结构或评分含义发生不兼容变化要递增对应编号，即使 skill 同时升级。
每次评审记录 `skill_version + skill_commit + game_build + report_schema + critic_scale + run_id`，不把游戏版本当 skill 版本。
离线复制包无提交信息时，填来源及未知；不得伪造 SHA。更新 skill 必须整包同步，不能把新版入口和旧附件混装。

## 二、发布流程

1. 在功能分支修改；更新 VERSION、metadata.version、README 当前版本及 CHANGELOG，同步相关协议。
2. 执行 `python scripts/validate.py --self-test`，再按 [协议验收场景](tests/acceptance.md) 检查流程；静态通过不等于真实浏览器端到端通过。
3. PR 写明变化、迁移、静态/模拟/真实验证边界；合并后核对远端文件和提交 SHA。
4. 有相应权限和工具时，为合并提交建不可移动的 `v<版本>` 标签及发布说明；标签目标必须是已验证的提交，不能仅指向一个未来会变化的分支。
5. 连接不提供 tag/release 写入时，使用 VERSION＋合并提交作为可复现标识，并明确标签未创建；不能用同名分支冒充 tag。

标签发布命令（只有获得授权且具备 Git 写入环境时执行）：
```sh
python scripts/validate.py --self-test
VERSION=$(cat VERSION)
git tag -a "v$VERSION" -m "game-design-review $VERSION"
git push origin "v$VERSION"
```
发布者需先确认当前 HEAD 就是目标合并提交。该命令不由评测游戏的 agent 自动执行；评测流程无仓库发布权限。

## 三、从旧版迁移

先前 README 标为 v0.2，附件合并后仍没有正式整包版本字段。0.3.0 是首次引入上述版本契约，不补造旧 tag 或旧发布记录。
原有四尺编号、P0/P1/P2、转段标签、Phase 0–5、十节总报告保留。旧附件中“十节输出”在多轮调用下指整次总报告，各轮只出短报告。
新用户继续点名 game-design-review；无需逐个装独立 skill。完整、多角度请求由总控路由，真人/媒体模块按需启用。
旧问题继续保留原证据与版本；按新协议复评须标新尺复评，不能当成游戏修复或分数上升。

## 四、回退

从已核验的旧 tag 或精确 commit 取回整个目录，在新 run 中记版本；不改历史报告、不覆盖正在进行中的会话。没有 tag 时按 CHANGELOG 中实际存在的提交定位。
