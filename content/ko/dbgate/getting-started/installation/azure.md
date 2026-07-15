---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: ko
title: Azure에 배포하기
weight: 20
---

DbGate Azure 에디션은 Azure 환경에서의 데이터베이스 관리를 위해 특별히 설계된 협업형 다중 사용자 웹 플랫폼입니다. Azure 인프라를 활용하여 클라우드 환경에서 운영되는 조직의 팀 협업을 간소화합니다. 브라우저 기반의 공유 인터페이스는 Azure와 매끄럽게 통합되면서 협업, 데이터 접근, 데이터베이스 관리를 단순화합니다.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}Azure의 DbGate{{< /button >}}


## DbGate Azure 주요 기능
DbGate Azure는 DbGate Team Premium과 동일한 기능을 지원하지만 Azure에 최적화되어 있습니다

* Azure 관리 ID 지원
* 사용자, 연결 및 역할 관리
* 데이터 탐색, 필터링 및 편집
* 데이터 가져오기 및 내보내기
* 비주얼 쿼리 빌더

## 설치 과정
Azure에서의 설치는 매우 간단하며, 거의 원클릭 과정입니다.

2 GB RAM 이상의 가상 머신을 권장합니다.

설치 후에는 관리자 비밀번호를 설정해야 하며, 그런 다음 연결, 사용자, 역할을 관리하고 권한을 부여할 수 있습니다.

## 구독 및 라이선스
DbGate Azure는 Azure Marketplace를 통해 구독할 수 있으며, 가격은 선택한 가상 머신의 프로세서 수에 따라 결정됩니다.

30일 무료 평가판을 통해 모든 DbGate 기능을 사용할 수 있습니다. 평가 기간이 끝나면 선택한 인스턴스 크기에 따라 Azure 요금제에 따라 청구됩니다. 모든 결제는 [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview) 구독을 통해 처리되므로 추가 라이선스는 필요하지 않습니다.

## DbGate Azure 업데이트
DbGate Azure는 전용 빌드를 사용하며 가상 서버에서 직접 실행됩니다(docker와 같은 추가 가상화 계층이 없습니다). 자동 업그레이드 기능이 있습니다. 시작 후 컨테이너가 최신 빌드를 요청하고, 발견되면 이전 버전을 교체합니다. 수동으로 업그레이드할 필요가 없습니다.

새 버전으로 가상 머신을 수동으로 새로 만들면 새 데이터베이스를 갖게 되므로(내부 MySQL 데이터베이스는 가상 머신의 일부입니다), 연결과 사용자를 새 가상 머신으로 옮기는 간단한 방법은 없습니다.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}Azure의 DbGate{{< /button >}}
