# X Thread Context Capture

面向单条 X/Twitter 帖子的深度上下文抓取项目。

这个仓库的目标不是做全量爬虫，而是围绕一条高信息密度的 X 帖子，产出一个可直接交给后续大模型或 Agent 继续分析的研究上下文包。项目当前包含：

- 一个可复用的 Codex skill
- 产品需求文档
- 开源项目 best-practices 调研
- 示例输出文件
- 安装与校验脚本

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
├── docs/
│   ├── prd.zh-CN.md
│   └── open-source-best-practices.md
├── scripts/
│   ├── install_skill.sh
│   └── validate_skill_repo.py
├── skills/
│   └── x-thread-context-capture/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
└── x-thread-contexts/
    └── *.md
```

## Skill 位置

仓库内的 skill 源码位于：

- [skills/x-thread-context-capture/SKILL.md](skills/x-thread-context-capture/SKILL.md)

发布到 GitHub 时，建议以仓库内 `skills/x-thread-context-capture/` 作为开源源代码的基准版本。

## 安装

将 skill 安装到默认 Codex skills 目录：

```bash
bash ./scripts/install_skill.sh
```

安装目标默认为：

```bash
${CODEX_HOME:-$HOME/.codex}/skills/x-thread-context-capture
```

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

## 示例输出

- [x-thread-context-karpathy-2036836816654147718.md](x-thread-contexts/x-thread-context-karpathy-2036836816654147718.md)
- [x-thread-context-karpathy-2036841069636370467.md](x-thread-contexts/x-thread-context-karpathy-2036841069636370467.md)

## 校验

运行仓库级自检：

```bash
python3 scripts/validate_skill_repo.py
```

该脚本会检查：

- 关键目录是否存在
- Skill frontmatter 是否完整
- 输出目录是否存在
- README / PRD / 调研文档是否齐全

## 后续建议

如果准备正式开源，下一步最值得补的是：

1. 选择并补充开源许可证
2. 增加 CI，在 PR 中自动跑仓库校验
3. 增加更多真实案例输出作为 examples
4. 建立 release / changelog 节奏
