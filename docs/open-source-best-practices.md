# Skills 开源项目最佳实践调研

调研日期：2026-04-07

## 调研目标

总结当前 agent skill / Claude Code / Codex 相关开源项目在结构设计、技能组织、文档、安装体验和工程化上的最佳实践，并落到本仓库。

## 参考来源

### 官方文档

- Anthropic, Skill authoring best practices
  - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic, Equipping agents for the real world with Agent Skills
  - https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills
- OpenAI, How OpenAI uses Codex
  - https://openai.com/business/guides-and-resources/how-openai-uses-codex/

### 代表性开源仓库

- qdhenry/Claude-Command-Suite
  - https://github.com/qdhenry/Claude-Command-Suite
- ChrisWiles/claude-code-showcase
  - https://github.com/ChrisWiles/claude-code-showcase

## 归纳出的最佳实践

### 1. 让 skill 的 frontmatter 成为强触发器

官方文档和开源示例都强调，`name` 与 `description` 不是附属信息，而是 skill 被触发时最核心的“入口元数据”。

实践要点：

- `description` 要同时说明“做什么”和“何时使用”
- 明确提到会触发 skill 的对象、文件类型、URL 类型或任务场景
- 命名保持简短稳定，目录名与 `name` 一致

对本仓库的启发：

- skill 已将 `x.com` / `twitter.com` 状态链接、thread、作者回复、模型研究上下文包等场景写入 description

### 2. 采用 progressive disclosure，而不是把所有内容塞进一个 SKILL.md

Anthropic 官方明确提出 progressive disclosure：元数据预加载，`SKILL.md` 按需读取，详细资料再通过 references/scripts 按需读取。

实践要点：

- `SKILL.md` 保持聚焦
- 大段模板、规则、案例拆入 `references/`
- 重复性强或需要确定性的操作，优先写成脚本

对本仓库的启发：

- 仓库中的 skill 已将模板与筛选规则拆到 `references/`
- 后续如果输出生成逻辑继续稳定，可继续补 deterministic scripts

### 3. 为重复、脆弱或高风险动作准备脚本，而不是每次临时生成

Anthropic 官方将“可执行脚本 + 明确校验”视为高价值模式，尤其适用于批量、破坏性或高一致性要求的任务。

实践要点：

- 能脚本化的安装、校验、同步动作尽量脚本化
- 让脚本输出清晰错误信息，降低 agent 和人工排错成本

对本仓库的启发：

- 已新增 `scripts/install_skill.sh`
- 已新增 `scripts/validate_skill_repo.py`

### 4. 开源项目不仅要有 skill，还要有可被人类快速理解的 repo 结构

像 `Claude-Command-Suite` 这类成熟仓库，都会把 README、安装方法、脚本、发布说明、贡献规则等显式放在仓库中。`claude-code-showcase` 也把目录结构、配置组成、GitHub Actions、最佳实践都写进 README。

实践要点：

- 根目录要有 README
- 文档收敛进 `docs/`
- 安装和使用方式要能一眼找到
- skill 源码应该直接存在于仓库内，而不是只存在于某台机器的本地目录

对本仓库的启发：

- 已新增根 `README.md`
- PRD 已移动到 `docs/`
- skill 已复制到 `skills/x-thread-context-capture/`

### 5. 为 agent 维护稳定的仓库级上下文

OpenAI 在 Codex 最佳实践中明确建议维护 `AGENTS.md`，用来承载命名约定、业务背景、目录用途和 repo 特有规则；`claude-code-showcase` 也强调项目级持久上下文文件的重要性。

实践要点：

- 把 repo 结构、输出位置、校验方法写进 `AGENTS.md`
- 不要指望 agent 从目录名自行推断所有规则

对本仓库的启发：

- 已新增根级 `AGENTS.md`

### 6. 输出产物要有专门目录，不要散落在根目录

虽然这条不是单一官方字段要求，但从工程管理和开源展示角度看，产物目录化是明显更成熟的做法。

实践要点：

- docs 与 outputs 分离
- examples / outputs 有固定目录
- 文件名应结构化、可检索

对本仓库的启发：

- 输出目录统一为 `x-thread-contexts/`
- 产物命名统一为 `x-thread-context-<author_handle>-<root_status_id>.md`

### 7. 面向公开发布时，应提供安装、验证和维护入口

优秀开源项目不仅提供源码，还会提供：

- 安装入口
- 校验入口
- 后续自动化空间，例如 GitHub Actions

对本仓库的启发：

- 已提供安装脚本和校验脚本
- 下一步可补 GitHub Actions，在 PR 上自动跑 `validate_skill_repo.py`

## 对本仓库的落地结论

本次已经落地：

1. 增加根 README
2. 将 PRD 移入 `docs/`
3. 将 skill 源码纳入仓库 `skills/`
4. 增加仓库级 `AGENTS.md`
5. 增加安装脚本
6. 增加校验脚本
7. 将输出集中到 `x-thread-contexts/`

## 下一步建议

如果目标是“公开展示个人专业能力”，最值得继续补的内容是：

1. 选择许可证并新增 `LICENSE`
2. 新增 GitHub Actions，在 PR / push 时自动校验仓库结构
3. 增加更多真实案例，形成案例库
4. 如果后续会演进 skill，补充 `CHANGELOG.md`
5. 如果希望接受外部贡献，补充 `CONTRIBUTING.md`
