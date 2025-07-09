from datetime import datetime

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("✅ Auto Deployment Successful!")
    print(f"Timestamp: {now}")
    print("This is from Jenkins → EC2 pipeline 🚀")

if __name__ == "__main__":
    main()
