"""Build a Minecraft 1.21.1 NeoForge mod against a supplied Java classpath."""

import argparse
import os
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile


def build(root, output, javac, classpath):
    with TemporaryDirectory() as folder:
        classes = Path(folder)
        java = sorted((root / "src/main/java").rglob("*.java"))
        if java:
            subprocess.run(
                [
                    str(javac), "-encoding", "UTF-8", "-nowarn", "-proc:none",
                    "-classpath", os.pathsep.join(map(str, classpath)), "-d", folder,
                    *map(str, java),
                ],
                check=True,
            )
        with ZipFile(output, "x", ZIP_DEFLATED) as jar:
            for source in (classes, root / "src/main/resources"):
                for file in sorted(source.rglob("*")):
                    if file.is_file():
                        jar.write(file, file.relative_to(source).as_posix())
            jar.write(root / "LICENSE", "META-INF/LICENSE.txt")
            for notice in sorted((root / "licenses").glob("*.txt")):
                jar.write(notice, f"META-INF/{notice.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--classpath-file", type=Path, required=True)
    parser.add_argument("--javac", default="javac")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    paths = [
        Path(line.strip()).resolve(strict=True)
        for line in args.classpath_file.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]
    build(Path(__file__).resolve().parent, args.output, args.javac, paths)
