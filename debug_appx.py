import requests, json, cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

# AES decrypt function
def decrypt(enc):
    try:
        enc = b64decode(enc.split(':')[0])
        key = '638udh3829162018'.encode('utf-8')
        iv = 'fedcba9876543210'.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(enc), AES.block_size)
        return plaintext.decode('utf-8')
    except Exception as e:
        print(f"[Decrypt Error] {e}")
        return ""

# Step 1: Login
def login(api_base, email, password):
    print("[Step 1] Trying login...")
    url = f"https://{api_base}/post/userLogin"
    headers = {"Auth-Key":"appxapi","User-Id":"-2"}
    data = {"email":email,"password":password}
    try:
        res = requests.post(url, data=data, headers=headers).json()
        print("[Login Response]", res)
        if res.get("status") == 200:
            return res["data"]["userid"], res["data"]["token"]
        else:
            print("[Login Failed] Status:", res.get("status"))
            return None, None
    except Exception as e:
        print("[Login Error]", e)
        return None, None

# Step 2: Fetch courses
def fetch_courses(api_base, userid, token):
    print("[Step 2] Fetching courses...")
    url = f"https://{api_base}/get/mycoursev2?userid={userid}"
    headers = {"Authorization":token,"Client-Service":"Appx","Auth-Key":"appxapi"}
    try:
        res = requests.get(url, headers=headers).json()
        print("[Courses Response]", res)
        return res.get("data", [])
    except Exception as e:
        print("[Courses Error]", e)
        return []

# Step 3: Fetch subjects/topics
def fetch_subjects(api_base, course_id, headers):
    print(f"[Step 3] Fetching subjects for course {course_id}...")
    url = f"https://{api_base}/get/allsubjectfrmlivecourseclass?courseid={course_id}&start=-1"
    res = requests.get(url, headers=headers).json()
    print("[Subjects Response]", res)
    return res.get("data", [])

# Step 4: Fetch videos
def fetch_videos(api_base, course_id, subject_id, headers):
    print(f"[Step 4] Fetching videos for subject {subject_id}...")
    url = f"https://{api_base}/get/alltopicfrmlivecourseclass?courseid={course_id}&subjectid={subject_id}&start=-1"
    res = requests.get(url, headers=headers).json()
    print("[Topics Response]", res)
    return res.get("data", [])

# Example run
if __name__ == "__main__":
    api = "api.appx.co.in"   # change to your API domain
    email = "yourid"
    password = "yourpass"

    userid, token = login(api, email, password)
    if userid and token:
        courses = fetch_courses(api, userid, token)
        if courses:
            headers = {"Authorization":token,"Client-Service":"Appx","Auth-Key":"appxapi"}
            for course in courses:
                cid = course["id"]
                subjects = fetch_subjects(api, cid, headers)
                for sub in subjects:
                    sid = sub["subjectid"]
                    topics = fetch_videos(api, cid, sid, headers)
                    # यहाँ पर हर topic का response print होगा
