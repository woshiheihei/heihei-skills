# X Thread Context Capture

Turn a single X/Twitter post into a model-ready research context pack.

这个仓库提供一个面向 Codex 的专业 skill，用来围绕单条高信息密度的 X/Twitter 帖子，抓取并整理一份适合后续大模型或 Agent 继续分析的 Markdown 上下文包。

它不是全量爬虫，也不是社媒归档工具。它更像一个“深挖单帖上下文”的研究工作流。

## Why This Exists

很多时候，真正有价值的不是“抓到整个平台的数据”，而是把一条关键帖子周围最重要的上下文整理清楚：

- root post 说了什么
- 作者后续怎么补充
- 哪些评论真正推动了讨论
- 讨论里出现了哪些关键人物、内部引用和外部链接

这个项目的目标，就是把这些信息收敛成一个单文件交付物，方便后续继续做研究、写作、分析或 Agent workflow。

## What You Get

- 一个可复用的 Codex skill：
  [skills/x-thread-context-capture/SKILL.md](skills/x-thread-context-capture/SKILL.md)
- 一份产品需求文档：
  [docs/prd.zh-CN.md](docs/prd.zh-CN.md)
- 一份开源 best-practices 调研：
  [docs/open-source-best-practices.md](docs/open-source-best-practices.md)
- 一组经过审阅的样例输出：
  [examples](examples)
- 一套面向公开仓库的基础设施：
  [LICENSE](LICENSE),
  [CONTRIBUTING.md](CONTRIBUTING.md),
  [SECURITY.md](SECURITY.md),
  [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md),
  [GitHub Actions](.github/workflows/validate.yml)

## Core Capabilities

- 围绕单条 X 帖子抓取 root post、作者 follow-ups、关键评论、关键人物和关键引用
- 以浏览器拟人化浏览为主，不依赖 X API 作为主路径
- 输出单一 Markdown 文件，适合继续喂给 ChatGPT、Claude、Gemini 或其他 agent
- 使用结构化命名，默认保存到 `cwd/x-thread-contexts/`
- 任务结束时关闭本次打开的抓取标签页，减少浏览器堆积

## Quick Start

如果你直接在这个仓库里启动 Codex，通常不需要额外安装。

仓库已经提供 repo-local 发现入口：

- `.agents/skills/x-thread-context-capture` -> `skills/x-thread-context-capture`

Codex 会扫描 `.agents/skills/`，因此这个 skill 可以在仓库内直接被发现。

如果你希望从 GitHub 安装，推荐两种方式。

Ask your agent:

```text
Please install the skill from https://github.com/woshiheihei/heihei-skills/tree/main/skills/x-thread-context-capture
```

For Codex with the built-in installer:

```text
$skill-installer install https://github.com/woshiheihei/heihei-skills/tree/main/skills/x-thread-context-capture
```

如果目标环境不支持自动安装，再手动复制 `skills/x-thread-context-capture/` 到对应 agent 的 skills 发现目录即可。

## Example Prompt

```text
Use $x-thread-context-capture to turn this X post into a structured-name Markdown research context pack saved under cwd/x-thread-contexts/.
```

默认输出路径：

```text
./x-thread-contexts/x-thread-context-<author_handle>-<root_status_id>.md
```

例如：

```text
./x-thread-contexts/x-thread-context-karpathy-2039805659525644595.md
```

## Output Shape

默认交付物是一份可独立阅读的 Markdown 文件，通常包含：

- 目标帖子元信息
- root post 原文
- 作者后续回复
- 高信号评论
- 关键人物
- X 内部引用与第三方链接
- 覆盖边界和不完整性说明

## Examples

- [x-thread-context-karpathy-2036836816654147718.md](examples/x-thread-context-karpathy-2036836816654147718.md)
- [x-thread-context-karpathy-2036841069636370467.md](examples/x-thread-context-karpathy-2036841069636370467.md)

说明：

- `examples/` 存放经过挑选和审阅的样例
- `x-thread-contexts/` 只作为本地运行输出目录，不提交运行时生成的 `.md` 文件

## Repository Layout

```text
.
├── .agents/
│   └── skills/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── docs/
├── examples/
├── scripts/
├── skills/
│   └── x-thread-context-capture/
└── x-thread-contexts/
```

关键目录说明：

- `skills/x-thread-context-capture/`: 开源发布的 skill source of truth
- `.agents/skills/`: Codex 在仓库内的 repo-local 发现入口
- `docs/`: PRD 与设计/调研文档
- `examples/`: 提交到仓库的样例输出
- `x-thread-contexts/`: 本地运行输出目录
- `scripts/validate_skill_repo.py`: 仓库结构校验脚本

## Validation

运行仓库级自检：

```bash
python3 scripts/validate_skill_repo.py
```

当前会检查：

- 关键文档是否存在
- GitHub 社区文件是否齐全
- skill frontmatter 是否完整
- 示例目录与运行输出目录是否同时存在
- 输出目录是否保留为可用状态

## Design Principles

- Browser-first over API-first
- Depth over breadth
- One deliverable file over scattered notes
- Author material first, discussion branches second
- Explicit coverage boundaries over pretending completeness

## Non-goals

- 不做整站或大规模 X 数据采集
- 不承诺导出完整评论区
- 不依赖官方 X API 作为核心路径
- 不把运行产物和仓库示例混在一起

## Community

- 许可证：[LICENSE](LICENSE)
- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)
- 安全策略：[SECURITY.md](SECURITY.md)
- 行为准则：[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- GitHub Actions 校验工作流：[.github/workflows/validate.yml](.github/workflows/validate.yml)

## Roadmap

- 在 GitHub 仓库设置中启用 private vulnerability reporting
- 增加更多真实案例输出到 `examples/`
- 建立首个 release，例如 `v0.1.0`
- 视发布受众补充英文 README 或双语说明
