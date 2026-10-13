from pathlib import Path
import json, re, html

root = Path(__file__).parent
dist = root / 'dist'
projects = json.loads((root / 'projects.json').read_text(encoding='utf-8'))

def nav(active):
    return ''.join(f'<a href="{name.lower()}.html"'+(' aria-current="page"' if active == name else '')+f'>{name}</a>' for name in ['WORK','ABOUT','EXPERTISE','CONTACT'])

def page(title, active, content, description):
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — STUDIO HOLLIN</title><meta name="description" content="{description}"><link rel="icon" type="image/png" href="assets/studio-hollin-logo.png"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="inner.css?v=5"></head><body class="inner-page" id="top"><a class="skip" href="#main">콘텐츠로 이동</a><header><a class="brand" href="index.html" aria-label="스튜디오홀린 홈"><img src="assets/studio-hollin-logo.png" alt="STUDIO HOLLIN" width="454" height="355"></a><nav aria-label="주 메뉴">{nav(active)}</nav><button class="menu-toggle" aria-expanded="false" aria-controls="mobile-nav">MENU</button></header><nav id="mobile-nav" class="mobile-nav" aria-label="모바일 메뉴" hidden><a href="index.html">HOME</a>{nav(active)}</nav><main id="main">{content}</main><footer class="inner-footer"><div class="footer-main"><a class="brand" href="index.html"><img src="assets/studio-hollin-logo.png" alt="STUDIO HOLLIN" width="454" height="355"></a><nav aria-label="하단 메뉴"><a href="index.html">HOME</a>{nav(active)}</nav><a href="mailto:info@studiohollin.com">info@studiohollin.com</a></div><div class="footer-bottom"><p>© 2026 STUDIO HOLLIN. ALL RIGHTS RESERVED.</p><a href="#top">BACK TO TOP</a></div></footer><script src="inner.js?v=4"></script></body></html>'''

def write(name, title, active, content, description):
    (dist / name).write_text(page(title,active,content,description), encoding='utf-8')

def tile(p):
    title=html.escape(p['title']); ko=html.escape(p['ko'])
    visual=f'<img src="assets/{p["image"]}" alt="{ko}" loading="lazy" width="800" height="500">' if p['image'] else '<div class="archive-art" aria-hidden="true"><span>HOLLIN</span><span>LIVE<br>PRODUCTION</span></div>'
    return f'<a class="work-tile" data-category="{p["category"]}" data-search="{html.escape(p["title"]+" "+p["ko"]+" "+p["scope"],quote=True)}" href="project-{p["slug"]}.html">{visual}<div class="tile-copy"><p>{p["label"]} {p["year"]}</p><h2>{title}</h2><span>VIEW PROJECT</span></div></a>'

cta = '<section class="next-section"><p class="eyebrow">LET’S CREATE BEYOND</p><h2>다음 장면을 함께 만듭니다.</h2><a class="outline-button" href="contact.html">GET IN TOUCH</a></section>'

heritage_data=json.loads((root/'heritage.json').read_text(encoding='utf-8'))
heritage='<section class="heritage section"><p class="eyebrow">FILM DOPAMINE / 2014–2024</p><h2>필름도파민 레이블 제작 이력</h2><p>브랜드 영상부터 엔터테인먼트, 기업 홍보와 포토까지.</p><div class="heritage-grid">'+''.join('<article><h3>'+html.escape(k)+'</h3><ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in v)+'</ul></article>' for k,v in heritage_data.items())+'</div></section>'

work = f'''<section class="page-visual work-visual"><img src="assets/stayc-purple.png" alt="STAYC VCR의 보랏빛 우주 공간 장면" fetchpriority="high"><div class="visual-copy"><p class="eyebrow">SELECTED PROJECTS</p><h1>OUR WORK<span>.</span></h1><p>브랜드에서 무대까지. 이야기를 완성하는 제작.</p></div></section><section class="gallery-section" aria-label="프로젝트 갤러리"><div class="archive-intro"><p class="eyebrow">PROJECT ARCHIVE</p><h2>다양한 이야기, 하나의 제작 역량.</h2><label for="project-search">프로젝트 검색</label><input type="search" id="project-search" placeholder="브랜드, 프로젝트, 제작 분야 검색" autocomplete="off"></div><div class="gallery-toolbar"><div class="filters" role="group" aria-label="프로젝트 분야"><button data-filter="all" aria-pressed="true">ALL</button><button data-filter="brand" aria-pressed="false">BRAND FILM</button><button data-filter="corporate" aria-pressed="false">CORPORATE</button><button data-filter="event" aria-pressed="false">EVENT FILM</button><button data-filter="media" aria-pressed="false">ARTIST & PERFORMANCE</button><button data-filter="live" aria-pressed="false">LIVE & SYSTEM</button></div><p id="result-count" role="status">{len(projects)} PROJECTS</p></div><div class="work-wall">''' + ''.join(tile(p) for p in projects) + '</div><p id="empty-results" hidden>검색 결과가 없습니다. 다른 검색어나 분야를 선택해 주세요.</p><button id="load-more" class="outline-button" hidden>MORE PROJECTS</button></section>'+heritage+cta
write('work.html','WORK','WORK',work,'브랜드필름과 기업 홍보영상, 아티스트 콘텐츠와 라이브 프로덕션. 스튜디오홀린의 대표 프로젝트를 만나보세요.')

about = '''<section class="page-heading"><p class="eyebrow">ABOUT STUDIO HOLLIN</p><h1>WHO WE ARE<span>.</span></h1></section><section class="about-cinema"><img src="assets/signal-harmony.jpg" alt="SIGNAL의 메트로놈과 초록빛 파형 장면" fetchpriority="high"></section><section class="about-manifesto"><p class="eyebrow">ALL-IN-ONE PRODUCTION</p><h2>이야기를 발견하고,<br>경험으로 완성하다.</h2><p>브랜드필름부터 기업 홍보, 공연과 라이브까지.<br>기획·촬영·후반 제작·현장 운영을 연결합니다.</p></section><section class="editorial section"><p class="eyebrow">OUR VISION</p><div class="editorial-columns"><h2>기획부터 완성까지,<br>올인원 프로덕션.</h2><div><p class="lead">보이지 않는 세계관을<br>하나의 완전한 경험으로.</p><p>좋은 콘텐츠는 목적을 이해하는 기획과 치밀한 제작으로 완성됩니다. 홀린은 고객의 구상을 함께 나누고, 기획부터 제작과 연출까지 일관된 시선으로 연결합니다.</p><p>브랜드와 제품의 매력, 기업과 기관의 메시지, 아티스트와 공연의 이야기를 각 프로젝트에 맞는 영상과 현장 경험으로 만듭니다.</p></div></div></section><section class="principles section"><p class="eyebrow">HOW WE THINK</p><div class="principle-grid"><article><span>01 / STORY</span><h3>세계관을 읽다.</h3><p>브랜드와 기업, 아티스트가 전하고 싶은 이야기를 이해하고 목적에 맞는 콘셉트와 장면을 기획합니다.</p></article><article><span>02 / IMMERSION</span><h3>경계를 지우다.</h3><p>영상과 공간, 빛과 소리가 하나의 흐름으로 이어지는 몰입을 설계합니다.</p></article><article><span>03 / DIRECTION</span><h3>끝까지 연결하다.</h3><p>콘셉트에서 제작과 현장 연출까지. 처음의 구상이 관객에게 전해지는 순간을 함께합니다.</p></article></div></section><section class="philosophy section"><p class="eyebrow">OUR PHILOSOPHY</p><h2>CREATE<br><span>BEYOND.</span></h2><div><p>보이는 것 너머를 기획하고,<br>기대 너머를 완성한다.</p><a class="outline-button" href="expertise.html">OUR EXPERTISE</a></div></section>'''
write('about.html','ABOUT','ABOUT',about,'브랜드와 기업, 공연을 아우르는 올인원 프로덕션. 스튜디오홀린의 비전과 제작 철학.')

services = [
('01','CREATIVE<br>DIRECTION','보이는 것 너머를 기획합니다.','브랜드와 기업, 아티스트의 메시지를 이해하고 콘셉트 기획부터 영상·현장 연출까지 시각적 방향을 설계합니다.','콘셉트 기획 / 브랜드 스토리텔링 / 영상 · 현장 연출','heartcream-closeup.jpg','heartcream','HEARTCREAM'),
('02','MEDIA<br>PRODUCTION','스크린의 경계를 지웁니다.','브랜드필름, 제품 광고, 기업·기관 홍보영상부터 아티스트 콘텐츠와 공연 영상까지. 기획, 촬영, 편집과 후반 제작 전반을 다룹니다.','브랜드필름 · 제품 광고 / 기업 · 기관 홍보 / 아티스트 · 공연 콘텐츠','signal-metronome.jpg','signal','SIGNAL'),
('03','LIVE<br>PRODUCTION','영상과 무대가 교감합니다.','콘서트와 팬미팅, 컨퍼런스와 기업 행사. 무대 연출, 현장 운영, 라이브 송출을 하나의 흐름으로 연결합니다.','무대 연출 / 행사 운영 / 라이브 송출','stayc-pink.png','partner-connect','PARTNER CONNECT'),
('04','AUDIO VISUAL<br>PRODUCTION','정교한 빛과 소리로 완성합니다.','음향과 영상, LED와 현장 시스템을 설계하고 운영해 무대의 감정을 온전히 전달합니다.','음향 · 영상 / LED / 현장 시스템 설계 및 운영','signal-title.jpg',None,None)
]
expertise = '<section class="page-heading"><p class="eyebrow">OUR CAPABILITIES</p><h1>WHAT WE DO<span>.</span></h1><div class="heading-summary"><h2>하나의 비전. 완전한 프로덕션.</h2><p>콘셉트에서 현장까지,<br>모든 과정이 같은 방향을 향하도록.</p></div></section><nav class="service-nav" aria-label="제작 분야">'+''.join(f'<a href="#service-{s[0]}">{s[0]} {s[1].replace("<br>", " ")}</a>' for s in services)+'</nav>'
service_alts = {'01':'HEARTCREAM 인물 클로즈업 장면','02':'SIGNAL 메트로놈 장면','03':'STAYC VCR의 분홍빛 우주 공간 장면','04':'SIGNAL 타이틀 장면'}
for no,title,heading,body,tags,img,slug,project in services:
    link = f'<a class="text-link" href="project-{slug}.html">RELATED WORK / {project}</a>' if slug else '<a class="text-link" href="work.html?category=live">LIVE & SYSTEM WORK</a>'
    expertise += f'<section class="service-feature" id="service-{no}"><div class="service-photo"><img src="assets/{img}" alt="{service_alts[no]}" loading="lazy"></div><div class="service-description"><p class="eyebrow">{no} / EXPERTISE</p><h2>{title}</h2><h3>{heading}</h3><p>{body}</p><p class="service-tags">{tags}</p>{link}</div></section>'
expertise += cta
write('expertise.html','EXPERTISE','EXPERTISE',expertise,'기획, 미디어 제작, 라이브 연출, 오디오 비주얼 시스템까지 스튜디오홀린의 제작 역량.')

contact = '''<section class="page-heading contact-heading"><p class="eyebrow">LET’S TALK</p><h1>CONTACT<span>.</span></h1><div class="heading-summary"><h2>다음 장면의 시작,<br>홀린과 함께.</h2><p>만들고 싶은 콘텐츠와 프로젝트,<br>그 첫 구상부터 들려주세요.</p></div></section><section class="contact-panel"><div><p class="eyebrow">PROJECT INQUIRY</p><a class="inquiry-mail" href="mailto:info@studiohollin.com">info@studiohollin.com</a><p>프로젝트의 성격, 일정, 제작 범위를 알려주시면<br>더 구체적인 이야기를 나눌 수 있습니다.</p><a class="outline-button" href="mailto:info@studiohollin.com?subject=STUDIO%20HOLLIN%20프로젝트%20문의">이메일로 프로젝트 문의</a></div><div class="contact-details"><div><p class="eyebrow">CALL US</p><a href="tel:+82315702726">031-570-2726</a></div><div><p class="eyebrow">COMPANY PROFILE</p><a href="assets/hollin-company-profile-2026.pdf" download>2026 회사소개서 다운로드 <span>PDF</span></a></div></div></section><section class="studio-location"><img src="assets/two-sides-call.jpg" alt="TWO SIDES의 전화가 걸려오는 장면"><div><p class="eyebrow">STUDIO HOLLIN</p><h2>브랜드에서 현장까지,<br>함께 만드는 경험.</h2><address>경기도 남양주시 순화궁로 249<br>별내역 파라곤스퀘어 M동 713호</address></div></section>'''
write('contact.html','CONTACT','CONTACT',contact,'스튜디오홀린 프로젝트 문의. info@studiohollin.com · 031-570-2726.')

for i,p in enumerate(projects):
    nextp = projects[(i+1)%len(projects)]
    content = f'''<section class="project-heading"><a class="back-link" href="work.html">ALL PROJECTS</a><p class="eyebrow">{p['label']}</p><h1>{p['title']}</h1><p class="project-korean">{p['ko']}</p></section><figure class="project-cover"><img src="assets/{p['image']}" alt="{p['ko']} 대표 장면" fetchpriority="high"></figure><section class="project-story section"><dl><div><dt>CATEGORY</dt><dd>{p['label']}</dd></div>'''
    if not p['image']:
        content = re.sub(r'<figure class="project-cover">.*?</figure>', '', content)
    if p['year']: content += f'<div><dt>YEAR</dt><dd>{p["year"]}</dd></div>'
    content += f'<div><dt>SCOPE</dt><dd>{p["scope"]}</dd></div></dl><div><p class="eyebrow">OVERVIEW</p><h2>{p["ko"]}</h2><p>{p["description"]}</p></div></section>'
    if p['gallery']:
        content += '<section class="project-gallery" aria-label="프로젝트 제작 이미지">'+''.join(f'<figure><img src="assets/{img}" alt="{p["ko"]} 제작 이미지 {j+1}" loading="lazy"></figure>' for j,img in enumerate(p['gallery']))+'</section>'
    content += f'<section class="project-pagination"><a href="work.html">ALL PROJECTS</a><a href="project-{nextp["slug"]}.html"><span>NEXT PROJECT</span><strong>{nextp["title"]}</strong></a></section>'
    write(f'project-{p["slug"]}.html',p['title'],'WORK',content,p['description'])

# Preserve the entire home composition; change only navigation destinations.
index_path = dist / 'index.html'
home = index_path.read_text(encoding='utf-8')
def menu_links(match):
    s=match.group(0)
    for name in ['work','about','expertise','contact']:
        s=s.replace(f'href="#{name}"',f'href="{name}.html"')
    return s
home=re.sub(r'<nav\b.*?</nav>',menu_links,home,flags=re.S)
index_path.write_text(home,encoding='utf-8')
print(f'Created 4 menu pages and {len(projects)} project detail pages.')
