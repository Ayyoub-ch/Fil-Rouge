from pathlib import Path
import subprocess
import sys


def main():
    dossier = Path(__file__).resolve().parent
    scripts = (
        "projet_meteo.py",
        "projet_meteo2.py",
        "projet_meteo3.py",
    )

    for nom_script in scripts:
        script = dossier / nom_script
        subprocess.run([sys.executable, str(script)], cwd=dossier, check=True)


if __name__ == "__main__":
    main()