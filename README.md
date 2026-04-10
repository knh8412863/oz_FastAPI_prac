# oz_FastAPI_prac

FastAPI 프레임워크 숙달 및 API 서버 구축 실습을 위한 저장소입니다.

## 🚀 학습 핵심 요약
- **비즈니스 로직 분리**: 요청(Request)과 응답(Response) 모델을 별도 파일로 분리하여 코드 가독성 및 유지보수성 향상
- **데이터 유효성 검사**: Pydantic의 `Field`와 `BaseModel`을 사용하여 서버 수준에서의 데이터 정제 기능 구현
- **API 설계 매커니즘**: 
  - `Path Parameter`: 특정 자원 식별 (`/users/{user_id}`)
  - `Query Parameter`: 조건 기반 검색 (`/users/search`)
  - `Request Body`: 새로운 자원 생성 (`POST /users`)

## 🛠 주요 구현 기능

### 1. 사용자 관리 API
- **전체 조회 (GET)**: 등록된 모든 사용자 목록 반환
- **조건 검색 (GET)**: Query Parameter(`name`, `job`)를 활용한 선택적 데이터 검색
- **상세 조회 (GET)**: Path Parameter를 사용하여 1 이상의 정수 ID를 가진 사용자 식별 및 반환
- **회원 등록 (POST)**: `UserCreateRequest` 모델을 통해 이름을 2~10자 이내로 제한하고 신규 유저 데이터 추가

### 2. 데이터 모델링 (Pydantic)
- **`request.py`**: 클라이언트로부터 받는 데이터의 제약 조건 설정 (최소/최대 길이 등)
- **`response.py`**: 서버가 반환하는 데이터 규격 정의 (불필요하거나 민감한 정보 유출 방지)

## 📁 폴더 구조
- `main.py`: 서버 인스턴스 생성 및 전체 라우팅 로직 제어
- `request.py`: API 요청 시 필요한 Pydantic 기반 스키마 정의
- `response.py`: API 응답 시 반환할 데이터 규격 정의
- `.venv/`: 프로젝트 독립 실행을 위한 Python 가상환경

## 🏃 실행 및 테스트
1. 가상환경 활성화: `source .venv/bin/activate`
2. 서버 실행: `fastapi dev`
3. 대화형 API 문서 확인: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)