# oz_FastAPI_prac

FastAPI 프레임워크 숙달 및 비동기 기반 API 서버 구축 실습을 위한 저장소입니다. 
기초적인 CRUD부터 비동기 최적화 및 스레드 풀 제어까지의 과정을 포함합니다.

## 🚀 학습 핵심 요약
- **의존성 주입(Dependency Injection)**: `Depends`와 `yield`를 활용한 세션 관리로 효율적인 리소스 할당 및 자동 종료 구현
- **ORM 기반 데이터베이스 연동**: SQLAlchemy를 통해 객체 지향적인 방식으로 SQLite DB 제어 및 데이터 영속성 확보
- **비동기 프로그래밍(Async/Await)**: `aiosqlite`와 `AsyncSession`을 도입하여 I/O 바운드 작업의 성능 최적화
- **라우터 기반 모듈화**: `APIRouter`를 사용해 기능별 폴더 구조를 설계하여 유지보수성 극대화
- **비즈니스 로직 분리**: 스키마(Request/Response), 데이터 모델(Models), DB 설정(Connection)의 독립적 관리

## 🛠 주요 구현 기능

### 1. 사용자 관리 API (CRUD)
- **전체 조회 및 조건 검색**: `name`, `job` 필터를 통한 동적 쿼리 및 전체 목록 반환
- **회원 관리**: 회원 등록(POST), 상세 조회(GET), 정보 수정(PATCH), 회원 삭제(DELETE) 기능 구현
- **예외 처리**: 존재하지 않는 데이터 요청 시 `404 Not Found` 등 적절한 HTTP 상태 코드 반환

### 2. 비동기(Async) 및 성능 최적화 전략
- **Async Database Connection**: `create_async_engine`을 사용하여 데이터베이스 연결 비동기화 및 논블로킹 쿼리 실행
- **스레드 풀 제어 (Thread Pool)**: `anyio`를 통해 워커 스레드 풀의 크기를 조정하여 서버의 동시 처리 성능 향상
- **Sync-to-Async 브릿지**: `run_in_threadpool`을 사용하여 비동기를 지원하지 않는 외부 라이브러리나 동기 함수를 이벤트 루프 차단 없이 실행

## 📁 폴더 구조
- `main.py`: 서버 전체 설정, 라우터 통합 및 **Thread Pool/Lifespan** 설정
- `database/`: 
  - `connection.py`: 기존 동기 방식 세션 설정
  - `connection_async.py`: **신규 비동기 방식 세션 설정 (aiosqlite)**
- `user/`: 유저 도메인 로직
  - `router.py`: API 엔드포인트 정의 (동기 → **비동기 핸들러로 전환**)
  - `models.py` / `request.py` / `response.py`: 데이터 모델 및 스키마 관리
- `local.db`: `sqlite+aiosqlite` 프로토콜을 통해 액세스되는 SQLite 데이터베이스 파일

## 🏃 실행 및 테스트
1. **가상환경 활성화**:
   ```bash
   source .venv/bin/activate