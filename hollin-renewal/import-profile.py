"""Import every company portfolio entry, retaining source page/cell provenance."""
from pathlib import Path
import json, re
import pdfplumber
import pypdfium2 as pdfium

root = Path(__file__).parent
source = root/'dist/assets/hollin-company-profile-2026.pdf'
pdf = pdfplumber.open(source)
render = pdfium.PdfDocument(str(source))
old = [p for p in json.loads((root/'projects.json').read_text(encoding='utf-8')) if p['slug'] in ['repeatm','lg-objet','stayc','aesop','yonsei-ibs','scl-conference','two-sides','signal','heartcream','partner-connect']]
featured = old[:]
projects = old[:]
# Existing project pages retain their URLs and galleries.
existing = {(14,1):'yonsei-ibs',(14,2):'aesop',(17,0):'repeatm',(17,4):'lg-objet'}
labels = {'brand':'BRAND & PRODUCT','corporate':'CORPORATE & INSTITUTION','media':'ARTIST & PERFORMANCE','event':'EVENT FILM','live':'LIVE & SYSTEM'}
for p in projects:
    p['sourcePage'] = {'repeatm':17,'lg-objet':17,'stayc':9,'aesop':14,'yonsei-ibs':14,'scl-conference':26,'two-sides':10,'signal':11,'heartcream':12,'partner-connect':26}[p['slug']]
    p['sourceType'] = 'portfolio'

def clean(s):
    s=s.replace('\n',' ').strip()
    for a,b in [('홍보영상','홍보 영상'),('스케치영상','스케치 영상'),('오프닝영상','오프닝 영상'),('기념영상','기념 영상'),('루핑영상','루핑 영상'),('제품홍보','제품 홍보'),('창업지원단',' 창업지원단 '),('서울과학기술대학교','서울과학기술대학교 '),('한양대학교','한양대학교 '),('SCL(서울의과학연구소)','SCL '),('새해인사의밤','새해 인사의 밤'),('사업설명회영상','사업설명회 영상')]: s=s.replace(a,b)
    for word in ['홍보','영상','행사','스케치','오프닝','루핑','기념','시스템','총괄','운영','송출','음향','단독','콘서트','창립','국제학술대회','개원식','사업설명회','토크콘서트','창업동아리','브이로그','퍼포먼스','제품','공간','갤러리','팝업스토어','성수동','가로수길점','루프탑','스타일랩','패션스케치','새해','송년회','인포그래픽','기술','소개','참가자','티저','특별강연','홈커밍데이','네트워킹데이','스페이스챌린지','급성심장정지','구급품질','향상','워크숍','정책발표대회','청소년회관','학술포럼','플라워','전시회','수료식','심포지엄','초청','유명인사','만남의장','의과대학','보건의료포럼','보건의료분과위원회','포럼','경진대회']:
        s=s.replace(word,' '+word+' ')
    for a,b in {'샤넬박서준':'샤넬 박서준','돌체앤가바나청하':'돌체앤가바나 청하','비오템류준열':'비오템 류준열','랑콤수지':'랑콤 수지','다이슨차은우':'다이슨 차은우','티르티르현빈':'티르티르 현빈','비디비치송지효':'비디비치 송지효','톰포드갓세븐진영':'톰포드 갓세븐 진영','코스모폴리탄메타황소윤':'코스모폴리탄 메타 황소윤','대한항공기내안전':'대한항공 기내 안전','동탄국제고':'동탄국제고 ','연세대IBS':'연세대 IBS','서울시립미술관x':'서울시립미술관 ×','LG 냉장고DIOS':'LG 냉장고 DIOS','샤넬넘버5':'샤넬 넘버5','헤라Urban':'헤라 Urban','맥홍콩':'맥 홍콩','아베다뉴트리플레니쉬조이':'아베다 뉴트리플레니쉬 조이','LG 청소기A9S':'LG 청소기 A9S','동인비싱글에센스':'동인비 싱글에센스','동인비하이드라바운스크림':'동인비 하이드라 바운스 크림','핏팻애견간식':'핏팻 애견간식','CNP 프로폴리스앰플':'CNP 프로폴리스 앰플','한성PC 건설':'한성PC건설','2022화물운전자의날':'2022 화물운전자의 날'}.items():s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()

coverage=[]
for n in range(14,25):
    page=pdf.pages[n-1]
    cols=4 if n in [14,15,16,19] else 5
    bands=[(265,315),(460,520)] if cols==4 else ([(211,249),(356,394)] if n==24 else [(203,241),(348,388),(492,535)])
    image_tops=[146,337] if cols==4 else ([118,263] if n==24 else [109,255,400])
    canvas=render[n-1].render(scale=2).to_pil()
    for row,(top,bottom) in enumerate(bands):
        for col in range(cols):
            cell=row*cols+col
            if n==24 and cell>=8:continue
            left=50+col*860/cols; right=left+860/cols
            title=clean(page.crop((left,top,right,bottom)).extract_text() or '')
            assert title, (n,cell)
            filename=f'portfolio-{n}-{cell+1}.jpg'
            # Crop the actual layout cell, including composited images and letterboxing.
            x=56+col*(215 if cols==4 else 172.7)
            y=image_tops[row]; w=204 if cols==4 else 157; h=115 if cols==4 else 89
            canvas.crop((int(x*2),int(y*2),int((x+w)*2),int((y+h)*2))).convert('RGB').save(root/'dist/assets'/filename,quality=92)
            if (n,cell) in existing:
                p=next(p for p in projects if p['slug']==existing[n,cell])
                p['sourceCell']=cell+1
                p['description']=title+' 프로젝트입니다.'
            else:
                category='event' if n>=20 else 'corporate' if n in [18,19] else 'brand' if n in [15,17] else 'media' if n==16 else 'corporate'
                if n==14 and cell in [2,3,4]:category='brand'
                if n==14 and cell==6:category='event'
                if n==16 and cell==6:category='brand'
                year=re.search(r'(?<!\d)20(?:21|22|23|24|25|26)(?!\d)',title)
                p=dict(slug=f'archive-{n}-{cell+1}',title=title,ko=title,category=category,label=labels[category],image=filename,scope='영상 제작',year=year.group() if year else '',gallery=[],description=title+' 프로젝트입니다.',sourcePage=n,sourceCell=cell+1,sourceType='portfolio')
                projects.append(p)
            coverage.append({'page':n,'cell':cell+1,'title':title,'slug':p['slug']})

# Live production is a separate scope from film production of the same event.
live_existing={'SCL40주년국제학술대회행사총괄진행':'scl-conference','한양대학교PARTNERCONNECT운영':'partner-connect'}
seen={}
for n in [26,27]:
    page=pdf.pages[n-1]
    for left,right in [(40,475),(475,950)]:
        text=page.crop((left,100,right,530)).extract_text() or ''
        for raw in text.split('\n'):
            if not raw.strip().startswith('•'):continue
            title=clean(raw.strip().lstrip('•').strip()).replace('선포식하품','선포식').replace('공군참조총장배','공군참모총장배')
            key=re.sub(r'\s+','',title)
            if '대한민국의학한림원학술포럼' in key:
                key='대한민국의학한림원학술포럼'
            if key in seen:
                coverage.append({'page':n,'title':title,'slug':seen[key],'duplicate':True});continue
            if key in live_existing:
                p=next(p for p in projects if p['slug']==live_existing[key])
            else:
                slug=f'live-{n}-{len(seen)+1}'
                scope=next((s for s in ['연출 및 시스템 총괄','무대 연출 총괄','음향, 시스템 총괄','행사 운영 총괄','시스템 총괄','음향, 송출','음향, 영상','행사 총괄','송출','음향','운영'] if re.sub(r'\s+','',s) in key),'라이브 프로덕션')
                year='2021' if '2021' in title else ''
                p=dict(slug=slug,title=title,ko=title,category='live',label=labels['live'],image='',scope=scope,year=year,gallery=[],description=title+' 프로젝트입니다.',sourcePage=n,sourceType='portfolio')
                projects.append(p)
            seen[key]=p['slug'];coverage.append({'page':n,'title':title,'slug':p['slug']})

heritage={
 '바이럴 광고':['샤넬','디올','랑콤','돌체앤가바나','톰포드','비오템','헤라','CNP','LG전자 A9S · DIOS · 오브제','아리따움','메타','SSG','셀럽 협업 바이럴'],
 '엔터테인먼트':['Teth · Fade · 최삼 · 화자 · Idiotape M/V','양양피아노 · 송영주 콘서트','아이돌 댄스 퍼포먼스','W매거진 샤넬탐구 시리즈','KT&G 상상패션런웨이'],
 '기업 홍보 · 행사':['다이슨 · 디올 · YSL 팝업스토어 홍보 영상','대한항공 기내 안전 영상','스타필드','이솝 가로수길','롯데 명동 페스티벌','연세대 IBS','한성PC건설'],
 '포토':['DAZED Korea','Arena Korea','NARS','MAC Hongkong','New Balance Korea','Daniel Wellington','Seoul Fashion Week']}
(root/'heritage.json').write_text(json.dumps(heritage,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'projects.json').write_text(json.dumps(projects,ensure_ascii=False,indent=2),encoding='utf-8')
coverage += [{'page':p['sourcePage'],'slug':p['slug'],'title':p['ko']} for p in featured if p['category']=='media']
coverage += [{'page':28,'title':t,'slug':next(p['slug'] for p in projects if t in p['title']) ,'duplicate':True} for t in ['정서주','이다온']]
(root/'portfolio-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(projects)} projects; {len(coverage)} source records; heritage separately attributed to Film Dopamine')
