# -*- coding: utf-8 -*-
# tushare token
TS_TOKEN = "df1add767608a3a3481997959084b942014f8ebb218878d631e5fc8b"


# symbol table
inustry_symbol_table = {
"000001":"上证指数",
"399001":"深证指数",
"399006":"创业板指",
"399005":"中小板指",
"880398":"医疗保健",
"880448":"电器仪表",
"880372":"食品饮料",
"880399":"家居用品",
"880380":"酿酒",
"880446":"电气设备",
"880390":"汽车类",
"880437":"通用机械",
"880422":"文教休闲",
"880431":"船舶",
"880351":"矿物制品",
"880464":"仓储物流",
"880400":"医药",
"880447":"工程机械",
"880310":"石油",
"880355":"日用化工",
"880497":"综合类",
"880430":"航空",
"880418":"传媒娱乐",
"880490":"通信设备",
"880440":"工业机械",
"880471":"银行",
"880387":"家用电器",
"880492":"元器件",
"880491":"半导体",
"880406":"商业连锁",
"880305":"电力",
"880476":"建筑",
"880452":"电信运营",
"880367":"纺织服饰",
"880344":"建材",
"880318":"钢铁",
"880493":"软件服务",
"880432":"运输设备",
"880350":"造纸",
"880335":"化工",
"880455":"供气供热",
"880459":"运输服务",
"880465":"交通设施",
"880424":"旅游",
"880456":"环境保护",
"880360":"农林牧渔",
"880482":"房地产",
"880453":"公共交通",
"880454":"水务",
"880494":"互联网",
"880324":"有色",
"880421":"广告包装",
"880489":"IT设备",
"880472":"证券",
"880474":"多元金融",
"880423":"酒店餐饮",
"880414":"商贸代理",
"880330":"化纤",
"880301":"煤炭",
"880473":"保险"
}

inustry_symbol_table_reverse = {
"上证指数":"000001",
"深证指数":"399001",
"创业板指":"399006",
"中小板指":"399005",
'医疗保健': '880398',
'电器仪表': '880448',
'食品饮料': '880372',
'家居用品': '880399',
'酿酒': '880380',
'电气设备': '880446',
'汽车类': '880390',
'通用机械': '880437',
'文教休闲': '880422',
'船舶': '880431',
'矿物制品': '880351',
'仓储物流': '880464',
'医药': '880400',
'工程机械': '880447',
'石油': '880310',
'日用化工': '880355',
'综合类': '880497',
'航空': '880430',
'传媒娱乐': '880418',
'通信设备': '880490',
'工业机械': '880440',
'银行': '880471',
'家用电器': '880387',
'元器件': '880492',
'半导体': '880491',
'商业连锁': '880406',
'电力': '880305',
'建筑': '880476',
'电信运营': '880452',
'纺织服饰': '880367',
'建材': '880344',
'钢铁': '880318',
'软件服务': '880493',
'运输设备': '880432',
'造纸': '880350',
'化工': '880335',
'供气供热': '880455',
'运输服务': '880459',
'交通设施': '880465',
'旅游': '880424',
'环境保护': '880456',
'农林牧渔': '880360',
'房地产': '880482',
'公共交通': '880453',
'水务': '880454',
'互联网': '880494',
'有色': '880324',
'广告包装': '880421',
'IT设备': '880489',
'证券': '880472',
'多元金融': '880474',
'酒店餐饮': '880423',
'商贸代理': '880414',
'化纤': '880330',
'煤炭': '880301',
'保险': '880473'
}

stock_table = {'证券': {'申万宏源': '000166', '东北证券': '000686', '锦龙股份': '000712', '国元证券': '000728', '国海证券': '000750', '广发证券': '000776', '长江证券': '000783', '山西证券': '002500', '国盛金控': '002670', '西部证券': '002673', '国信证券': '002736', '第一创业': '002797', '华西证券': '002926', '长城证券': '002939', '华林证券': '002945', '东方财富': '300059', '南京证券': '601990', '方正证券': '601901', '中国银河': '601881', '浙商证券': '601878', '光大证券': '601788', '中银证券': '601696', '华泰证券': '601688', '东吴证券': '601555', '国联证券': '601456', '兴业证券': '601377', '中原证券': '601375', '红塔证券': '601236', '国泰君安': '601211', '东兴证券': '601198', '天风证券': '601162', '财通证券': '601108', '太平洋': '601099', '中信建投': '601066', '招商证券': '600999', '东方证券': '600958', '中泰证券': '600918', '华安证券': '600909', '哈投股份': '600864', '海通证券': '600837', '华鑫股份': '600621', '西南证券': '600369', '华创阳安': '600155', '国金证券': '600109', '湘财股份': '600095', '国投资本': '600061', '中信证券': '600030'}}

stock_table_reverse = {'证券': {'000166': '申万宏源', '000686': '东北证券', '000712': '锦龙股份', '000728': '国元证券', '000750': '国海证券', '000776': '广发证券', '000783': '长江证券', '002500': '山西证券', '002670': '国盛金控', '002673': '西部证券', '002736': '国信证券', '002797': '第一创业', '002926': '华西证券', '002939': '长城证券', '002945': '华林证券', '300059': '东方财富', '601990': '南京证券', '601901': '方正证券', '601881': '中国银河', '601878': '浙商证券', '601788': '光大证券', '601696': '中银证券', '601688': '华泰证券', '601555': '东吴证券', '601456': '国联证券', '601377': '兴业证券', '601375': '中原证券', '601236': '红塔证券', '601211': '国泰君安', '601198': '东兴证券', '601162': '天风证券', '601108': '财通证券', '601099': '太平洋', '601066': '中信建投', '600999': '招商证券', '600958': '东方证券', '600918': '中泰证券', '600909': '华安证券', '600864': '哈投股份', '600837': '海通证券', '600621': '华鑫股份', '600369': '西南证券', '600155': '华创阳安', '600109': '国金证券', '600095': '湘财股份', '600061': '国投资本', '600030': '中信证券'}}

# inustry_symbol_table_reverse = {
# '房地产': '880482', '公共交通': '880453', '水务': '880454', '互联网': '880494', '有色': '880324', '广告包装': '880421', 'IT设备': '880489',
# '证券': '880472', '多元金融': '880474', '酒店餐饮': '880423', '商贸代理': '880414', '化纤': '880330', '煤炭': '880301', '保险': '880473'}

if __name__ == "__main__":
    reverse = {}
    for k, v in inustry_symbol_table.items():
        reverse[v] = k
    print(reverse)
