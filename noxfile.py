import platform
import os
import nox

os_platform = platform.system()

@nox.session
def postgres(session):
    """Запустить postgres."""

    # Директория для сохранения данных
    session.run(
        "mkdir",
        "-p",
        "-m",
        "777",
        "./.postgres_data",
        external=True,
    )
    # Убрать права: sudo chmod -R 777 ./.postgres_data

    # Запуск образа postgres
    session.run(
        "sudo",
        "docker",
        "run",
        "-d",
        "-p",
        "5431:5432",
        "-e",
        "POSTGRES_PASSWORD=pgpwd",
        "-e",
        "POSTGRES_DB=tstbase",
        "-e",
        "PGDATA=/var/lib/postgresql/data/pgdata",
        "-v",
        f"{os.path.abspath('./.postgres_data')}:/var/lib/postgresql/data",
        "-v",
        f"{os.path.abspath('./migrations')}:/docker-entrypoint-initdb.d",
        "postgres:17.0",
        external=True,
    )
    print("---------")
    print("Connect to postgres")
    print("base : tstbase")
    print("POSTGRES_PASSWORD : pgpwd")

