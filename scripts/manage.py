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

if __name__ == "__main__":
    app()
