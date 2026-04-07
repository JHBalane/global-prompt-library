#!/usr/bin/env python3
"""
Pack Validator for Global Prompt Library

Validates prompt pack JSON files against the schema and checks for common issues.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple


class PackValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        
        # Valid values for enum fields
        self.valid_categories = ["productivity", "creative", "business", "development"]
        self.valid_languages = ["en", "de", "es", "fr", "it", "pt", "nl", "pl", "zh", "ja"]
        self.valid_difficulties = ["beginner", "intermediate", "advanced"]
        self.valid_models = ["gpt", "claude", "gemini", "all"]
        
    def validate_pack_file(self, file_path: str) -> Tuple[bool, List[str], List[str]]:
        """Validate a pack file and return success status, errors, and warnings."""
        self.errors = []
        self.warnings = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                pack_data = json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False, self.errors, self.warnings
        except FileNotFoundError:
            self.errors.append(f"File not found: {file_path}")
            return False, self.errors, self.warnings
        
        # Validate pack structure
        self._validate_pack_metadata(pack_data)
        self._validate_prompts(pack_data.get("prompts", []))
        
        # Check for warnings
        self._check_warnings(pack_data)
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _validate_pack_metadata(self, pack: Dict[str, Any]) -> None:
        """Validate pack-level metadata."""
        # Required fields
        required_fields = {
            "id": str,
            "name": str, 
            "version": str,
            "author": dict,
            "description": str,
            "category": str,
            "language": str,
            "license": str,
            "created": str,
            "prompts": list
        }
        
        for field, expected_type in required_fields.items():
            if field not in pack:
                self.errors.append(f"Missing required field: {field}")
            elif not isinstance(pack[field], expected_type):
                self.errors.append(f"Field '{field}' must be of type {expected_type.__name__}")
        
        # Validate specific fields
        if "id" in pack:
            if not re.match(r"^[a-z0-9-]+$", pack["id"]):
                self.errors.append("Pack ID must contain only lowercase letters, numbers, and hyphens")
            if len(pack["id"]) < 3 or len(pack["id"]) > 50:
                self.errors.append("Pack ID must be between 3 and 50 characters")
        
        if "version" in pack:
            if not re.match(r"^\d+\.\d+\.\d+$", pack["version"]):
                self.errors.append("Version must follow semantic versioning (e.g., 1.0.0)")
        
        if "category" in pack:
            if pack["category"] not in self.valid_categories:
                self.errors.append(f"Category must be one of: {', '.join(self.valid_categories)}")
        
        if "language" in pack:
            if pack["language"] not in self.valid_languages:
                self.errors.append(f"Language must be one of: {', '.join(self.valid_languages)}")
        
        if "license" in pack:
            if pack["license"] != "TextDeck-Community-1.0":
                self.errors.append("License must be 'TextDeck-Community-1.0'")
        
        if "created" in pack:
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", pack["created"]):
                self.errors.append("Created date must be in YYYY-MM-DD format")
        
        # Validate author
        if "author" in pack and isinstance(pack["author"], dict):
            self._validate_author(pack["author"])
        
        # Validate tags
        if "tags" in pack:
            self._validate_tags(pack["tags"])
    
    def _validate_author(self, author: Dict[str, Any]) -> None:
        """Validate author information."""
        required_fields = ["name", "github"]
        
        for field in required_fields:
            if field not in author:
                self.errors.append(f"Author missing required field: {field}")
        
        if "github" in author:
            if not re.match(r"^[a-zA-Z0-9-]+$", author["github"]):
                self.errors.append("GitHub username can only contain letters, numbers, and hyphens")
            if len(author["github"]) > 39:
                self.errors.append("GitHub username too long")
        
        if "website" in author:
            if not author["website"].startswith(("http://", "https://")):
                self.errors.append("Author website must be a valid URL")
        
        if "email" in author:
            if "@" not in author["email"]:
                self.errors.append("Author email must be a valid email address")
    
    def _validate_tags(self, tags: List[str]) -> None:
        """Validate tags array."""
        if not isinstance(tags, list):
            self.errors.append("Tags must be an array")
            return
        
        if len(tags) == 0:
            self.warnings.append("Pack should have at least one tag")
        
        if len(tags) > 10:
            self.errors.append("Pack can have at most 10 tags")
        
        for tag in tags:
            if not isinstance(tag, str):
                self.errors.append("All tags must be strings")
            elif not re.match(r"^[a-z0-9-]+$", tag):
                self.errors.append(f"Tag '{tag}' can only contain lowercase letters, numbers, and hyphens")
            elif len(tag) > 20:
                self.errors.append(f"Tag '{tag}' is too long (max 20 characters)")
    
    def _validate_prompts(self, prompts: List[Dict[str, Any]]) -> None:
        """Validate all prompts in the pack."""
        if len(prompts) < 3:
            self.errors.append("Pack must contain at least 3 prompts")
        
        if len(prompts) > 50:
            self.errors.append("Pack can contain at most 50 prompts")
        
        prompt_ids = set()
        
        for i, prompt in enumerate(prompts):
            # Check for duplicate IDs
            if "id" in prompt:
                if prompt["id"] in prompt_ids:
                    self.errors.append(f"Duplicate prompt ID: {prompt['id']}")
                prompt_ids.add(prompt["id"])
            
            self._validate_prompt(prompt, i)
    
    def _validate_prompt(self, prompt: Dict[str, Any], index: int) -> None:
        """Validate a single prompt."""
        prefix = f"Prompt {index + 1}"
        
        # Required fields
        required_fields = {
            "id": str,
            "title": str,
            "description": str,
            "content": str
        }
        
        for field, expected_type in required_fields.items():
            if field not in prompt:
                self.errors.append(f"{prefix}: Missing required field '{field}'")
            elif not isinstance(prompt[field], expected_type):
                self.errors.append(f"{prefix}: Field '{field}' must be of type {expected_type.__name__}")
        
        # Validate ID format
        if "id" in prompt:
            if not re.match(r"^[a-z0-9-]+$", prompt["id"]):
                self.errors.append(f"{prefix}: ID must contain only lowercase letters, numbers, and hyphens")
        
        # Check content length
        if "content" in prompt:
            if len(prompt["content"]) < 20:
                self.warnings.append(f"{prefix}: Content seems very short")
            if len(prompt["content"]) > 2000:
                self.errors.append(f"{prefix}: Content too long (max 2000 characters)")
            
            # Check for variables
            variables_in_content = re.findall(r"\{\{(\w+)\}\}", prompt["content"])
            declared_variables = []
            
            if "variables" in prompt:
                declared_variables = [var.get("name", "") for var in prompt["variables"]]
            
            # Check if all variables in content are declared
            for var in variables_in_content:
                if var not in declared_variables:
                    self.warnings.append(f"{prefix}: Variable '{var}' used in content but not declared")
            
            # Check if all declared variables are used
            for var in declared_variables:
                if var not in variables_in_content:
                    self.warnings.append(f"{prefix}: Variable '{var}' declared but not used in content")
        
        # Validate variables
        if "variables" in prompt:
            self._validate_variables(prompt["variables"], prefix)
        
        # Validate examples
        if "examples" in prompt:
            self._validate_examples(prompt["examples"], prefix)
        
        # Validate optional fields
        if "difficulty" in prompt:
            if prompt["difficulty"] not in self.valid_difficulties:
                self.errors.append(f"{prefix}: Difficulty must be one of: {', '.join(self.valid_difficulties)}")
        
        if "model_compatibility" in prompt:
            if not isinstance(prompt["model_compatibility"], list):
                self.errors.append(f"{prefix}: Model compatibility must be an array")
            else:
                for model in prompt["model_compatibility"]:
                    if model not in self.valid_models:
                        self.errors.append(f"{prefix}: Invalid model '{model}'. Must be one of: {', '.join(self.valid_models)}")
        
        if "tags" in prompt:
            self._validate_tags(prompt["tags"])
    
    def _validate_variables(self, variables: List[Dict[str, Any]], prefix: str) -> None:
        """Validate prompt variables."""
        if not isinstance(variables, list):
            self.errors.append(f"{prefix}: Variables must be an array")
            return
        
        var_names = set()
        
        for i, var in enumerate(variables):
            if not isinstance(var, dict):
                self.errors.append(f"{prefix}: Variable {i + 1} must be an object")
                continue
            
            # Required fields
            if "name" not in var:
                self.errors.append(f"{prefix}: Variable {i + 1} missing 'name' field")
            elif var["name"] in var_names:
                self.errors.append(f"{prefix}: Duplicate variable name '{var['name']}'")
            else:
                var_names.add(var["name"])
                
                # Validate name format
                if not re.match(r"^[a-z0-9_]+$", var["name"]):
                    self.errors.append(f"{prefix}: Variable name '{var['name']}' can only contain lowercase letters, numbers, and underscores")
            
            if "description" not in var:
                self.errors.append(f"{prefix}: Variable {i + 1} missing 'description' field")
            elif len(var["description"]) < 5:
                self.warnings.append(f"{prefix}: Variable '{var.get('name', i + 1)}' description is very short")
    
    def _validate_examples(self, examples: List[Dict[str, Any]], prefix: str) -> None:
        """Validate prompt examples."""
        if not isinstance(examples, list):
            self.errors.append(f"{prefix}: Examples must be an array")
            return
        
        if len(examples) > 3:
            self.errors.append(f"{prefix}: Maximum 3 examples allowed")
        
        for i, example in enumerate(examples):
            if not isinstance(example, dict):
                self.errors.append(f"{prefix}: Example {i + 1} must be an object")
                continue
            
            if "input" not in example:
                self.errors.append(f"{prefix}: Example {i + 1} missing 'input' field")
            
            if "output" not in example:
                self.errors.append(f"{prefix}: Example {i + 1} missing 'output' field")
            elif len(example["output"]) < 10:
                self.warnings.append(f"{prefix}: Example {i + 1} output seems very short")
    
    def _check_warnings(self, pack: Dict[str, Any]) -> None:
        """Check for potential issues that aren't errors."""
        # Check description length
        if "description" in pack and len(pack["description"]) < 20:
            self.warnings.append("Pack description is quite short")
        
        # Check if pack has tags
        if "tags" not in pack or len(pack["tags"]) == 0:
            self.warnings.append("Pack should have tags for better discoverability")
        
        # Check for updated field
        if "updated" not in pack:
            self.warnings.append("Consider adding 'updated' field to track modifications")
        
        # Check prompt count
        prompts = pack.get("prompts", [])
        if len(prompts) < 5:
            self.warnings.append("Consider adding more prompts for a richer pack")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate Global Prompt Library pack files")
    parser.add_argument("file", help="Path to the pack JSON file to validate")
    parser.add_argument("--warnings", action="store_true", help="Show warnings in addition to errors")
    
    args = parser.parse_args()
    
    validator = PackValidator()
    success, errors, warnings = validator.validate_pack_file(args.file)
    
    if errors:
        print("❌ Validation failed:")
        for error in errors:
            print(f"  ERROR: {error}")
    
    if warnings and args.warnings:
        print("⚠️  Warnings:")
        for warning in warnings:
            print(f"  WARNING: {warning}")
    
    if success:
        print("✅ Validation passed!")
        if warnings:
            print(f"   ({len(warnings)} warnings - use --warnings to see them)")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()