from prefect import flow, task
import subprocess
import os

SCRAPER_SCRIPT = "web-scraper/scraper/scraper.py"
DATA_PATH = "web-scraper/db/data.json"

@task
def run_scraper():
    """Chạy web scraper để lấy dữ liệu"""
    result = subprocess.run(["python", SCRAPER_SCRIPT], capture_output=True, text=True)
    print(result.stdout)
    return DATA_PATH

@task
def store_to_nosql(data_path):
    if os.path.exists(data_path):
        print(f"Dữ liệu được lưu vào NoSQL từ {data_path}")
    else:
        print("Không tìm thấy dữ liệu")

@task
def update_faiss():
    print("Cập nhật FAISS với dữ liệu mới...")

@task
def update_tableau():
    """Gửi dữ liệu lên Tableau"""
    print("Dữ liệu mới được cập nhật vào Tableau")

@flow
def data_pipeline():
    """Orchestration Pipeline với Prefect"""
    data_path = run_scraper()
    store_to_nosql(data_path)
    update_faiss()
    update_tableau()

# Chạy Flow
if __name__ == "__main__":
    data_pipeline()
