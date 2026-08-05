#!/usr/bin/env python3
"""Validate data/resources.yml against the expected schema and basic quality rules."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "resources.yml"

REQUIRED_FIELDS = {
    "name",
    "url",
    "organization",
    "description",
    "categories",
    "resource_type",
    "status",
    "federal_relevance",
}

VALID_STATUSES = {"active", "maintenance", "archived", "unknown"}
VALID_RESOURCE_TYPES = {
    "standard",
    "guidance",
    "tool",
    "framework",
    "content",
    "platform",
    "training",
    "community",
    "reference",
}

# Categories from docs/taxonomy.md (kept in sync manually)
VALID_CATEGORIES = {
    "foundations",
    "rmf-80053",
    "fedramp-oscal-ato",
    "continuous-monitoring",
    "supply-chain",
    "devsecops",
    "zero-trust-iam",
    "cloud",
    "experimental-infrastructure",
    "cyber-ranges",
    "synthetic-users",
    "exercise-orchestration",
    "cyber-physical",
    "scientific-workflows",
    "uncertainty-quantification",
    "provenance",
    "security-automation",
    "containers-k8s",
    "observability-ir",
    "accessibility",
    "ai-governance",
    "privacy-records",
    "acquisition",
    "oss-policy",
    "case-studies",
    "training-communities",
    "reference-architectures",
}


def load_data() -> list[dict[str, Any]]:
    if not DATA_FILE.exists():
        print(f"ERROR: {DATA_FILE} does not exist", file=sys.stderr)
        sys.exit(1)
    with DATA_FILE.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list):
        print("ERROR: resources.yml must be a YAML list", file=sys.stderr)
        sys.exit(1)
    return data


def validate(resources: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_urls: set[str] = set()
    seen_names: set[str] = set()

    for idx, item in enumerate(resources):
        prefix = f"[{idx}] {item.get('name', '<unnamed>')}"

        if not isinstance(item, dict):
            errors.append(f"{prefix}: entry is not a mapping")
            continue

        missing = REQUIRED_FIELDS - set(item.keys())
        if missing:
            errors.append(f"{prefix}: missing required fields: {sorted(missing)}")

        name = item.get("name")
        if name:
            if name in seen_names:
                errors.append(f"{prefix}: duplicate name '{name}'")
            seen_names.add(name)

        url = item.get("url")
        if url:
            if not isinstance(url, str) or not url.startswith(("http://", "https://")):
                errors.append(f"{prefix}: invalid URL format")
            if url in seen_urls:
                errors.append(f"{prefix}: duplicate URL '{url}'")
            seen_urls.add(url)

        desc = item.get("description", "")
        if isinstance(desc, str) and (len(desc) < 20 or len(desc) > 600):
            errors.append(f"{prefix}: description length should be 20–600 characters")

        status = item.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"{prefix}: invalid status '{status}'")

        rtype = item.get("resource_type")
        if rtype and rtype not in VALID_RESOURCE_TYPES:
            errors.append(f"{prefix}: invalid resource_type '{rtype}'")

        cats = item.get("categories")
        if cats is not None:
            if not isinstance(cats, list):
                errors.append(f"{prefix}: categories must be a list")
            else:
                for c in cats:
                    if c not in VALID_CATEGORIES:
                        errors.append(f"{prefix}: unknown category '{c}'")

        # Executable tools should have security notes
        if rtype == "tool" and not item.get("security_notes"):
            errors.append(f"{prefix}: tools should include security_notes")

    return errors


def main() -> int:
    resources = load_data()
    errors = validate(resources)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(resources)} resources validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
