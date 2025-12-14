from db_helper import get_conn
from auth import register_user, login_user
from migrate_users_txt import migrate_users
from insert_using_pandas import migrate_csv_to_db
from pathlib import Path

def main():
    print("\n=== Running Automated Test Runner ===")

    # migrate users.txt -> SQLite
    try:
        migrate_users()
        print("Users migrated ✔")
    except Exception as e:
        print("Migration skipped:", e)

    # register a demo user
    register_user("demo_user", "DemoPass123!")
    print("Login test:", login_user("demo_user", "DemoPass123!"))

    # migrate CSV file if exists
    csv_file = Path.cwd() / "Data" / "cyber_incidents.csv"
    if csv_file.exists():
        migrate_csv_to_db(csv_file)
        print("CSV migrated ✔")
    else:
        print("CSV file NOT FOUND ❌")

    # show record counts
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        print("Users count:", cur.fetchone()[0])
        cur.execute("SELECT COUNT(*) FROM cyber_incidents")
        print("Incidents count:", cur.fetchone()[0])

if __name__ == "__main__":
    main()

