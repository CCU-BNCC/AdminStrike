import requests

def banner():
    print("\n🔍 Admin Panel Finder by MD ABDULLAH\n")

def load_paths():
    return [
        "admin/", "admin.php", "admin/login.php", "administrator/", "admin1.php", "cpanel/",
        "adminpanel/", "login.php", "admin_area/", "admin/login/", "panel/", "user/login.php",
        "admin123/", "backend/", "admin/login.html", "adminarea/"
    ]

def scan(target):
    if not target.startswith("http"):
        target = "http://" + target

    print(f"\n🎯 Scanning: {target}\n")

    paths = load_paths()
    headers = {'User-Agent': 'AdminStrike/1.0'}

    for path in paths:
        url = f"{target}/{path}"
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code == 200:
                print(f"✅ Found: {url}")
            elif res.status_code == 403:
                print(f"⚠️ Forbidden: {url}")
        except:
            pass

def main():
    banner()
    target = input("🌐 Enter target website (e.g. example.com): ").strip()
    scan(target)

if __name__ == "__main__":
    main()
