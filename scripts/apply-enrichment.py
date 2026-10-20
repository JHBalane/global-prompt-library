#!/usr/bin/env python3
"""
Merge enrichment/<pack-id>.json into the built packs.

The packs in packs/official/ are generated (scripts/make-packs.py) or edited by
hand; what a reader needs beyond the prompt itself lives next to them in
enrichment/, keyed by prompt id:

    {
      "<prompt-id>": {
        "use_case": "...",              # when to reach for it
        "why_it_works": "...",          # what the rules in the prompt do
        "example": {"input": {...}, "output": "..."},
        "de": {                          # any language code
          "title", "description", "content",
          "variables": {"<name>": {"label", "description", "placeholder"}},
          "use_case", "why_it_works",
          "example": {"input": {...}, "output": "..."}
        }
      }
    }

Run it after make-packs.py, which rewrites the generated packs from scratch:

    python3 scripts/make-packs.py && python3 scripts/apply-enrichment.py && python3 scripts/build-index.py

A translation must use exactly the original's {{variables}}; anything else
stops the run, because the app fills a template by those names.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs" / "official"
ENRICHMENT = ROOT / "enrichment"
PLACEHOLDER = re.compile(r"\{\{([a-z0-9_]+)\}\}")
LANG = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")


def placeholders(text: str) -> set[str]:
    return set(PLACEHOLDER.findall(text))


def main() -> int:
    packs = {}
    for path in PACKS.glob("*.json"):
        pack = json.loads(path.read_text())
        packs[pack["id"]] = (path, pack)

    failed = False
    for source in sorted(ENRICHMENT.glob("*.json")):
        pack_id = source.stem
        if pack_id not in packs:
            print(f"✗ {source.name}: no pack with id '{pack_id}'")
            failed = True
            continue
        path, pack = packs[pack_id]
        enrichment = json.loads(source.read_text())
        prompts = {p["id"]: p for p in pack["prompts"]}

        for prompt_id, extra in enrichment.items():
            prompt = prompts.get(prompt_id)
            if prompt is None:
                print(f"✗ {pack_id}/{prompt_id}: no such prompt")
                failed = True
                continue
            names = {v["name"] for v in prompt["variables"]}

            for key in ("use_case", "why_it_works"):
                if key in extra:
                    prompt[key] = extra[key]
            if "example" in extra:
                missing = names - set(extra["example"]["input"])
                if missing:
                    print(f"✗ {pack_id}/{prompt_id}: example lacks {sorted(missing)}")
                    failed = True
                prompt["examples"] = [extra["example"]]

            for lang, t in extra.items():
                if not LANG.match(lang):
                    continue
                used = placeholders(t["content"])
                if used != names:
                    print(f"✗ {pack_id}/{prompt_id} [{lang}]: variables {sorted(used)} ≠ {sorted(names)}")
                    failed = True
                translation = {
                    "title": t["title"],
                    "description": t["description"],
                    "content": t["content"],
                    "variables": t["variables"],
                }
                for key in ("use_case", "why_it_works"):
                    if key in t:
                        translation[key] = t[key]
                if "example" in t:
                    translation["examples"] = t["example"]["input"]
                    translation["example_output"] = t["example"]["output"]
                prompt.setdefault("translations", {})[lang] = translation

        path.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n")
        print(f"  -> {path.relative_to(ROOT)} ({len(enrichment)} prompts enriched)")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
