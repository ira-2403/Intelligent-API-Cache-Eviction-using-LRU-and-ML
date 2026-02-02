import csv
import os
from datetime import datetime
LOG_FILE="backend/data/request_logs.csv"
def log_request(url,cache_status,response_time_ms,data_size,method="GET"):
    file_exists=os.path.isfile(LOG_FILE)
    with open(LOG_FILE,mode="a",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp",
                "url",
                "method",
                "cache_status",
                "response_time_ms",
                "data_size"
            ])
        writer.writerow([
            datetime.now().isoformat(),
            url,
            method,
            cache_status,
            response_time_ms,
            data_size
        ])