import requests
import json

print("\n==================================================")
print("1. Konsep API, Monolitik, dan Headless")
print("==================================================\n")

print("• Monolitik = Backend + Frontend bersatu.")
print("  Contoh: Django membuat HTML langsung.\n")
print("• Headless / Decoupled = Backend dan Frontend terpisah.")
print("  - Backend: menyediakan data lewat API (JSON)")
print("  - Frontend: mengambil data dari API lalu menampilkan\n")

print("• API = perantara (seperti pelayan restoran)")
print("  - Frontend = pelanggan")
print("  - Backend = dapur")
print("  - API = pelayan yang menerima request & membawa response (JSON)\n")


print("\n==================================================")
print("2. Contoh JSON")
print("==================================================\n")

contoh_json = {
    "nik": "3501234567890001",
    "nama_lengkap": "Budi Santoso",
    "alamat": "Jl. Merdeka 10",
    "no_telepon": "081234567890"
}

print("Data JSON Warga:")
print(json.dumps(contoh_json, indent=2))


print("\n==================================================")
print("3. GET: Mengambil Daftar Pengguna (ReqRes API)")
print("==================================================\n")

res = requests.get("https://reqres.in/api/users?page=2")
print("Status Code:", res.status_code)
print("Response JSON:")
print(json.dumps(res.json(), indent=2))


print("\n==================================================")
print("4. GET: Mengambil Satu Pengguna")
print("==================================================\n")

res = requests.get("https://reqres.in/api/users/2")
print("Status Code:", res.status_code)
print("Response JSON:")
print(json.dumps(res.json(), indent=2))


print("\n==================================================")
print("5. POST: Membuat Pengguna Baru")
print("==================================================\n")

res = requests.post("https://reqres.in/api/users", json={"name": "budi", "job": "leader"})
print("Status Code:", res.status_code)
print("Response JSON:")
print(json.dumps(res.json(), indent=2))


print("\n==================================================")
print("6. GET: User Tidak Ditemukan (404)")
print("==================================================\n")

res = requests.get("https://reqres.in/api/users/23")
print("Status Code:", res.status_code)
print("Response JSON:")
print(json.dumps(res.json(), indent=2))
