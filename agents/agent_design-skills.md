# Skills: agent_design (Visual Creative Specialist)

## Skill: generate_visual_brief
Purpose: Convert a user request into a structured visual brief for production.
Input: platform, format, topic, copy_text, mood_style, dimensions (optional)
Output: normalized_brief JSON with defaults filled

## Skill: select_image_provider
Purpose: Choose the best image provider for the brief.
Input: normalized_brief
Output: provider (ideogram | dalle3 | stable_diffusion), rationale

Selection guidance:
- ideogram: text-on-image, branded social creative (default)
- dalle3: polished concept imagery
- stable_diffusion: style control / custom workflows

## Skill: build_canva_template_payload
Purpose: Build a Canva-ready payload for template automation.
Input: normalized_brief, brand_config
Output: template_payload JSON with text, assets, dimensions, logo placement

## Skill: apply_brand_rules
Purpose: Validate a creative against LandWise brand rules.
Input: metadata, design attributes, brand_config
Output: pass/fail + violations list

Checks:
- allowed colors only
- approved fonts only
- logo placement by format
- required dimensions by format
- readability/contrast sanity check

## Skill: export_creative_asset
Purpose: Export final creative in production-ready format.
Input: rendered_asset, format_profile
Output: file_path, mime_type, dimensions, checksum

Output path:
- /Users/shaunducker/Desktop/LandWise/creatives/

## Skill: queue_for_approval
Purpose: Queue generated creative in JARVIS approval system.
Input: file_path, preview_text, brief_summary
Output: action_id, queue_status

Endpoint:
- POST http://localhost:8000/gm/actions

## Skill: generate_ab_variants
Purpose: Create 2-4 creative variants for A/B testing.
Input: normalized_brief, variation_strategy
Output: variant_paths + diff notes

## Skill: fallback_local_composite
Purpose: Produce asset without Canva when API is unavailable.
Input: normalized_brief, provider_output, brand_config
Output: final_composited_asset

Tooling:
- Sharp (Node) or Pillow (Python)

## Skill: handoff_to_agent_content
Purpose: Return copy/content revisions required for visual fit.
Input: visual_constraints, layout_feedback
Output: revision_request for agent_content
