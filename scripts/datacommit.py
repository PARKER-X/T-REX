chunk_size = 50_000_000  # approx 50 MB per chunk
with open("/Users/Guest/Desktop/T-REX/data/raw/pretraining_hindi_english_normalized.txt", "r", encoding="utf-8") as f:
    chunk_num = 0
    while True:
        lines = f.readlines(chunk_size)
        if not lines:
            break
        with open(f"chunk_{chunk_num}.txt", "w", encoding="utf-8") as out:
            out.writelines(lines)
        chunk_num += 1
