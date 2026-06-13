from llm_parser import generate_outline
from ppt_builder import build_ppt

def load_input(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    input_text = load_input("example_input.txt")

    print("生成PPT大纲中...")

    outline = generate_outline(input_text)

    print("生成PPT文件中...")

    output_file = build_ppt(outline)

    print(f"完成：{output_file}")
