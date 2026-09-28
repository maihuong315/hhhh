import streamlit as st
import pymysql
from pymysql.cursors import DictCursor
from datetime import datetime


st.set_page_config(
    page_title="TourMate - MySQL Test",
    page_icon="🧭",
    layout="wide"
)


# =========================================================
# MYSQL CONFIG
# =========================================================

MYSQL_CONFIG = {
    "host": "mysql-19728385-npmaihuong-927f.b.aivencloud.com",
    "port": 27942,
    "user": "avnadmin",

    # ĐIỀN PASSWORD AIVEN HIỆN TẠI CỦA EM Ở ĐÂY
    "password": "AVNS_zBDlzsF9I5fC-EdWcl0",

    "database": "defaultdb",
}


# =========================================================
# CONNECT MYSQL
# =========================================================

def get_conn():

    return pymysql.connect(
        host=MYSQL_CONFIG["host"],
        port=MYSQL_CONFIG["port"],
        user=MYSQL_CONFIG["user"],
        password=MYSQL_CONFIG["password"],
        database=MYSQL_CONFIG["database"],
        charset="utf8mb4",
        cursorclass=DictCursor,
        connect_timeout=20,
        read_timeout=20,
        write_timeout=20,
        autocommit=True
    )


# =========================================================
# TEST CONNECTION
# =========================================================

st.title("🧭 TourMate")

st.subheader("🔧 Kiểm tra kết nối Aiven MySQL")


st.write(
    "Host:",
    MYSQL_CONFIG["host"]
)

st.write(
    "Port:",
    MYSQL_CONFIG["port"]
)

st.write(
    "Database:",
    MYSQL_CONFIG["database"]
)

st.write(
    "User:",
    MYSQL_CONFIG["user"]
)


if st.button(
    "🔌 KIỂM TRA KẾT NỐI",
    type="primary",
    use_container_width=True
):

    try:

        conn = get_conn()

        with conn.cursor() as cursor:

            cursor.execute(
                "SELECT VERSION() AS version"
            )

            result = cursor.fetchone()


        conn.close()


        st.success(
            "🟢 KẾT NỐI MYSQL THÀNH CÔNG!"
        )


        st.write(
            "MySQL version:",
            result["version"]
        )


    except pymysql.err.OperationalError as e:

        st.error(
            "🔴 MYSQL KHÔNG KẾT NỐI ĐƯỢC"
        )

        st.code(
            str(e)
        )


    except Exception as e:

        st.error(
            "🔴 CÓ LỖI"
        )

        st.exception(e)
