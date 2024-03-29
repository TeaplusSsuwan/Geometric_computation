#---------------------------------------------------------------------------#

def luas_segitiga():
  """
  คำนวณพื้นที่ของรูปสามเหลี่ยม
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    alas = float(input("  ป้อนความยาวฐานของรูปสามเหลี่ยม: "))
    tinggi = float(input("  ป้อนความสูงของรูปสามเหลี่ยม: "))

    # คำนวณพื้นที่
    area = (alas * tinggi) / 2

    # แสดงผลลัพธ์
    print("  พื้นที่ของรูปสามเหลี่ยม =", area )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break


def luas_persegi():
  """
  คำนวณพื้นที่ของรูปสี่เหลี่ยมจัตุรัส
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    sisi = float(input("  ป้อนความยาวด้านของรูปสี่เหลี่ยมจัตุรัส: "))

    # คำนวณพื้นที่
    area = sisi ** 2

    # แสดงผลลัพธ์
    print("  พื้นที่ของรูปสี่เหลี่ยมจัตุรัส =", area )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break
 

def luas_persegipanjang():
  """
  คำนวณพื้นที่ของรูปสี่เหลี่ยมผืนผ้า
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    panjang = float(input("  ป้อนความยาวของรูปสี่เหลี่ยมผืนผ้า: "))
    lebar = float(input("  ป้อนความกว้างของรูปสี่เหลี่ยมผืนผ้า: "))
    
    # คำนวณพื้นที่
    area = panjang*lebar

    # แสดงผลลัพธ์
    print("  พื้นที่ของรูปสี่เหลี่ยมผืนผ้า =", area )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break


def luas_lingkaran():
  """
  คำนวณพื้นที่ของรูปวงกลม
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    jarijari = float(input("  ป้อนรัศมีของรูปวงกลม: "))

    # คำนวณพื้นที่
    area = 3.14159 * jarijari ** 2

    # แสดงผลลัพธ์
    print("  พื้นที่ของรูปวงกลม =",area )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break


def luas_trapesium():
  """
  คำนวณพื้นที่ของรูปสี่เหลี่ยมคางหมู
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    alas1 = float(input("  ป้อนความยาวฐานล่างของรูปสี่เหลี่ยมคางหมู: "))
    alas2 = float(input("  ป้อนความยาวฐานบนของรูปสี่เหลี่ยมคางหมู: "))
    tinggi = float(input("  ป้อนความสูงของรูปสี่เหลี่ยมคางหมู: "))

    # คำนวณพื้นที่
    area = ((alas1 + alas2) * tinggi) / 2

    # แสดงผลลัพธ์
    print("  พื้นที่ของรูปสี่เหลี่ยมคางหมู =",area )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break
  

def volume_kubus():
  """
  คำนวณปริมาตรของรูปลูกบาศก์
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    sisi = float(input("  ป้อนความยาวด้านของรูปลูกบาศก์: "))
    
    # คำนวณปริมาตร
    volume =sisi ** 3

    # แสดงผลลัพธ์
    print("  ปริมาตรของรูปลูกบาศก์ =",volume )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break
  

def volume_balok():
  """
  คำนวณปริมาตรของรูปทรงสี่เหลี่ยมผืนผ้า
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    panjang = float(input("  ป้อนความยาวของรูปทรงสี่เหลี่ยมผืนผ้า: "))
    lebar = float(input("  ป้อนความกว้างของรูปทรงสี่เหลี่ยมผืนผ้า: "))
    tinggi = float(input("  ป้อนความสูงของรูปทรงสี่เหลี่ยมผืนผ้า: "))

    # คำนวณปริมาตร
    volume = panjang * lebar * tinggi

    # แสดงผลลัพธ์
    print("  ปริมาตรของรูปทรงสี่เหลี่ยมผืนผ้า =",volume )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break


def volume_bola():
  """
  คำนวณปริมาตรของรูปทรงกลม
  """  
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    jarijari = float(input("  ป้อนรัศมีของรูปทรงกลม: "))

    # คำนวณปริมาตร
    volume = (4/3) * 3.14159 * jarijari ** 3

    # แสดงผลลัพธ์
    print("  ปริมาตรของรูปทรงกลม =",volume )
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break


def volume_ellipsoid():
  """
  คำนวณปริมาตรของทรงวงรี
  """
  while True:

    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    asize = float(input("ป้อนความยาวแกนกึ่งเอก: "))
    bsize = float(input("ป้อนความยาวแกนกึ่งโท: "))
    csize = float(input("ป้อนความยาวแกนกึ่งสูง: "))

    # คำนวณปริมาตรของ
    volume = (4/3) * 3.14159 * asize * bsize * csize

    # แสดงผลลัพธ์
    print("ปริมาตรของทรงวงรี =", volume)
    print('-'*30)

      # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break


def volume_kerucut():
  """
  คำนวณปริมาตรของรูปทรงกรวย
  """
  while True:
    
    # รับค่าพารามิเตอร์จากผู้ใช้ภายในฟังก์ชัน
    jarijari = float(input("ป้อนรัศมีของรูปทรงกรวย: "))
    tinggi = float(input("ป้อนความสูงของรูปทรงกรวย: "))

    # คำนวณปริมาตร
    volume = (1/3) * 3.14159 * jarijari ** 2 * tinggi

    # แสดงผลลัพธ์
    print("ปริมาตรของรูปทรงกรวย =", volume)
    print('-'*30)

    # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการคำนวณอีกครั้งหรือไม่ (y/n): ")
    if choice.lower() == "n":
      break
    elif choice.lower() == "y":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")
      break

#---------------------------------------------------------------------------#

def main():
  while True:
    print('-'*30)
    print("โปรแกรมคำนวณทางเรขาคณิต")
    print('-'*30)
    # รับค่าพารามิเตอร์จากผู้ใช้เพื่อเลือกประเภทการคำนวณ
    type = input("เลือกประเภทการคำนวณ \n     1 : การคำนวณพื้นที่ของรูปเราขาคณิต \n     2 : การคำนวณหาปริมาตรของรูปเราขาคณิต \n"+ ("-"*20) +"\n  กรอกหมายเลขของประเภทการคำนวณ : ")
    print('-'*30)
    if type == "1":
      # รับค่าพารามิเตอร์จากผู้ใช้เพื่อเลือกประเภทของรูปทรง
      print('  ชุดโปรแกรมคำนวณพื้นที่')
      bentuk = input("  เลือกประเภทของรูปทรง \n     1 : สามเหลี่ยม \n     2 : สี่เหลี่ยมจัตุรัส \n     3 : สี่เหลี่ยมผืนผ้า \n     4 : วงกลม \n     5 : สี่เหลี่ยมคางหมู \n"+ ("-"*20) +"\n  กรอกหมายเลขของประเภทรูปทรง : ")
      print('-'*30)
      if bentuk == "1":
        luas_segitiga()
      elif bentuk == "2":
        luas_persegi()
      elif bentuk == "3":
        luas_persegipanjang()
      elif bentuk == "4":
        luas_lingkaran()
      elif bentuk == "5":
        luas_trapesium()
      else:
        print("  รูปแบบไม่ถูกต้อง")
    elif type == "2":
      # รับค่าพารามิเตอร์จากผู้ใช้เพื่อเลือกประเภทของรูปทรง
      print('  ชุดโปรแกรมคำนวณปริมาตร')
      bentuk = input("  เลือกประเภทของรูปทรง \n     6 : ลูกบาศก์ \n     7 : บาล์ก \n     8 : ทรงกลม\n     9 : ทรงรี\n     10 : ทรงกรวย\n"+ ("-"*20) +"\n  กรอกหมายเลขของประเภทรูปทรง : ")
      print('-'*30)
      if bentuk == "6":
        volume_kubus()
      elif bentuk == "7":
        volume_balok()
      elif bentuk == "8":
        volume_bola()
      elif bentuk == "9":
        volume_ellipsoid()
      elif bentuk == "10":
        volume_kerucut()
      else:
        print("  รูปแบบไม่ถูกต้อง")
    else:
      print("  รูปแบบไม่ถูกต้อง")

    # ตรวจสอบว่าผู้ใช้ต้องการออกหรือไม่
    choice = input("ต้องการออกหรือไม่ (y/n): ")
    if choice.lower() == "y":
      break
    elif choice.lower() == "n":
      continue
    else:
      print("ตัวเลือกไม่ถูกต้อง")

  print("--- โปรแกรมเสร็จสิ้นการทำงาน ---")
  print('-'*30)
if __name__ == "__main__":
  main()

  #---------------------------------------------------------------------------#