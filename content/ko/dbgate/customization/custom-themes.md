---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: ko
title: 사용자 지정 테마
weight: 10
---

DbGate는 유연한 테마 기능을 지원합니다. 다양한 UI 요소의 색상을 변경하여 나만의 테마를 만들 수 있습니다.

테마는 JSON 파일로 만들어집니다. 사용자 지정 테마를 만드는 가장 간단한 방법은 테마 AI 어시스턴트를 사용하는 것입니다.

## 테마 AI 어시스턴트
테마 AI 어시스턴트를 실행하려면 설정/테마를 연 다음 "Customize with AI assistant" 버튼을 클릭하세요.

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

테마 AI 어시스턴트는 지시에 따라 테마를 사용자 지정합니다. 어떤 색상을 어떻게 변경할지 지정할 수 있습니다. 예를 들어 "기본 색상을 초록색으로, 배경색을 진한 회색으로 만들어 줘"라고 말할 수 있습니다.

![screenshot](/screenshots/dbgate-green.png)

AI 어시스턴트로 테마를 생성하는 데는 몇 분이 걸리며, 약 280개의 변수가 생성됩니다. 테마가 생성된 후 "Apply Theme" 버튼을 클릭하면 새 테마를 사용할 수 있습니다. "Save theme" 버튼을 사용하여 테마를 JSON 파일로 저장할 수도 있습니다. 저장된 모든 테마는 테마 선택기에서 사용할 수 있습니다. 파일 위젯 {{< mdi "file" >}}에서 테마를 관리(이름 변경, 편집, 삭제)할 수도 있습니다.

## DbGate Cloud에서 테마 공유하기
DbGate Cloud를 사용하여 다른 DbGate 사용자와 테마를 공유할 수 있습니다. 테마를 공유하려면 [DbGate 지식 베이스 저장소](https://github.com/dbgate/dbgate-knowledge-base)에서 풀 리퀘스트를 생성하세요. 테마는 folder-Themes 디렉터리에 저장됩니다. 예시는 기존 테마를 참고하세요. 테마 JSON 파일을 해당 디렉터리에 복사한 후 풀 리퀘스트를 생성하기만 하면 됩니다. 풀 리퀘스트가 병합되면 테마 선택기에서 모든 DbGate 사용자가 해당 테마를 사용할 수 있습니다.
