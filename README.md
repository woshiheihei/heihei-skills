# X Thread Context Capture

面向单条 X/Twitter 帖子的深度上下文抓取项目。

这个仓库的目标不是做全量爬虫，而是围绕一条高信息密度的 X 帖子，产出一个可直接交给后续大模型或 Agent 继续分析的研究上下文包。项目当前包含：

- 一个可复用的 Codex skill
- 产品需求文档
- 开源项目 best-practices 调研
- 示例输出文件
- 校验脚本
- GitHub 社区与发布基础设施

## 核心能力

- 围绕单条 X 帖子抓取 root post、作者 follow-up、关键评论、关键人物、关键引用
- 以浏览器拟人化浏览为主，不依赖 X API 作为主路径
- 输出单一 Markdown 研究文件，适合继续喂给 ChatGPT、Gemini、Claude 或其他 agent
- 默认将结果沉淀到 `x-thread-contexts/`，避免结果散落在仓库根目录

## 仓库结构

```text
.
├── AGENTS.md
├── README.md
├── .agents/
│   └── skills/
│       └── x-thread-context-capture -> ../../skills/x-thread-context-capture
├── docs/
│   ├── prd.zh-CN.md
│   └── open-source-best-practices.md
├── examples/
│   └── *.md
├── scripts/
│   └── validate_skill_repo.py
├── skills/
│   └── x-thread-context-capture/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
└── x-thread-contexts/
    └── .gitkeep
```

## Skill 位置

仓库内的 skill 源码位于：

- [skills/x-thread-context-capture/SKILL.md](skills/x-thread-context-capture/SKILL.md)

发布到 GitHub 时，建议以仓库内 `skills/x-thread-context-capture/` 作为开源源代码的基准版本。

为了让 Codex 在仓库内直接发现该 skill，仓库还包含一个 repo-local 入口：

- `.agents/skills/x-thread-context-capture` -> `skills/x-thread-context-capture`

## 安装

这个仓库默认不提供平台专属安装脚本，而是优先采用更轻量、也更接近当前 skills 生态的两种方式。

如果你直接在这个仓库里启动 Codex，通常不需要额外安装。Codex 会扫描仓库内的 `.agents/skills/`，这个 skill 可以被直接发现。

推荐方式：Ask your agent

```text
Please install the skill from https://github.com/<your-org-or-user>/<repo>/tree/main/skills/x-thread-context-capture
```

如果你在使用 Codex，也可以直接调用原生的 `$skill-installer`：

```text
$skill-installer install https://github.com/<your-org-or-user>/<repo>/tree/main/skills/x-thread-context-capture
```

这种做法与 `openai/skills` 的官方分发方式一致，也比维护仓库自定义 shell 安装脚本更简单、可移植。

如果目标环境不支持自动安装，再退回手动复制目录即可：将 `skills/x-thread-context-capture/` 放入目标 agent 的 skills 发现目录。

## 使用方式

示例 prompt：

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

## 文档

- 产品需求文档：[docs/prd.zh-CN.md](docs/prd.zh-CN.md)
- 开源最佳实践调研：[docs/open-source-best-practices.md](docs/open-source-best-practices.md)

## 社区与发布

- 许可证：[LICENSE](LICENSE)
- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)
- 安全策略：[SECURITY.md](SECURITY.md)
- 行为准则：[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- GitHub Actions 校验工作流：[.github/workflows/validate.yml](.github/workflows/validate.yml)

## 示例输出

- [x-thread-context-karpathy-2036836816654147718.md](examples/x-thread-context-karpathy-2036836816654147718.md)
- [x-thread-context-karpathy-2036841069636370467.md](examples/x-thread-context-karpathy-2036841069636370467.md)

## 校验

运行仓库级自检：

```bash
python3 scripts/validate_skill_repo.py
```

该脚本会检查：

- 关键目录是否存在
- Skill frontmatter 是否完整
- 示例目录与运行输出目录是否同时存在
- 输出目录是否存在
- README / PRD / 调研文档是否齐全

## 安装策略说明

这份仓库刻意把“安装”设计成文档约定，而不是额外的 shell 封装，原因是：

- Codex 官方支持 repo-local `.agents/skills/` 发现机制，仓库内可以直接暴露 skill
- `openai/skills` 官方仓库本身就推荐通过 Codex 内置的 `$skill-installer` 从 GitHub 目录安装
- `baoyu-skills` 这类代表性开源仓库也把 “Ask the Agent” 作为正式安装选项
- 对公开仓库来说，少一个自定义安装脚本，通常就少一层平台兼容性和维护成本

## 后续建议

如果准备正式开源，下一步最值得补的是：

1. 在 GitHub 仓库设置中启用 private vulnerability reporting
2. 增加更多真实案例输出作为 `examples/`
3. 建立首个 release，例如 `v0.1.0`
4. 视发布受众补充英文 README 或双语说明
