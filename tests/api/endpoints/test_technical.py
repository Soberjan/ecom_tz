from urllib.parse import urlencode

from tests.database.database_fixture import database, filled_db 
from tests.api.endpoints.client_fixture import client 

def test_technical(client):
    csv_content = (
        "full_name,subject,grade\n"
        "Вася,русский,5\n"
        "Петя,математика,4\n"
    )

    response = client.post(
        "/upload-grades",
        files={
            "file": (
                "grades.csv",
                csv_content,
                "text/csv",
            )
        },
    ).json()
    assert response['status'] == "ok"
