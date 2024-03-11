def luas_segitiga(alas, tinggi):
  """
  คำนวณพื้นที่ของรูปสามเหลี่ยม
  """
  return (alas * tinggi) / 2

def keliling_segitiga(sisi1, sisi2, sisi3):
  """
  คำนวณความยาวรอบรูปของรูปสามเหลี่ยม
  """
  return sisi1 + sisi2 + sisi3

def luas_persegi(sisi):
  """
  คำนวณพื้นที่ของรูปสี่เหลี่ยมจัตุรัส
  """
  return sisi ** 2

def keliling_persegi(sisi):
  """
  คำนวณความยาวรอบรูปของรูปสี่เหลี่ยมจัตุรัส
  """
  return 4 * sisi

def luas_persegipanjang(panjang, lebar):
  """
  คำนวณพื้นที่ของรูปสี่เหลี่ยมผืนผ้า
  """
  return panjang * lebar

def keliling_persegipanjang(panjang, lebar):
  """
  คำนวณความยาวรอบรูปของรูปสี่เหลี่ยมผืนผ้า
  """
  return 2 * (panjang + lebar)

def luas_lingkaran(jarijari):
  """
  คำนวณพื้นที่ของรูปวงกลม
  """
  return 3.14159 * jarijari ** 2

def keliling_lingkaran(jarijari):
  """
  คำนวณความยาวรอบรูปของรูปวงกลม
  """
  return 2 * 3.14159 * jarijari

def luas_trapesium(alas1, alas2, tinggi):
  """
  คำนวณพื้นที่ของรูปสี่เหลี่ยมคางหมู
  """
  return ((alas1 + alas2) * tinggi) / 2

def keliling_trapesium(sisi1, sisi2, alas1, alas2):
  """
  คำนวณความยาวรอบรูปของรูปสี่เหลี่ยมคางหมู
  """
  return sisi1 + sisi2 + alas1 + alas2

def volume_kubus(sisi):
  """
  คำนวณปริมาตรของรูปลูกบาศก์
  """
  return sisi ** 3

def volume_balok(panjang, lebar, tinggi):
  """
  คำนวณปริมาตรของรูปทรงสี่เหลี่ยมผืนผ้า
  """
  return panjang * lebar * tinggi

def volume_bola(jarijari):
  """
  คำนวณปริมาตรของรูปทรงกลม
  """
  return (4/3) * 3.14159 * jarijari ** 3

def main():
  # รับค่าพารามิเตอร์จากผู้ใช้
  bentuk = input("เลือกประเภทของรูปทรง (1. สามเหลี่ยม, 2. สี่เหลี่ยมจัตุรัส, 3. สี่เหลี่ยมผืนผ้า, 4. วงกลม, 5. สี่เหลี่ยมคางหมู, 6. ลูกบาศก์, 7. บาล์ก, 8. ทรงกลม): ")
  if bentuk == "1":
    alas = float(input("ป้อนความยาวฐานของรูปสามเหลี่ยม: "))
    tinggi = float(input("ป้อนความสูงของรูปสามเหลี่ยม: "))
    print("พื้นที่ของรูปสามเหลี่ยม =", luas_segitiga(alas, tinggi))
  elif bentuk == "2":
    sisi = float(input("ป้อนความยาวด้านของรูปสี่เหลี่ยมจัตุรัส: "))
    print("พื้นที่ของรูปสี่เหลี่ยมจัตุรัส =", luas_persegi(sisi))
  elif bentuk == "3":
    panjang = float(input("ป้อนความยาวของรูปสี่เหลี่ยมผืนผ้า: "))
    lebar = float(input("ป้อนความกว้างของรูปสี่เหลี่ยมผืนผ้า: "))
    print("พื้นที่ของรูปสี่เหลี่ยมผืนผ้า =", luas_persegipanjang(panjang, lebar))
  elif bentuk == "4":
    jarijari = float(input("ป้อนรัศมีของรูปวงกลม: "))
    print("พื้นที่ของรูปวงกลม =", luas_lingkaran(jarijari))
  elif bentuk == "5":
    alas1 = float(input("ป้อนความยาวฐานล่างของรูปสี่เหลี่ยมคางหมู: "))
    alas2 = float(input("ป้อนความยาวฐานบนของรูปสี่เหลี่ยมคางหมู: "))
    tinggi = float(input("ป้อนความสูงของรูปสี่เหลี่ยมคางหมู: "))
    print("พื้นที่ของรูปสี่เหลี่ยมคางหมู =", luas_trapesium(alas1, alas2, tinggi))
  elif bentuk == "6":
    sisi = float(input("ป้อนความยาวด้านของรูปลูกบาศก์: "))
    print("ปริมาตรของรูปลูกบาศก์ =", volume_kubus(sisi))
  elif bentuk == "7":
    panjang = float(input("ป้อนความยาวของรูปทรงสี่เหลี่ยมผืนผ้า: "))
    lebar = float(input("ป้อนความกว้างของรูปทรงสี่เหลี่ยมผืนผ้า: "))
    tinggi = float(input("ป้อนความสูงของรูปทรงสี่เหลี่ยมผืนผ้า: "))
    print("ปริมาตรของรูปทรงสี่เหลี่ยมผืนผ้า =", volume_balok(panjang, lebar, tinggi))
  elif bentuk == "8":
    jarijari = float(input("ป้อนรัศมีของรูปทรงกลม: "))
    print("ปริมาตรของรูปทรงกลม =", volume_bola(jarijari))
  else:
    print("รูปแบบไม่ถูกต้อง")

if __name__ == "__main__":
  main()