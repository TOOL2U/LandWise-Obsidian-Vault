# LandWise Knowledge Vault

This is the central knowledge repository for the LandWise AI system — a multi-agent orchestration platform running on macOS.

## Vault Structure

- **system/** — Core system configs, MCP server setup, integration points
- **jarvis/** — JARVIS GM orchestrator state, prompt templates, logs
- **agents/** — Individual agent souls, skill definitions, memory
- **workflows/** — Repeatable playbooks for common tasks
- **memory/** — Persistent agent memory, session logs, conversation history
- **logs/** — Integration logs, system events, audit trails
- **assets/** — Images, reference docs, external knowledge

## Quick Start

1. **Open in Obsidian:** File > Open Vault > Choose `/Users/shaunducker/Desktop/LandWise/Obsidian-Vault`
2. **Install Local REST API Plugin:** In Obsidian Settings > Community Plugins > Search "Local REST API" > Install
3. **Start MCP Server:** See system/mcp-server-startup.md
4. **Connect to JARVIS:** See jarvis/integration.md

## Key Files

- [[soul.md]] — JARVIS identity and system prompt
- [[status.md]] — Current vault state and integration status
- [[system/mcp-config.json]] — MCP server configuration
- [[jarvis/integration.md]] — JARVIS bridge integration points
- [[workflows/README.md]] — Workflow index

## Last Updated

2026-04-04 — Initial vault creation and structure setup
