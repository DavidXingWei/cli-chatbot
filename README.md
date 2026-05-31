# cli-chatbot

A command-line chatbot powered by the DeepSeek API. It supports multiple roles, remembers conversation context, controls token usage, and handles errors gracefully.

一个基于 DeepSeek API 的命令行聊天机器人。支持多角色切换、对话记忆、Token 用量控制和优雅的错误处理。

---

## Features / 功能特性

- **Multiple roles / 多角色** — Switch between assistant, e-commerce agent, and Python tutor, each with its own personality. 在通用助手、电商客服、Python 导师之间切换，每个角色有独立的人设。
- **Conversation memory / 对话记忆** — Remembers earlier messages so it can answer follow-up questions in context. 记住之前的对话，能联系上下文回答追问。
- **Token control / Token 控制** — Two-layer truncation (by turn count, then by estimated tokens) keeps requests within budget. 双层截断（先按轮数，再按估算 Token）控制每次请求的长度。
- **Graceful error handling / 优雅的错误处理** — Clear messages for missing API keys, network errors, and rate limits. 缺少 API key、网络错误、请求过频时都有清晰提示。

---

## Requirements / 环境要求

- Python 3.8+
- A DeepSeek API key / 一个 DeepSeek API 密钥

---

## Installation / 安装

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/DavidXingWei/cli-chatbot.git
cd cli-chatbot

# Install dependencies / 安装依赖
pip install -r requirements.txt
```

---

## Configuration / 配置

Create a `.env` file in the project root and add your API key.

在项目根目录创建 `.env` 文件，填入你的 API 密钥。

```
DEEPSEEK_API_KEY=your_key_here
```

You can copy `.env.example` as a starting point.

可以复制 `.env.example` 作为模板。

---

## Usage / 使用方法

```bash
python main.py
```

On start, choose a role (press Enter for default). Then chat freely.

启动后选择一个角色（直接回车使用默认）。然后就可以自由对话了。

### Commands / 命令

| Command / 命令 | Description / 说明 |
|---|---|
| `/exit` | Quit the program / 退出程序 |
| `/clear` | Clear conversation history / 清空对话历史 |
| `/role` | Switch to a different role / 切换角色 |

You can also press `Ctrl+C` to exit at any time.

也可以随时按 `Ctrl+C` 退出。

---

## Roles / 角色

| Role / 角色 | Description / 说明 |
|---|---|
| `default` | A helpful general assistant / 通用助手 |
| `ecommerce` | A customer service agent for an electronics store / 电子产品商店的客服 |
| `teacher` | A patient Python programming tutor / 耐心的 Python 编程导师 |

---

## Screenshots / 截图

<!-- Add your screenshots here / 在这里添加截图 -->
<!-- 例如 / e.g.: -->
<!-- ![基本对话](screenshots/01-basic.png) -->
<!-- ![清空历史](screenshots/02-clear.png) -->
<!-- ![角色切换](screenshots/03-role.png) -->
<!-- ![错误处理](screenshots/04-error.png) -->

---

## Project Structure / 项目结构

```
cli-chatbot/
├── chatbot.py        # Chatbot class: roles, memory, token control / 核心类
├── main.py           # CLI entry point and command loop / 命令行入口
├── .env.example      # Example environment file / 环境变量模板
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Notes / 说明

This is my second project. I learned a lot about API integration, conversation state management, and error handling while building it.

这是我的第二个项目。在做的过程中，我学到了很多关于 API 集成、对话状态管理和错误处理的知识。
