from sqlalchemy import create_engine


def main():
    login = "root"
    password = "qwerty"
    host = "localhost"
    port = "33061"
    dbname = "company"

    engine = create_engine(
        f"mysql+pymysql://{login}:{password}@{host}:{port}/{dbname}"
    )
    sql = "SELECT * FROM company.archived_users;"

    with engine.connect() as conn:
        result = conn.execute(sql)
        for row in result:
            print(row)


if __name__ == "__main__":
    main()
