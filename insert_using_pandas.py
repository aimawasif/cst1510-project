# insert_using_pandas.py
import pandas as pd
from pathlib import Path
from db_helper import get_conn
import datetime

DATA_DIR = Path.cwd() / "Data"   # change to "DATA" if your folder is uppercase
csv_path = DATA_DIR / "cyber_incidents.csv"

def migrate_csv_to_db(csv_path):
    if not csv_path.exists():
        print("CSV not found:", csv_path)
        return
    df = pd.read_csv(csv_path)
    print("CSV columns:", df.columns.tolist())
    # Basic cleaning / mapping - adjust to your CSV column names
    df = df.rename(columns={c: c.strip() for c in df.columns})
    rows = []
    for _, r in df.iterrows():
        title = r.get('title') or r.get('incident') or "No title"
        description = r.get('description') or r.get('details') or ""
        severity = None
        if 'severity' in r and pd.notna(r['severity']):
            try:
                severity = int(r['severity'])
            except:
                severity = None
        reported_by = r.get('reported_by') if 'reported_by' in r else None
        reported_at = r.get('reported_at') or datetime.datetime.utcnow().isoformat()
        rows.append((title, description, severity, reported_by, reported_at))

    with get_conn() as conn:
        cur = conn.cursor()
        cur.executemany(
            "INSERT INTO cyber_incidents (title,description,severity,reported_by,reported_at) VALUES (?,?,?,?,?)",
            rows
        )
        conn.commit()
    print(f"Inserted {len(rows)} rows into cyber_incidents.")

if __name__ == "__main__":
    migrate_csv_to_db(csv_path)
