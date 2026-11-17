하다가 모르겠을 때, 질문은 무조건 자세하게 내가 필요한 부분을 알 수 있게 물어볼 것. 
너무 포괄적으로 물어보면 내가 궁금한 게 아닌 점까지 미리 답지를 제시하려고 함.

~ 이거 왜 안 돼? 
    -> 이러면 자꾸 AI가 먼저 제작해서 줘버림.

지금 여기까지 ~이런 방식으로 생각해서 코드를 짰어. 근데 지금 ~이런 에러가 나고, 만약 돌아가고 있다고 하더라도 DB랑 연결이 안 되었어.
그렇다면 어떻게 하는 게 더 정확한 방식일까? 내가 생각하기에는 ~가 문제인 거 같은데, 어떻게 해결하는 게 좋을지 봐줄래? 
    -> 좀 더 자세하고 내 문제가 무엇인지 정확히 체크해주기. 하나씩 이해하는 게 주목적이기 때문.

Q&A
Q1. file_db.py에서 model_validate()를 쓰는 이유? 그게 무슨 뜻인 건지? 어떤 형식인 건지, 왜 쓰는 건지 잘 모르겠어.
    A1. DB모델을 스키마로 변환한다라는 뜻. (*강사님 코드에도 주석으로 달려있음.)
    FileSchemas.model_validate(fileTable)
    fileTable을 검사해서 FileSchemas 모양으로 만들어 줘 하고 시키는 것.

model_validate 없이 직접 옮겨 쓰면?
    
    result = FileSchemas(
        id = fileTable.id,
        filename = fileTable.filename
    )

fileTable은 SQLAlchemy가 만든 DB 전용 객체임. 그대로 돌리면 FastAPI가 JSON으로 바꾸다가 에러가 나거나 이상한 값이 섞일 수 있다. 그래서 필요한 칸만 깔끔하게 옮겨 적는 스키마로 바꿔주는 것이다. (영수증 같은 거임)

Q2. 코드를 읽어보고 어색하거나 이상한 부분이 있으면 알려줄래? 잘못된 부분이 아니라면 말하지 않아도 괜찮아. 더 편한 방식이나 그런 걸 알려달라는 게 아니야.
    A2. routes와 db에 적혀있는 저장과 기록 추가 방식이 충돌하고 있다. file_routes의 경우 wb write 모드로 binary를 연다고 적혀있음. 
    w는 파일이 없으면 새로 만들고, 이미 그 파일이 있다면 덮어쓴다. (추가가 아니라 아예 새롭게 생성, 이전 것은 삭제)
    DB에는 이름이 겹치는지 확인하지 않고 항상 새 행을 추가하게 되어 있음. id는 autoincrement라서 순서대로 자동으로 늘어난다.
    즉, unique 설정이 없기 때문에 같은 이름이 여럿 있어도 DB에 추가된다.
    -> routes는 덮어쓰기, db는 계속 추가로 동작하는 중!

Q2-1. 그럼 문제가 되는 코드를 해결하는 과정에서 생긴 질문이야. 
async def insert_file(filename : str, db : Session) -> FileInfo | None:
    exist_file =  ( 
                    db.query(file_model.FileInfo)
                    .filter( file_model.FileInfo.filename == file.filename )
                    .first()
                  )
    if exist_file:
        return None
이렇게 쓰면 되는 걸까? 아니면 이렇게 써도 오류가 난다면 어떤 게 문제인 거야? 지금 정확히 해결하는 방법을 잘 모르겠어. 문법이 틀린 거 같은데, 왜 틀린 건지 모르겠어.
    A2. user_db.insert 구조와 같은 모양을 하고 있음. 고칠 곳은 두 개! 
        1. file.filename -> filename (함수가 받은 문자열 변수 이름 그대로 넣어줘야함)
        2. 반환 타입 FileInfo -> Fileschemas
        
async def insert_file(filename : str, db : Session) -> Fileschemas | None:
    exist_file =  ( 
                    db.query(file_model.FileInfo)
                    .filter( file_model.FileInfo.filename == filename )
                    .first()
                  )
    if exist_file:
        return None

    fileTable = file_model.FileInfo(filename=filename)
    
    db.add(fileTable)
    db.commit()
    db.refresh(fileTable)
    return Fileschemas.model_validate(fileTable)

Q2-2. 처음에 쓴 FileInfo를 쓰는 방식은 따로 없을까? 눈에 익었던 방식으로 이렇게 썼던 거 같아서 적은 건데 Fileschemas로 받는 거라고 했잖아. 그럼 내가 왜 이걸 생각했는지 알 수 있을까?
A2-2. 그런 방식도 있음!

from models.file_model import FileInfo     # ← 이름을 직접 쓰려면 import 필요
async def insert_file(filename : str, db : Session) -> FileInfo | None:
    ...(중복 확인 그대로)...

    fileTable = FileInfo(filename=filename)
    db.add(fileTable)
    db.commit()
    db.refresh(fileTable)
    return fileTable          # ← 바꾸지 않고 DB 객체 그대로 돌려줌

다만 어디선가 한 번 바꿔야 한다. FileInfo는 DB 전용 객체! 사용자에게 JSON으로 보내기 직전에 스키마로 변환해주어야 한다. 바꾸지 않고 그대로 보내면 FastAPI가 JSON으로 만들다가 에러가 난다. QA 노트 Q1번과 같은 이유.

Q3. 이어서 잘못된 부분이 있다면 어떤 거라고? 짚어줘볼래? 
A3. return {"msg" : "업로드 성공", "filename" : result}
    result에는 insert_file이 돌려준 Fileschemas 상자가 들어있음. 상자 안에는 id와 filename이 같이 들어있다.
    {
        "msg": "업로드 성공",
        "filename": { "id": 1, "filename": "cat.png" }
    }
    id까지 들어간 파일 정보 전체가 들어감!

Q3-1. 그럼 여기서 FileInfo를 쓰는 거야?
A3-1. 써도 동작은 하지만 추천하지 않음! 프로젝트 안에 이미 FileInfo라는 클래스가 있음. result에 든 건 FileInfo가 아니라 Fileschemas 상자. 
      코드 읽는 사람이 보기에 DB 객체를 그대로 보내나? 에 대한 오해가 생길 수 있고, JSON 이름표는 소문자로 씀! 프론트엔드에서는 소문자로 쓰는 게 일반적!

Q4. 그럼 지금까지 내가 계속 헷갈리는 게 schemas랑 db 쪽을 반대로 이해하고 있어서인 걸까?
A4. 완전히 반대로 생각하고 있는 건 아님. 다만 model과 schemas를 자주 섞어서 쓰고 있음. id, filename을 둘 다 갖고 있어서 헷갈리는 듯하다.
    헷갈리는 부분을 만드는 순서 쪽에 적어두고 다시 공부하는 게 도움이 될 거 같음. 

    model(FileInfo) DB랑 이야기할 때만 쓴다! db 폴더 함수 안에서만 보인다.
    schemas(Fileschemas) 밖과 이야기할 때 쓴다. 요청을 받거나 응답을 보낼 때.
    model_validate는 둘 사이 경계에서 model을 schemas로 바꿔주는 일을 한다.


**모든 질문이 밖과 대화하는 자리에 model을 써서 나온 질문. 어떻게 방향이 뻗어나가는 건지 확인해서 잡아주면 될 듯.**