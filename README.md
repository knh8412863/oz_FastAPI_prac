# oz_FastAPI_prac

FastAPI 프레임워크 숙달 및 API 서버 구축 실습을 위한 저장소입니다.

## 🚀 학습 핵심 요약
- **ORM 기반 데이터베이스 연동**: SQLAlchemy를 사용하여 Python 객체와 SQLite DB를 매핑하고 데이터 영속성 확보
- **라우터 기반 모듈화**: `APIRouter`를 사용해 기능별(User, 등)로 경로를 분리하여 대규모 프로젝트 구조 설계
- **비즈니스 로직 분리**: 요청(Request), 응답(Response), DB 설정(Connection), 모델(Models)을 독립적인 파일로 관리
- **HTTP 상태 코드 및 유효성 검사**: Pydantic 모델과 Path/Query Parameter를 활용한 견고한 데이터 검증

## 🛠 주요 구현 기능

### 1. 사용자 관리 API (Database 연동)
- **전체 조회 (GET)**: DB에 저장된 모든 사용자 목록 반환
- **조건 검색 (GET)**: Query Parameter(`name`, `job`) 기반 필터링 조회
- **회원 등록 (POST)**: `Session`을 통해 DB에 새로운 유저 정보를 `commit`하여 영구 저장
- **회원 수정 (PATCH)**: `update_user_handler`를 통한 기존 데이터의 일부 수정(Partial Update) 처리

### 2. 데이터베이스 설정 (SQLAlchemy)
- **Engine**: SQLite(`local.db`)와의 접속 및 커넥션 관리
- **Session**: `sessionmaker`를 사용하여 하나의 작업 단위(Transaction) 관리
- **Context Manager**: `with SessionFactory() as session:` 방식을 사용하여 세션의 자동 종료(Close) 보장

## 📁 폴더 구조 (업데이트)
- `main.py`: 서버 전체 설정 및 라우터 등록
- `database/`: DB 관련 로직 전용 폴더
  - `connection.py`: DB 엔진 및 세션 팩토리 설정
- `user/`: 사용자 관련 기능 모듈화 폴더
  - `router.py`: 사용자 관련 API 엔드포인트 정의
  - `request.py / response.py`: 전용 스키마 관리
- `local.db`: 데이터가 실제로 저장되는 SQLite 파일

## 🏃 실행 및 테스트
1. 가상환경 활성화: `source .venv/bin/activate`
2. 서버 실행: `fastapi dev`
3. 대화형 API 문서 확인: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)