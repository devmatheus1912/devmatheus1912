"""Build the profile activity SVGs from the live GitHub API.

Run from this repo:  python assets/build_activity.py
Requires the GitHub CLI (`gh`) authenticated as devmatheus1912.
"""

from __future__ import annotations

import json
import subprocess
import xml.sax.saxutils as xml
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

QUERY = """
query {
  viewer {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date contributionCount }
        }
      }
    }
    repositories(first: 20, ownerAffiliations: OWNER) {
      nodes {
        name
        languages(first: 12, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "dark": {
        "fg": "#E6EDF3",
        "muted": "#8B949E",
        "faint": "#6E7681",
        "empty": "#161B22",
        "track": "#21262D",
        "rule": "#21262D",
        "levels": ["#161B22", "#0E4429", "#006D32", "#26A641", "#39D353"],
        "other": "#6E7681",
    },
    "light": {
        "fg": "#1F2328",
        "muted": "#656D76",
        "faint": "#818B98",
        "empty": "#EBEDF0",
        "track": "#EAEEF2",
        "rule": "#D8DEE4",
        "levels": ["#EBEDF0", "#9BE9A8", "#40C463", "#30A14E", "#216E39"],
        "other": "#8C959F",
    },
}


def gh_json() -> dict:
    proc = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(proc.stdout)["data"]["viewer"]


def streaks(days: list[tuple[date, int]]) -> tuple[int, int]:
    longest = run = 0
    for _, count in days:
        if count > 0:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    current = 0
    for _, count in reversed(days):
        if count > 0:
            current += 1
        else:
            break
    return current, longest


def level_for(count: int, peak: int) -> int:
    if count <= 0 or peak <= 0:
        return 0
    quarter = peak / 4
    if count <= quarter:
        return 1
    if count <= quarter * 2:
        return 2
    if count <= quarter * 3:
        return 3
    return 4


def language_rows(repos: list[dict]) -> list[dict]:
    sizes: dict[str, int] = {}
    colors: dict[str, str] = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            sizes[name] = sizes.get(name, 0) + edge["size"]
            colors[name] = edge["node"]["color"] or "#8B949E"
    ranked = sorted(sizes.items(), key=lambda item: item[1], reverse=True)
    total = sum(sizes.values()) or 1
    top = ranked[:3]
    other = total - sum(size for _, size in top)
    parts = [size for _, size in top] + ([other] if other else [])
    names = [name for name, _ in top] + (["Other"] if other else [])
    bar_colors = [colors[name] for name, _ in top] + (["other"] if other else [])
    pct = share(parts)
    rows = []
    for name, color, percent, size in zip(names, bar_colors, pct, parts):
        rows.append(
            {
                "name": name,
                "color": color,
                "percent": percent,
                "bytes": size,
            }
        )
    return rows


def share(parts: list[int], digits: int = 1) -> list[float]:
    scale = 10**digits
    total = sum(parts) or 1
    raw = [part * 100 * scale / total for part in parts]
    floors = [int(value) for value in raw]
    leftover = 100 * scale - sum(floors)
    order = sorted(range(len(parts)), key=lambda i: raw[i] - floors[i], reverse=True)
    for index in order[:leftover]:
        floors[index] += 1
    return [value / scale for value in floors]


def fmt_int(value: int) -> str:
    return f"{value:,}"


def fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def fmt_day(value: date) -> str:
    return f"{value.day} {value.strftime('%b')} {value.year}"


def esc(value: str) -> str:
    return xml.escape(value)


def text(
    x: float,
    y: float,
    content: str,
    size: int,
    fill: str,
    weight: int = 400,
    anchor: str = "start",
    spacing: float = 0,
    tabular: bool = False,
) -> str:
    style = ' font-variant-numeric="tabular-nums"' if tabular else ""
    tracking = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-family="{FONT}" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
        f'dominant-baseline="hanging"{tracking}{style}>{esc(content)}</text>'
    )


def build_svg(theme_name: str, stats: dict) -> str:
    theme = THEMES[theme_name]
    cell = 11
    gap = 3
    step = cell + gap
    label_w = 28
    weeks = stats["weeks"]
    grid_w = label_w + len(weeks) * step - gap
    width = grid_w

    parts: list[str] = []
    y = 0

    parts.append(
        text(0, y, "LAST 12 MONTHS", 11, theme["faint"], 600, spacing=1.4)
    )
    parts.append(
        text(
            width,
            y,
            f"UPDATED {stats['updated']}",
            11,
            theme["faint"],
            600,
            anchor="end",
            spacing=1.4,
        )
    )
    y = 28
    parts.append(text(0, y, fmt_int(stats["total"]), 54, theme["fg"], 600, tabular=True))
    y = 92
    parts.append(
        text(0, y, "contributions in the last year", 16, theme["muted"], 400)
    )

    y = 132
    metrics = [
        (fmt_int(stats["current"]), "day streak"),
        (fmt_int(stats["longest"]), "longest streak"),
        (fmt_int(stats["active"]), "active days"),
    ]
    x = 0
    for index, (number, label) in enumerate(metrics):
        parts.append(text(x, y, number, 22, theme["fg"], 600, tabular=True))
        parts.append(text(x, y + 28, label, 13, theme["muted"]))
        x += 168
        if index < len(metrics) - 1:
            parts.append(
                f'<rect x="{x - 28}" y="{y + 4}" width="1" height="36" fill="{theme["rule"]}"/>'
            )

    y = 196
    parts.append(text(0, y, "CONTRIBUTIONS", 11, theme["faint"], 600, spacing=1.4))

    # Label a month on the week that contains its 1st.
    # Drop a label that would collide with the next one (partial first month).
    month_y = y + 22
    candidates: list[tuple[int, str]] = []
    first_day = weeks[0][0][0]
    candidates.append((0, first_day.strftime("%b")))
    for index, week in enumerate(weeks):
        for day, _count in week:
            if day.day == 1:
                candidates.append((index, day.strftime("%b")))
                break
    for index, (col, name) in enumerate(candidates):
        nxt = candidates[index + 1][0] if index + 1 < len(candidates) else 99
        if nxt - col < 3:
            continue
        parts.append(text(label_w + col * step, month_y, name, 11, theme["muted"]))

    grid_y = month_y + 18
    for row, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        parts.append(text(0, grid_y + row * step + 1, name, 10, theme["faint"]))

    for index, week in enumerate(weeks):
        for row, (_day, count) in enumerate(week):
            color = theme["levels"][level_for(count, stats["peak_count"])]
            parts.append(
                f'<rect x="{label_w + index * step}" y="{grid_y + row * step}" '
                f'width="{cell}" height="{cell}" rx="2" fill="{color}"/>'
            )

    legend_y = grid_y + 7 * step + 8
    legend = "Less"
    parts.append(text(label_w, legend_y, legend, 11, theme["faint"]))
    lx = label_w + 32
    for color in theme["levels"]:
        parts.append(
            f'<rect x="{lx}" y="{legend_y}" width="11" height="11" rx="2" fill="{color}"/>'
        )
        lx += 15
    parts.append(text(lx + 4, legend_y, "More", 11, theme["faint"]))
    peak = f"Peak  ·  {fmt_day(stats['peak_day'])}  ·  {fmt_int(stats['peak_count'])}"
    parts.append(text(width, legend_y, peak, 11, theme["muted"], anchor="end", tabular=True))

    lang_y = legend_y + 36
    parts.append(text(0, lang_y, "LANGUAGES", 11, theme["faint"], 600, spacing=1.4))
    parts.append(
        text(width, lang_y, "BY SIZE", 11, theme["faint"], 600, anchor="end", spacing=1.4)
    )

    row_y = lang_y + 24
    name_w = 108
    pct_w = 52
    bar_x = name_w
    bar_w = width - name_w - pct_w
    for row in stats["languages"]:
        color = theme["other"] if row["color"] == "other" else row["color"]
        parts.append(text(0, row_y, row["name"], 14, theme["fg"], 500))
        parts.append(
            f'<rect x="{bar_x}" y="{row_y + 4}" width="{bar_w}" height="7" rx="3.5" fill="{theme["track"]}"/>'
        )
        fill_w = max(7, round(bar_w * row["percent"] / 100))
        parts.append(
            f'<rect x="{bar_x}" y="{row_y + 4}" width="{fill_w}" height="7" rx="3.5" fill="{color}"/>'
        )
        parts.append(
            text(width, row_y, fmt_pct(row["percent"]), 14, theme["muted"], anchor="end", tabular=True)
        )
        row_y += 28

    foot_y = row_y + 6
    parts.append(
        text(
            0,
            foot_y,
            "Private contributions included.",
            12,
            theme["faint"],
        )
    )
    height = foot_y + 18

    body = "\n  ".join(parts)
    title = (
        f"{fmt_int(stats['total'])} contributions in the last year. "
        f"Current streak {stats['current']} days. "
        + ", ".join(f"{row['name']} {fmt_pct(row['percent'])}" for row in stats["languages"])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
  <title>{esc(title)}</title>
  {body}
</svg>
'''


def main() -> None:
    viewer = gh_json()
    calendar = viewer["contributionsCollection"]["contributionCalendar"]
    weeks_raw = calendar["weeks"]
    days: list[tuple[date, int]] = []
    weeks: list[list[tuple[date, int]]] = []
    for week in weeks_raw:
        column = []
        for item in week["contributionDays"]:
            day = date.fromisoformat(item["date"])
            count = int(item["contributionCount"])
            column.append((day, count))
            days.append((day, count))
        weeks.append(column)

    current, longest = streaks(days)
    active = sum(1 for _, count in days if count > 0)
    peak_day, peak_count = max(days, key=lambda item: item[1])
    updated = datetime.now().strftime("%d %b %Y").upper()
    languages = language_rows(viewer["repositories"]["nodes"])

    stats = {
        "total": int(calendar["totalContributions"]),
        "current": current,
        "longest": longest,
        "active": active,
        "peak_day": peak_day,
        "peak_count": peak_count,
        "updated": updated,
        "weeks": weeks,
        "languages": languages,
    }
    OUT.mkdir(exist_ok=True)
    for name in THEMES:
        path = OUT / f"activity-{name}.svg"
        path.write_text(build_svg(name, stats), encoding="utf-8")
        print(f"wrote {path.name}")

    print(f"total {stats['total']}")
    print(f"streak {current} longest {longest} active {active}")
    print(f"peak {peak_day.isoformat()} {peak_count}")
    for row in languages:
        print(f"{row['name']} {row['percent']} {row['bytes']}")


if __name__ == "__main__":
    main()
