# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(HERE, 'assets')
assets_opt_dir = os.path.join(HERE, 'assets_opt')

# Medical Certificate & Official Evidence Illustration
def create_leave_evidence_asset():
    w, h = 480, 640
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    # Document border
    draw.rectangle([0, 0, w-1, h-1], outline=(203, 213, 225), width=2)
    # Header hospital seal stamp
    draw.ellipse([w//2 - 36, 30, w//2 + 36, 102], outline=(36, 107, 253), width=3)
    draw.line([(w//2, 45), (w//2, 87)], fill=(36, 107, 253), width=6)
    draw.line([(w//2 - 21, 66), (w//2 + 21, 66)], fill=(36, 107, 253), width=6)

    # Hospital Title
    draw.text((w//2 - 110, 115), "โรงพยาบาลศูนย์การแพทย์มหาวิทยาลัย", fill=(15, 23, 42))
    draw.text((w//2 - 80, 138), "ใบรับรองแพทย์ตรวจรักษาทางการ", fill=(71, 85, 105))

    # Decorative separator
    draw.line([40, 165, w - 40, 165], fill=(226, 232, 240), width=2)

    # Patient info
    draw.text((50, 185), "ชื่อ-นามสกุลผู้ป่วย: นายธนพล กิจบำรุง", fill=(30, 41, 59))
    draw.text((50, 210), "รหัสนักศึกษา: 660510123 คณะศึกษาศาสตร์", fill=(71, 85, 105))
    draw.text((50, 235), "วันที่เข้ารับการตรวจ: 15 ตุลาคม 2569 เวลา 08:30 น.", fill=(71, 85, 105))

    # Diagnosis box
    draw.rounded_rectangle([45, 275, w - 45, 395], radius=8, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    draw.text((60, 290), "การวินิจฉัยโรคทางการแพทย์:", fill=(15, 23, 42))
    draw.text((60, 315), "ผู้ป่วยมีอาการไข้หวัดใหญ่เฉียบพลัน ปวดศีรษะและมีไข้สูง 38.6 C", fill=(220, 38, 38))
    draw.text((60, 340), "เห็นสมควรให้หยุดพักรักษาตัวและสังเกตอาการเป็นเวลา 2 วัน", fill=(30, 41, 59))
    draw.text((60, 365), "ตั้งแต่วันที่ 15 ตุลาคม ถึง 16 ตุลาคม 2569", fill=(30, 41, 59))

    # Official Doctor Signature & Stamp Area
    draw.ellipse([w - 170, 430, w - 70, 530], outline=(220, 38, 38), width=3)
    draw.text((w - 155, 470), "ตรวจรักษาแล้ว", fill=(220, 38, 38))
    draw.text((60, 470), "แพทย์ผู้ตรวจ: นพ. วีรวัฒน์ เกียรติขจร", fill=(30, 41, 59))
    draw.text((60, 495), "เลขที่ใบประกอบวิชาชีพเวชกรรม: ว.48912", fill=(71, 85, 105))

    # Hospital verification QR code simulation
    draw.rectangle([50, 545, 110, 605], fill=(15, 23, 42))
    draw.rectangle([62, 557, 98, 593], fill=(255, 255, 255))
    draw.rectangle([70, 565, 90, 585], fill=(15, 23, 42))
    draw.text((125, 555), "เอกสารออกผ่านระบบเวชระเบียนสถาบัน", fill=(16, 185, 129))
    draw.text((125, 575), "ยืนยันความถูกต้องด้วยลายมือชื่อดิจิทัล PKI", fill=(100, 116, 139))

    p1 = os.path.join(assets_dir, 'medical_cert_sample.jpg')
    p2 = os.path.join(assets_opt_dir, 'medical_cert_sample.jpg')
    im.save(p1, quality=92)
    im.save(p2, quality=88)
    print("Generated medical_cert_sample.jpg")

create_leave_evidence_asset()
