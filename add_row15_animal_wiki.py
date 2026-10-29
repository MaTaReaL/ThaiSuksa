# -*- coding: utf-8 -*-
"""
Helper script to inject Row 15: Campus Animal Encyclopedia, Community Wiki & Welfare Flow (S61-S64)
into generate_thai_suksa_flow.py and recompile the complete flow board.
"""

import os
import re

SCRIPT_PATH = os.path.join("ไทยศึกษา", "generate_thai_suksa_flow.py")

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. Screen Implementations for Row 15
# ---------------------------------------------------------------------------
s61_s64_code = '''
def s61_campus_animal_wiki():
    """61. สารานุกรมสัตว์และวิกิชุมชนมหาวิทยาลัย (Campus Animal Wiki Directory)"""
    return f"""
    <div class="scr">
      {sb()}
      <!-- Top App Bar -->
      <div class="bar" style="justify-content:space-between;padding:0 20px;border-bottom:1px solid #E2E8F0;background:#fff;">
        <div class="row" style="gap:10px;align-items:center;">
          <div class="ib" data-go="S07" style="cursor:pointer;background:#F8FAFC;border:1px solid #E2E8F0;">
            {ic("left", 18, C['navy'])}
          </div>
          <div>
            <div style="font-size:11px;color:#64748B;font-weight:600;">สารานุกรมและวิกิชุมชน</div>
            <div style="font-size:16px;font-weight:800;color:{C['navy']};">สารานุกรมสัตว์ในมหาวิทยาลัย</div>
          </div>
        </div>
        <div class="row" style="gap:6px;">
          <div class="ib" data-go="S64" style="cursor:pointer;background:#EFF6FF;border:1px solid #DBEAFE;color:{C['blue']};" title="เรดาร์พิกัดสัตว์">
            <span style="font-size:15px;">📍</span>
          </div>
          <div class="ib" data-go="S63" style="cursor:pointer;background:#FFFBEB;border:1px solid #FDE68A;color:#D97706;" title="แจ้งพบสัตว์ / เพิ่มข้อมูล">
            <span style="font-size:15px;">➕</span>
          </div>
        </div>
      </div>

      <!-- Scrollable Body Content -->
      <div class="body" style="padding:14px 18px 100px;gap:14px;overflow-y:auto;">

        <!-- Quick Access Banner: Live Radar & Welfare Fund -->
        <div class="card" data-go="S64" style="background:linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);border:1px solid #FDE68A;padding:12px 14px;border-radius:18px;cursor:pointer;">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div class="row" style="gap:10px;align-items:center;">
              <div style="width:38px;height:38px;border-radius:12px;background:#F59E0B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 3px 10px rgba(245,158,11,0.35);">
                🐾
              </div>
              <div>
                <div style="font-size:13px;font-weight:800;color:#92400E;">กองทุนสวัสดิภาพสัตว์ & ทำหมันจรจัด</div>
                <div style="font-size:11px;color:#B45309;">ยอดเงินกองทุน ฿48,650 • แตะเพื่อดูเรดาร์พิกัดสด</div>
              </div>
            </div>
            <div style="background:#F59E0B;color:#fff;font-weight:800;font-size:11px;padding:4px 10px;border-radius:8px;">
              เรดาร์สด ➜
            </div>
          </div>
        </div>

        <!-- Search Bar with Instant Filter -->
        <div class="card" style="padding:8px 14px;background:#fff;border:1px solid #E2E8F0;border-radius:16px;display:flex;align-items:center;gap:10px;">
          {ic("search", 18, "#94A3B8")}
          <input id="animal_search_input" type="text" placeholder="ค้นหาชื่อสัตว์ สายพันธุ์ หรือพิกัดอาคาร..." style="border:none;outline:none;width:100%;font-size:13px;color:#101C36;background:transparent;" oninput="searchAnimalWiki(this.value)">
          <div id="animal_search_clear" onclick="clearAnimalSearch()" style="display:none;cursor:pointer;color:#94A3B8;font-size:12px;font-weight:700;">✕</div>
        </div>

        <!-- Category Filter Chips -->
        <div class="row" style="gap:8px;overflow-x:auto;padding-bottom:2px;scrollbar-width:none;">
          <div class="animal-filter-chip on" data-cat="all" onclick="filterAnimalCat('all')" style="white-space:nowrap;padding:6px 14px;border-radius:20px;font-size:11.5px;font-weight:700;background:#246BFD;color:#fff;cursor:pointer;border:1px solid #246BFD;">
            ทั้งหมด (18 ตัว)
          </div>
          <div class="animal-filter-chip" data-cat="dog" onclick="filterAnimalCat('dog')" style="white-space:nowrap;padding:6px 14px;border-radius:20px;font-size:11.5px;font-weight:600;background:#fff;color:#64748B;cursor:pointer;border:1px solid #E2E8F0;">
            🐕 สุนัขมหาวิทยาลัย
          </div>
          <div class="animal-filter-chip" data-cat="cat" onclick="filterAnimalCat('cat')" style="white-space:nowrap;padding:6px 14px;border-radius:20px;font-size:11.5px;font-weight:600;background:#fff;color:#64748B;cursor:pointer;border:1px solid #E2E8F0;">
            🐈 แมวประจำคณะ
          </div>
          <div class="animal-filter-chip" data-cat="wild" onclick="filterAnimalCat('wild')" style="white-space:nowrap;padding:6px 14px;border-radius:20px;font-size:11.5px;font-weight:600;background:#fff;color:#64748B;cursor:pointer;border:1px solid #E2E8F0;">
            🦎 ตัวเงินตัวทอง & นก
          </div>
          <div class="animal-filter-chip" data-cat="help" onclick="filterAnimalCat('help')" style="white-space:nowrap;padding:6px 14px;border-radius:20px;font-size:11.5px;font-weight:600;background:#fff;color:#DC2626;cursor:pointer;border:1px solid #FECACA;">
            ⚠️ ต้องการความช่วยเหลือ
          </div>
        </div>

        <!-- Data Integrity Community Guidelines Note -->
        <div style="background:#F1F5F9;border-left:3px solid #246BFD;border-radius:10px;padding:8px 12px;font-size:11px;color:#475569;line-height:1.45;">
          <strong>นโยบายสารานุกรมข้อเท็จจริง:</strong> ข้อมูลที่ไม่ทราบประวัติหรือไม่มีหลักฐานแน่ชัด จะระบุ <span style="background:#E2E8F0;color:#1E293B;padding:1px 6px;border-radius:4px;font-weight:700;">ไม่มีข้อมูล</span> โดยไม่แต่งเติม เพื่อความปลอดภัยและการรักษาที่ถูกต้อง
        </div>

        <!-- Animal Wiki Cards List -->
        <div id="animal_cards_container" style="display:flex;flex-direction:column;gap:12px;">

          <!-- Card 1: พี่เตี้ย คณะวิศวกรรมศาสตร์ -->
          <div class="card animal-entry-card" data-cat="dog" data-name="พี่เตี้ย วิศวะ" data-go="S62" style="padding:14px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;cursor:pointer;transition:transform 0.2s;">
            <div class="row" style="gap:12px;align-items:flex-start;">
              <!-- Animal Photo Frame -->
              <div style="position:relative;width:68px;height:68px;border-radius:16px;background:linear-gradient(135deg,#FEF3C7,#FDE68A);display:flex;align-items:center;justify-content:center;font-size:34px;flex-shrink:0;box-shadow:0 4px 12px rgba(245,158,11,0.2);">
                🐕
                <div style="position:absolute;bottom:-4px;right:-4px;width:18px;height:18px;border-radius:50%;background:#10B981;border:2px solid #fff;display:flex;align-items:center;justify-content:center;color:#fff;font-size:10px;font-weight:900;" title="ทำหมันแล้ว">✓</div>
              </div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <span style="font-size:14.5px;font-weight:800;color:{C['navy']};">พี่เตี้ย คณะวิศวกรรมศาสตร์</span>
                  <span class="badge b-blue" style="font-size:10px;">สุนัขพันธุ์ทาง</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:2px;">ชื่อเล่น: เตี้ยวิศวะ • พี่หล่อประจำตึกแดง</div>
                <div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px;">
                  <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:10px;">📍 ใต้ถุนตึกวิศวะฯ</span>
                  <span class="badge b-green" style="font-size:10px;">💉 วัคซีนพิษสุนัขบ้าครบ</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">วันเกิด: ไม่มีข้อมูล</span>
                </div>
              </div>
            </div>
            <!-- Status & Territory Bar -->
            <div style="margin-top:10px;padding:8px 10px;background:#F8FAFC;border:1px solid #F1F5F9;border-radius:12px;font-size:11px;color:#334155;display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#059669;font-weight:600;">● นอนหลับอยู่หน้าตึกวิศวะฯ (15 นาทีที่แล้ว)</span>
              <span style="color:{C['blue']};font-weight:700;">ดูประวัติ ➜</span>
            </div>
          </div>

          <!-- Card 2: เจ้าส้มซ่า คณะอักษรศาสตร์ -->
          <div class="card animal-entry-card" data-cat="cat" data-name="เจ้าส้มซ่า อักษร แมวส้ม" data-go="S62" style="padding:14px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;cursor:pointer;transition:transform 0.2s;">
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="position:relative;width:68px;height:68px;border-radius:16px;background:linear-gradient(135deg,#FFEDD5,#FED7AA);display:flex;align-items:center;justify-content:center;font-size:34px;flex-shrink:0;box-shadow:0 4px 12px rgba(249,115,22,0.2);">
                🐈
                <div style="position:absolute;bottom:-4px;right:-4px;width:18px;height:18px;border-radius:50%;background:#10B981;border:2px solid #fff;display:flex;align-items:center;justify-content:center;color:#fff;font-size:10px;font-weight:900;" title="ทำหมันแล้ว">✓</div>
              </div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <span style="font-size:14.5px;font-weight:800;color:{C['navy']};">เจ้าส้มซ่า คณะอักษรศาสตร์</span>
                  <span class="badge" style="background:#FFEDD5;color:#C2410C;font-size:10px;">แมวไทยลายส้ม</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:2px;">ชอบคลอเคลียขาเวลาอ่านหนังสือ • ขี้อ้อน</div>
                <div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px;">
                  <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:10px;">📍 ลานโพธิ์ อาคาร 36 ปี</span>
                  <span class="badge b-green" style="font-size:10px;">💉 วัคซีนไข้หัดครบ</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">ไมโครชิป: ไม่มีข้อมูล</span>
                </div>
              </div>
            </div>
            <div style="margin-top:10px;padding:8px 10px;background:#F8FAFC;border:1px solid #F1F5F9;border-radius:12px;font-size:11px;color:#334155;display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#059669;font-weight:600;">● นั่งตากแดดอุ่นๆ ใต้ม้านั่งลานโพธิ์</span>
              <span style="color:{C['blue']};font-weight:700;">ดูประวัติ ➜</span>
            </div>
          </div>

          <!-- Card 3: พี่ก้อน แห่งสระแก้ว -->
          <div class="card animal-entry-card" data-cat="wild" data-name="พี่ก้อน สระแก้ว ตัวเงินตัวทอง ตัวเหี้ย" data-go="S62" style="padding:14px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;cursor:pointer;transition:transform 0.2s;">
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="position:relative;width:68px;height:68px;border-radius:16px;background:linear-gradient(135deg,#DCFCE7,#BBF7D0);display:flex;align-items:center;justify-content:center;font-size:34px;flex-shrink:0;box-shadow:0 4px 12px rgba(34,197,94,0.2);">
                🦎
              </div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <span style="font-size:14.5px;font-weight:800;color:{C['navy']};">พี่ก้อน แห่งสระแก้ว</span>
                  <span class="badge b-green" style="font-size:10px;">ตัวเงินตัวทองยักษ์</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:2px;">รักสงบ นอนอาบแดดช่วงเที่ยง • สัตว์ป่าคุ้มครอง</div>
                <div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px;">
                  <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:10px;">📍 ริมสระแก้ว สวนแก้ว</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">อายุ: ไม่มีข้อมูล</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">เพศ: ไม่มีข้อมูล</span>
                </div>
              </div>
            </div>
            <div style="margin-top:10px;padding:8px 10px;background:#F8FAFC;border:1px solid #F1F5F9;border-radius:12px;font-size:11px;color:#334155;display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#D97706;font-weight:600;">⚠️ สังเกตการณ์ระยะห่าง 3 ม. ห้ามโยนเศษอาหาร</span>
              <span style="color:{C['blue']};font-weight:700;">ดูประวัติ ➜</span>
            </div>
          </div>

          <!-- Card 4: น้องเฉาก๊วย ประตูหน้าวัง -->
          <div class="card animal-entry-card" data-cat="dog" data-name="น้องเฉาก๊วย หมาดำ ประตูหน้า ป้อมยาม" data-go="S62" style="padding:14px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;cursor:pointer;transition:transform 0.2s;">
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="position:relative;width:68px;height:68px;border-radius:16px;background:linear-gradient(135deg,#334155,#1E293B);display:flex;align-items:center;justify-content:center;font-size:34px;flex-shrink:0;box-shadow:0 4px 12px rgba(30,41,59,0.3);">
                🐕‍🦺
                <div style="position:absolute;bottom:-4px;right:-4px;width:18px;height:18px;border-radius:50%;background:#10B981;border:2px solid #fff;display:flex;align-items:center;justify-content:center;color:#fff;font-size:10px;font-weight:900;" title="ทำหมันแล้ว">✓</div>
              </div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <span style="font-size:14.5px;font-weight:800;color:{C['navy']};">น้องเฉาก๊วย ป้อมประตูหน้า</span>
                  <span class="badge b-navy" style="font-size:10px;">สุนัขไทยสีดำ</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:2px;">เป็นมิตรกับเจ้าหน้าที่ รปภ. • ชอบเฝ้าทางเข้า</div>
                <div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px;">
                  <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:10px;">📍 ป้อม รปภ. ประตู 1</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">วัคซีน: ไม่มีข้อมูล</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">สายพันธุ์เดิม: ไม่มีข้อมูล</span>
                </div>
              </div>
            </div>
            <div style="margin-top:10px;padding:8px 10px;background:#F8FAFC;border:1px solid #F1F5F9;border-radius:12px;font-size:11px;color:#334155;display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#059669;font-weight:600;">● เฝ้าป้อมร่วมกับเจ้าหน้าที่ รปภ.</span>
              <span style="color:{C['blue']};font-weight:700;">ดูประวัติ ➜</span>
            </div>
          </div>

          <!-- Card 5: นกยูงหลวงประจำวัง -->
          <div class="card animal-entry-card" data-cat="wild" data-name="นกยูงหลวง พระราชวังสนามจันทร์" data-go="S62" style="padding:14px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;cursor:pointer;transition:transform 0.2s;">
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="position:relative;width:68px;height:68px;border-radius:16px;background:linear-gradient(135deg,#065F46,#047857);display:flex;align-items:center;justify-content:center;font-size:34px;flex-shrink:0;box-shadow:0 4px 12px rgba(6,95,70,0.25);">
                🦚
              </div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <span style="font-size:14.5px;font-weight:800;color:{C['navy']};">นกยูงหลวง ประจำพระราชวัง</span>
                  <span class="badge b-green" style="font-size:10px;">นกยูงอินเดีย</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:2px;">รำแพนหางสวยงาม • ดูแลโดยสำนักพระราชวัง</div>
                <div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px;">
                  <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:10px;">📍 สวนป่าพระราชวัง</span>
                  <span class="badge b-green" style="font-size:10px;">ตรวจสุขภาพประจำปี</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">วันเกิด: ไม่มีข้อมูล</span>
                </div>
              </div>
            </div>
            <div style="margin-top:10px;padding:8px 10px;background:#F8FAFC;border:1px solid #F1F5F9;border-radius:12px;font-size:11px;color:#334155;display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#059669;font-weight:600;">● เดินเล่นบนลานหญ้าเขียวข้างพระที่นั่ง</span>
              <span style="color:{C['blue']};font-weight:700;">ดูประวัติ ➜</span>
            </div>
          </div>

          <!-- Card 6: น้องขาวมอม (ยังไม่มีชื่อทางการ - เพิ่งพบใหม่) -->
          <div class="card animal-entry-card" data-cat="help" data-name="น้องขาวมอม บาดเจ็บ ลูกหมา ตึกวิทย์" data-go="S63" style="padding:14px;background:#fff;border:1.5px dashed #EF4444;border-radius:20px;cursor:pointer;transition:transform 0.2s;">
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="position:relative;width:68px;height:68px;border-radius:16px;background:linear-gradient(135deg,#FEE2E2,#FECACA);display:flex;align-items:center;justify-content:center;font-size:34px;flex-shrink:0;box-shadow:0 4px 12px rgba(239,68,68,0.25);">
                🐶
                <div style="position:absolute;top:-4px;right:-4px;width:18px;height:18px;border-radius:50%;background:#EF4444;border:2px solid #fff;display:flex;align-items:center;justify-content:center;color:#fff;font-size:10px;font-weight:900;">!</div>
              </div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <span style="font-size:14.5px;font-weight:800;color:#991B1B;">น้องขาวมอม (ยังไม่มีชื่อ)</span>
                  <span class="badge b-red" style="font-size:10px;">⚠️ เคสขอความช่วยเหลือ</span>
                </div>
                <div style="font-size:11px;color:#DC2626;margin-top:2px;">ขาหลังกะเผลก • นักศึกษาเพิ่งแจ้งพบเมื่อ 20 นาทีที่แล้ว</div>
                <div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px;">
                  <span class="badge" style="background:#FEE2E2;color:#991B1B;font-size:10px;">📍 ซอกบันไดตึกวิทย์ 2</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">วัคซีน: ไม่มีข้อมูล</span>
                  <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:10px;">เจ้าของ: ไม่มีข้อมูล</span>
                </div>
              </div>
            </div>
            <div style="margin-top:10px;padding:8px 10px;background:#FFF1F2;border:1px solid #FECDD3;border-radius:12px;font-size:11px;color:#991B1B;display:flex;justify-content:space-between;align-items:center;">
              <span style="font-weight:700;">● สัตวแพทย์อาสากำลังลงพื้นที่ตรวจ</span>
              <span style="color:#EF4444;font-weight:800;">แตะร่วมแจ้งข้อมูล ➜</span>
            </div>
          </div>

        </div>

        <!-- Floating Add Button -->
        <div data-go="S63" style="cursor:pointer;background:linear-gradient(135deg, #246BFD 0%, #1D4ED8 100%);color:#fff;padding:14px;border-radius:18px;text-align:center;font-size:14px;font-weight:700;box-shadow:0 8px 24px rgba(36,107,253,0.35);margin-top:4px;">
          ➕ ร่วมส่งข้อมูลวิกิ / รายงานพิกัดพบสัตว์ใหม่
        </div>

      </div>
    </div>
    """


def s62_animal_details_and_health():
    """62. ข้อมูลสัตว์ประจำวิทยาเขตและประวัติสุขภาพ (Animal Detail Profile & Health Log)"""
    return f"""
    <div class="scr">
      {sb()}
      <!-- Top App Bar -->
      <div class="bar" style="justify-content:space-between;padding:0 20px;border-bottom:1px solid #E2E8F0;background:#fff;">
        <div class="row" style="gap:10px;align-items:center;">
          <div class="ib" data-go="S61" style="cursor:pointer;background:#F8FAFC;border:1px solid #E2E8F0;">
            {ic("left", 18, C['navy'])}
          </div>
          <div>
            <div style="font-size:11px;color:#64748B;font-weight:600;">สารานุกรมสัตว์ประจำวิทยาเขต</div>
            <div style="font-size:16px;font-weight:800;color:{C['navy']};">ประวัติและสุขภาพ: พี่เตี้ย</div>
          </div>
        </div>
        <div class="row" style="gap:6px;">
          <div class="ib" data-go="S63" style="cursor:pointer;background:#EFF6FF;border:1px solid #DBEAFE;color:{C['blue']};" title="แก้ไขข้อมูลวิกิ">
            <span style="font-size:15px;">✏️</span>
          </div>
          <div class="ib" onclick="showToast('แชร์ลิงก์สารานุกรมพี่เตี้ยเรียบร้อยแล้ว')" style="cursor:pointer;background:#F8FAFC;border:1px solid #E2E8F0;color:{C['navy']};">
            {ic("share", 16, C['navy'])}
          </div>
        </div>
      </div>

      <!-- Scrollable Body Content -->
      <div class="body" style="padding:14px 18px 100px;gap:14px;overflow-y:auto;">

        <!-- Animal Profile Hero Card -->
        <div class="card" style="padding:18px;background:linear-gradient(135deg, #FFFBEB 0%, #FFFFFF 100%);border:1px solid #FDE68A;border-radius:24px;">
          <div class="row" style="gap:14px;align-items:center;">
            <div style="position:relative;width:80px;height:80px;border-radius:22px;background:linear-gradient(135deg,#FEF3C7,#FDE68A);display:flex;align-items:center;justify-content:center;font-size:44px;flex-shrink:0;box-shadow:0 8px 20px rgba(245,158,11,0.25);">
              🐕
              <div style="position:absolute;bottom:-3px;right:-3px;width:22px;height:22px;border-radius:50%;background:#10B981;border:2.5px solid #fff;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:900;">✓</div>
            </div>
            <div>
              <div class="row" style="gap:6px;align-items:center;">
                <span style="font-size:18px;font-weight:900;color:{C['navy']};">พี่เตี้ย วิศวกรรมศาสตร์</span>
              </div>
              <div style="font-size:12px;color:#D97706;font-weight:600;margin-top:2px;">เตี้ยวิศวะ • พี่หล่อขวัญใจชาวตึกแดง</div>
              <div class="row" style="gap:6px;margin-top:6px;">
                <span class="badge b-blue" style="font-size:10px;">สุนัขพันธุ์ทาง</span>
                <span class="badge b-green" style="font-size:10px;">ทำหมันแล้ว</span>
                <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:10px;">เพศผู้</span>
              </div>
            </div>
          </div>
          <!-- Community Verification Pill -->
          <div style="margin-top:14px;padding:8px 12px;background:#ECFDF5;border:1px solid #A7F3D0;border-radius:12px;display:flex;align-items:center;gap:8px;font-size:11px;color:#047857;font-weight:600;">
            <span style="font-size:14px;">🛡️</span>
            <span>บันทึกข้อมูลและตรวจสอบโดย: ชมรมสวัสดิภาพสัตว์มหาวิทยาลัยศิลปากร</span>
          </div>
        </div>

        <!-- Strict Truthful Data Table ("ตัวใหนไม่มีข้อมูลตรงใหน เขียนว่าไม่มีข้อมูล อย่ามั่วเกิน") -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:8px;">
            <span style="font-size:13.5px;font-weight:800;color:{C['navy']};">ข้อมูลทะเบียนและประวัติความเป็นมา</span>
            <span class="badge" style="background:#F1F5F9;color:#64748B;font-size:9.5px;">มาตรฐานวิกิข้อเท็จจริง</span>
          </div>
          <div style="font-size:11px;color:#64748B;line-height:1.45;margin-bottom:12px;">
            * รายละเอียดใดที่ไม่สามารถยืนยันหลักฐานแน่ชัด จะระบุ <strong>"ไม่มีข้อมูล"</strong> เพื่อความโปร่งใสและถูกต้องตามความเป็นจริง
          </div>

          <!-- Fact Table Rows -->
          <div style="display:flex;flex-direction:column;gap:8px;font-size:12px;">
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">รหัสสารานุกรม</span>
              <span style="font-weight:700;color:{C['navy']};">SU-DOG-001</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">วันเกิดที่แน่ชัด</span>
              <span class="badge" style="background:#F1F5F9;color:#64748B;font-weight:700;">ไม่มีข้อมูล</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">อายุโดยประมาณ</span>
              <span style="font-weight:700;color:{C['navy']};">5-6 ปี (ประมาณตามสภาพฟันและกระดูก)</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">สายพันธุ์บรรพบุรุษ</span>
              <span class="badge" style="background:#F1F5F9;color:#64748B;font-weight:700;">ไม่มีข้อมูล (สายพันธุ์ผสม)</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">เลขไมโครชิปประจำตัว</span>
              <span class="badge" style="background:#F1F5F9;color:#64748B;font-weight:700;">ไม่มีข้อมูล</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">เจ้าของตามกฎหมาย</span>
              <span class="badge" style="background:#F1F5F9;color:#64748B;font-weight:700;">ไม่มีข้อมูล (สุนัขชุมชนของมหาวิทยาลัย)</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">น้ำหนักปัจจุบัน</span>
              <span style="font-weight:700;color:{C['navy']};">14.2 กก. (ชั่งเมื่อ 15 ก.ย. 2569)</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #F1F5F9;">
              <span style="color:#64748B;">สถานะทำหมัน</span>
              <span style="font-weight:700;color:#059669;">ทำหมันแล้ว (บากหูขวาเพื่อเป็นสัญลักษณ์)</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;">
              <span style="color:#64748B;">ผู้ดูแลหลักในพื้นที่</span>
              <span style="font-weight:700;color:{C['navy']};">ชมรมคนรักสัตว์ & ป้าร้านข้าวตึกวิศวะฯ</span>
            </div>
          </div>
        </div>

        <!-- Usual Territory & Hotspots -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:10px;">
            <span style="font-size:13.5px;font-weight:800;color:{C['navy']};">อาณาเขตประจำและจุดที่พบบ่อย</span>
            <span class="badge b-blue" style="font-size:9.5px;">เรดาร์พิกัด</span>
          </div>
          <!-- Territory Breakdown -->
          <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:10px;">
            <div style="background:#F8FAFC;padding:10px 12px;border-radius:12px;border:1px solid #E2E8F0;">
              <div class="row" style="justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:{C['navy']};">📍 จุดหลัก (80%): ใต้ถุนตึกวิศวกรรมศาสตร์</span>
                <span style="font-size:11px;font-weight:800;color:{C['blue']};">ม้านั่งหินอ่อน</span>
              </div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">ชอบนอนรับลมช่วง 07:30 - 09:30 น. และ 16:30 - 18:00 น.</div>
            </div>
            <div style="background:#F8FAFC;padding:10px 12px;border-radius:12px;border:1px solid #E2E8F0;">
              <div class="row" style="justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:{C['navy']};">📍 จุดรอง (15%): ลานจามจุรี สวนร่มรื่น</span>
                <span style="font-size:11px;font-weight:800;color:#059669;">ใต้ร่มเงา</span>
              </div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">มักไปเดินเล่นและทักทายนักศึกษาช่วงเย็น</div>
            </div>
            <div style="background:#F8FAFC;padding:10px 12px;border-radius:12px;border:1px solid #E2E8F0;">
              <div class="row" style="justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:{C['navy']};">📍 จุดเดินเล่น (5%): สะพานข้ามสระแก้ว</span>
                <span style="font-size:11px;font-weight:800;color:#D97706;">เดินตรวจตรา</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Feeding Guidelines & Health Warning -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:10px;">
            <span style="font-size:13.5px;font-weight:800;color:{C['navy']};">คู่มือการให้อาหาร & ข้อควรระวัง</span>
            <span class="badge b-red" style="font-size:9.5px;">คำเตือนสำคัญ</span>
          </div>

          <div style="display:flex;flex-direction:column;gap:8px;">
            <!-- Safe Foods -->
            <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:12px;padding:10px 12px;">
              <div style="font-size:11.5px;font-weight:800;color:#166534;margin-bottom:4px;">✅ อาหารที่อนุญาตให้ได้:</div>
              <div style="font-size:11px;color:#15803D;line-height:1.5;">
                • อาหารเม็ดสำเร็จรูปสำหรับสุนัขโตควบคุมน้ำหนัก<br>
                • อกไก่ต้มสุก หรือตับต้ม (ไม่ใส่เกลือ ไม่ใส่ซีอิ๊ว ไม่ปรุงรส)<br>
                • น้ำสะอาดบริสุทธิ์ (เติมในชามจุดทางการ)
              </div>
            </div>

            <!-- Forbidden Foods -->
            <div style="background:#FEF2F2;border:1px solid #FECACA;border-radius:12px;padding:10px 12px;">
              <div style="font-size:11.5px;font-weight:800;color:#991B1B;margin-bottom:4px;">❌ อาหารต้องห้ามเด็ดขาด (อันตรายถึงชีวิต):</div>
              <div style="font-size:11px;color:#B91C1C;line-height:1.5;">
                • กระดูกไก่ กระดูกหมู (เสี่ยงทิ่มแทงหลอดอาหารและกระเพาะ)<br>
                • ช็อกโกแลต โกโก้ ชา กาแฟ นมวัว หัวหอม กระเทียม องุ่น ลูกเกด<br>
                • อาหารปรุงรสเค็ม เผ็ด หรือขนมขบเคี้ยวของคน
              </div>
            </div>

            <!-- Health Note -->
            <div style="background:#FEF3C7;border:1px solid #FDE68A;border-radius:12px;padding:8px 12px;font-size:11px;color:#92400E;line-height:1.45;">
              ⚠️ <strong>ประกาศสุขภาพ:</strong> พี่เตี้ยได้รับอาหารครบ 2 มื้อต่อวันเป็นเวลาจากทีมผู้ดูแลแล้ว ขณะนี้น้ำหนักเกินเกณฑ์เล็กน้อย <strong>ของดให้อาหารเพิ่มเด็ดขาด</strong>
            </div>
          </div>
        </div>

        <!-- Medical & Vaccine History Log -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:10px;">
            <span style="font-size:13.5px;font-weight:800;color:{C['navy']};">ประวัติการรักษาและวัคซีน</span>
            <span class="badge b-green" style="font-size:9.5px;">อัปเดต 2568</span>
          </div>

          <div style="display:flex;flex-direction:column;gap:10px;">
            <!-- Record 1 -->
            <div style="display:flex;gap:10px;align-items:flex-start;">
              <div style="width:28px;height:28px;border-radius:50%;background:#ECFDF5;color:#10B981;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;">💉</div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;">
                  <span style="font-size:12px;font-weight:700;color:{C['navy']};">วัคซีนป้องกันโรคพิษสุนัขบ้า</span>
                  <span style="font-size:10px;color:#64748B;">15 มี.ค. 2568</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:1px;">ฉีดเข็มกระตุ้นประจำปี • น.สพ. กองอาคารสถานที่ • ปลอกคอเขียว</div>
              </div>
            </div>
            <!-- Record 2 -->
            <div style="display:flex;gap:10px;align-items:flex-start;">
              <div style="width:28px;height:28px;border-radius:50%;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;">💊</div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;">
                  <span style="font-size:12px;font-weight:700;color:{C['navy']};">หยอดหลังป้องกันเห็บหมัด & พยาธิ</span>
                  <span style="font-size:10px;color:#64748B;">15 ก.ย. 2567</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:1px;">ป้องกันพยาธิหนอนหัวใจและเห็บหมัดประจำไตรมาส</div>
              </div>
            </div>
            <!-- Record 3 -->
            <div style="display:flex;gap:10px;align-items:flex-start;">
              <div style="width:28px;height:28px;border-radius:50%;background:#F1F5F9;color:#64748B;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;">🩹</div>
              <div style="flex:1;">
                <div class="row" style="justify-content:space-between;">
                  <span style="font-size:12px;font-weight:700;color:{C['navy']};">ผ่าตัดทำหมันสุนัขชุมชน</span>
                  <span style="font-size:10px;color:#64748B;">12 ม.ค. 2565</span>
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:1px;">โครงการควบคุมประชากรสุนัข • แผลหายสนิท ปลอดภัย</div>
              </div>
            </div>
            <!-- Unknown record note -->
            <div style="background:#F8FAFC;padding:8px 10px;border-radius:8px;font-size:10.5px;color:#64748B;">
              ประวัติการตรวจเลือดคัดกรองโรคทางพันธุกรรม: <span style="font-weight:700;">ไม่มีข้อมูล</span>
            </div>
          </div>
        </div>

        <!-- Community Stories & Anecdotes -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:10px;">
            <span style="font-size:13.5px;font-weight:800;color:{C['navy']};">เรื่องเล่าจากชาวมหาวิทยาลัย</span>
            <span class="badge" style="background:#EFF6FF;color:{C['blue']};font-size:9.5px;">2 บันทึก</span>
          </div>

          <div style="display:flex;flex-direction:column;gap:8px;">
            <div style="background:#F8FAFC;padding:10px 12px;border-radius:12px;border:1px solid #F1F5F9;">
              <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:4px;">
                <span style="font-size:11px;font-weight:700;color:{C['navy']};">พี่ปีสี่ วิศวะฯ</span>
                <span style="font-size:10px;color:#94A3B8;">2 สัปดาห์ก่อน</span>
              </div>
              <div style="font-size:11.5px;color:#334155;line-height:1.45;">
                "พี่เตี้ยชอบนอนเฝ้าหน้าลิฟต์ตอนเช้า นักศึกษาคนไหนลูบหัวก่อนเข้าสอบมักจะได้เกรด A เป็นความเชื่อประจำคณะไปแล้วครับ"
              </div>
            </div>
            <div style="background:#F8FAFC;padding:10px 12px;border-radius:12px;border:1px solid #F1F5F9;">
              <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:4px;">
                <span style="font-size:11px;font-weight:700;color:{C['navy']};">น้องปีหนึ่ง คณะอักษรฯ</span>
                <span style="font-size:10px;color:#94A3B8;">เมื่อวานนี้</span>
              </div>
              <div style="font-size:11.5px;color:#334155;line-height:1.45;">
                "ตอน 17:00 น. พี่เตี้ยเดินมาส่งพวกเราที่ป้ายรถราง น่ารักและสุภาพมาก ไม่เคยกระโชกใส่ใครเลย"
              </div>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="row" style="gap:10px;">
          <div data-go="S63" style="flex:1;background:#fff;border:1.5px solid {C['blue']};color:{C['blue']};padding:12px;border-radius:16px;text-align:center;font-size:13px;font-weight:700;cursor:pointer;">
            📍 เช็กอินพิกัดที่พบวันนี้
          </div>
          <div data-go="S63" style="flex:1;background:linear-gradient(135deg,{C['blue']},{C['navy']});color:#fff;padding:12px;border-radius:16px;text-align:center;font-size:13px;font-weight:700;cursor:pointer;box-shadow:0 4px 14px rgba(36,107,253,0.3);">
            ✏️ เสนอแก้ไขข้อมูลวิกิ
          </div>
        </div>

      </div>
    </div>
    """


def s63_contribute_animal_sighting():
    """63. ร่วมแบ่งปันข้อมูลและรายงานพิกัดพบสัตว์ (Crowdsource Wiki Contribution & Sighting Report)"""
    return f"""
    <div class="scr">
      {sb()}
      <!-- Top App Bar -->
      <div class="bar" style="justify-content:space-between;padding:0 20px;border-bottom:1px solid #E2E8F0;background:#fff;">
        <div class="row" style="gap:10px;align-items:center;">
          <div class="ib" data-go="S61" style="cursor:pointer;background:#F8FAFC;border:1px solid #E2E8F0;">
            {ic("left", 18, C['navy'])}
          </div>
          <div>
            <div style="font-size:11px;color:#64748B;font-weight:600;">วิกิชุมชนนักศึกษา</div>
            <div style="font-size:16px;font-weight:800;color:{C['navy']};">ร่วมแบ่งปันข้อมูล & แจ้งพบสัตว์</div>
          </div>
        </div>
        <div class="ib" onclick="showToast('คู่มือการเขียนวิกิชุมชน: ระบุข้อมูลจริง ไม่แต่งเติม')" style="cursor:pointer;background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;">
          {ic("info", 18, "#64748B")}
        </div>
      </div>

      <!-- Scrollable Form Body -->
      <div class="body" style="padding:14px 18px 100px;gap:14px;overflow-y:auto;">

        <!-- Community Wiki Mission Banner -->
        <div class="card" style="padding:14px;background:linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);border:1px solid #BFDBFE;border-radius:20px;">
          <div class="row" style="gap:10px;align-items:flex-start;">
            <div style="width:36px;height:36px;border-radius:10px;background:{C['blue']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;">
              🤝
            </div>
            <div>
              <div style="font-size:13px;font-weight:800;color:#1E40AF;">พลังวิกิชุมชนเพื่อสวัสดิภาพสัตว์มอ</div>
              <div style="font-size:11px;color:#1E3A8A;margin-top:2px;line-height:1.45;">
                ร่วมกันรายงานพิกัดล่าสุด หรือแจ้งพบสัตว์บาดเจ็บ เพื่อให้เพื่อนนักศึกษาและทีมสัตวแพทย์ดูแลได้อย่างทันท่วงที
              </div>
            </div>
          </div>
        </div>

        <!-- Strict Truthful Data Notice Rule -->
        <div style="background:#FEF3C7;border-left:3.5px solid #F59E0B;border-radius:10px;padding:10px 12px;font-size:11.5px;color:#92400E;line-height:1.45;">
          ⚠️ <strong>กฎสำคัญของวิกิชุมชน:</strong> ช่องใดที่ไม่ทราบข้อมูลแน่ชัด เช่น วันเกิด สายพันธุ์ หรือประวัติวัคซีน ให้เลือกหรือพิมพ์ว่า <span style="background:#FDE68A;color:#78350F;padding:1px 6px;border-radius:4px;font-weight:700;">ไม่มีข้อมูล</span> โดยเด็ดขาด ห้ามแต่งเติมข้อมูลที่ไม่ตรงกับความเป็นจริง
        </div>

        <!-- Form Section -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;display:flex;flex-direction:column;gap:14px;">

          <!-- 1. Report Type -->
          <div>
            <div style="font-size:12px;font-weight:700;color:{C['navy']};margin-bottom:6px;">1. วัตถุประสงค์การรายงาน</div>
            <div class="row" style="gap:6px;">
              <div style="flex:1;padding:8px 6px;background:#EFF6FF;border:1.5px solid {C['blue']};border-radius:10px;text-align:center;font-size:11px;font-weight:700;color:{C['blue']};cursor:pointer;">
                📍 แจ้งพิกัดที่พบ
              </div>
              <div style="flex:1;padding:8px 6px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;text-align:center;font-size:11px;font-weight:600;color:#64748B;cursor:pointer;">
                ➕ เสนอเพิ่มสัตว์ใหม่
              </div>
              <div style="flex:1;padding:8px 6px;background:#FEF2F2;border:1px solid #FECACA;border-radius:10px;text-align:center;font-size:11px;font-weight:700;color:#DC2626;cursor:pointer;">
                🚨 บาดเจ็บ/ขอยา
              </div>
            </div>
          </div>

          <!-- 2. Select Animal -->
          <div>
            <div style="font-size:12px;font-weight:700;color:{C['navy']};margin-bottom:6px;">2. เลือกสัตว์ในสารานุกรม (หรือระบุหากเป็นตัวใหม่)</div>
            <select id="animal_select_dropdown" style="width:100%;padding:10px 12px;background:#F8FAFC;border:1px solid #CBD5E1;border-radius:12px;font-size:13px;color:{C['navy']};font-weight:600;outline:none;">
              <option value="tia">พี่เตี้ย คณะวิศวกรรมศาสตร์</option>
              <option value="som">เจ้าส้มซ่า คณะอักษรศาสตร์</option>
              <option value="gon">พี่ก้อน แห่งสระแก้ว (ตัวเงินตัวทอง)</option>
              <option value="chao">น้องเฉาก๊วย ป้อม รปภ. ประตูหน้า</option>
              <option value="peacock">นกยูงหลวง ประจำพระราชวังสนามจันทร์</option>
              <option value="new">➕ สัตว์ตัวใหม่ (ยังไม่มีชื่อในระบบ)</option>
            </select>
          </div>

          <!-- 3. Sighting Location -->
          <div>
            <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:6px;">
              <span style="font-size:12px;font-weight:700;color:{C['navy']};">3. พิกัดและสถานที่ที่พบ</span>
              <span onclick="autoFillAnimalGPS()" style="font-size:11px;color:{C['blue']};font-weight:700;cursor:pointer;">📍 ใช้ GPS สด</span>
            </div>
            <input id="animal_loc_input" type="text" value="ใต้โต๊ะม้าหินอ่อน ใกล้ตู้เต่าบิน คณะวิศวกรรมศาสตร์" style="width:100%;box-sizing:border-box;padding:10px 12px;background:#F8FAFC;border:1px solid #CBD5E1;border-radius:12px;font-size:13px;color:#101C36;outline:none;">
          </div>

          <!-- 4. Date and Time -->
          <div>
            <div style="font-size:12px;font-weight:700;color:{C['navy']};margin-bottom:6px;">4. วันที่และเวลาที่สังเกตเห็น</div>
            <input type="text" value="15 ตุลาคม 2569 เวลา 14:35 น. (ปัจจุบัน)" readonly style="width:100%;box-sizing:border-box;padding:10px 12px;background:#F1F5F9;border:1px solid #E2E8F0;border-radius:12px;font-size:12.5px;color:#475569;outline:none;">
          </div>

          <!-- 5. Behavior & Observed Status -->
          <div>
            <div style="font-size:12px;font-weight:700;color:{C['navy']};margin-bottom:6px;">5. สภาพและพฤติกรรมที่สังเกตเห็น</div>
            <div class="row" style="gap:6px;flex-wrap:wrap;">
              <span class="badge" style="background:#EFF6FF;color:{C['blue']};border:1px solid #BFDBFE;padding:5px 10px;border-radius:8px;font-size:11px;font-weight:700;cursor:pointer;">✓ ร่าเริง/ปกติ</span>
              <span class="badge" style="background:#F8FAFC;color:#64748B;border:1px solid #E2E8F0;padding:5px 10px;border-radius:8px;font-size:11px;cursor:pointer;">กำลังนอนหลับ</span>
              <span class="badge" style="background:#F8FAFC;color:#64748B;border:1px solid #E2E8F0;padding:5px 10px;border-radius:8px;font-size:11px;cursor:pointer;">กำลังกินอาหาร</span>
              <span class="badge" style="background:#F8FAFC;color:#64748B;border:1px solid #E2E8F0;padding:5px 10px;border-radius:8px;font-size:11px;cursor:pointer;">มีอาการซึม</span>
              <span class="badge" style="background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;padding:5px 10px;border-radius:8px;font-size:11px;cursor:pointer;">มีบาดแผล</span>
            </div>
          </div>

          <!-- 6. Photo Upload Preview -->
          <div>
            <div style="font-size:12px;font-weight:700;color:{C['navy']};margin-bottom:6px;">6. ภาพถ่ายปัจจุบัน (ช่วยยืนยันตัวตน)</div>
            <div style="border:2px dashed #CBD5E1;border-radius:16px;padding:14px;background:#F8FAFC;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;cursor:pointer;">
              <div style="width:40px;height:40px;border-radius:50%;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;font-size:20px;">
                📷
              </div>
              <span style="font-size:12px;font-weight:700;color:{C['navy']};">แตะเพื่อถ่ายรูป หรือเลือกรูปจากคลัง</span>
              <span style="font-size:10.5px;color:#94A3B8;">แนบแล้ว 1 รูป: พี่เตี้ย_นอนหน้าตึก_1435.jpg (1.8 MB)</span>
            </div>
          </div>

          <!-- 7. Additional Wiki Details -->
          <div>
            <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:6px;">
              <span style="font-size:12px;font-weight:700;color:{C['navy']};">7. รายละเอียดเพิ่มเติมสำหรับสารานุกรม</span>
              <span style="font-size:10.5px;color:#D97706;">ไม่ทราบให้เขียน "ไม่มีข้อมูล"</span>
            </div>
            <textarea id="animal_note_textarea" rows="3" style="width:100%;box-sizing:border-box;padding:10px 12px;background:#F8FAFC;border:1px solid #CBD5E1;border-radius:12px;font-size:12px;color:#101C36;outline:none;font-family:inherit;line-height:1.45;">สีขนสีน้ำตาลทอง หางกุดเล็กน้อย ขาหลังซ้ายมีรอยแผลเป็นเก่า นิสัยเป็นมิตร ไม่เห่าคนแปลกหน้า ส่วนประวัติโรคประจำตัว: ไม่มีข้อมูล</textarea>
          </div>

          <!-- 8. Contributor Identity -->
          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:10px 12px;">
            <div style="font-size:11px;font-weight:700;color:{C['navy']};margin-bottom:6px;">ข้อมูลผู้ร่วมแบ่งปัน:</div>
            <div class="row" style="gap:8px;align-items:center;">
              <input type="checkbox" id="anon_chk" style="width:16px;height:16px;">
              <label for="anon_chk" style="font-size:11.5px;color:#334155;cursor:pointer;">ส่งในนาม: ธนพล กิตติบำรุง (หรือติ๊กเพื่อไม่ระบุตัวตน)</label>
            </div>
          </div>

          <!-- Submit Button -->
          <div onclick="submitAnimalContribution()" style="background:linear-gradient(135deg, {C['blue']} 0%, #1D4ED8 100%);color:#fff;padding:14px;border-radius:16px;text-align:center;font-size:14px;font-weight:800;cursor:pointer;box-shadow:0 8px 20px rgba(36,107,253,0.35);">
            🚀 บันทึกและส่งข้อมูลเข้าสู่วิกิชุมชน
          </div>

        </div>

      </div>
    </div>
    """


def s64_animal_radar_and_welfare():
    """64. แผนที่เรดาร์และสวัสดิภาพสัตว์ในวิทยาเขต (Campus Animal Radar & Animal Welfare Fund)"""
    return f"""
    <div class="scr">
      {sb()}
      <!-- Top App Bar -->
      <div class="bar" style="justify-content:space-between;padding:0 20px;border-bottom:1px solid #E2E8F0;background:#fff;">
        <div class="row" style="gap:10px;align-items:center;">
          <div class="ib" data-go="S61" style="cursor:pointer;background:#F8FAFC;border:1px solid #E2E8F0;">
            {ic("left", 18, C['navy'])}
          </div>
          <div>
            <div style="font-size:11px;color:#64748B;font-weight:600;">สวัสดิภาพสัตว์และแผนที่</div>
            <div style="font-size:16px;font-weight:800;color:{C['navy']};">เรดาร์สัตว์ & กองทุนสวัสดิภาพ</div>
          </div>
        </div>
        <div class="ib" data-go="S63" style="cursor:pointer;background:#EFF6FF;border:1px solid #DBEAFE;color:{C['blue']};" title="แจ้งพิกัดด่วน">
          <span style="font-size:15px;">➕</span>
        </div>
      </div>

      <!-- Scrollable Body Content -->
      <div class="body" style="padding:14px 18px 100px;gap:14px;overflow-y:auto;">

        <!-- Campus Radar Live Map Card -->
        <div class="card" style="padding:14px;background:#fff;border:1px solid #E2E8F0;border-radius:24px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:10px;">
            <div class="row" style="gap:6px;align-items:center;">
              <span style="font-size:14px;font-weight:800;color:{C['navy']};">แผนที่เรดาร์พิกัดสัตว์แบบสด</span>
              <span class="badge b-green" style="font-size:9.5px;">● เรดาร์ทำงาน</span>
            </div>
            <span style="font-size:11px;color:#64748B;">ม.ศิลปากร สนามจันทร์</span>
          </div>

          <!-- Radar Visual Box -->
          <div style="position:relative;width:100%;height:190px;background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%);border-radius:18px;overflow:hidden;border:1px solid #334155;box-shadow:inset 0 2px 10px rgba(0,0,0,0.5);">
            <!-- Map Grid & Water Pond Visual -->
            <svg width="100%" height="100%" style="position:absolute;inset:0;">
              <defs>
                <pattern id="radar_grid" width="30" height="30" patternUnits="userSpaceOnUse">
                  <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#334155" stroke-width="0.5" opacity="0.4" />
                </pattern>
              </defs>
              <rect width="100%" height="100%" fill="url(#radar_grid)" />
              <!-- Sa Kaeo Pond -->
              <ellipse cx="180" cy="95" rx="60" ry="32" fill="#0284C7" opacity="0.35" stroke="#38BDF8" stroke-width="1.5" />
              <text x="180" y="99" fill="#7DD3FC" font-size="10" font-weight="700" text-anchor="middle">สระแก้ว</text>
              <!-- Campus Green Lawns -->
              <rect x="20" y="25" width="75" height="50" rx="10" fill="#065F46" opacity="0.4" stroke="#10B981" stroke-width="1" />
              <text x="57" y="54" fill="#6EE7B7" font-size="9" font-weight="600" text-anchor="middle">ตึกวิศวะฯ</text>
              <rect x="270" y="30" width="80" height="50" rx="10" fill="#831843" opacity="0.35" stroke="#F43F5E" stroke-width="1" />
              <text x="310" y="59" fill="#FDA4AF" font-size="9" font-weight="600" text-anchor="middle">ตึกอักษรฯ</text>
              <rect x="250" y="120" width="95" height="50" rx="10" fill="#0369A1" opacity="0.35" stroke="#38BDF8" stroke-width="1" />
              <text x="297" y="149" fill="#BAE6FD" font-size="9" font-weight="600" text-anchor="middle">ป้อมประตูหน้า</text>
            </svg>

            <!-- Animated Radar Sweep -->
            <div style="position:absolute;top:50%;left:50%;width:220px;height:220px;margin-top:-110px;margin-left:-110px;border-radius:50%;border:1px solid rgba(56,189,248,0.3);box-shadow:0 0 20px rgba(56,189,248,0.15);pointer-events:none;"></div>

            <!-- Pin 1: พี่เตี้ย (วิศวะฯ) -->
            <div data-go="S62" style="position:absolute;top:40px;left:48px;cursor:pointer;display:flex;flex-direction:column;align-items:center;">
              <div style="width:26px;height:26px;border-radius:50%;background:#F59E0B;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 10px #F59E0B;">🐕</div>
              <span style="background:rgba(15,23,42,0.85);color:#FDE68A;font-size:9.5px;font-weight:700;padding:2px 6px;border-radius:6px;margin-top:2px;">พี่เตี้ย</span>
            </div>

            <!-- Pin 2: เจ้าส้มซ่า (อักษรฯ) -->
            <div data-go="S62" style="position:absolute;top:45px;left:298px;cursor:pointer;display:flex;flex-direction:column;align-items:center;">
              <div style="width:26px;height:26px;border-radius:50%;background:#FB923C;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 10px #FB923C;">🐈</div>
              <span style="background:rgba(15,23,42,0.85);color:#FED7AA;font-size:9.5px;font-weight:700;padding:2px 6px;border-radius:6px;margin-top:2px;">เจ้าส้มซ่า</span>
            </div>

            <!-- Pin 3: พี่ก้อน (สระแก้ว) -->
            <div data-go="S62" style="position:absolute;top:80px;left:168px;cursor:pointer;display:flex;flex-direction:column;align-items:center;">
              <div style="width:26px;height:26px;border-radius:50%;background:#10B981;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 10px #10B981;">🦎</div>
              <span style="background:rgba(15,23,42,0.85);color:#A7F3D0;font-size:9.5px;font-weight:700;padding:2px 6px;border-radius:6px;margin-top:2px;">พี่ก้อน</span>
            </div>

            <!-- Pin 4: น้องเฉาก๊วย (ป้อม รปภ.) -->
            <div data-go="S62" style="position:absolute;top:130px;left:285px;cursor:pointer;display:flex;flex-direction:column;align-items:center;">
              <div style="width:26px;height:26px;border-radius:50%;background:#64748B;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 10px #64748B;">🐕‍🦺</div>
              <span style="background:rgba(15,23,42,0.85);color:#E2E8F0;font-size:9.5px;font-weight:700;padding:2px 6px;border-radius:6px;margin-top:2px;">น้องเฉาก๊วย</span>
            </div>

            <!-- Pin 5: น้องขาวมอม (เคสขอความช่วยเหลือ) -->
            <div data-go="S63" style="position:absolute;top:125px;left:65px;cursor:pointer;display:flex;flex-direction:column;align-items:center;">
              <div style="width:28px;height:28px;border-radius:50%;background:#EF4444;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 12px #EF4444;animation:pulseTarget 2s infinite;">🐶</div>
              <span style="background:#EF4444;color:#fff;font-size:9px;font-weight:800;padding:2px 6px;border-radius:6px;margin-top:2px;">⚠️ ขาวมอม</span>
            </div>
          </div>

          <!-- Radar Legend -->
          <div class="row" style="justify-content:space-between;margin-top:10px;font-size:10.5px;color:#64748B;padding:0 4px;">
            <span>🐕 สุนัข (7)</span>
            <span>🐈 แมว (6)</span>
            <span>🦎 สัตว์น้ำ/เลื้อยคลาน (3)</span>
            <span style="color:#DC2626;font-weight:700;">⚠️ ฉุกเฉิน (1)</span>
          </div>
        </div>

        <!-- Emergency Animal Medical Rescue Hotlines -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #FECACA;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:8px;">
            <div class="row" style="gap:8px;align-items:center;">
              <span style="font-size:18px;">🚨</span>
              <span style="font-size:13.5px;font-weight:800;color:#991B1B;">สายด่วนกู้ภัย & สัตวแพทย์ฉุกเฉิน</span>
            </div>
            <span class="badge b-red" style="font-size:9.5px;">24 ชั่วโมง</span>
          </div>
          <div style="font-size:11px;color:#B91C1C;margin-bottom:12px;">พบสัตว์บาดเจ็บรุนแรง ถูกรถชน หรือแสดงอาการดุร้ายผิดปกติ ติดต่อได้ทันที</div>

          <div style="display:flex;flex-direction:column;gap:8px;">
            <!-- Hotline 1 -->
            <a href="tel:034255099" style="text-decoration:none;display:flex;justify-content:space-between;align-items:center;background:#FEF2F2;border:1px solid #FECDD3;padding:10px 12px;border-radius:12px;">
              <div>
                <div style="font-size:12px;font-weight:800;color:#991B1B;">งานรักษาความปลอดภัย & กองอาคารสถานที่</div>
                <div style="font-size:10.5px;color:#B91C1C;">สายด่วน ม.ศิลปากร สนามจันทร์ (24 ชม.)</div>
              </div>
              <span style="background:#EF4444;color:#fff;font-size:11px;font-weight:800;padding:6px 12px;border-radius:8px;">📞 034-255-099</span>
            </a>
            <!-- Hotline 2 -->
            <a href="tel:034351901" style="text-decoration:none;display:flex;justify-content:space-between;align-items:center;background:#F8FAFC;border:1px solid #E2E8F0;padding:10px 12px;border-radius:12px;">
              <div>
                <div style="font-size:12px;font-weight:800;color:{C['navy']};">โรงพยาบาลสัตว์ กำแพงแสน (พันธมิตร)</div>
                <div style="font-size:10.5px;color:#64748B;">รับรักษาอุบัติเหตุฉุกเฉินตลอด 24 ชั่วโมง</div>
              </div>
              <span style="background:{C['navy']};color:#fff;font-size:11px;font-weight:800;padding:6px 12px;border-radius:8px;">📞 034-351-901</span>
            </a>
          </div>
        </div>

        <!-- Campus Stray Animal Welfare Fund -->
        <div class="card" style="padding:16px;background:linear-gradient(135deg, #FFFBEB 0%, #FFFFFF 100%);border:1px solid #FDE68A;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:8px;">
            <div class="row" style="gap:8px;align-items:center;">
              <span style="font-size:18px;">🐾</span>
              <span style="font-size:13.5px;font-weight:800;color:#92400E;">กองทุนสวัสดิภาพสัตว์จรจัดในมหาวิทยาลัย</span>
            </div>
            <span class="badge" style="background:#FEF3C7;color:#D97706;font-size:9.5px;">ตรวจสอบได้ 100%</span>
          </div>

          <!-- Financial Snapshot -->
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;">
            <div style="background:#fff;border:1px solid #FDE68A;border-radius:12px;padding:10px;text-align:center;">
              <div style="font-size:10.5px;color:#64748B;">ยอดกองทุนคงเหลือ</div>
              <div style="font-size:16px;font-weight:900;color:#B45309;margin-top:2px;">฿ 48,650.00</div>
            </div>
            <div style="background:#fff;border:1px solid #FDE68A;border-radius:12px;padding:10px;text-align:center;">
              <div style="font-size:10.5px;color:#64748B;">ค่าอาหาร & ยาเดือนนี้</div>
              <div style="font-size:16px;font-weight:900;color:{C['navy']};margin-top:2px;">฿ 12,400.00</div>
            </div>
          </div>

          <!-- Annual Medical & Care Stats -->
          <div style="font-size:11px;color:#78350F;line-height:1.5;margin-bottom:12px;background:rgba(254,243,199,0.5);padding:8px 10px;border-radius:10px;">
            📊 <strong>ผลงานสวัสดิภาพปี 2568:</strong> ฉีดวัคซีนป้องกันโรคแล้ว 42 ตัว • ผ่าตัดทำหมันสำเร็จ 18 ตัว • ส่งรักษาอุบัติเหตุจนหายดี 9 เคส
          </div>

          <!-- Donation Buttons -->
          <div class="row" style="gap:8px;">
            <div onclick="donateAnimalWelfare(50)" style="flex:1;background:#fff;border:1.5px solid #F59E0B;color:#D97706;padding:10px;border-radius:12px;text-align:center;font-size:12px;font-weight:800;cursor:pointer;">
              ❤️ ร่วมบริจาค ฿50
            </div>
            <div onclick="donateAnimalWelfare(100)" style="flex:1;background:linear-gradient(135deg,#F59E0B,#D97706);color:#fff;padding:10px;border-radius:12px;text-align:center;font-size:12px;font-weight:800;cursor:pointer;box-shadow:0 3px 10px rgba(245,158,11,0.3);">
              ❤️ ร่วมบริจาค ฿100
            </div>
          </div>
        </div>

        <!-- Official Campus Feeding Stations -->
        <div class="card" style="padding:16px;background:#fff;border:1px solid #E2E8F0;border-radius:20px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:10px;">
            <span style="font-size:13.5px;font-weight:800;color:{C['navy']};">จุดให้อาหารและน้ำสะอาดทางการ</span>
            <span class="badge b-blue" style="font-size:9.5px;">3 จุดหลัก</span>
          </div>

          <div style="display:flex;flex-direction:column;gap:8px;font-size:11.5px;color:#334155;">
            <div style="display:flex;gap:8px;align-items:center;background:#F8FAFC;padding:8px 10px;border-radius:10px;">
              <span>🥣</span>
              <div><strong>จุดที่ 1:</strong> ซุ้มข้างโรงอาหารกลาง (เติมอาหารเม็ดและน้ำสะอาด 08:00 & 16:30 น.)</div>
            </div>
            <div style="display:flex;gap:8px;align-items:center;background:#F8FAFC;padding:8px 10px;border-radius:10px;">
              <span>🥣</span>
              <div><strong>จุดที่ 2:</strong> ศาลาพักผ่อนริมสระแก้ว (สำหรับนกน้ำและสัตว์ป่า ห้ามให้อาหารเค็ม)</div>
            </div>
            <div style="display:flex;gap:8px;align-items:center;background:#F8FAFC;padding:8px 10px;border-radius:10px;">
              <span>🥣</span>
              <div><strong>จุดที่ 3:</strong> ลานจอดรถหลังคณะวิศวกรรมศาสตร์ (จุดดูแลสุนัขชุมชน)</div>
            </div>
          </div>
        </div>

      </div>
    </div>
    """
'''

# ---------------------------------------------------------------------------
# 2. SCREENS list entry for Row 15
# ---------------------------------------------------------------------------
row15_screens_entry = '''  # Row 15: Campus Animal Encyclopedia, Community Wiki & Welfare (Cols 0..3)
  ("S61", "61. สารานุกรมสัตว์และวิกิชุมชนมหาวิทยาลัย", s61_campus_animal_wiki, 14, 0, "สารานุกรมสัตว์ในมหาวิทยาลัย วิกิชุมชน และสวัสดิภาพสัตว์"),
  ("S62", "62. ข้อมูลสัตว์ประจำวิทยาเขตและประวัติสุขภาพ", s62_animal_details_and_health, 14, 1, ""),
  ("S63", "63. ร่วมแบ่งปันข้อมูลและรายงานพิกัดพบสัตว์", s63_contribute_animal_sighting, 14, 2, ""),
  ("S64", "64. แผนที่เรดาร์และสวัสดิภาพสัตว์ในวิทยาเขต", s64_animal_radar_and_welfare, 14, 3, ""),
'''

# ---------------------------------------------------------------------------
# 3. Connections for Row 15
# ---------------------------------------------------------------------------
row15_connections_entry = '''    # Row 15: Campus Animal Encyclopedia & Community Wiki Flow
    ("S07", "S61", "สารานุกรมสัตว์มหาวิทยาลัย", "bottom", "top"),
    ("S08", "S61", "เมนูวิกิสัตว์ & ชุมชน", "bottom", "top"),
    ("S61", "S62", "แตะดูประวัติ & สุขภาพสัตว์", "right", "left"),
    ("S62", "S61", "กลับสารานุกรมสัตว์", "left", "right"),
    ("S61", "S63", "ร่วมแจ้งพิกัด & เพิ่มข้อมูล", "right", "left"),
    ("S63", "S61", "ส่งข้อมูลเสร็จ -> กลับวิกิ", "left", "right"),
    ("S62", "S63", "อัปเดตข้อมูลตัวนี้", "top", "bottom"),
    ("S61", "S64", "เปิดแผนที่เรดาร์ & กองทุน", "right", "left"),
    ("S64", "S61", "กลับสารานุกรมสัตว์", "left", "right"),
    ("S61", "S07", "กลับหน้าหลัก", "left", "right"),
'''

# ---------------------------------------------------------------------------
# 4. Banner in S07 (Home)
# ---------------------------------------------------------------------------
s07_banner = '''        <!-- Campus Animal Wiki & Welfare Card Banner -->
        <div class="card" data-go="S61" style="background:linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);border:1px solid #FDE68A;padding:12px 14px;border-radius:16px;cursor:pointer;">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div class="row" style="gap:10px;align-items:center;">
              <div style="width:36px;height:36px;border-radius:10px;background:#F59E0B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 3px 10px rgba(245,158,11,0.35);">
                🐾
              </div>
              <div>
                <div style="font-size:13px;font-weight:700;color:#92400E;">สารานุกรมสัตว์ & วิกิชุมชนมหาวิทยาลัย</div>
                <div style="font-size:11px;color:#B45309;">เปิดดูประวัติพี่เตี้ย เจ้าส้ม พิกัดประจำ และร่วมแบ่งปันข้อมูล</div>
              </div>
            </div>
            <div style="display:flex;align-items:center;gap:4px;">
              <span class="badge" style="background:#F59E0B;color:#fff;font-size:10px;padding:2px 8px;border-radius:999px;">วิกิ</span>
              {ic("right", 16, "#92400E")}
            </div>
          </div>
        </div>
'''

# ---------------------------------------------------------------------------
# 5. Menu item in S08 (Drawer)
# ---------------------------------------------------------------------------
s08_menu_item = '        ("heart", "สารานุกรมสัตว์ & วิกิชุมชน", "S61", "วิกิสัตว์"),\n'

# ---------------------------------------------------------------------------
# 6. JavaScript helper functions for Animal Wiki
# ---------------------------------------------------------------------------
animal_js = '''
      // 11. Campus Animal Wiki & Crowdsourcing Mechanics (S61, S62, S63, S64)
      window.filterAnimalCat = function(cat) {
        document.querySelectorAll('.animal-filter-chip').forEach(function(ch) {
          ch.classList.remove('on');
          ch.style.background = '#fff';
          ch.style.color = (ch.getAttribute('data-cat') === 'help') ? '#DC2626' : '#64748B';
          ch.style.borderColor = (ch.getAttribute('data-cat') === 'help') ? '#FECACA' : '#E2E8F0';
          if (ch.getAttribute('data-cat') === cat) {
            ch.classList.add('on');
            ch.style.background = (cat === 'help') ? '#DC2626' : '#246BFD';
            ch.style.color = '#fff';
            ch.style.borderColor = (cat === 'help') ? '#DC2626' : '#246BFD';
          }
        });

        document.querySelectorAll('.animal-entry-card').forEach(function(card) {
          var cCat = card.getAttribute('data-cat');
          if (cat === 'all' || cCat === cat) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      };

      window.searchAnimalWiki = function(query) {
        var q = (query || '').toLowerCase().trim();
        var clr = document.getElementById('animal_search_clear');
        if (clr) clr.style.display = q ? 'block' : 'none';

        document.querySelectorAll('.animal-entry-card').forEach(function(card) {
          var text = (card.innerText || '').toLowerCase() + ' ' + (card.getAttribute('data-name') || '').toLowerCase();
          if (!q || text.indexOf(q) !== -1) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      };

      window.clearAnimalSearch = function() {
        var inp = document.getElementById('animal_search_input');
        if (inp) inp.value = '';
        var clr = document.getElementById('animal_search_clear');
        if (clr) clr.style.display = 'none';
        filterAnimalCat('all');
      };

      window.autoFillAnimalGPS = function() {
        var inp = document.getElementById('animal_loc_input');
        if (inp) {
          inp.value = 'พิกัด GPS: 13.8197° N, 100.0435° E (หน้าลานจามจุรี คณะวิศวกรรมศาสตร์)';
        }
        showToast('📍 ดึงพิกัดจากระบบดาวเทียม GPS สำเร็จแล้ว');
      };

      window.submitAnimalContribution = function() {
        showToast('🎉 บันทึกข้อมูลเข้าสู่วิกิชุมชนเรียบร้อยแล้ว! ทีมงานจะตรวจสอบและยืนยันข้อมูล');
        setTimeout(function() {
          jumpToScreen('S61');
        }, 1200);
      };

      window.donateAnimalWelfare = function(amount) {
        showToast('❤️ ขอบคุณที่ร่วมสมทบทุนค่าอาหาร & ทำหมันสัตว์ ฿' + amount + ' ผ่าน Camplus Wallet สำเร็จ!');
      };
'''

# ---------------------------------------------------------------------------
# APPLY PATCHES
# ---------------------------------------------------------------------------

# Insert screen functions before SCREENS = [
screens_marker = "SCREENS = ["
if screens_marker in content and "def s61_campus_animal_wiki" not in content:
    content = content.replace(screens_marker, s61_s64_code + "\n" + screens_marker, 1)
    print("Inserted screen functions for S61-S64.")

# Insert screens list entry into SCREENS = [
m_s60 = re.search(r'\(["\']S60["\'],.*?\n', content)
if m_s60 and '"S61"' not in content:
    idx = m_s60.end()
    content = content[:idx] + row15_screens_entry + content[idx:]
    print("Inserted S61-S64 into SCREENS list.")

# Insert connections into connections list
m_conn = re.search(r'\(["\']S57["\'],\s*["\']S07["\'],.*?\n', content)
if m_conn and '("S61", "S62"' not in content:
    idx = m_conn.end()
    content = content[:idx] + row15_connections_entry + content[idx:]
    print("Inserted Row 15 prototype connections.")

# Insert S07 Banner
emergency_banner_end = '<!-- Emergency & SOS Quick Access Card Banner -->'
if emergency_banner_end in content and "สารานุกรมสัตว์ & วิกิชุมชนมหาวิทยาลัย" not in content:
    content = content.replace(emergency_banner_end, s07_banner + "\n        " + emergency_banner_end, 1)
    print("Inserted Animal Wiki banner into S07 Home.")

# Insert S08 Menu Item
m_menu = re.search(r'\(["\']heart["\'],\s*.*?S57.*?\n', content)
if m_menu and "สารานุกรมสัตว์ & วิกิชุมชน" not in content:
    idx = m_menu.end()
    content = content[:idx] + s08_menu_item + content[idx:]
    print("Inserted Animal Wiki menu item into S08 Drawer.")

# Insert Javascript helpers before closing </script>
m_script = re.search(r'</script>', content)
if m_script and "filterAnimalCat" not in content:
    idx = m_script.start()
    content = content[:idx] + animal_js + "\n    " + content[idx:]
    print("Inserted Animal Wiki JavaScript mechanics.")

# Clean up any leftover stray tuples after generate_board()
tail_cleanup_pattern = r'if __name__ == "__main__":\s+generate_board\(\)\s+# Row 13: Emergency.*'
content = re.sub(tail_cleanup_pattern, 'if __name__ == "__main__":\n    generate_board()\n', content, flags=re.DOTALL)

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("generate_thai_suksa_flow.py updated successfully!")

