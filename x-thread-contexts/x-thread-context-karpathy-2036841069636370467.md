# 目标推文

- URL: https://x.com/karpathy/status/2036841069636370467
- 作者: Andrej Karpathy (@karpathy)
- 发布时间: 12:22 AM · Mar 26, 2026
- 抓取时间: 2026-04-07 13:32:33 +0800
- 抓取方式: Chrome DevTools MCP snapshots on x.com individual status pages, thread view, and X search
- 覆盖说明: 目标链接本身是 Karpathy 对自己上一条推文的自回复，不是独立起始帖；本文将该 URL 视为目标根帖，同时补入其上游自引主帖、可见作者后续检索结果、4 条高信号评论，以及 1 条由评论引出的 X 内部引用和外部链接预览。

## 1. Root Tweet

- URL: https://x.com/karpathy/status/2036841069636370467
- 作者: Andrej Karpathy (@karpathy)
- 时间: 12:22 AM · Mar 26, 2026
- 可见互动信号: 145 replies, 51 reposts, 1689 likes, 175 bookmarks, 240K views
- 关系说明: visible on X as a self-reply to https://x.com/karpathy/status/2036836816654147718

原文:

```text
(I cycle through all LLMs over time and all of them seem to do this so it's not any particular implementation but something deeper, e.g. maybe during training, a lot of the information in the context window is relevant to the task, so the LLMs develop a bias to use what is given, then at test time overfit to anything that happens to RAG its way there via a memory feature (?))
```

## 2. 作者后续回复

- 检索结果: no further visible author replies found for this target status after checking `https://x.com/karpathy/thread/2036841069636370467` and X search `from:karpathy conversation_id:2036841069636370467` in `Latest`.
- 搜索页状态: X returned `No results for "from:karpathy conversation_id:2036841069636370467"`.
- 备注: 目标推文本身已经是作者对上一条自线程主帖的补充回复，因此作者侧上下文主要体现在上游自引主帖，而不是该 status 下面的继续回帖。

## 3. 关键评论

### 3.1 Cheng Lou

- URL: https://x.com/_chenglou/status/2036872558415651128
- 作者: Cheng Lou (@_chenglou)
- 时间: 2:27 AM · Mar 26, 2026
- 可见互动信号: 1 reply, 0 reposts, 2 likes, 0 bookmarks, 758 views
- 外部链接/内部引用: follow-up self-reply in same subthread captured in section 5

原文:

```text
Afaik there was a post earlier months here that dissected ChatGPT and found that it only used persisted memories + the last few chats, no rag?
```

### 3.2 @deepfates

- URL: https://x.com/deepfates/status/2036846827736358955
- 作者: @deepfates
- 时间: 12:45 AM · Mar 26, 2026
- 可见互动信号: 5 replies, 4 reposts, 63 likes, 10 bookmarks, 6,852 views
- 外部链接/内部引用: none visible on the comment page

原文:

```text
I think the context window is the only thing that's real to them. They know what's in the weights as much as it's implied by what's in the context window. prop stuffing with rag is not like human memory. it would be better to let them access all previous conversations in code
```

### 3.3 Artyom

- URL: https://x.com/artyomvnsv/status/2036843128653586834
- 作者: Artyom (@artyomvnsv)
- 时间: 12:30 AM · Mar 26, 2026
- 可见互动信号: 2 replies, 0 reposts, 25 likes, 1 bookmark, 3,745 views
- 外部链接/内部引用: none visible on the comment page

原文:

```text
Could be because time is a less prominent dimension in the training corpus whereas it's one of the main ones at inference time. Especially for chat.
```

### 3.4 Brian Atwood

- URL: https://x.com/batwood011/status/2036856801975500908
- 作者: Brian Atwood (@batwood011)
- 时间: 1:24 AM · Mar 26, 2026
- 可见互动信号: 0 replies, 0 reposts, 0 likes, 0 bookmarks, 454 views
- 外部链接/内部引用: none visible on the comment page

原文:

```text
I think it *is* a particular implementation - shared across all the major providers - which is the single-persona, "everything for everyone" DTC chatbot.

In very narrow domains it's much easier to build compelling, reliable, useful memory systems.
```

## 4. 关键人物

- Andrej Karpathy (@karpathy): root author; frames the core claim that memory features cause distracting over-personalization and overfitting to injected context.
- Cheng Lou (@_chenglou): high-signal commenter who connects the discussion to an earlier investigation of ChatGPT memory behavior and then surfaces a concrete reference.
- @deepfates: pushes the "context window is the only thing that's real" framing and argues for code-level access to past conversations rather than prop-stuffing via RAG.
- Artyom (@artyomvnsv): offers a training-vs-inference-time hypothesis focused on temporal information being underrepresented during training.
- Brian Atwood (@batwood011): reframes the issue as a product implementation problem tied to general-purpose DTC chatbots rather than an unavoidable universal memory failure.
- Manthan Gupta (@manthanguptaa): indirectly enters the thread through Cheng Lou's follow-up quote; his earlier post is cited as evidence that ChatGPT memory may not use RAG.

## 5. 关键引用内容

### 5.1 X 内部引用

#### 5.1.1 上游自引主帖

- 来源: https://x.com/karpathy/status/2036836816654147718
- 被引用者: Andrej Karpathy (@karpathy)
- 时间: visible on X as Mar 26, 2026
- 引用出现在: target status page and `/thread/2036841069636370467`

原文:

```text
One common issue with personalization in all LLMs is how distracting memory seems to be for the models. A single question from 2 months ago about some topic can keep coming up as some kind of a deep interest of mine with undue mentions in perpetuity. Some kind of trying too hard.
```

#### 5.1.2 Cheng Lou 的后续自回复与引用帖

- 来源: https://x.com/_chenglou/status/2036876048718323732
- 被引用者: Manthan Gupta (@manthanguptaa)
- 时间: visible on X as Mar 26, 2026 for Cheng Lou follow-up; quoted post preview shows Dec 10, 2025
- 引用出现在: Cheng Lou comment page `https://x.com/_chenglou/status/2036872558415651128`

原文:

```text
Found it
```

可见引用预览原文:

```text
I spent the last few days prompting ChatGPT to understand how its memory system actually works.

Spoiler alert: There is no RAG used
```

### 5.2 第三方外部链接

- URL: https://manthanguptaa.in/posts/chatgpt_
- 来源评论/来源推文: Cheng Lou follow-up `https://x.com/_chenglou/status/2036876048718323732`
- X 页面可见预览文案:

```text
A blog on how chatgpt's memory works
```

## 6. 覆盖边界备注

- 已明确覆盖: 目标 status 原文与元数据、它所回复的上游 Karpathy 主帖、作者是否还有后续回复的检索结果、4 条高信号评论、1 条由评论引出的 X 内部引用、以及对应第三方链接预览。
- 已搜索但未见更多作者回复: `https://x.com/karpathy/thread/2036841069636370467` and X search `from:karpathy conversation_id:2036841069636370467` in `Latest`.
- 本结果是有意选择性的 context pack，不是完整评论区导出；在可见页面继续下滚后，新增内容已明显更偏重复、低信号或枝节讨论。
- 互动数字均为抓取时页面快照中的可见值，不应视为稳定事实。
