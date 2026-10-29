# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kit import (
    W, H, C, USER, CSS, ICONS, ic, img, avatar, sb, hi, bar, nav, uni, uni_seal, badge,
    btn, field, labeled, screen_bg_hint, qr_svg, get_b64_uri
)

# ---------------------------------------------------------------------------
# S13B: 13B. ยื่นคำร้องขอลาเรียนออนไลน์ Online Class Leave Request Form
# ---------------------------------------------------------------------------
def s13b_leave_request():
    """13B. ยื่นคำร้องขอลาเรียนออนไลน์"""
    return f'''
    <div class="scr">
      {sb()}
      
      <!-- Top App Bar -->
      <div style="background:#fff;padding:12px 20px;border-bottom:1px solid #E2E8F0;flex:none;">
        <div class="row" style="justify-content:space-between;align-items:center;">
          <div class="row" style="gap:10px;">
            <div class="ib" data-go="S12" style="width:36px;height:36px;cursor:pointer;">{ic("left", 18)}</div>
            <div>
              <div style="font-size:11px;color:#64748B;">ระบบทะเบียนและการศึกษา</div>
              <div style="font-weight:800;font-size:15px;color:{C['navy']};">ยื่นเรื่องลาเรียนออนไลน์</div>
            </div>
          </div>
          <div class="ib" data-go="S13C" style="width:36px;height:36px;cursor:pointer;" title="ประวัติการลา">{ic("receipt", 18, C['blue'])}</div>
        </div>
      </div>

      <!-- Scrollable Form Body -->
      <div class="body" style="padding:14px 20px 100px;gap:14px;overflow-y:auto;">
        
        <!-- Target Class Card -->
        <div class="card" style="padding:12px 14px;background:#F8FAFC;border-left:4px solid {C['blue']};">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <span class="badge b-blue" style="font-size:10px;">วิชาที่ขอลาเรียน</span>
            <span style="font-size:11px;color:{C['blue']};font-weight:600;cursor:pointer;" data-go="S12">เปลี่ยนวิชา</span>
          </div>
          <div style="font-weight:800;font-size:14px;color:{C['navy']};margin-top:6px;">
            462301 สื่อนวัตกรรมการเรียนรู้
          </div>
          <div style="font-size:11.5px;color:#64748B;margin-top:2px;">
            วันจันทร์ที่ 19 ตุลาคม 2569 เวลา 09:00 - 12:00 น.
          </div>
          <div class="row" style="gap:12px;margin-top:6px;font-size:11px;color:#64748B;">
            <span>อาจารย์ผู้สอน: ผศ.ดร.กมลวรรณ สุขุมินทร์</span>
            <span>ห้อง ED-304</span>
          </div>
        </div>

        <!-- Leave Type Selector -->
        <div class="sec"><span>ประเภทการขอลา</span></div>
        <div class="row" style="gap:8px;">
          <div class="card" style="flex:1;padding:10px;text-align:center;background:#EFF6FF;border:1.5px solid {C['blue']};cursor:pointer;">
            <div style="font-size:18px;">🩺</div>
            <div style="font-weight:800;font-size:12.5px;color:{C['navy']};margin-top:4px;">ลาป่วย</div>
            <div style="font-size:10px;color:#2563EB;margin-top:2px;">มีใบรับรองแพทย์</div>
          </div>
          <div class="card" style="flex:1;padding:10px;text-align:center;background:#fff;border:1px solid #CBD5E1;cursor:pointer;" onclick="showToast('เลือกประเภทลากิจจำเป็น')">
            <div style="font-size:18px;">📋</div>
            <div style="font-weight:700;font-size:12.5px;color:{C['navy']};margin-top:4px;">ลากิจธุระ</div>
            <div style="font-size:10px;color:#64748B;margin-top:2px;">กิจธุระจำเป็น</div>
          </div>
          <div class="card" style="flex:1;padding:10px;text-align:center;background:#fff;border:1px solid #CBD5E1;cursor:pointer;" onclick="showToast('เลือกประเภทลาปฏิบัติหน้าที่สถาบัน')">
            <div style="font-size:18px;">🏛️</div>
            <div style="font-weight:700;font-size:12.5px;color:{C['navy']};margin-top:4px;">ลางานสถาบัน</div>
            <div style="font-size:10px;color:#64748B;margin-top:2px;">แข่งขันทักษะ/กีฬา</div>
          </div>
        </div>

        <!-- Date Range Picker -->
        <div class="sec"><span>ช่วงวันที่ขอลา</span></div>
        <div class="card" style="padding:12px 14px;background:#fff;">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div>
              <div style="font-size:10.5px;color:#64748B;">ตั้งแต่วันที่</div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};margin-top:2px;">19 ต.ค. 2569 (09:00 น.)</div>
            </div>
            <span style="color:#94A3B8;">→</span>
            <div>
              <div style="font-size:10.5px;color:#64748B;">ถึงวันที่</div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};margin-top:2px;">20 ต.ค. 2569 (18:00 น.)</div>
            </div>
          </div>
          <div style="margin-top:8px;padding-top:8px;border-top:1px solid #F1F5F9;font-size:11px;color:#059669;font-weight:700;">
            ✓ รวมระยะเวลาลาเรียน 2 วัน นับเป็น 6 คาบเรียน
          </div>
        </div>

        <!-- Reason Description Textarea -->
        <div class="sec"><span>สาเหตุและความจำเป็นในการลา</span></div>
        <div style="background:#fff;border:1.5px solid #CBD5E1;border-radius:12px;padding:10px 12px;">
          <textarea style="width:100%;height:68px;border:none;background:transparent;outline:none;font:500 12.5px 'IBM Plex Sans Thai';color:{C['navy']};resize:none;" placeholder="ระบุอาการเจ็บป่วยหรือเหตุผลความจำเป็น...">มีอาการไข้สูง 38.6 องศา และปวดศีรษะอย่างรุนแรง แพทย์วินิจฉัยว่าเป็นไข้หวัดใหญ่เฉียบพลัน เห็นควรให้พักรักษาตัวที่หอพัก</textarea>
        </div>

        <!-- Document / Image Evidence Upload Section -->
        <div class="sec"><span>แนบหลักฐานเอกสารที่น่าเชื่อถือ</span></div>
        
        <!-- Attached Evidence Card Uploaded Medical Certificate -->
        <div class="card" style="padding:12px;background:#F0FDF4;border:1.5px solid #86EFAC;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div class="row" style="gap:10px;">
              <div style="width:48px;height:64px;border-radius:6px;overflow:hidden;flex:none;box-shadow:0 2px 8px rgba(0,0,0,0.12);background:#fff;">
                {img("medical_cert_sample.jpg", "width:100%;height:100%;object-fit:cover;")}
              </div>
              <div>
                <div class="row" style="gap:4px;">
                  <span class="badge b-green" style="font-size:9.5px;">✓ ใบรับรองแพทย์ รพ.ศูนย์การแพทย์</span>
                </div>
                <div style="font-weight:700;font-size:12.5px;color:{C['navy']};margin-top:3px;">
                  ใบรับรองแพทย์_รพ_15ตค2569.jpg
                </div>
                <div style="font-size:10.5px;color:#15803D;margin-top:2px;">
                  มีลายเซ็นแพทย์และตราประทับโรงพยาบาล • ตรวจสอบแล้ว
                </div>
              </div>
            </div>
            <span style="font-size:12px;color:#EF4444;font-weight:700;cursor:pointer;" onclick="showToast('ลบเอกสารแนบแล้ว')">✕</span>
          </div>
        </div>

        <!-- Add More Evidence Button -->
        <div style="border:1.5px dashed #93C5FD;border-radius:12px;padding:12px;text-align:center;background:#EFF6FF;cursor:pointer;" onclick="showToast('เลือกไฟล์หรือถ่ายรูปหลักฐานเพิ่มเติม')">
          <div class="row" style="justify-content:center;gap:6px;color:{C['blue']};font-weight:700;font-size:12px;">
            {ic("camera", 16, C['blue'])} <span>ถ่ายภาพหรือเลือกไฟล์หลักฐานเพิ่ม</span>
          </div>
          <div style="font-size:10.5px;color:#64748B;margin-top:2px;">
            รองรับไฟล์ JPG, PNG, PDF ขนาดไม่เกิน 25 MB
          </div>
        </div>

      </div>

      <!-- Sticky Submit Bar -->
      <div style="position:absolute;bottom:0;left:0;right:0;background:#fff;border-top:1.5px solid #E2E8F0;padding:12px 20px;box-shadow:0 -6px 20px rgba(0,0,0,0.06);z-index:20;">
        <button class="btn bp" data-go="S13C" style="width:100%;height:48px;font-size:13.5px;font-weight:700;background:linear-gradient(135deg, #246BFD 0%, #1D4ED8 100%);border:none;box-shadow:0 6px 18px rgba(36,107,253,0.3);cursor:pointer;">
          ยื่นคำร้องขอลาเรียนส่งถึงอาจารย์ผู้สอน →
        </button>
      </div>

    </div>
    '''

# ---------------------------------------------------------------------------
# S13C: 13C. ติดตามสถานะและประวัติการลา Leave Request History & Status
# ---------------------------------------------------------------------------
def s13c_leave_status():
    """13C. ติดตามสถานะและประวัติการลา"""
    return f'''
    <div class="scr">
      {sb()}
      
      <!-- Top Navigation -->
      <div style="background:#fff;padding:12px 20px;border-bottom:1px solid #E2E8F0;flex:none;">
        <div class="row" style="justify-content:space-between;align-items:center;">
          <div class="row" style="gap:10px;">
            <div class="ib" data-go="S12" style="width:36px;height:36px;cursor:pointer;">{ic("left", 18)}</div>
            <div>
              <div style="font-size:11px;color:#64748B;">ทะเบียนการเข้าเรียน</div>
              <div style="font-weight:800;font-size:15px;color:{C['navy']};">สถานะคำร้องขอลาเรียน</div>
            </div>
          </div>
          <div class="ib" data-go="S13B" style="width:36px;height:36px;cursor:pointer;" title="ยื่นคำร้องใหม่">{ic("plus", 18, C['blue'])}</div>
        </div>

        <!-- Filter Status Chips -->
        <div class="chips" style="margin-top:10px;gap:6px;overflow-x:auto;">
          <div class="chip on">ทั้งหมด 3 รายการ</div>
          <div class="chip">อนุมัติแล้ว 2</div>
          <div class="chip">รออาจารย์พิจารณา 1</div>
        </div>
      </div>

      <!-- History List Body -->
      <div class="body" style="padding:14px 20px 100px;gap:14px;overflow-y:auto;">
        
        <!-- Active Submitted Request Card -->
        <div class="sec"><span>คำร้องที่ยื่นล่าสุด</span></div>
        <div class="card" style="padding:14px;background:#fff;border:1.5px solid #F59E0B;box-shadow:0 6px 18px rgba(245,158,11,0.08);">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div class="row" style="gap:8px;">
              <span style="font-size:18px;">🩺</span>
              <div>
                <div style="font-weight:800;font-size:13.5px;color:{C['navy']};">ลาป่วย 2 วัน</div>
                <div style="font-size:11px;color:#64748B;">วิชา: 462301 สื่อนวัตกรรมการเรียนรู้</div>
              </div>
            </div>
            <span class="badge b-amber" style="font-size:9.5px;font-weight:700;">รออาจารย์อนุมัติ</span>
          </div>

          <div style="margin-top:10px;background:#FFFBEB;border-radius:8px;padding:8px 10px;font-size:11.5px;color:#92400E;line-height:1.4;">
            ช่วงเวลาลา: 19 - 20 ตุลาคม 2569<br>
            เหตุผล: มีไข้สูง 38.6 C แพทย์สั่งพักรักษาตัว
          </div>

          <!-- Evidence Badge -->
          <div class="row" style="justify-content:space-between;align-items:center;margin-top:10px;padding-top:8px;border-top:1px solid #F1F5F9;">
            <div class="row" style="gap:6px;font-size:11px;color:#059669;font-weight:700;">
              <span>📄</span> มีใบรับรองแพทย์แนบ
            </div>
            <button class="btn bs" style="height:28px;padding:0 8px;font-size:10.5px;cursor:pointer;" onclick="showToast('เปิดดูเอกสารใบรับรองแพทย์')">
              ดูหลักฐาน
            </button>
          </div>
        </div>

        <!-- Attendance Quota Overview Strip -->
        <div class="sec"><span>สิทธิ์เวลาเรียนคงเหลือประจำเทอม</span></div>
        <div class="card" style="padding:14px;background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%);color:#fff;border:none;">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div>
              <div style="font-size:11px;color:#94A3B8;">เกณฑ์เวลาเรียนขั้นต่ำ 80%</div>
              <div style="font:800 18px 'Inter';color:#fff;margin-top:2px;">เข้าเรียนแล้ว 94.2%</div>
            </div>
            <span class="badge b-green" style="font-size:10px;">สิทธิ์สอบครบถ้วน</span>
          </div>
          <div style="margin-top:10px;font-size:11px;color:#CBD5E1;">
            สามารถลาเรียนได้อีกไม่เกิน 2 ครั้ง โดยไม่กระทบสิทธิ์การเข้าสอบปลายภาค
          </div>
        </div>

        <!-- Past Approved Leaves Section -->
        <div class="sec"><span>ประวัติการลาที่ผ่านการอนุมัติแล้ว</span></div>

        <!-- Past Item 1 -->
        <div class="card" style="padding:12px 14px;background:#fff;border-left:4px solid #10B981;">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <span class="badge b-green" style="font-size:9.5px;">✓ อนุมัติแล้ว</span>
            <span style="font-size:10.5px;color:#64748B;">อนุมัติเมื่อ 2 ก.ย. 2569</span>
          </div>
          <div style="font-weight:700;font-size:13px;color:{C['navy']};margin-top:4px;">
            ลากิจธุระ 1 วัน • วิชา 462303 การออกแบบ UI
          </div>
          <div style="font-size:11px;color:#64748B;margin-top:2px;">
            อาจารย์ผู้อนุมัติ: ผศ.ดร. ธีรภัทร อัจฉริยะกุล
          </div>
        </div>

        <!-- Past Item 2 -->
        <div class="card" style="padding:12px 14px;background:#fff;border-left:4px solid #10B981;">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <span class="badge b-green" style="font-size:9.5px;">✓ อนุมัติแล้ว</span>
            <span style="font-size:10.5px;color:#64748B;">อนุมัติเมื่อ 14 ส.ค. 2569</span>
          </div>
          <div style="font-weight:700;font-size:13px;color:{C['navy']};margin-top:4px;">
            ลางานสถาบัน 2 วัน • เข้าร่วมแข่งขันทักษะวิชาการระดับชาติ
          </div>
          <div style="font-size:11px;color:#64748B;margin-top:2px;">
            อาจารย์ผู้อนุมัติ: รศ.ดร. นภัสสร วงศ์ศิลป์
          </div>
        </div>

      </div>

      <!-- Bottom Navigation Button -->
      <div style="position:absolute;bottom:0;left:0;right:0;background:#fff;border-top:1.5px solid #E2E8F0;padding:12px 20px;box-shadow:0 -6px 20px rgba(0,0,0,0.06);z-index:20;">
        <button class="btn bp" data-go="S12" style="width:100%;height:46px;font-size:13px;font-weight:700;cursor:pointer;">
          กลับสู่ตารางเรียน
        </button>
      </div>

    </div>
    '''

print("All Leave system screens defined successfully!")
