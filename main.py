import os

LINE = "I set my password to \"incorrect\" so every time I forget it, the computer gently tells me what it is."

OUT = "/output/entry.txt"

def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
