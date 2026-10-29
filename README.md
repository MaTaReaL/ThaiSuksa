# 🎓 ไทยศึกษา (THAI SUKSA) - Smart Campus Mobile Platform v3.0

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20Web-246BFD.svg)]()
[![Device Target](https://img.shields.io/badge/Device-iPhone%2016%20Pro%20Max-101C36.svg)]()
[![Design System](https://img.shields.io/badge/Design%20System-Figma%20Tokens%20v3.0-F59E0B.svg)]()
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-10B981.svg)]()

> **ไทยศึกษา (THAI SUKSA)** คือระบบนิเวศดิจิทัลระดับองค์กรและแพลตฟอร์มโมบายล์สมาร์ตแคมปัสสำหรับนิสิตนักศึกษาไทย ออกแบบและพัฒนาด้วยมาตรฐานระดับ Enterprise Mobile Design System (รองรับ 44 หน้าจอความละเอียดสูงบน iPhone 16 Pro Max) รวบรวมฟังก์ชันการเรียนการสอน บัตรประจำตัวนักศึกษาดิจิทัล ระบบการเงิน กยศ. และวิถีชีวิตในมหาวิทยาลัยไว้อย่างครบวงจร

---

## 🌟 จุดเด่นของโปรเจกต์ (Key Highlights)

- 📱 **44 หน้าจอความละเอียดสูง (High-Fidelity):** ออกแบบสัดส่วนจริง `440px × 956px` (3x Display Scale) บน iPhone 16 Pro Max
- 🎨 **Design System ระดับพรีเมียม:** ใช้สีอัตลักษณ์ Luxury Navy (`#101C36`), Royal Blue (`#246BFD`), Accent Gold (`#F59E0B`), และ Emerald Green (`#10B981`)
- 🔤 **ระบบตัวอักษรมาตรฐาน:** จับคู่ฟอนต์ `IBM Plex Sans Thai` และ `Plus Jakarta Sans` เพื่อความคมชัดสูงสุดทั้งภาษาไทยและอังกฤษ
- ♿ **WCAG 2.1 AA Compliant:** ทุกคอนทราสต์ของข้อความและปุ่มผ่านเกณฑ์ความเข้าถึงระดับสากล ไม่ต่ำกว่า 4.5:1
- 🌐 **Interactive Complete Flow:** สามารถเปิดทดสอบและสำรวจทั้ง 44 หน้าจอได้โดยตรงผ่านเว็บเบราว์เซอร์ พร้อมระบบซูม ขยาย และสลับดูรายละเอียด

---

## 📂 โครงสร้างและหมวดหมู่หน้าจอ (Screen Architecture)

โครงสร้างบอร์ดจัดเรียงทั้งหมด 15 แถว (Row 01 - Row 15) ครอบคลุมฟังก์ชันการใช้งาน 44 หน้าจอ:

| แถว (Row) | หมวดหมู่การใช้งาน (Module) | รายการหน้าจอ (Screens) |
|---|---|---|
| **Row 01 - 02** | **Onboarding & Identity Gateway** | S01 Splash Screen, S02 Onboarding Carousel, S03 University Selection Matrix, S04 Authentication & SSO Gateway, S05 NDID Registration, S06 Password Recovery |
| **Row 03 - 04** | **Master Dashboard & Profile** | S07 Home Dashboard (Master), S08 Hamburger Navigation Drawer, S09 Notification Center, S10 Student Profile & Settings, S11 Digital Student ID Pass |
| **Row 05 - 06** | **Academics & Examination** | S12 Schedule Matrix & Weekly View, S13 Class Details Modal, S14 Exam Matrix & Seat Allocations, S15 Academic Calendar & Events |
| **Row 07 - 08** | **Campus Life & Live Navigation** | S16 News & Announcements Feed, S17 News Reader, S18 Activities & Clubs Hub, S19 Event Terms & Hours, S20 Registration Confirmation, S21 Interactive Campus Map, S22 Building & Room Info, S23 Route GPS, S24 Live EV Tram Tracker |
| **Row 09 - 11** | **Facilities & Financial Ecosystem** | S25 Smart Room Booking, S26 QR Access Pass, S27 EV & Fleet Rental, S28 e-Petitions (คำร้อง), S29 Campus Wallet, S30 QR Pay Scanner, S31 Slip e-Receipt, S32 Tuition Invoice & PromptPay, S33 กยศ. Student Loan Portal |
| **Row 12 - 13** | **Student Welfare & Community** | S34 Volunteer Hours Tracker (36 ชม.), S35 Dormitory Life & Utility Meter Pay, S36 Community Forum & Q&A, S37 Discord Lounge & Voice Matrix |
| **Row 14** | **AI Campus Copilot** | S38 Thai Suksa AI Copilot (ตอบคำถามวิชาการ, ตรวจสอบเกณฑ์ทุน, และนำทางตึก) |
| **Row 15** | **Campus Wildlife & Fauna Wiki** | S61 Animal Wiki Hub, S62 Wildlife Detail Card, S63 Community Observation & Report, S64 Campus Wildlife Radar |

---

## 🚀 วิธีการเปิดใช้งานและรันโปรเจกต์ (Getting Started)

### 1. โคลนคลังข้อมูล (Clone Repository)
โปรเจกต์นี้ใช้ **Git LFS (Large File Storage)** ในการจัดการไฟล์โฟลว์บอร์ด HTML ขนาดใหญ่:
```bash
git lfs install
git clone https://github.com/MaTaReaL/ThaiSuksa.git
cd ThaiSuksa
```

### 2. เปิดใช้งานผ่าน Local Web Server
คุณสามารถเปิดดูหน้าพอร์ทัลหลักและบอร์ดความละเอียดสูงได้โดยใช้คำสั่งง่ายๆ:

**ใช้ Python (แนะนำ):**
```bash
python -m http.server 8000
```
เปิดเบราว์เซอร์ไปที่ `http://localhost:8000`

**หรือเปิดไฟล์ตรงในเบราว์เซอร์:**
- ดับเบิลคลิกเปิดไฟล์ `index.html` เพื่อเข้าสู่พอร์ทัลรวม
- หรือเปิด `ไทยศึกษา_complete_flow.html` เพื่อทดสอบ Interactive Flowboard ทั้ง 44 หน้าจอ

---

## 🎨 สเปกและโทเคนระบบดีไซน์ (Design Tokens)

สามารถอ่านเอกสารแนวทางระบบดีไซน์ฉบับสมบูรณ์ได้ที่ [FIGMA_DESIGN_SYSTEM_GUIDELINES.md](FIGMA_DESIGN_SYSTEM_GUIDELINES.md)

### พาเลตต์สีหลัก (Color Palette)
- **Brand Navy:** `#101C36` (พื้นหลังและหัวเรื่องหลัก)
- **Royal Blue (Primary):** `#246BFD` (ปุ่มหลัก ลิงก์ และการเน้นฟังก์ชันสำคัญ)
- **Deep Navy (Surface):** `#0B132B` (พื้นหลังการ์ดและเลเยอร์ซ้อน)
- **Honor Gold:** `#F59E0B` (เครื่องหมายเกียรตินิยมและแต้มรางวัล)
- **Emerald Success:** `#10B981` (สถานะสำเร็จ, บัตรผ่าน, และยอดเงิน)

### สัดส่วนหน้าจอ (Screen Viewport)
- **Device:** iPhone 16 Pro Max
- **Width:** `440px`
- **Height:** `956px`
- **Border Radius:** `54px` (Physical Shell), `48px` (Screen Viewport)
- **Dynamic Island:** `125px × 37px`

---

## 📄 ลิขสิทธิ์และผู้พัฒนา (License & Author)

- **ผู้พัฒนาและออกแบบ:** ธนพล กิจบำรุง (Thanapol Kitbumrung)
- **คณะ:** ศึกษาศาสตร์ ภาควิชาเทคโนโลยีการศึกษา มหาวิทยาลัยศิลปากร
- **GitHub:** [@MaTaReaL](https://github.com/MaTaReaL)
