#!/usr/bin/env python3
"""
Pack builder.

Authoring a pack should mean writing prompts, not writing JSON. Source files in
`authoring/*.py` carry the pack metadata and a list of prompts; everything
mechanical — prompt ids, the `variables` array, descriptions and examples — is
derived here from the `{{placeholders}}` in the prompt body via the shared
lexicon, so the same variable never gets two different descriptions.

    python3 scripts/make-packs.py            # build every authoring source
    python3 scripts/make-packs.py hiring     # build one, by pack id

Writes packs/official/<id>.json. Run scripts/build-index.py afterwards.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from variable_lexicon import lookup  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AUTHORING = ROOT / "authoring"
OUT_DIR = ROOT / "packs" / "official"

PLACEHOLDER = re.compile(r"\{\{([a-z0-9_]+)\}\}")

AUTHOR = {"name": "TextDeck", "github": "JHBalane"}
LICENSE = "TextDeck-Community-1.0"
VALID_CATEGORIES = {"productivity", "creative", "business", "development"}
VALID_DIFFICULTY = {"beginner", "intermediate", "advanced"}


def slugify(title: str) -> str:
    s = title.lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:50]


def variables_for(content: str) -> list[dict]:
    """One entry per distinct placeholder, in order of first appearance."""
    seen: list[str] = []
    for name in PLACEHOLDER.findall(content):
        if name not in seen:
            seen.append(name)

    out = []
    for name in seen:
        description, example = lookup(name)
        entry = {"name": name, "description": description}
        if example is not None:
            entry["example"] = example
        else:
            print(f"  ! no lexicon entry for {{{{{name}}}}} — add one to variable_lexicon.py")
        entry["required"] = True
        out.append(entry)
    return out


def build_pack(source) -> dict:
    meta = source.PACK
    assert meta["category"] in VALID_CATEGORIES, f"bad category: {meta['category']}"

    prompts = []
    ids: set[str] = set()
    for p in source.PROMPTS:
        title = p["title"]
        pid = p.get("id") or slugify(title)
        assert pid not in ids, f"duplicate prompt id in {meta['id']}: {pid}"
        ids.add(pid)

        difficulty = p.get("difficulty", "beginner")
        assert difficulty in VALID_DIFFICULTY, f"bad difficulty: {difficulty}"

        content = p["content"].strip()
        prompts.append({
            "id": pid,
            "title": title,
            "description": p["description"],
            "content": content,
            "variables": variables_for(content),
            "tags": p.get("tags", meta.get("tags", [])[:3]),
            "difficulty": difficulty,
        })

    return {
        "id": meta["id"],
        "name": meta["name"],
        "version": meta.get("version", "1.0.0"),
        "author": AUTHOR,
        "description": meta["description"],
        "category": meta["category"],
        "language": meta.get("language", "en"),
        "regions": meta.get("regions", ["US", "GB", "DE", "AT", "CH"]),
        "license": LICENSE,
        "created": meta["created"],
        "updated": meta.get("updated", meta["created"]),
        "tags": meta["tags"],
        "prompts": prompts,
    }


def load_source(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    wanted = set(sys.argv[1:])
    sources = sorted(AUTHORING.glob("*.py"))
    if not sources:
        print("no authoring sources found")
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total = 0
    built = 0
    for path in sources:
        source = load_source(path)
        pack_id = source.PACK["id"]
        if wanted and pack_id not in wanted:
            continue
        print(f"building {pack_id}")
        pack = build_pack(source)
        out = OUT_DIR / f"{pack_id}.json"
        out.write_text(json.dumps(pack, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  -> {out.relative_to(ROOT)} ({len(pack['prompts'])} prompts)")
        total += len(pack["prompts"])
        built += 1

    print(f"\n{built} packs, {total} prompts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
