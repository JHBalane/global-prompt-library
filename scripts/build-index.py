#!/usr/bin/env python3
"""
Global Prompt Library Index Builder

This script scans all prompt packs and generates the master index.json file
that apps can use to discover and download prompt packs.
"""

import json
import os
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class IndexBuilder:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.packs_dir = self.root_dir / "packs"
        self.catalog_dir = self.root_dir / "catalog"
        
    def scan_packs(self) -> List[Dict[str, Any]]:
        """Scan all pack directories and load pack metadata."""
        packs = []
        
        # Scan official packs
        official_dir = self.packs_dir / "official"
        if official_dir.exists():
            for pack_file in official_dir.glob("*.json"):
                pack_data = self._load_pack(pack_file, "official")
                if pack_data:
                    packs.append(pack_data)
        
        # Scan community packs
        community_dir = self.packs_dir / "community"
        if community_dir.exists():
            for category_dir in community_dir.iterdir():
                if category_dir.is_dir():
                    for pack_file in category_dir.glob("*.json"):
                        pack_data = self._load_pack(pack_file, "community")
                        if pack_data:
                            packs.append(pack_data)
        
        return packs
    
    def _load_pack(self, pack_file: Path, pack_type: str) -> Dict[str, Any] | None:
        """Load and validate a single pack file."""
        try:
            with open(pack_file, 'r', encoding='utf-8') as f:
                pack_data = json.load(f)
            
            # Add metadata
            pack_data["type"] = pack_type
            pack_data["file_path"] = str(pack_file.relative_to(self.root_dir))
            
            # Calculate file hash for integrity
            file_hash = self._calculate_file_hash(pack_file)
            pack_data["file_hash"] = file_hash
            
            # Calculate pack statistics
            pack_data["stats"] = self._calculate_pack_stats(pack_data)
            
            # Validate required fields
            if self._validate_pack(pack_data):
                return pack_data
            else:
                print(f"Warning: Invalid pack {pack_file}")
                return None
                
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading pack {pack_file}: {e}")
            return None
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file for integrity checking."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def _calculate_pack_stats(self, pack_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate statistics for a pack."""
        prompts = pack_data.get("prompts", [])
        
        stats = {
            "prompt_count": len(prompts),
            "total_variables": sum(len(prompt.get("variables", [])) for prompt in prompts),
            "has_examples": sum(1 for prompt in prompts if prompt.get("examples")),
            "difficulty_breakdown": {},
            "tags": []
        }
        
        # Count difficulty levels
        for prompt in prompts:
            difficulty = prompt.get("difficulty", "beginner")
            stats["difficulty_breakdown"][difficulty] = stats["difficulty_breakdown"].get(difficulty, 0) + 1
        
        # Collect unique tags
        all_tags = set()
        for prompt in prompts:
            all_tags.update(prompt.get("tags", []))
        all_tags.update(pack_data.get("tags", []))
        stats["tags"] = sorted(list(all_tags))
        
        return stats
    
    def _validate_pack(self, pack_data: Dict[str, Any]) -> bool:
        """Basic validation of pack structure."""
        required_fields = ["id", "name", "version", "author", "description", "category", "language", "prompts"]
        
        for field in required_fields:
            if field not in pack_data:
                return False
        
        # Validate prompts
        prompts = pack_data.get("prompts", [])
        if not isinstance(prompts, list) or len(prompts) < 3:
            return False
        
        for prompt in prompts:
            prompt_required = ["id", "title", "description", "content"]
            for field in prompt_required:
                if field not in prompt:
                    return False
        
        return True
    
    def build_index(self) -> Dict[str, Any]:
        """Build the complete index."""
        packs = self.scan_packs()
        
        # Sort packs by type (official first) then by name
        packs.sort(key=lambda x: (x["type"] != "official", x["name"]))
        
        # Create categories summary
        categories = {}
        languages = {}
        total_prompts = 0
        
        for pack in packs:
            # Category stats
            category = pack["category"]
            if category not in categories:
                categories[category] = {"count": 0, "prompts": 0}
            categories[category]["count"] += 1
            categories[category]["prompts"] += len(pack["prompts"])
            
            # Language stats
            language = pack["language"]
            if language not in languages:
                languages[language] = {"count": 0, "prompts": 0}
            languages[language]["count"] += 1
            languages[language]["prompts"] += len(pack["prompts"])
            
            total_prompts += len(pack["prompts"])
        
        # Build index structure
        index = {
            "version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "schema_version": "1.0.0",
            "repository": {
                "url": "https://github.com/textdeck/global-prompt-library",
                "commit": self._get_git_commit() or "unknown"
            },
            "stats": {
                "total_packs": len(packs),
                "total_prompts": total_prompts,
                "categories": categories,
                "languages": languages
            },
            "packs": []
        }
        
        # Add pack summaries (without full prompt content for smaller index)
        for pack in packs:
            pack_summary = {
                "id": pack["id"],
                "name": pack["name"],
                "version": pack["version"],
                "author": pack["author"],
                "description": pack["description"],
                "category": pack["category"],
                "language": pack["language"],
                "tags": pack.get("tags", []),
                "type": pack["type"],
                "file_path": pack["file_path"],
                "file_hash": pack["file_hash"],
                "created": pack["created"],
                "updated": pack.get("updated", pack["created"]),
                "stats": pack["stats"]
            }
            index["packs"].append(pack_summary)
        
        return index
    
    def _get_git_commit(self) -> str | None:
        """Get current git commit hash if available."""
        try:
            import subprocess
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"], 
                capture_output=True, 
                text=True, 
                cwd=self.root_dir
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass
        return None
    
    def save_index(self, index: Dict[str, Any]) -> None:
        """Save the index to catalog/index.json."""
        self.catalog_dir.mkdir(exist_ok=True)
        
        index_file = self.catalog_dir / "index.json"
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        print(f"Index saved to {index_file}")
        print(f"Total packs: {index['stats']['total_packs']}")
        print(f"Total prompts: {index['stats']['total_prompts']}")
    
    def build_and_save(self) -> None:
        """Main method to build and save the index."""
        print("Building Global Prompt Library index...")
        index = self.build_index()
        self.save_index(index)
        print("Index build complete!")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build Global Prompt Library index")
    parser.add_argument(
        "--root", 
        default=".", 
        help="Root directory of the prompt library (default: current directory)"
    )
    parser.add_argument(
        "--output", 
        help="Output file path (default: catalog/index.json)"
    )
    
    args = parser.parse_args()
    
    builder = IndexBuilder(args.root)
    builder.build_and_save()


if __name__ == "__main__":
    main()