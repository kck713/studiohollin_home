# STUDIO HOLLIN 리뉴얼 초안

2026 회사소개서와 studiohollin.com을 바탕으로 만든 정적 웹사이트입니다.
브랜드 이미지 강화, 대형 작품 이미지, 절제된 내비게이션을 중심으로 구성했습니다.

## 보기

`dist/index.html`을 브라우저로 열거나 `dist`에서 정적 웹 서버를 실행합니다.
현재 작업의 로컬 미리보기 주소는 http://127.0.0.1:8765/ 입니다.

## 구성

- 브랜드 메인 화면
- WORK: 분야 필터와 작품 그리드, 프로젝트 상세 페이지 173개, 검색과 더 보기
- ABOUT: 회사의 비전, 제작 철학, 브랜드 방향성
- EXPERTISE: 4가지 제작 분야와 관련 프로젝트
- CONTACT: 프로젝트 문의, 연락처와 위치
- 이메일·전화 연결, 회사소개서 PDF 다운로드
- 모바일 메뉴와 반응형 레이아웃

## 콘텐츠 기준

- 모든 프로젝트명·연도·역할·이미지는 제공된 회사소개서를 근거로 작성했습니다.
- 소개서 9–12, 14–24, 26–28쪽의 실적을 반영했습니다. 중복 3건을 병합한 173개 프로젝트이며, 7쪽의 필름도파민 레이블 제작 이력은 별도 표기했습니다. 개인 경력 페이지는 제외했습니다.
- 초안의 메인 비주얼과 갤러리는 PDF의 스틸 이미지입니다. 동영상 재생 기능은 제공하지 않습니다.
- 영문 히어로 보조 카피와 한국어 소개 문구 일부는 소개서의 방향성을 바탕으로 편집한 제안 문구입니다.
- 기존 운영 사이트와 도메인은 변경하지 않았습니다.

## 편집

페이지: `dist/index.html` / 디자인: `dist/style.css` / 프로젝트 데이터 및 동작: `dist/app.js`

메뉴 페이지: `dist/work.html`, `dist/about.html`, `dist/expertise.html`, `dist/contact.html`

메뉴 페이지 디자인과 동작: `dist/inner.css`, `dist/inner.js`

메뉴 및 상세 페이지 생성: `build-pages.py` / 프로젝트 데이터: `projects.json`
생성기를 수정한 뒤 Python으로 실행하면 메뉴 페이지와 상세 페이지를 재생성합니다.
홈은 디자인과 본문을 보존하고 메뉴 링크만 독립 페이지로 연결합니다.

## 검증 및 게시 상태

- 전체 178개 HTML 페이지의 로컬 파일 참조 검사 통과.
- 홈은 메뉴 링크 외 변경 없음 확인.
- 개인 소개 및 개인 경력 섹션 없음 확인.
- 로컬 WORK 페이지 HTTP 200 응답 확인.
- 2026-10-08 브라우저 검증: WORK 필터 결과 2개/4개, TWO SIDES 상세 이동, 모바일 메뉴 이동 및 Escape 닫기 확인. 390px 모바일에서 ABOUT·WORK·EXPERTISE·CONTACT와 대표 상세 화면 검토. 확인한 화면에서 가로 넘침 및 콘솔 오류 없음. 이메일·전화·PDF 링크 대상 확인(이메일 전송 및 전화 실행 안 함).
- 외부 Sites 게시 및 자료 업로드는 미승인 상태로 실행하지 않았습니다.

## 참고

- 기존 사이트: https://studiohollin.com/
- 디자인 참고: https://www.dstrict.com/
- 사용자 제공: 2026 주식회사 홀린 회사소개서_통합본.pdf

## 2026-10-12 전체 실적 업데이트

- `import-profile.py`: PDF 실적과 해당 셀 이미지 추출.
- `portfolio-coverage.json`: 원본 페이지와 각 프로젝트 대응, 중복 병합 기록.
- `heritage.json`: 필름도파민 레이블(2014–2024)의 분야별 제작 이력.
- 173개 고유 프로젝트, 130개 미디어 실적 셀의 누락 여부와 로컬 링크 검증.
- 브라우저에서 검색, 분야 필터, 더 보기 확인. 모바일 390px 검색 화면 확인.
- 영상 URL이 제공되지 않은 항목은 소개서의 스틸 이미지와 프로젝트 정보로 구성했습니다.

## 2026-10-13 이미지 교체

- 메뉴 페이지 상단 이미지, EXPERTISE 섹션, ABOUT 이미지를 제공된 STAYC·SIGNAL·HEARTCREAM·TWO SIDES 스틸로 교체.
- 홈 히어로의 작은 텍스트 라벨 제거.

## 2026-10-26 이미지 최적화

- 4K 원본 이미지를 2560px 폭 JPEG(품질 82)로 재압축. `stayc-pink`, `stayc-purple`은 투명 영역이 없어 PNG에서 JPG로 변환.
- 사용하지 않는 `heartcream-room.jpg` 삭제.
- 대형 이미지 합계 약 13.8MB → 0.9MB. WORK 첫 화면 이미지 4.7MB → 228KB.
- 178개 HTML 로컬 참조 검사 통과. WORK·EXPERTISE·CONTACT 1440px·390px 화면 확인, 가로 넘침 및 콘솔 오류 없음.

## 배포 (GitHub Pages)

`gh-pages` 브랜치는 `hollin-renewal/dist`만 담은 배포용 브랜치입니다. `main`에 변경을 병합한 뒤 저장소 루트에서 다음을 실행해 갱신합니다.

```
git subtree push --prefix hollin-renewal/dist origin gh-pages
```

## 2026-10-26 고화질 이미지 교체

- 사용자 업로드 원본 122장(`image-uploads/`)을 파일명(프로젝트명)으로 프로젝트와 매칭해 교체.
  - 기존 이미지 93장 교체, 이미지가 없던 LIVE 프로젝트 27개에 대표 이미지 추가(`project-<slug>.jpg`), 스탠스·창퀴즈온더블럭은 두 번째 장을 갤러리에 추가.
  - 2560px 이하 JPEG(품질 85)로 변환. 위아래 단색 여백(레터박스·흰 띠)은 잘라내고, 잘라낸 결과가 2.4:1보다 납작하면 사이트 배경색(#0b0b0b)으로 16:9에 맞춤.
- `image-replacement-list.xlsx` 해상도·상태 갱신. 남은 교체 대상 59장(주로 BRAND & PRODUCT, ARTIST & PERFORMANCE와 대표 프로젝트 갤러리).
- 178개 HTML 로컬 참조 검사 통과. WORK(LIVE·EVENT 필터), 상세, 홈, 390px 모바일 확인. 콘솔·요청 오류 없음.

## 2026-10-26 홈 SELECTED WORK 구성과 프로젝트 숨김

- 홈 SELECTED WORK를 ARTIST & PERFORMANCE 4개(STAYC, SIGNAL, HEARTCREAM, TWO SIDES)로 구성. 인물이 멀리 있거나 옆모습인 고화질 스틸을 대표 이미지로 사용하고, 홈 분야 필터는 제거.
  - 네 프로젝트의 기존 PDF 추출 이미지는 `projects.json`의 `archived_images`에 보관.
  - 홈 목록은 `projects.json`의 `"featured": 순서`로 정하며, `build-pages.py`가 `dist/app.js`를 갱신.
- 홈 히어로를 사용자 제공 SIGNAL 고화질 원본(`signal-hero.jpg`, 1920px)으로 교체.
- 대표 이미지가 없거나 가로 1280px 미만인 49개 프로젝트를 숨김(`"hidden": true`). 숨긴 프로젝트는 WORK 목록, 상세 페이지, NEXT PROJECT 연결에서 빠지고, 프로젝트가 없는 분야 필터(BRAND FILM)도 자동으로 사라짐.

### 숨긴 프로젝트 다시 보이기

1. `projects.json`에서 해당 프로젝트의 `"hidden": true` 줄을 지움 (고화질 이미지로 교체했다면 `image`도 함께 수정).
2. `python3 build-pages.py` 실행 → WORK 목록과 상세 페이지가 다시 생성됨.
3. `main` 반영 후 `gh-pages` 갱신.
