# read_isam.py
import struct

DATA_PATH = r"C:\jsy.java\java-education-007\voyage_data.isam"
INDEX_PATH = r"C:\jsy.java\java-education-007\voyage_index.txt"

RECORD_SIZE = 32
STRUCT_FMT = "<i d d H d B B"  # little-endian

def load_index(path=INDEX_PATH):
    idx = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            date_iso, off = line.strip().split("\t")
            idx[date_iso] = int(off)
    return idx

def read_record_at_offset(offset, path=DATA_PATH):
    with open(path, "rb") as f:
        f.seek(offset)
        raw = f.read(RECORD_SIZE)
    date_yyyymmdd, lat, lon, leg_id, leg_prog, port_from, port_to = struct.unpack(STRUCT_FMT, raw)
    return {
        "date_yyyymmdd": date_yyyymmdd,
        "lat": lat,
        "lon": lon,
        "leg_id": leg_id,
        "leg_progress_km": leg_prog,
        "port_from_id": port_from,
        "port_to_id": port_to,
    }

def read_by_date(date_iso):
    idx = load_index()
    if date_iso not in idx:
        raise KeyError(f"Date {date_iso} not found in index")
    return read_record_at_offset(idx[date_iso])

def scan_all(limit=10):
    rows = []
    with open(DATA_PATH, "rb") as f:
        for _ in range(limit):
            raw = f.read(RECORD_SIZE)
            if not raw or len(raw) < RECORD_SIZE:
                break
            date_yyyymmdd, lat, lon, leg_id, leg_prog, port_from, port_to = struct.unpack(STRUCT_FMT, raw)
            rows.append((date_yyyymmdd, lat, lon, leg_id, leg_prog, port_from, port_to))
    return rows

if __name__ == "__main__":
    # 예: 특정 날짜 읽기
    rec = read_by_date("2025-10-01")
    print("Record @ 2025-10-01:", rec)

    # 예: 앞에서부터 5건 훑어보기
    print("\nFirst 5 records:")
    for r in scan_all(limit=5):
        print(r)
