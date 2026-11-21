# Voxy Biome Colors

Keeps Voxy's constant-color probe compatible with biome-aware color providers.

## Installation

Java 21, Minecraft 1.21.1, and NeoForge. Tested with 21.1.265. Download `voxy_biome_colors-1.0.1.jar` from Releases. Install the client mod with Roxy 0.4.2 and its specified Voxy build 0.2.16-beta. The fix provides a neutral color for Voxy's synthetic probe when no biome is supplied.

修复 Voxy 没有群系上下文时的色样探测，保留真实群系的草地、树叶和水体颜色。

## Build

Use JDK 21 and Python 3.11+. Create a text file with one absolute JAR path per line for the mapped Minecraft 1.21.1 and NeoForge 21.1.265 libraries.

```sh
python build.py --classpath-file classpath.txt --output voxy_biome_colors-1.0.1.jar
```

## License and feedback

MIT. Voxy and Roxy are separate projects. Obtain them from their official project pages.

Report issues here with reproduction steps and your Minecraft, NeoForge and mod versions.
