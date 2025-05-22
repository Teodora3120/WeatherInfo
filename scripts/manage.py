import subprocess
import typer

app = typer.Typer()

@app.command()
def run():
    subprocess.run(["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"])

@app.command()
def build():
    subprocess.run(["docker-compose", "build"])

@app.command()
def up():
    subprocess.run(["docker-compose", "up", "-d"])

@app.command()
def down():
    subprocess.run(["docker-compose", "down"])

@app.command()
def restart():
    subprocess.run(["docker-compose", "restart"])

@app.command()
def migrate():
    subprocess.run([
        "docker-compose", "exec", "weather_app",
        "alembic", "upgrade", "head"
    ])

@app.command()
def makemigrations(message: str = typer.Option(..., "--message", "-m", help="Migration message")):
    subprocess.run([
        "docker-compose", "exec", "weather_app",
        "alembic", "revision", "--autogenerate", "-m", message
    ])

if __name__ == "__main__":
    app()
