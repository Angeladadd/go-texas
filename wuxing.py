import sxtwl

# 五行 mapping
gan_wuxing = {'甲':'木','乙':'木','丙':'火','丁':'火','戊':'土','己':'土','庚':'金','辛':'金','壬':'水','癸':'水'}
zhi_wuxing = {'寅':'木','卯':'木','巳':'火','午':'火','申':'金','酉':'金','亥':'水','子':'水','辰':'土','戌':'土','丑':'土','未':'土'}
wuxing_relation = {
    '木': {'生': '火', '克': '土', '被克': '金', '被生': '水'},
    '火': {'生': '土', '克': '金', '被克': '水', '被生': '木'},
    '土': {'生': '金', '克': '水', '被克': '木', '被生': '火'},
    '金': {'生': '水', '克': '木', '被克': '火', '被生': '土'},
    '水': {'生': '木', '克': '火', '被克': '土', '被生': '金'}
}

def gan_zhi(date):
    y, m, d = date.year, date.month, date.day
    ganzhi = sxtwl.fromSolar(y, m, d).getDayGZ()
    return gan_wuxing[ganzhi.tg], zhi_wuxing[ganzhi.dz]

def texas_fortune(date):
    _gan, _zhi = gan_zhi(date)
    gan, zhi = gan_wuxing[_gan], zhi_wuxing[_zhi]
    elements = {
        'money': 0, # 正偏财星影响
        'decision': 0, # 印星影响
        'risk': 0, # 官杀影响
        'mental': 0, # 比劫影响
    }

    # 财运分析（我克者为财）
    elements['money'] += (25 if wuxing_relation[gan]['克'] == gan else 0)
    elements['money'] += (15 if wuxing_relation[zhi]['克'] == zhi else 0)

    # 决策能力（生我者为印）
    elements['decision'] += (20 if wuxing_relation[gan]['被生'] == gan else 0)
    elements['decision'] += (10 if wuxing_relation[zhi]['被生'] == zhi else 0)

    # 风险控制（克我者为官杀）
    elements['risk'] += (30 if wuxing_relation[gan]['被克'] == gan else 0)
    elements['risk'] += (20 if wuxing_relation[zhi]['被克'] == zhi else 0)

    # 心理博弈（同我者为比劫）
    elements['mental'] += (15 if wuxing_relation[gan] == gan else 0)
    elements['mental'] += (10 if wuxing_relation[zhi] == zhi else 0)

    suitability = (
        elements['money'] * 0.4 +
        elements['decision'] * 0.3 +
        elements['mental'] * 0.2 -
        elements['risk'] * 0.3
    )
    return max(0, min(100, suitability)), elements

def texas_advice(suitability):
    return suitability >= 50





