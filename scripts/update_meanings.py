#!/usr/bin/env python3
"""
Script to update meanings in N*kan.json files using final.csv dictionary.
"""

import csv
import glob
import json
import os
import re

CSV_PATH = os.path.expanduser('~/02_Community/06_Bunchaway/tu-dien-nhat-viet/final.csv')
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'data')

# Load CSV dictionary
csv_dict = {}
print(f"Loading dictionary from {CSV_PATH}...")
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            term = row[0].strip()
            meaning = row[1].strip()
            csv_dict[term] = meaning

print(f"Loaded {len(csv_dict)} dictionary terms.")

# Kana to Kanji mapping for words written in Kana in quiz files
kana_to_kanji = {
    'おおげさ': '大袈裟',
    'はまる': '嵌まる',
    'ところ': '所',
    'あふれる': '溢れる',
    'あみもの': '編み物',
    'あらわす': '著す',
    'おおざっぱ': '大雑把',
    'おかず': '菜',
    'おはよう': 'お早う',
    'おめでたい': 'お目出度い',
    'かけざん': '掛け算',
    'こくせき': '国籍',
    'こしらえる': '拵える',
    'しっぽ': '尻尾',
    'すまない': '済まない',
    'たんす': '箪笥',
    'ついで': '序で',
    'つまずく': '躓く',
    'でたらめ': '出鱈目',
    'ねじ': '螺子',
    'のこぎり': '鋸',
    'ばからしい': '馬鹿らしい',
    'ばね': '発条',
    'はめる': '嵌める',
    'ひゃっかじてん': '百科事典',
    'ふくめる': '含める',
    'ふざける': '巫山戯る',
    'まく': '巻く',
    'まざる': '混ざる',
    'まじる': '混じる',
    'まぜる': '混ぜる',
    'またぐ': '跨ぐ',
    'まぶた': '瞼',
    'みじめ': '惨め',
    'めちゃくちゃ': '滅茶苦茶',
    'めでたい': '目出度い',
    'めまい': '目眩',
    'もやす': '燃やす',
    'やかましい': '喧しい',
    'やかん': '薬缶',
    'やっつける': '遣っ付ける',
    'やむをえない': '止むを得ない',
    'わがまま': '我が儘',
    'こうよう もみじ': '紅葉',
}

# Direct definitions for conversational phrases, prefixes, suffixes, and geographical names
direct_definitions = {
    '～営': 'DOANH\nDo... vận hành, quản lý (ví dụ: công doanh, quốc doanh, tư doanh)',
    '～合せ': 'HỢP\nHiệp lại, kết hợp, tổng cộng',
    'てっぺん': 'Đỉnh, chóp, ngọn, đỉnh đầu',
    '行っていらっしゃい': 'Chúc đi bình an / Chúc một ngày tốt lành (lời chào người đi ra ngoài)',
    'おかけください': 'Xin mời ngồi',
    'おかげさまで': 'Nhờ ơn trời / Nhờ có bạn giúp đỡ',
    'おかまいなく': 'Xin đừng bận tâm vì tôi / Cứ tự nhiên',
    'お元気で': 'Bảo trọng nhé / Giữ gìn sức khỏe nhé',
    'お世話になりました': 'Cảm ơn bạn đã giúp đỡ tôi suốt thời gian qua',
    'お待ちください': 'Xin vui lòng đợi một chút',
    'おまちどおさま': 'Xin lỗi vì đã để quý khách/bạn phải chờ lâu',
    'ごめんください': 'Xin lỗi, có ai ở nhà không? / Cho hỏi có ai không?',
    'しつれいしました かん': 'Tôi đã thất lễ rồi / Xin thứ lỗi',
    'そのころ': 'Thời gian đó, dạo đó, hồi đó',
    'そのため': 'Do đó, vì lý do đó, bởi vậy',
    'そば': 'Mì soba (mì kiều mạch Nhật Bản)',
    'それなら': 'Nếu vậy thì..., Nếu thế thì...',
    'それはいけませんね かん': 'Thế thì không được rồi / Đáng tiếc thật',
    'たちまち': 'Ngay lập tức, trong tích tắc, đột nhiên',
    'とっくに': 'Từ lâu rồi, đã lâu lắm rồi',
    'ともかく': 'Dù sao đi nữa, khoan bàn tới',
    'なにしろ': 'Dù sao thì, bởi vì là...',
    'なんとも': 'Không... chút nào (khi đi với phủ định), thực sự là',
    'ひとまず': 'Tạm thời, trước mắt, hãy khoan',
    '防': 'PHÒNG\nPhòng chống, ngăn ngừa',
    'やたらに': 'Bừa bãi, thiếu suy nghĩ, quá mức',
    'やっぱり': 'Quả nhiên, đúng như dự đoán, rốt cuộc thì',
    '帯広': 'Thành phố Obihiro (thuộc Hokkaido, Nhật Bản)',
    '旭川': 'Thành phố Asahikawa (thuộc Hokkaido, Nhật Bản)',
    '十勝': 'Vùng Tokachi (thuộc Hokkaido, Nhật Bản)',
    '大雪山国立公園': 'Vườn quốc gia Daisetsuzan (Hokkaido, Nhật Bản)'
}

def lookup(kanji):
    k = kanji.strip()
    if k in direct_definitions:
        return direct_definitions[k]
    if k in csv_dict:
        return csv_dict[k]
    if k in kana_to_kanji and kana_to_kanji[k] in csv_dict:
        return csv_dict[kana_to_kanji[k]]
    
    cleaned = k.replace(' ', '').strip('～~')
    if cleaned in direct_definitions:
        return direct_definitions[cleaned]
    if cleaned in csv_dict:
        return csv_dict[cleaned]
    if cleaned.rstrip('な') in csv_dict:
        return csv_dict[cleaned.rstrip('な')]
    if cleaned in kana_to_kanji and kana_to_kanji[cleaned] in csv_dict:
        return csv_dict[kana_to_kanji[cleaned]]
    
    parts = [p.strip().strip('～~').rstrip('な') for p in re.split(r'[;、/]', cleaned) if p.strip()]
    for p in parts:
        if p in direct_definitions:
            return direct_definitions[p]
        if p in csv_dict:
            return csv_dict[p]
        if p in kana_to_kanji and kana_to_kanji[p] in csv_dict:
            return csv_dict[kana_to_kanji[p]]
    return None

json_files = sorted(glob.glob(os.path.join(DATA_DIR, 'N*kan.json')))
print(f"Found {len(json_files)} JSON files in {DATA_DIR}.")

total_all = 0
updated_all = 0

for jf in json_files:
    fname = os.path.basename(jf)
    with open(jf, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    file_total = len(data)
    file_updated = 0
    
    for item in data:
        k = item.get('kanji', '')
        meaning_vn = lookup(k)
        if meaning_vn:
            item['meaning'] = meaning_vn
            file_updated += 1
        else:
            print(f"WARNING: Unmatched kanji in {fname}: {k}")
            
    with open(jf, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ {fname}: Updated {file_updated}/{file_total} entries ({file_updated/file_total*100:.1f}%)")
    total_all += file_total
    updated_all += file_updated

print("=" * 50)
print(f"Migration completed! Total: {updated_all}/{total_all} ({(updated_all/total_all)*100:.2f}%)")
