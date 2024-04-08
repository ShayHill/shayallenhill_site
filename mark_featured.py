"""Mark the [1st, 6th, 7th, 8th, 9th, 10th] posts as featured.

:author: Shay Hill
:created: 2024-04-08
"""

from pathlib import Path

POST_DIR = Path(__file__, "..", "_posts").resolve()

POSTS = list(POST_DIR.iterdir())


def _find_category_line(lines: list[str]) -> tuple[int, str]:
    for i, line in enumerate(lines):
        if line.startswith('categories:'):
            return i, line
    msg = "No categories line found in post."
    raise ValueError(msg)

def _read_post(post: Path) -> list:
    with open(post, "r", encoding="utf-8") as f:
        return f.readlines()

def _write_post(post: Path, lines: list):
    with open(post, "w", encoding="utf-8") as f:
        f.writelines(lines)


def _group_by_category():
    cat2posts: dict[str, list[Path]] = {}
    for post in POSTS:
        lines = _read_post(post)
        _, line = _find_category_line(lines)
        cat_list = line.split(': ')[1].strip()[1:-1]
        categories = {x.strip() for x in cat_list.split(',')}
        for cat in categories:
            if cat not in cat2posts:
                cat2posts[cat] = []
            cat2posts[cat].append(post)
    return cat2posts

def _unmark_featured():
    for post in POSTS:
        lines = _read_post(post)
        for i, line in enumerate(lines):
            if line.startswith('categories:'):
                lines[i] = line.replace(', featured', '')
                _write_post(post, lines)
                break

def _mark_featured():
    cat2posts = _group_by_category()
    seen = set(POSTS[-5:])
    posts_to_mark = [POSTS[-1]]
    for cat, posts in cat2posts.items():
        try:
            post = next(p for p in reversed(posts) if p not in seen)
        except StopIteration:
            continue
        posts_to_mark.append(post)
        seen.add(post)
    for post in posts_to_mark:
        lines = _read_post(post)
        i_cat, l_cat = _find_category_line(lines)
        lines[i_cat] = lines[i_cat].replace(']' , ', featured]')
        _write_post(post, lines)

_unmark_featured()
_mark_featured()







