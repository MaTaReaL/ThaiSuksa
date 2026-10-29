# คู่มือระบบการออกแบบและสถาปัตยกรรมคอมโพเนนต์สำหรับ Figma (Figma Master Component & Auto Layout Guidelines)
**โครงการ:** ไทยศึกษา (THAI SUKSA) — National Smart Campus & University Life Mobile Application  
**เวอร์ชัน:** 3.0 (Enterprise Professional Hand-off)  
**มาตรฐานอุปกรณ์เป้าหมาย:** iPhone 16 Pro Max (`440px × 956px`, 3x Display Scale)

---

## 1. ปรัชญาการออกแบบ (Design Principles: Anti-Generic AI Look)
การออกแบบแอปพลิเคชัน "ไทยศึกษา" หลีกเลี่ยงหน้าตาแบบ Template ทั่วไป (No generic gradient cards, No exaggerated neon glows, No repetitive uniform cards) โดยใช้หลักการดังนี้:
1. **Human Craftsmanship & Editorial Density:** ลำดับสายตา (Hierarchy) ชัดเจน ตัวอักษรใช้ฟอนต์สไตล์โมเดิร์น **IBM Plex Sans Thai** ร่วมกับ **Plus Jakarta Sans** สำหรับตัวเลขและภาษาอังกฤษ มีน้ำหนักตัวอักษร 5 ระดับ (300, 400, 500, 600, 700)
2. **Tactile Hierarchy & Hairline Precision:** พื้นหลังใช้ระบบ Dual-layer Canvas (`#F8FAFC` สำหรับพื้นที่ทั่วไป และ `#101C36` Deep Midnight Navy สำหรับส่วนระบบสำคัญ) ใช้เส้นขอบแบบ Hairline Border `1px solid rgba(226, 232, 240, 0.8)` เพื่อความคมชัดสูงบนหน้าจอความละเอียดสูง
3. **Accessibility First (WCAG 2.1 AA):** อัตราส่วนความเปรียบต่างของสี (Color Contrast Ratio) เกิน 4.5:1 สำหรับข้อความปกติ และ 3:1 สำหรับปุ่ม/กราฟิกสำคัญ

---

## 2. โครงสร้าง Design Tokens (Token Reference)

### 2.1 Color Tokens
```yaml
Colors:
  Brand / Primary:
    primary-500: "#246BFD"    # Electric Royal Blue (สีหลักสำหรับการกระทำ CTA, แถบสำคัญ)
    primary-100: "#EAF1FF"    # Tinted Blue Soft Surface (พื้นหลังการ์ดที่กำลังเลือก)
    primary-50:  "#F5F8FF"    # Subtle Accent Background
  Brand / Midnight:
    midnight-950: "#090E1A"   # Deep Void Navy (พื้นหลังเข้มสุด)
    midnight-900: "#101C36"   # Signature Header & Splash Screen Navy
    midnight-800: "#1A2B4C"   # Midnight Card Surface
  Accent / Cyan:
    cyan-400: "#58D6FF"       # Tech Spire Glow & Digital Indicator
    cyan-100: "#E3F8FF"       # Subtle Cyan Chip
  Accent / Gold:
    gold-500: "#F59E0B"       # Golden Pagoda Spire & Honor Crest
    gold-100: "#FEF3C7"       # Gold Trophy & Scholarship Chip
  Semantic:
    success-emerald: "#10B981"  # ผ่านการอนุมัติ / จ่ายเงินสำเร็จ
    warning-amber:   "#F59E0B"  # รอดำเนินการ / ใกล้ถึงเวลา
    danger-rose:     "#EF4444"  # ยกเลิก / ขาดเรียน / ยอดค้างชำระ
    neutral-canvas:  "#F8FAFC"  # หน้าจอหลัก Light Mode
    neutral-surface: "#FFFFFF"  # การ์ดและโมดูลสีขาว
    neutral-border:  "#E2E8F0"  # เส้นขอบคมกริบ
    neutral-text-main: "#0F172A" # ข้อความหลัก อ่านง่ายที่สุด
    neutral-text-sub:  "#64748B" # ข้อความอธิบายประกอบ
```

### 2.2 Typography Scale (IBM Plex Sans Thai + Plus Jakarta Sans)
* **Display Header 1:** `30px` / Line-height `38px` / Bold (700) — *ใช้กับยอดเงินคงเหลือ, เลข Digital ID*
* **Section Title (H2):** `20px` / Line-height `28px` / Semi-bold (600) — *หัวข้อเซกชันหลัก*
* **Card Header (H3):** `16px` / Line-height `24px` / Semi-bold (600) — *ชื่อรายวิชา, ชื่อกิจกรรม*
* **Body Text (Regular):** `14px` / Line-height `22px` / Regular (400) & Medium (500) — *เนื้อหาทั่วไป*
* **Caption / Meta:** `12px` / Line-height `18px` / Medium (500) — *เวลา, ห้องเรียน, หมวดหมู่*
* **Micro Badge:** `11px` / Line-height `14px` / Semi-bold (600) — *ชิปสถานะ, แท็กรายวิชา*

### 2.3 Spacing & Radius Tokens
* **Base Unit:** `4px`
* **Spacing:** `4px` (xs), `8px` (sm), `12px` (md), `16px` (lg), `20px` (xl), `24px` (2xl), `32px` (3xl)
* **Corner Radius:** `8px` (ปุ่มย่อย), `14px` (Input / Chip), `18px` (Card), `26px` (Bottom Sheet / Large Modal), `9999px` (Pill / Avatar)

---

## 3. สถาปัตยกรรมคอมโพเนนต์ใน Figma (Master Components ❖ vs Instances ◇)

ในการนำไปจัดทำบน Figma ต้องสร้าง Master Component (`❖`) ไว้ที่หน้า **01_Design_System_Master** แล้วนำสำเนา Instance (`◇`) ไปประกอบในแต่ละหน้าจอ โดยมีโครงสร้างดังนี้:

### ❖ 0. Component Set: `❖ Logo & App Badge / Master`
* **Master Component:** `❖ Brand Logo / Master App Badge` (`thai_suksa_logo.png`)
  * **File Asset:** `thai_suksa_logo.png` (1024 × 1024 px PNG ต้นฉบับคงสภาพสมบูรณ์ 100% ไม่ถูกตัดต่อหรือดัดแปลงเนื้อภาพใดๆ ทั้งสิ้น)
  * **Visual Elements:**
    * สัญลักษณ์ยอดปรางค์เจดีย์สีทองคำเปลว (สถาบันศิลปวัฒนธรรม ม.ศิลปากร & ความเป็นไทย)
    * หนังสือเปิดสีน้ำเงินสดสะท้อนการศึกษาและปัญญาสมัยใหม่ (Open Knowledge)
    * หัวปากกาสีน้ำเงินไซอันสะท้อนการเขียนและนวัตกรรม
    * พิกเซลข้อมูลดิจิทัล (Digital Transformation Matrix)
    * ตัวอักษรภาษาไทย "ไทยศึกษา" สีกรมท่าหนักแน่น พร้อมใบโพธิ์/ช่อชัยพฤกษ์สีทองบนสระไอ
    * ทรงการ์ด Squircle โค้งมนนุ่มนวล พร้อมพื้นหลังสีขาวสะท้อนความบริสุทธิ์ของปัญญา
  * **Variants & Responsive Sizing:**
    * `Variant = Splash Screen (S01)`: Width `180px`, Height `180px`, Border-radius `42px`, Shadow: `0 24px 60px rgba(0,0,0,0.65), 0 0 50px rgba(88,214,255,0.3)`
    * `Variant = App Header / Welcome (S02)`: Width `34px`, Height `34px`, Border-radius `9px`, Shadow: `0 2px 8px rgba(0,0,0,0.12)`
    * `Variant = Drawer Header (S08)`: Width `34px`, Height `34px`, Border-radius `9px`, Shadow: `0 3px 10px rgba(0,0,0,0.3)`
    * `Variant = Student Digital ID (S11)`: Width `38px`, Height `38px`, Border-radius `10px`, Shadow: `0 4px 12px rgba(0,0,0,0.4)`
    * `Variant = Canvas Master Banner`: Width `68px`, Height `68px`, Border-radius `18px`

---

### ❖ 1. Component Set: `❖ Button / Primary & Secondary`
* **Master Component:** `❖ Button`
  * **Auto Layout:** Direction `Horizontal`, Alignment `Center`, Padding: Left/Right `20px`, Top/Bottom `14px`, Gap `8px`
  * **Sizing:** Width `Fill Container` (สำหรับปุ่มเต็มความกว้าง) หรือ `Hug Contents` (สำหรับปุ่มในแถว), Height `52px`
  * **Properties & Variants:**
    * `Variant = Primary` (Fill: `#246BFD`, Text: White `#FFFFFF`, Shadow: `0 8px 20px rgba(36,107,253,0.3)`)
    * `Variant = Secondary` (Fill: `#EAF1FF`, Text: `#246BFD`, Border: None)
    * `Variant = Midnight` (Fill: `#101C36`, Text: White `#FFFFFF`)
    * `Variant = Outline` (Fill: Transparent, Text: `#0F172A`, Border: `1.5px solid #E2E8F0`)
    * `Variant = Danger` (Fill: `#EF4444`, Text: White `#FFFFFF`)
    * `State = Default / Hover / Pressed / Disabled`
    * `Icon = None / Leading / Trailing / Icon-Only`
* **ตัวลูก (Child Instance ◇):** ในหน้าจอ `S01 (Splash)`, `S02 (Login)`, `S15 (Wallet Pay)` ให้ลาก `◇ Button` ไปวางแล้ว Override เฉพาะข้อความภาษาไทย เช่น "เริ่มต้นใช้งาน", "สแกนจ่าย QR Code"

---

### ❖ 2. Component Set: `❖ Top Navigation Bar`
* **Master Component:** `❖ Header / TopBar`
  * **Frame Size:** Width `440px`, Height `60px`, Auto Layout `Horizontal`, Alignment `Center`, Padding: `0 20px`, Gap `12px`
  * **Sub-elements:**
    * `Left Slot (Instance ◇ Icon-Button)`: ลูกศรย้อนกลับ `arrow-left` (ขนาดกรอบ `42x42px`, Radius `12px`, Border `1px solid #E2E8F0`)
    * `Center Slot (Text)`: Text Layer ชื่อหน้าจอ `H3 (17px, Semi-bold)` Auto Layout `Fill Container`, Text-align `Center`
    * `Right Slot (Instance ◇ Icon-Button)`: กระดิ่งแจ้งเตือน หรือปุ่มตัวเลือก `more-horizontal`
  * **Variants:**
    * `Theme = Light` (Background `#FFFFFF`, Text `#0F172A`, Icon Border `#E2E8F0`)
    * `Theme = Midnight` (Background `#101C36`, Text `#FFFFFF`, Icon Border `rgba(255,255,255,0.15)`)

---

### ❖ 3. Component Set: `❖ Navigation / Global Tab Bar`
* **Master Component:** `❖ Navigation / BottomTabBar`
  * **Frame Size:** Width `440px`, Height `90px`, Auto Layout `Horizontal`, Space-between, Padding: `10px 16px 24px`, Background: `#FFFFFF` พร้อม Hairline Border-top `1px solid #E2E8F0` และ Shadow `0 -6px 20px rgba(16,28,54,0.04)`
  * **5 Child Slots (Instances ◇ Tab Item):**
    1. `◇ Tab / Home` (Icon: Home, Label: "หน้าหลัก")
    2. `◇ Tab / Schedule` (Icon: Calendar, Label: "ตารางเรียน")
    3. `◇ Tab / Wallet` (Icon: Wallet, Label: "กระเป๋าเงิน")
    4. `◇ Tab / Community` (Icon: Users/Message, Label: "ชุมชน/ดิสคอร์ด")
    5. `◇ Tab / Profile` (Icon: User, Label: "โปรไฟล์")
  * **Tab Item Variants:**
    * `Active = True` (Icon Color: `#246BFD`, Label: Bold `#246BFD`, Indicator Dot เล็กๆ สีฟ้าใต้ไอคอน)
    * `Active = False` (Icon Color: `#94A3B8`, Label: Medium `#94A3B8`)

---

### ❖ 4. Component: `❖ Student Digital ID Card (Master)`
* **Master Component:** `❖ Card / DigitalID`
  * **Frame Size:** Width `392px`, Height `224px`, Radius `22px`, Overflow `Hidden`
  * **Visual Styling:**
    * พื้นหลัง: Linear Gradient `135deg, #101C36 0%, #162B55 60%, #1E3A8A 100%`
    * ลวดลายคลื่น Hologram: SVG Vector ลายน้ำเรืองแสงสีทองและฟ้า
  * **Internal Elements (Auto Layout Vertical):**
    * `Row 1 (Header)`: ตราสัญลักษณ์ ม.ศิลปากร (`36x36px`) + ข้อความ "บัตรประจำตัวนักศึกษาดิจิทัล / มหาวิทยาลัยศิลปากร" + ชิป "ACTIVE ENROLLED"
    * `Row 2 (Body)`: รูปโปรไฟล์นักศึกษา (`64x64px`, Radius `16px`, Border `2px solid #58D6FF`) + ชื่อ "นายธนพล กิจบำรุง" + รหัส "670610452" + คณะศึกษาศาสตร์ สาขาเทคโนโลยีการศึกษา
    * `Row 3 (Footer)`: บาร์โค้ด / QR Code ดิจิทัลสำหรับสแกนเข้าห้องสมุดและสอบ

---

### ❖ 5. Component: `❖ Status & Category Chip`
* **Master Component:** `❖ Chip / Status`
  * **Auto Layout:** Height `26px`, Padding: Left/Right `10px`, Top/Bottom `3px`, Radius `13px`, Gap `4px`
  * **Variants:**
    * `Semantic = Success` (Bg: `#ECFDF5`, Border: `#A7F3D0`, Text: `#065F46`)
    * `Semantic = Info` (Bg: `#EFF6FF`, Border: `#BFDBFE`, Text: `#1E40AF`)
    * `Semantic = Warning` (Bg: `#FFFBEB`, Border: `#FDE68A`, Text: `#92400E`)
    * `Semantic = Danger` (Bg: `#FEF2F2`, Border: `#FECACA`, Text: `#991B1B`)
    * `Semantic = Navy` (Bg: `#101C36`, Border: `#101C36`, Text: `#FFFFFF`)

---

### ❖ 6. Component: `❖ Interactive List Tile / Feature Row`
* **Master Component:** `❖ Tile / ActionRow`
  * **Auto Layout:** Width `Fill Container`, Padding: `14px 16px`, Background `#FFFFFF`, Radius `16px`, Border `1px solid #E2E8F0`, Gap `14px`
  * **Slots:**
    * `Leading Slot`: Icon Box ขนาด `44x44px`, Radius `14px`, สีตามประเภท (เช่น รถบัส = ฟ้า, จองห้อง = ม่วง, ทุน = ทอง)
    * `Center Slot`: Title `H3 (15px, 600)` + Subtitle `Caption (13px, 400, #64748B)`
    * `Trailing Slot`: Badge สถานะ + Chevron ลูกศรขวา

---

## 4. โครงสร้างหน้าจอและหมวดหมู่การจัดบอร์ดใน Figma (38 Screens Master Breakdown)

| รหัส | ชื่อหน้าจอ (Screen Name) | ฟังก์ชันที่ตอบโจทย์อาจารย์และผู้ใช้ | โครงสร้างหลัก (Key Master Components Used) |
|---|---|---|---|
| **S01** | Splash Screen (Luxury Brand Launch) | โลโก้มาสเตอร์ในกรอบ Glassmorphic Halo พร้อมแสงออร่าลึก สมเกียรติสถาบันและกระทรวง อว. | `❖ Logo / Master App Badge`, `❖ CTA Glow Button` |
| **S02** | Welcome & Onboarding | แนะนำระบบ Smart Campus, Camplus & National ID | `❖ Carousel Indicator`, `❖ Button Primary` |
| **S03** | University Selection Matrix | ค้นหาและเลือกเชื่อมต่อสถาบันการศึกษาทั่วประเทศ (ตราสถาบันจริง) | `❖ Search Bar`, `❖ University Badge Grid (SU, CU, TU, KU, MU)` |
| **S04** | Authentication & SSO Gateway | เข้าสู่ระบบด้วย SSO สถาบัน / Digital Thai ID | `❖ Input Field`, `❖ Social SSO Buttons` |
| **S05** | Registration & Identity Verify | สมัครสมาชิก ยืนยันตัวตนผ่าน NDID | `❖ Form Stepper`, `❖ OTP Input Group` |
| **S06** | Forgot Password & Recovery | กู้คืนรหัสผ่านและตั้งรหัสผ่านใหม่ทาง SMS/Email | `❖ Input Field`, `❖ Security Alert Box` |
| **S07** | Home Dashboard (Master) | ตารางเรียนประจำวัน, กิจกรรมด่วน, ทางลัด 8 บริการ, บอร์ดชุมชน | `❖ Quick Actions Grid`, `❖ Class Card`, `❖ BottomTabBar` |
| **S08** | Hamburger Menu Drawer [Overlay] | เมนูนำทางแบบเปิดข้าง เข้าถึงทั้ง 38 ฟังก์ชันในระบบ | `❖ Drawer Side Sheet`, `❖ Menu Item Row` |
| **S09** | Notification Center | แจ้งเตือนตารางเรียน เปลี่ยนห้อง กิจกรรมใหม่ ยอดเงินเข้า | `❖ Notification Item Tile`, `❖ Clear All Link` |
| **S10** | Student Profile & Settings | ข้อมูลนายธนพล กิจบำรุง, คณะศึกษาศาสตร์, สาขาเทคโนฯ, GPAX 3.72 | `❖ Profile Card`, `❖ Stat Badge Group` |
| **S11** | Digital Student ID Pass | บัตรนักศึกษาดิจิทัลทางการ ม.ศิลปากร สแกนบาร์โค้ด/QR | `❖ Smart ID Pass`, `❖ Official SU Seal` |
| **S12** | Schedule & Weekly View | ตารางเรียนรายวัน/สัปดาห์ พร้อมห้องเรียนและผู้สอน | `❖ Date Scroller`, `❖ Timeline Item Tile` |
| **S13** | Class Details [Bottom Sheet] | ข้อมูลวิชา 462301, แผนที่ตึกศึกษา 3, ปุ่มเปิดนำทาง | `❖ Bottom Sheet Modal`, `❖ Map Button` |
| **S14** | Exam Schedule & Seat Matrix | ตารางสอบ วันเวลา รหัสห้องสอบ เลขที่นั่งสอบ | `❖ Exam Ticket Card`, `❖ Countdown Tag` |
| **S15** | Academic Calendar & Events | ปฏิทินกำหนดการมหาวิทยาลัย และเพิ่มนัดหมายส่วนตัว | `❖ Calendar Month View`, `❖ Event Item Card` |
| **S16** | News & Announcements Feed | ข่าวมหาวิทยาลัย ข่าวคณะศึกษาศาสตร์ ประกาศ อว. | `❖ News Hero Banner`, `❖ Article Filter Chip` |
| **S17** | News Detail & Reader | รายละเอียดข่าว บุ๊กมาร์ก และแชร์ให้เพื่อน | `❖ Article Reader View`, `❖ Floating Share Bar` |
| **S18** | Activities & Clubs Hub | ค้นหาชมรม สมัครร่วมกิจกรรม และดูประวัติ | `❖ Club Directory Card`, `❖ Join Button` |
| **S19** | Event Detail & Terms | รายละเอียดเงื่อนไขกิจกรรม Hackathon และชั่วโมงกิจกรรม | `❖ Event Hero Card`, `❖ Registration Button` |
| **S20** | Registration Confirmation [Modal] | ยืนยันการสมัครกิจกรรม สำเร็จพร้อมเพิ่มลงปฏิทิน | `❖ Modal Popup`, `❖ Calendar Sync Link` |
| **S21** | Interactive Campus Map & GPS | แผนที่อาคาร ม.ศิลปากร วิทยาเขตพระราชวังสนามจันทร์ | `❖ Map Viewport`, `❖ Route Navigation Pin` |
| **S22** | Building & Room Details | รายละเอียดอาคารศึกษา 3 สิ่งอำนวยความสะดวก | `❖ Facility Info Sheet`, `❖ Floor Directory` |
| **S23** | Navigation & Directions | เส้นทางการเดินเท้าและขับรถภายในวิทยาเขต | `❖ Direction Turn Card`, `❖ ETA Badge` |
| **S24** | Live EV Tram Tracker | แผนที่รถรางไฟฟ้า จุดจอด เวลามาถึงแบบสด (Real-time) | `❖ Live Tram Tracker`, `❖ Station Schedule List` |
| **S25** | Smart Space & Room Booking | จองห้องเรียน, Co-working space, ห้องติวกลุ่มหอสมุด | `❖ Time Slot Grid`, `❖ Resource Selector` |
| **S26** | Booking Pass & Smart QR Access | บัตรคิวการจอง สแกน QR ปลดล็อกประตูอัตโนมัติ | `❖ QR Pass Ticket`, `❖ Countdown Lock` |
| **S27** | Fleet & Equipment Rental | ยืมจักรยาน Smart EV, iPad แล็บ, จองรถตู้สถาบัน | `❖ Vehicle Status Card`, `❖ Unlock NFC Button` |
| **S28** | Student e-Petitions (คำร้อง) | ยื่นคำร้องขอหนังสือรับรอง, ดรอปเรียนออนไลน์ ตรวจสถานะ | `❖ Petition Type Tile`, `❖ Status Timeline` |
| **S29** | Campus Wallet (งบ 3,000 ฿/ด.) | กระเป๋าเงินดิจิทัล สวัสดิการค่าครองชีพรัฐบาล Camplus | `❖ Balance Card`, `❖ Transaction History Tile` |
| **S30** | QR Scanner & Food Pay | สแกนจ่ายเงินโรงอาหารเพชรรัตน เลือกลดหย่อน Camplus | `❖ Viewfinder Scanner`, `❖ Amount Confirm Sheet` |
| **S31** | Digital e-Receipt & Payment Slip | สลิปชำระเงินดิจิทัลพร้อมรหัสอ้างอิงและตราประทับ | `❖ Perforated Ticket Slip`, `❖ Share Button` |
| **S32** | Tuition Fee Payment & Receipt | ชำระค่าเทอม 18,500 ฿ สแกน PromptPay & ใบเสร็จอิเล็กทรอนิกส์ | `❖ Invoice Breakdown Card`, `❖ PromptPay QR Generator` |
| **S33** | Student Loan (กยศ. e-Portal) | ยื่นกู้ยืม ตรวจสถานะ 4 ขั้นตอน ค่าครองชีพ 3,000 ฿/ด. | `❖ 4-Step Loan Stepper`, `❖ Allowance Schedule` |
| **S34** | Volunteer Hours Tracker | ตรวจชั่วโมงจิตอาสา 36/36 ชม. ดาวน์โหลด e-Certificate อว. | `❖ Progress Radial/Bar`, `❖ Verified Events Log` |
| **S35** | Dormitory Life & Utility Pay | หอพักทับแก้ว 3 ห้อง 412, มิเตอร์น้ำ/ไฟ, ชำระบิล 3,186 ฿ | `❖ Room Summary Card`, `❖ Meter Billing Card` |
| **S36** | Community Forum & Q&A | กระดานสนทนานักศึกษา ถามตอบ ติวสอบ และรีวิว | `❖ Discussion Thread Card`, `❖ Upvote/Reply Component` |
| **S37** | Thai Suksa Discord Lounge | ห้องแชตและพูดคุยเสียงสด (Voice Matrix) แยกคณะ/สาขา | `❖ Discord Server Rail`, `❖ Live Audio Status Bar` |
| **S38** | Thai Suksa AI Campus Copilot | ผู้ช่วยปัญญาประดิษฐ์ตอบคำถาม แนะนำตึก และตรวจเกณฑ์ทุน | `❖ Chat Message Bubble (User/AI)`, `❖ Prompt Pill` |

---

## 5. คำแนะนำในการประกอบร่างบน Figma (Auto Layout Rules)
1. **Never use Fixed Width inside Cards:** เลเยอร์ข้อความภายใน Card ทุกชิ้นต้องตั้งค่าเป็น `Fill Container (Horizontal)` เสมอ เพื่อให้รองรับข้อความภาษาไทยที่มีความยาวผันแปรโดยไม่ตกขอบ
2. **Auto Layout Padding Standards:**
   * หน้าจอหลัก (Screen Body): `Padding: 0 20px`, `Vertical Gap: 16px`
   * การ์ดทั่วไป (Standard Card): `Padding: 16px`, `Radius: 18px`
   * ปุ่มหลัก (Primary Button): `Height: 52px`, `Radius: 16px`
3. **Naming Convention:**
   * Frame หน้าจอ: `Screen / [รหัส] - [ชื่อภาษาอังกฤษ]` เช่น `Screen / S07 - Home Dashboard`
   * คอมโพเนนต์แม่: `❖ [หมวดหมู่] / [ชื่อคอมโพเนนต์] / [Variant]` เช่น `❖ Button / Primary / Large`
   * คอมโพเนนต์ลูก: `◇ [หมวดหมู่] / [ชื่อคอมโพเนนต์]`
