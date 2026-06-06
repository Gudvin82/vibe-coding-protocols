from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import shutil

from .utils import print_output, repo_root

STATUS_ORDER = ["TODO", "DOING", "DONE", "ARCHIVED / NOT TAKEN"]
STATUS_ALIASES = {
    "todo": "TODO",
    "doing": "DOING",
    "done": "DONE",
    "archived": "ARCHIVED / NOT TAKEN",
    "archived / not taken": "ARCHIVED / NOT TAKEN",
    "archived-not-taken": "ARCHIVED / NOT TAKEN",
}

ALLOWED_TYPES = {
    "idea",
    "feature",
    "bug",
    "refactor",
    "security",
    "docs",
    "operations",
    "tech-debt",
    "api-integration",
    "review-finding",
    "prod-error",
    "audit-follow-up",
}
ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}
ALLOWED_SOURCES = {"user", "ai", "audit", "prod-error", "review", "roadmap", "manual"}
ALLOWED_ROUTES = {
    "Starter",
    "Hardening",
    "Maintenance",
    "UI Ownership",
    "Post-Task Review",
    "Third-party API Intake",
    "Operations",
    "Public Site",
    "Backlog",
    "Unknown",
}
ALLOWED_ARCH_IMPACT = {"none", "docs-only", "component-level", "cross-layer", "production-critical"}

TABLE_COLUMNS = [
    "ID",
    "Priority",
    "Type",
    "Title",
    "Route",
    "Source",
    "Owner",
    "Created",
    "Updated",
    "Architecture impact",
    "Validation required",
    "Review required",
    "Linked docs",
    "Notes",
]
HEADER_ROW = "| " + " | ".join(TABLE_COLUMNS) + " |"
SEPARATOR_ROW = "|" + "|".join(["---"] * len(TABLE_COLUMNS)) + "|"
REQUIRED_SECTIONS = ["# Project Backlog", "## Rules", *[f"## {name}" for name in STATUS_ORDER]]
REQUIRED_TABLE_MARKERS = [HEADER_ROW]
EMPTY_VALUE = "-"


@dataclass
class BacklogItem:
    status: str
    id: str
    priority: str
    type: str
    title: str
    route: str
    source: str
    owner: str
    created: str
    updated: str
    architecture_impact: str
    validation_required: str
    review_required: str
    linked_docs: str
    notes: str

    def to_dict(self) -> dict[str, str]:
        return {
            "status": self.status,
            "id": self.id,
            "priority": self.priority,
            "type": self.type,
            "title": self.title,
            "route": self.route,
            "source": self.source,
            "owner": self.owner,
            "created": self.created,
            "updated": self.updated,
            "architecture_impact": self.architecture_impact,
            "validation_required": self.validation_required,
            "review_required": self.review_required,
            "linked_docs": self.linked_docs,
            "notes": self.notes,
        }


@dataclass
class BacklogDocument:
    preamble: list[str]
    items: list[BacklogItem]


def backlog_path(root: Path | None = None) -> Path:
    return repo_root(root) / "PROJECT_BACKLOG.md"


TEMPLATE_PATH = Path("templates/PROJECT_BACKLOG.md")
AUDIT_BACKLOG_EXAMPLE_PATH = Path(".vcp/audit-backlog.example.json")


def backups_dir(root: Path) -> Path:
    return root / ".vcp" / "runtime" / "backups"


def _now_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def _timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def _normalize_status(status: str) -> str:
    key = status.strip().lower()
    if status in STATUS_ORDER:
        return status
    if key in STATUS_ALIASES:
        return STATUS_ALIASES[key]
    raise ValueError(f"Unknown backlog status: {status}")


def _split_cells(line: str) -> list[str]:
    if not line.strip().startswith("|"):
        raise ValueError(f"Expected table row, got: {line}")
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _section_heading(status: str) -> str:
    return f"## {status}"


def _build_preamble() -> list[str]:
    return [
        "<!-- vcp-artifact: PROJECT_BACKLOG -->",
        "<!-- vcp-version: v0.8.7 -->",
        "<!-- methodology-version: v1.4 -->",
        "",
        "# Project Backlog",
        "",
        "## Rules",
        "",
        "- Use this backlog for tasks, ideas, bugs, operations follow-up, review follow-up, and product work.",
        "- Keep it separate from `AUDIT_BACKLOG.md`.",
        "- IDs must be unique and stable. Do not renumber existing items.",
        "- If an item is split, create new IDs and reference the parent in notes.",
        "- If duplicates are merged, keep the oldest ID and reference merged IDs in notes.",
        "- Add or update an item before implementation starts when a new request arrives.",
        "- If architecture impact is not `none`, update linked architecture docs in the same task or create a follow-up item.",
        "- Example rows below illustrate the format. Replace them with real project state.",
        "",
        "## ID convention",
        "",
        "- Default VCP prefix: `VCP-001`, `VCP-002`, `VCP-003`",
        "- Copied project prefixes may be customized: `PROJECT-001`, `SP-001`, `APP-001`",
        "",
    ]


def parse_backlog_text(text: str) -> BacklogDocument:
    lines = text.splitlines()
    items: list[BacklogItem] = []
    preamble: list[str] = []
    current_status: str | None = None
    line_index = 0
    seen_first_section = False

    while line_index < len(lines):
        line = lines[line_index]
        stripped = line.strip()
        if stripped in {_section_heading(status) for status in STATUS_ORDER}:
            current_status = stripped.removeprefix("## ")
            seen_first_section = True
            line_index += 1
            while line_index < len(lines) and not lines[line_index].strip():
                line_index += 1
            if line_index >= len(lines):
                break
            header = lines[line_index].strip()
            if header != HEADER_ROW:
                raise ValueError(f"Unexpected table header under {current_status}: {header}")
            line_index += 1
            if line_index >= len(lines) or lines[line_index].strip() != SEPARATOR_ROW:
                raise ValueError(f"Missing table separator under {current_status}")
            line_index += 1
            while line_index < len(lines):
                row = lines[line_index]
                row_stripped = row.strip()
                if not row_stripped:
                    line_index += 1
                    continue
                if row_stripped.startswith("## "):
                    break
                cells = _split_cells(row)
                if len(cells) != len(TABLE_COLUMNS):
                    raise ValueError(f"Unexpected column count in {current_status}: {row}")
                item = BacklogItem(
                    status=current_status,
                    id=cells[0],
                    priority=cells[1],
                    type=cells[2],
                    title=cells[3],
                    route=cells[4],
                    source=cells[5],
                    owner=cells[6],
                    created=cells[7],
                    updated=cells[8],
                    architecture_impact=cells[9],
                    validation_required=cells[10],
                    review_required=cells[11],
                    linked_docs=cells[12],
                    notes=cells[13],
                )
                items.append(item)
                line_index += 1
            continue
        if not seen_first_section:
            preamble.append(line)
        line_index += 1

    if not preamble:
        preamble = _build_preamble()
    return BacklogDocument(preamble=preamble, items=items)


def load_document(root: Path | None = None) -> BacklogDocument:
    path = backlog_path(root)
    if not path.exists():
        raise FileNotFoundError(path)
    return parse_backlog_text(path.read_text(encoding="utf-8"))


def render_backlog(doc: BacklogDocument) -> str:
    lines = list(doc.preamble)
    status_buckets = {status: [] for status in STATUS_ORDER}
    for item in doc.items:
        status_buckets[item.status].append(item)
    for status in STATUS_ORDER:
        if lines and lines[-1] != "":
            lines.append("")
        lines.append(_section_heading(status))
        lines.append("")
        lines.append(HEADER_ROW)
        lines.append(SEPARATOR_ROW)
        for item in status_buckets[status]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        item.id,
                        item.priority,
                        item.type,
                        item.title,
                        item.route,
                        item.source,
                        item.owner,
                        item.created,
                        item.updated,
                        item.architecture_impact,
                        item.validation_required,
                        item.review_required,
                        item.linked_docs,
                        item.notes,
                    ]
                )
                + " |"
            )
    return "\n".join(lines).rstrip() + "\n"


def _validate_item(item: BacklogItem) -> list[str]:
    errors: list[str] = []
    if item.priority not in ALLOWED_PRIORITIES:
        errors.append(f"{item.id}: invalid priority {item.priority}")
    if item.type not in ALLOWED_TYPES:
        errors.append(f"{item.id}: invalid type {item.type}")
    if item.source not in ALLOWED_SOURCES:
        errors.append(f"{item.id}: invalid source {item.source}")
    if item.route not in ALLOWED_ROUTES:
        errors.append(f"{item.id}: invalid route {item.route}")
    if item.architecture_impact not in ALLOWED_ARCH_IMPACT:
        errors.append(f"{item.id}: invalid architecture impact {item.architecture_impact}")
    if not item.id:
        errors.append("Backlog item missing ID")
    if not item.title:
        errors.append(f"{item.id or 'unknown'}: missing title")
    if not item.created:
        errors.append(f"{item.id}: missing created date")
    if not item.updated:
        errors.append(f"{item.id}: missing updated date")
    return errors


def validate_document(doc: BacklogDocument) -> list[str]:
    errors: list[str] = []
    rendered = render_backlog(doc)
    for marker in REQUIRED_SECTIONS:
        if marker not in rendered:
            errors.append(f"Missing section: {marker}")
    for marker in REQUIRED_TABLE_MARKERS:
        if rendered.count(marker) < len(STATUS_ORDER):
            errors.append(f"Missing standardized table header: {marker}")
            break
    ids: set[str] = set()
    for item in doc.items:
        errors.extend(_validate_item(item))
        if item.id in ids:
            errors.append(f"Duplicate ID: {item.id}")
        ids.add(item.id)
    return errors


def _validate_audit_backlog_json(path: Path) -> dict[str, Any]:
    import json

    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    if not isinstance(data, dict):
        errors.append("Audit backlog payload must be a JSON object.")
    items = data.get("items", [])
    if not isinstance(items, list):
        errors.append("items must be a list")
        items = []
    fingerprints: set[str] = set()
    allowed_status = {"active", "resolved", "stale", "superseded", "accepted-risk"}
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"items[{idx}] must be an object")
            continue
        for field in ["id", "fingerprint", "title", "source", "severity", "status", "first_seen", "last_seen"]:
            if field not in item:
                errors.append(f"items[{idx}] missing field: {field}")
        fingerprint = item.get("fingerprint")
        if fingerprint in fingerprints:
            errors.append(f"duplicate fingerprint: {fingerprint}")
        if fingerprint:
            fingerprints.add(fingerprint)
        if item.get("status") not in allowed_status:
            errors.append(f"items[{idx}] invalid status: {item.get('status')}")
    return {
        "ok": not errors,
        "path": str(path),
        "errors": errors,
        "count": len(items),
    }


def validate(json_mode: bool = False, root: Path | None = None, path: str | None = None) -> int:
    if path:
        target = Path(path)
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        payload = _validate_audit_backlog_json(target)
        print_output(payload, json_mode)
        return 0 if payload["ok"] else 1
    base = repo_root(root)
    path = backlog_path(base)
    errors: list[str] = []
    if not path.exists():
        errors.append("PROJECT_BACKLOG.md is missing.")
        payload = {"ok": False, "path": str(path), "errors": errors}
        print_output(payload, json_mode)
        return 1
    try:
        doc = load_document(base)
        errors.extend(validate_document(doc))
    except Exception as exc:  # noqa: BLE001
        errors.append(str(exc))
    payload = {
        "ok": not errors,
        "path": str(path),
        "errors": errors,
        "required_sections": REQUIRED_SECTIONS,
        "table_columns": TABLE_COLUMNS,
    }
    print_output(payload, json_mode)
    return 0 if not errors else 1


def summarize(path: str | None = None, json_mode: bool = False, root: Path | None = None) -> int:
    base = repo_root(root)
    target = Path(path).resolve() if path else (base / AUDIT_BACKLOG_EXAMPLE_PATH)
    if not target.exists():
        payload = {"ok": False, "error": f"Audit backlog file not found: {target}"}
        print_output(payload, json_mode)
        return 1
    import json

    data = json.loads(target.read_text(encoding="utf-8"))
    items = data.get("items", [])
    status_counts: dict[str, int] = {}
    severity_counts: dict[str, int] = {}
    for item in items:
        status = item.get("status", "unknown")
        severity = item.get("severity", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    payload = {
        "ok": True,
        "path": str(target),
        "count": len(items),
        "status_counts": status_counts,
        "severity_counts": severity_counts,
    }
    print_output(payload, json_mode)
    return 0


def template(root: Path | None = None) -> int:
    base = repo_root(root)
    path = base / TEMPLATE_PATH
    print(path.read_text(encoding="utf-8").rstrip())
    return 0


def _ensure_runtime_backup(root: Path, source: Path) -> Path:
    target_dir = backups_dir(root)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"PROJECT_BACKLOG.{_timestamp()}.md"
    shutil.copy2(source, target)
    return target


def _write_document(root: Path, doc: BacklogDocument, *, dry_run: bool) -> dict[str, Any]:
    path = backlog_path(root)
    text = render_backlog(doc)
    errors = validate_document(doc)
    if errors:
        raise ValueError("; ".join(errors))
    if dry_run:
        return {
            "modified": False,
            "dry_run": True,
            "path": str(path),
            "backup": None,
            "preview": text,
        }
    backup = _ensure_runtime_backup(root, path)
    original = path.read_text(encoding="utf-8")
    path.write_text(text, encoding="utf-8")
    post_errors = validate_document(load_document(root))
    if post_errors:
        path.write_text(original, encoding="utf-8")
        raise ValueError("Write failed validation and was restored from backup: " + "; ".join(post_errors))
    return {
        "modified": True,
        "dry_run": False,
        "path": str(path),
        "backup": str(backup),
    }


def _canonical_type(value: str) -> str:
    return value.strip().lower().replace("_", "-")


def _canonical_source(value: str) -> str:
    return value.strip().lower()


def _canonical_route(value: str) -> str:
    lowered = value.strip().lower()
    for route in ALLOWED_ROUTES:
        if route.lower() == lowered:
            return route
    return value


def _canonical_arch(value: str) -> str:
    return value.strip().lower()


def _matches(item: BacklogItem, *, status: str | None, type_: str | None, priority: str | None, source: str | None, route: str | None) -> bool:
    return (
        (status is None or item.status == status)
        and (type_ is None or item.type == type_)
        and (priority is None or item.priority == priority)
        and (source is None or item.source == source)
        and (route is None or item.route == route)
    )


def _grouped_items(items: list[BacklogItem]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {status: [] for status in STATUS_ORDER}
    for item in items:
        grouped[item.status].append(item.to_dict())
    return grouped


def list_items(
    *,
    root: Path | None = None,
    status: str | None = None,
    type_: str | None = None,
    priority: str | None = None,
    source: str | None = None,
    route: str | None = None,
    json_mode: bool = False,
) -> int:
    base = repo_root(root)
    doc = load_document(base)
    norm_status = _normalize_status(status) if status else None
    norm_type = _canonical_type(type_) if type_ else None
    norm_priority = priority if priority else None
    norm_source = _canonical_source(source) if source else None
    norm_route = _canonical_route(route) if route else None
    items = [
        item for item in doc.items if _matches(item, status=norm_status, type_=norm_type, priority=norm_priority, source=norm_source, route=norm_route)
    ]
    payload = {
        "ok": True,
        "count": len(items),
        "filters": {
            "status": norm_status,
            "type": norm_type,
            "priority": norm_priority,
            "source": norm_source,
            "route": norm_route,
        },
        "items": [item.to_dict() for item in items],
        "grouped": _grouped_items(items),
    }
    if json_mode:
        print_output(payload, True)
    else:
        for group in STATUS_ORDER:
            group_items = payload["grouped"][group]
            if not group_items:
                continue
            print(f"## {group}")
            for item in group_items:
                print(f"- {item['id']} [{item['priority']}] {item['title']} ({item['type']}, {item['route']}, owner: {item['owner']})")
            print("")
    return 0


def _id_parts(item_id: str) -> tuple[str, int] | None:
    if "-" not in item_id:
        return None
    prefix, number = item_id.rsplit("-", 1)
    if not number.isdigit():
        return None
    return prefix, int(number)


def _next_id(doc: BacklogDocument, prefix: str | None = None) -> str:
    pairs = [_id_parts(item.id) for item in doc.items]
    valid_pairs = [pair for pair in pairs if pair is not None]
    selected_prefix = prefix
    if selected_prefix is None:
        selected_prefix = valid_pairs[0][0] if valid_pairs else "VCP"
    selected_prefix = selected_prefix.upper()
    numbers = [number for item_prefix, number in valid_pairs if item_prefix.upper() == selected_prefix]
    next_number = (max(numbers) + 1) if numbers else 1
    width = max(3, len(str(next_number)))
    return f"{selected_prefix}-{next_number:0{width}d}"


def _find_item(doc: BacklogDocument, item_id: str) -> BacklogItem:
    for item in doc.items:
        if item.id == item_id:
            return item
    raise KeyError(item_id)


def add_item(
    *,
    title: str,
    type_: str,
    priority: str,
    source: str = "user",
    route: str = "Unknown",
    owner: str = EMPTY_VALUE,
    architecture_impact: str = "none",
    notes: str = EMPTY_VALUE,
    linked_docs: str = EMPTY_VALUE,
    validation_required: str = EMPTY_VALUE,
    review_required: str = EMPTY_VALUE,
    id_prefix: str | None = None,
    dry_run: bool = False,
    json_mode: bool = False,
    root: Path | None = None,
) -> int:
    base = repo_root(root)
    doc = load_document(base)
    item = BacklogItem(
        status="TODO",
        id=_next_id(doc, id_prefix),
        priority=priority,
        type=_canonical_type(type_),
        title=title.strip(),
        route=_canonical_route(route),
        source=_canonical_source(source),
        owner=owner.strip() or EMPTY_VALUE,
        created=_now_date(),
        updated=_now_date(),
        architecture_impact=_canonical_arch(architecture_impact),
        validation_required=validation_required.strip() or EMPTY_VALUE,
        review_required=review_required.strip() or EMPTY_VALUE,
        linked_docs=linked_docs.strip() or EMPTY_VALUE,
        notes=notes.strip() or EMPTY_VALUE,
    )
    doc.items.append(item)
    write_result = _write_document(base, doc, dry_run=dry_run)
    payload = {
        "ok": True,
        "action": "add",
        "item": item.to_dict(),
        "write_result": write_result,
        "summary": f"Added {item.id} to TODO.",
    }
    print_output(payload, json_mode)
    return 0


def move_item(
    *,
    item_id: str,
    status: str,
    reason: str | None = None,
    validation: str | None = None,
    review: str | None = None,
    dry_run: bool = False,
    json_mode: bool = False,
    root: Path | None = None,
) -> int:
    base = repo_root(root)
    doc = load_document(base)
    item = _find_item(doc, item_id)
    target_status = _normalize_status(status)
    if target_status == "ARCHIVED / NOT TAKEN" and not reason:
        raise ValueError("archive move requires a reason")
    item.status = target_status
    item.updated = _now_date()
    if validation:
        item.validation_required = validation.strip()
    if review:
        item.review_required = review.strip()
    if reason:
        item.notes = reason.strip() if item.notes in {EMPTY_VALUE, ""} else f"{item.notes}; {reason.strip()}"
    write_result = _write_document(base, doc, dry_run=dry_run)
    payload = {
        "ok": True,
        "action": "move",
        "item": item.to_dict(),
        "write_result": write_result,
        "summary": f"Moved {item.id} to {target_status}.",
    }
    print_output(payload, json_mode)
    return 0


def done_item(*, item_id: str, validation: str | None = None, review: str | None = None, dry_run: bool = False, json_mode: bool = False, root: Path | None = None) -> int:
    validation_value = validation.strip() if validation else "missing evidence"
    review_value = review.strip() if review else "missing evidence"
    return move_item(
        item_id=item_id,
        status="DONE",
        validation=validation_value,
        review=review_value,
        dry_run=dry_run,
        json_mode=json_mode,
        root=root,
    )


def archive_item(*, item_id: str, reason: str, dry_run: bool = False, json_mode: bool = False, root: Path | None = None) -> int:
    return move_item(
        item_id=item_id,
        status="ARCHIVED / NOT TAKEN",
        reason=reason,
        dry_run=dry_run,
        json_mode=json_mode,
        root=root,
    )


def _parse_date(value: str) -> datetime | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except Exception:  # noqa: BLE001
        return None


def report(json_mode: bool = False, root: Path | None = None) -> int:
    base = repo_root(root)
    doc = load_document(base)
    counts_by_status = {status: 0 for status in STATUS_ORDER}
    counts_by_priority = {priority: 0 for priority in sorted(ALLOWED_PRIORITIES)}
    old_open_items: list[dict[str, str]] = []
    p0_p1_open: list[dict[str, str]] = []
    arch_items: list[dict[str, str]] = []
    missing_done_evidence: list[dict[str, str]] = []
    prod_error_items: list[dict[str, str]] = []
    now = datetime.now()
    for item in doc.items:
        counts_by_status[item.status] += 1
        counts_by_priority[item.priority] = counts_by_priority.get(item.priority, 0) + 1
        if item.status in {"TODO", "DOING"} and item.priority in {"P0", "P1"}:
            p0_p1_open.append(item.to_dict())
        if item.architecture_impact != "none":
            arch_items.append(item.to_dict())
        if item.status == "DONE" and (item.validation_required in {EMPTY_VALUE, "", "missing evidence"} or item.review_required in {EMPTY_VALUE, "", "missing evidence"}):
            missing_done_evidence.append(item.to_dict())
        if item.source == "prod-error" or item.type == "prod-error":
            prod_error_items.append(item.to_dict())
        created_dt = _parse_date(item.created)
        if created_dt and item.status in {"TODO", "DOING"} and (now - created_dt).days >= 30:
            old_open_items.append(item.to_dict())

    if p0_p1_open:
        next_focus = "Resolve or explicitly triage open P0/P1 items first."
    elif any(counts_by_status[status] for status in ["DOING"]):
        next_focus = "Finish DOING items and attach validation/review evidence before starting more work."
    elif arch_items:
        next_focus = "Review backlog items with architecture impact and sync project memory docs."
    else:
        next_focus = "Pull the highest-priority TODO item into DOING with a validation plan."

    payload = {
        "ok": True,
        "counts_by_status": counts_by_status,
        "counts_by_priority": counts_by_priority,
        "old_open_items": old_open_items,
        "p0_p1_open_items": p0_p1_open,
        "architecture_impact_items": arch_items,
        "done_missing_evidence": missing_done_evidence,
        "prod_error_items": prod_error_items,
        "recommended_next_focus": next_focus,
    }
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Backlog counts by status: {counts_by_status}")
        print(f"Backlog counts by priority: {counts_by_priority}")
        print(f"Recommended next focus: {next_focus}")
        if p0_p1_open:
            print("Open P0/P1 items:")
            for item in p0_p1_open:
                print(f"- {item['id']} {item['title']}")
    return 0
