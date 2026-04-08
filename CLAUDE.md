# Obsidian Vault — Claude Configuration
<!-- kepano/obsidian-skills installed 2026-04-06 -->

## VAULT CONTEXT

This is the **LandWise Obsidian Vault** — the persistent memory and knowledge base for the LandWise AI system (JARVIS orchestrator + 11-agent crew).

**Vault path:** `~/Desktop/LandWise/Obsidian-Vault/`
**JARVIS soul:** `soul.md`
**Bridge:** `http://localhost:8000`

---

## SKILLS LIBRARY

Before working with any vault files, discover and read the relevant SKILL.md from `.claude/skills/`:

```bash
find "$PWD/.claude/skills" -name SKILL.md | sort
```

| Trigger | Skill | File |
|---------|-------|------|
| `.md` files, wikilinks, embeds, callouts, frontmatter | `obsidian-markdown` | `.claude/skills/obsidian-markdown/SKILL.md` |
| `.base` files, filters, formulas, table/card views | `obsidian-bases` | `.claude/skills/obsidian-bases/SKILL.md` |
| `.canvas` files, mind maps, flowcharts | `json-canvas` | `.claude/skills/json-canvas/SKILL.md` |
| `obsidian` CLI, vault ops, plugin dev | `obsidian-cli` | `.claude/skills/obsidian-cli/SKILL.md` |
| Reading URLs, web articles, docs | `defuddle` | `.claude/skills/defuddle/SKILL.md` |

### Reference Files
Extended documentation available under `.claude/skills/<name>/references/`:
- `obsidian-markdown`: `CALLOUTS.md`, `EMBEDS.md`, `PROPERTIES.md`
- `obsidian-bases`: `FUNCTIONS_REFERENCE.md`
- `json-canvas`: `EXAMPLES.md`

---

## OBSIDIAN FILE RULES

- **Notes:** `.md` files with YAML frontmatter
- **Databases:** `.base` files (Obsidian Bases feature)
- **Canvases:** `.canvas` files (JSON Canvas format)
- **Templates:** `templates/` folder
- **Memory:** `memory/` folder — agent-maintained state files

### Wikilinks
Use `[[Note Name]]` for internal vault links. Never use `[text](path.md)` for internal notes.

### Frontmatter
Every note should have at minimum:
```yaml
---
tags:
  - category/subcategory
---
```

---

## GLOBAL SKILLS

Also check global skill directories for additional capabilities:
```bash
for dir in "$HOME/.claude/skills" "$HOME/antigravity-awesome-skills/skills" "$PWD/.claude/skills" "$PWD/Jarvis/skills"; do
  [ -d "$dir" ] && find "$dir" -maxdepth 2 -name SKILL.md 2>/dev/null | grep -i "<keyword>"
done
```

---

## MEMORY FILES

| File | Purpose |
|------|---------|
| `soul.md` | JARVIS identity + agent roster |
| `memory/status.md` | Current pipeline + lead status |
| `memory/calendar.md` | Live Google Calendar sync |
| `memory/sync-schedule.md` | Agent sync schedule |

Always read `soul.md` before vault-level operations.
