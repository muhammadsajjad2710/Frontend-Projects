from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_thirty_projects_exist():
    folders = [path for path in ROOT.iterdir() if path.is_dir() and (path / "index.html").exists()]
    assert len(folders) == 30

def test_each_index_has_title_and_framework():
    for path in ROOT.iterdir():
        index = path / "index.html"
        if not index.exists():
            continue
        text = index.read_text(encoding="utf-8")
        assert "<title>" in text
        assert 'name="generator"' in text
        assert (path / "styles.css").exists()
