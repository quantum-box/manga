from pathlib import Path
import sys,time
src,dst=map(Path,sys.argv[1:3])
for attempt in range(30):
    try:
        data=src.read_bytes()
        if not data.startswith(b'\x89PNG\r\n\x1a\n') or not data.endswith(b'IEND\xaeB\x60\x82'):
            raise ValueError('Generated PNG is not fully saved yet')
        dst.parent.mkdir(parents=True,exist_ok=True)
        temp=dst.with_suffix('.copying')
        temp.write_bytes(data);temp.replace(dst)
        print(dst.name,len(data),'bytes')
        break
    except (OSError,ValueError):
        if attempt==29:raise
        time.sleep(0.25)
