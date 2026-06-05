from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .utils import dump_json, load_json, print_output, repo_root, repo_version

CARD_TYPES = {
    "route",
    "protocol",
    "adoption_pack",
    "command",
    "report",
    "template",
    "benchmark",
    "concept",
    "platform",
    "preset",
    "workflow",
    "diagnostic",
}
RISK_LEVELS = {"low", "medium", "high", "critical", "variable"}
MATURITY_LEVELS = {"experimental", "local-stable", "stable", "deprecated"}
REQUIRED_FIELDS = [
    "id",
    "type",
    "name",
    "summary",
    "use_when",
    "do_not_use_when",
    "risk_level",
    "domains",
    "maps_to",
    "entry_files",
    "related_files",
    "cli",
    "outputs",
    "stop_conditions",
    "validation",
    "version",
]
MAP_FIELDS = ["sdlc_phase", "ai_failure_modes", "project_state", "risk_categories"]


def cards_root(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "cards"


def card_paths(root: Path | None = None) -> list[Path]:
    return sorted(cards_root(root).rglob("*.json"))


def load_cards(root: Path | None = None) -> list[dict[str, Any]]:
    cards = []
    for path in card_paths(root):
        data = load_json(path)
        data["__path"] = str(path.relative_to(repo_root(root)))
        cards.append(data)
    return cards


def _text_haystack(card: dict[str, Any]) -> str:
    bits: list[str] = [str(card.get("id", "")), str(card.get("name", "")), str(card.get("summary", ""))]
    for field in ["domains", "use_when", "do_not_use_when", "entry_files", "related_files", "cli", "outputs", "stop_conditions", "validation"]:
        bits.extend(str(x) for x in card.get(field, []))
    maps = card.get("maps_to", {})
    if isinstance(maps, dict):
        for key in MAP_FIELDS:
            bits.extend(str(x) for x in maps.get(key, []))
    return "\n".join(bits).lower()


def list_cards(
    type_filter: str | None = None,
    json_mode: bool = False,
    recommended: bool = False,
    maturity: str | None = None,
    platform: str | None = None,
    domain: str | None = None,
) -> int:
    cards = load_cards()
    if type_filter:
        cards = [card for card in cards if card.get("type") == type_filter]
    if recommended:
        cards = [card for card in cards if card.get("recommended") is True]
    if maturity:
        cards = [card for card in cards if card.get("maturity") == maturity]
    if platform:
        cards = [card for card in cards if platform in card.get("platforms", [])]
    if domain:
        cards = [card for card in cards if domain in card.get("domains", [])]
    items = [
        {
            "id": card.get("id"),
            "type": card.get("type"),
            "name": card.get("name"),
            "maturity": card.get("maturity"),
            "recommended": card.get("recommended"),
            "platforms": card.get("platforms", []),
            "badges": card.get("badges", []),
            "path": card.get("__path"),
        }
        for card in cards
    ]
    if json_mode:
        print_output({"total": len(items), "items": items}, True)
    else:
        for item in items:
            print(f"{item['type']}: {item['id']} ({item['path']})")
    return 0


def show_card(card_id: str, json_mode: bool = False) -> int:
    matches = [card for card in load_cards() if card.get("id") == card_id]
    if not matches:
        print(f"Card not found: {card_id}")
        return 1
    if len(matches) > 1:
        print(f"Duplicate card id: {card_id}")
        for card in matches:
            print(f"- {card.get('__path')}")
        return 1
    card = matches[0]
    if json_mode:
        print_output(card, True)
    else:
        print(dump_json(card))
    return 0


def collect_card_validation(root: Path | None = None) -> tuple[list[dict[str, Any]], list[str]]:
    root = repo_root(root)
    target_version = repo_version(root)
    errors: list[str] = []
    cards = load_cards(root)
    ids: dict[str, list[str]] = defaultdict(list)
    for card in cards:
        ids[str(card.get("id"))].append(card["__path"])
        for field in REQUIRED_FIELDS:
            if field not in card:
                errors.append(f"Missing field {field} in {card['__path']}")
        if card.get("type") not in CARD_TYPES:
            errors.append(f"Invalid card type in {card['__path']}: {card.get('type')}")
        if card.get("risk_level") not in RISK_LEVELS:
            errors.append(f"Invalid risk level in {card['__path']}: {card.get('risk_level')}")
        maturity = card.get("maturity")
        if maturity is not None and maturity not in MATURITY_LEVELS:
            errors.append(f"Invalid maturity in {card['__path']}: {maturity}")
        recommended = card.get("recommended")
        if recommended is not None and not isinstance(recommended, bool):
            errors.append(f"recommended must be boolean in {card['__path']}")
        for key in ["platforms", "badges"]:
            if key in card and not isinstance(card[key], list):
                errors.append(f"{key} must be a list in {card['__path']}")
        maps = card.get("maps_to")
        if not isinstance(maps, dict):
            errors.append(f"maps_to must be an object in {card['__path']}")
        else:
            for key in MAP_FIELDS:
                if key not in maps or not isinstance(maps[key], list):
                    errors.append(f"maps_to.{key} must be a list in {card['__path']}")
        for key in [
            "use_when",
            "do_not_use_when",
            "domains",
            "entry_files",
            "related_files",
            "cli",
            "outputs",
            "stop_conditions",
            "validation",
        ]:
            if key in card and not isinstance(card[key], list):
                errors.append(f"{key} must be a list in {card['__path']}")
        for rel in card.get("entry_files", []) + card.get("related_files", []):
            if isinstance(rel, str) and rel.endswith((".md", ".json", ".py", ".sh", ".txt", ".yml", ".yaml", ".ps1", ".cmd")):
                if not (root / rel).exists():
                    errors.append(f"Missing referenced path from {card['__path']}: {rel}")
        if card.get("version") != target_version:
            errors.append(f"Card version mismatch in {card['__path']}: {card.get('version')}")
    for card_id, paths in ids.items():
        if len(paths) > 1:
            errors.append(f"Duplicate card id {card_id}: {', '.join(paths)}")
    return cards, errors


def validate_cards(json_mode: bool = False) -> int:
    root = repo_root()
    cards, errors = collect_card_validation(root)
    payload = {"ok": not errors, "count": len(cards), "errors": errors}
    if json_mode:
        print_output(payload, True)
    else:
        if errors:
            for error in errors:
                print(error)
        else:
            print(f"Cards validation passed. ({len(cards)} cards)")
    return 0 if not errors else 1


def search_cards(query: str, json_mode: bool = False) -> int:
    needle = query.strip().lower()
    matches = []
    for card in load_cards():
        if needle in _text_haystack(card):
            matches.append(
                {
                    "id": card.get("id"),
                    "type": card.get("type"),
                    "name": card.get("name"),
                    "summary": card.get("summary"),
                    "path": card.get("__path"),
                }
            )
    payload = {"query": query, "count": len(matches), "results": matches}
    if json_mode:
        print_output(payload, True)
    else:
        for item in matches:
            print(f"{item['id']} [{item['type']}] - {item['summary']}")
    return 0
