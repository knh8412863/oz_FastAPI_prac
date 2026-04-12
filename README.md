# oz_FastAPI_prac

FastAPI 프레임워크 숙달 및 API 서버 구축 실습을 위한 저장소입니다.

## 🚀 학습 핵심 요약
- **의존성 주입(Dependency Injection)**: `Depends`와 `yield`를 활용한 세션 관리로 효율적인 리소스 할당 및 자동 종료 구현
- **ORM 기반 데이터베이스 연동**: SQLAlchemy를 통해 객체 지향적인 방식으로 SQLite DB 제어 및 데이터 영속성 확보
- **라우터 기반 모듈화**: `APIRouter`를 사용해 기능별 폴더 구조를 설계하여 유지보수성 극대화
- **비즈니스 로직 분리**: 스키마(Request/Response), 데이터 모델(Models), DB 설정(Connection)의 완전한 분리

## 🛠 주요 구현 기능

### 1. 사용자 관리 API (Database & DI 적용)
- **전체 조회 (GET)**: `Depends(get_session)`를 통해 주입된 세션으로 모든 사용자 목록 반환
- **조건 검색 (GET)**: 이름(`name`) 또는 직업(`job`) 필터를 통한 동적 쿼리 조회
- **상세 조회 (GET)**: 존재하지 않는 ID 조회 시 `404 Not Found` 예외 처리 구현
- **회원 등록 (POST)**: 새로운 사용자 객체 생성 후 `commit` 및 최신 정보 `refresh` 반환
- **정보 수정 (PATCH)**: 기존 사용자의 특정 필드(`job`)를 부분 수정하는 로직 구현
- **회원 삭제 (DELETE)**: `204 No Content` 상태 코드를 반환하며 즉시 삭제(Delete Statement) 처리

### 2. 데이터베이스 및 세션 전략
- **`get_session()`**: `yield` 키워드를 사용하여 API 요청 시 세션을 생성하고, 응답이 끝난 후 자동으로 `close()` 하도록 설계 (안전한 자원 관리)
- **Engine & SessionFactory**: `autocommit=False` 설정을 통해 명시적인 트랜잭션 관리 실습

## 📁 폴더 구조
- `main.py`: 서버 전체 설정 및 라우터 통합
- `database/`: DB 접속 엔진 및 세션 의존성(`get_session`) 관리
- `user/`: 유저 도메인 관련 로직 모듈화
  - `router.py`: API 엔드포인트 및 의존성 주입(`Depends`) 적용
  - `models.py`: SQLAlchemy 테이블 정의
  - `request.py / response.py`: Pydantic 기반 데이터 유효성 검증 모델
- `local.db`: 실시간 데이터가 저장되는 SQLite 데이터베이스 파일

## 🏃 실행 및 테스트
1. 가상환경 활성화: `source .venv/bin/activate`
2. 서버 실행: `fastapi dev`
3. 대화형 API 문서 확인: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)