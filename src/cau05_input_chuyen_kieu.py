ma_may = input("Nhập mã máy: ")
cong_suat_w_text = input("Nhập công suất W: ")
so_phut_text = input("Nhập số phút sử dụng: ")
don_gia_text = input("Nhập đơn giá điện/kWh: ")

print(type(ma_may))
print(type(cong_suat_w_text))
print(type(so_phut_text))
print(type(don_gia_text))

cong_suat_w = float(cong_suat_w_text)
so_phut = int(so_phut_text)
don_gia_kwh = float(don_gia_text)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng:", dien_nang_kwh)
print("Chi phí:", chi_phi)