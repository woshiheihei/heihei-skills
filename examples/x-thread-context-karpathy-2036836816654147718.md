# 目标推文

- URL: https://x.com/karpathy/status/2036836816654147718
- 作者: Andrej Karpathy (@karpathy)
- 发布时间: 12:05 AM · Mar 26, 2026
- 抓取时间: 2026-04-07 13:40:22 CST
- 抓取方式: Chrome DevTools MCP snapshots on x.com root status page, `/thread/2036836816654147718`, individual status pages, and X search `from:karpathy conversation_id:2036836816654147718` in `Latest`
- 覆盖说明: 已覆盖根帖、5 条可见作者后续回复、这些回复对应的上游评论、3 条额外高信号评论、以及 1 条在评论区出现的第三方链接预览。`/thread` 页面露出了 4 条作者回复，X 搜索额外补出了 1 条只在 search 中清晰出现的作者回复。

## 1. Root Tweet

- URL: https://x.com/karpathy/status/2036836816654147718
- 作者: Andrej Karpathy (@karpathy)
- 时间: 12:05 AM · Mar 26, 2026
- 可见互动信号: 1768 replies, 1545 reposts, 21243 likes, 3345 bookmarks, 2.6M views

原文:

```text
One common issue with personalization in all LLMs is how distracting memory seems to be for the models. A single question from 2 months ago about some topic can keep coming up as some kind of a deep interest of mine with undue mentions in perpetuity. Some kind of trying too hard.
```

## 2. 作者后续回复

### 2.1 回复 @karpathy

- 作者回复 URL: https://x.com/karpathy/status/2036841069636370467
- 回复时间: 12:22 AM · Mar 26, 2026
- 可见互动信号: 145 replies, 51 reposts, 1689 likes, 175 bookmarks, 240K views
- 上游评论 URL: https://x.com/karpathy/status/2036836816654147718

上游评论原文:

```text
One common issue with personalization in all LLMs is how distracting memory seems to be for the models. A single question from 2 months ago about some topic can keep coming up as some kind of a deep interest of mine with undue mentions in perpetuity. Some kind of trying too hard.
```

作者回复原文:

```text
(I cycle through all LLMs over time and all of them seem to do this so it's not any particular implementation but something deeper, e.g. maybe during training, a lot of the information in the context window is relevant to the task, so the LLMs develop a bias to use what is given, then at test time overfit to anything that happens to RAG its way there via a memory feature (?))
```

### 2.2 回复 @doodlestein 和 @Qivshi1

- 作者回复 URL: https://x.com/karpathy/status/2036844441236103487
- 回复时间: 12:35 AM · Mar 26, 2026
- 可见互动信号: 42 replies, 9 reposts, 469 likes, 75 bookmarks, 48.2K views
- 上游评论 URL: https://x.com/doodlestein/status/2036841924171043048

上游评论原文:

```text
Seems like an easy fix with a time-decaying salience factor, kind of like synaptic strength fading when a pathway isn’t reinforced.
```

作者回复原文:

```text
If I had to guess it's less decay and more that memories have naive RAG-like implementations, so you're at the mercy of whatever happens to retrieve in the top k via embeddings. They don't process you in aggregate and over time (probably compute constraints) so they struggle to identify what's fleeting (?). Anyway just guesses, but it's cringe :D
```

### 2.3 回复 @KenWattana

- 作者回复 URL: https://x.com/karpathy/status/2036846449103917436
- 回复时间: 12:43 AM · Mar 26, 2026
- 可见互动信号: 11 replies, 5 reposts, 518 likes, 11 bookmarks, 36.2K views
- 上游评论 URL: https://x.com/KenWattana/status/2036845377014686077

上游评论原文:

```text
It’s sort of like when people always say your name in a conversation in an effort to influence you but instead it just comes off as smarmy and out of place
```

作者回复原文:

```text
yes exactly! a bit like i'm being manipulated in some creepy way. "please like me, look how much i know about you, we are good friends".
```

### 2.4 再次回复 @KenWattana

- 作者回复 URL: https://x.com/karpathy/status/2036848219188351207
- 回复时间: 12:50 AM · Mar 26, 2026
- 可见互动信号: 8 replies, 1 repost, 55 likes, 11 bookmarks, 5,767 views
- 上游评论 URL: https://x.com/KenWattana/status/2036847283107750302
- 附带媒体: X 页面可见 1 张图片附件；快照未暴露图片 alt 文本

上游评论原文:

```text
“how to win friends and influence people, LLM edition”

Context is really hard! And making it timely. Miss once and it’s so jarring.

Also things that it injects sometimes that I wish it didn’t because I randomly used it as a search engine at one point - it’s like work/personal divide
```

作者回复原文:

```text
Yeah, agree that it's a hard problem. It might be the EQ version of uncanny valley.
```

### 2.5 回复 @AnubhawM

- 作者回复 URL: https://x.com/karpathy/status/2036851031355904165
- 回复时间: 1:01 AM · Mar 26, 2026
- 可见互动信号: 40 replies, 6 reposts, 542 likes, 46 bookmarks, 48.2K views
- 上游评论 URL: https://x.com/AnubhawM/status/2036849257659940907

上游评论原文:

```text
Also what's up with LLMs always asking a follow up question? "Now would you like me to [insert semi-relevant arbitrary next step, like generate a graphic]". Is that just to keep users engaged and using the platform? Because sometimes I just need a direct answer and that's it. If I do need to continue the convo, it's usually not in the direction of the LLM suggestion.
```

作者回复原文:

```text
Yeah, it's engagementmaxxing, probably A/B tests extremely well. It's not how a real friend would talk to you, it's sleezy and weird. 1) I feel like it's just trying to keep me talking and 2) I feel awkward not answering its question - you wouldn't usually do that with a person.
```

## 3. 关键评论

### 3.1 elvis

- URL: https://x.com/omarsar0/status/2036848587775041872
- 作者: elvis (@omarsar0)
- 时间: 12:52 AM · Mar 26, 2026
- 可见互动信号: 4 replies, 7 reposts, 106 likes, 64 bookmarks, 15.5K views
- 外部链接/内部引用: none visible on the comment page

原文:

```text
This is why, in my experience, the simplest forms of memory work best with current LLMs. For my personalized agents, what has worked is a simple file storage system (Obsidian vaults) with metadata to allow for searching across dimensions like time, categories, workstreams, etc. Memory is effective if implemented methodically, not just dumping a bunch of random data points or markdown files into folders/indexes just because you can. There are so many opinions about how memory should be implemented correctly for agents, but IMO it's a balance between search relevance, discoverability, structure, and context awareness. All is possible to build today, but not perfect, so it's worth taking the time to tune memory yourself as you interact with your agents. A bit like when you improve agent skills progressively. That's the level of personalization no one is talking about.
```

### 3.2 Vox

- URL: https://x.com/Voxyz_ai/status/2036837405664137620
- 作者: Vox (@Voxyz_ai)
- 时间: 12:07 AM · Mar 26, 2026
- 可见互动信号: 0 replies, 0 reposts, 10 likes, 1 bookmark, 1,579 views
- 外部链接/内部引用: none visible on the comment page

原文:

```text
i've seen this too. one throwaway preference turns into lore way too easily.

memory should decay unless it gets repeated, reinforced, or tied to an active project. otherwise the model starts roleplaying a version of you from 8 weeks ago.
```

### 3.3 Matthew Berman

- URL: https://x.com/MatthewBerman/status/2036848204088828258
- 作者: Matthew Berman (@MatthewBerman)
- 时间: 12:50 AM · Mar 26, 2026
- 可见互动信号: 14 replies, 0 reposts, 111 likes, 7 bookmarks, 10.5K views
- 外部链接/内部引用: none visible on the comment page

原文:

```text
knowing which memories to drop is just as important as knowing which memories to prioritize
```

## 4. 关键人物

- Andrej Karpathy (@karpathy): 根帖作者，提出“LLM personalization memory 太用力、太分心”的核心问题，并在回复里补上对 RAG-like memory、EQ uncanny valley、以及 engagementmaxxing 的解释。
- Ken Wattana (@KenWattana): 提供了“别人总喊你名字来影响你”的类比，并继续把问题扩展到“work/personal divide”，触发了 Karpathy 两条高价值回复。
- Jeffrey Emanuel (@doodlestein): 用 time-decaying salience factor 的角度切入，触发 Karpathy 对“不是 decay 而是 naive retrieval / top-k embeddings”的技术猜测。
- Anubhaw Mathur (@AnubhawM): 把讨论从“记忆过度个性化”扩展到“LLM 总是追问下一步”的产品行为，促成 Karpathy 明确提出 `engagementmaxxing` 这一判断。
- elvis (@omarsar0): 给出“简单文件存储 + metadata + 检索结构化”的具体实现派立场，是评论区里最完整的 memory system 实践视角之一。
- Vox (@Voxyz_ai): 凝练地提出“memory should decay unless repeated / reinforced / active”，代表评论区中最直接的 temporal decay 立场。

## 5. 关键引用内容

### 5.1 X 内部引用

- 未见独立的 quoted X post 成为这条根帖主讨论的核心材料。
- 可确认的 X 内部上下文主要是作者自己的 root + self-reply chain，以及作者对评论的直接回复，这些内容已分别收录在第 1 节和第 2 节。

### 5.2 第三方外部链接

- URL: https://t.co/OCrJyuPrzn
- 来源评论/来源推文: rohan (@_Rohan_Patil) `https://x.com/_Rohan_Patil/status/2036872232157446619`
- X 页面可见预览文案:

```text
It doesn't hurt to ask: Question-asking increases liking - PubMed
From pubmed.ncbi.nlm.nih.gov
```

## 6. 覆盖边界备注

- 已明确覆盖: 根帖原文与元数据、`/thread/2036836816654147718` 可见作者链、X search `from:karpathy conversation_id:2036836816654147718` in `Latest` 暴露的作者回复、每条作者回复对应的上游评论、3 条额外高信号评论，以及 1 条评论区外链预览。
- 已搜索但未见更多作者回复: 在 `Latest` 搜索结果中，可见作者回复只包括 `2036841069636370467`、`2036844441236103487`、`2036846449103917436`、`2036848219188351207`、`2036851031355904165`；继续浏览后未见新的可见作者回复结果。
- 不完整风险: `2036848219188351207` 附带图片，但快照未暴露 alt 文本或可直接转录的图片内容，因此这里只记录“有图片附件”这一可见事实，不对图片语义做推断。
- 这是有意选择性的 context pack，不是完整评论区导出；优先保留作者物料、作者互动过的上游评论，以及能代表主要讨论分支的高信号评论。
- 互动数字均为抓取当时的可见页面快照，不应视为稳定事实。
