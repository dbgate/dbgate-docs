---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: ko
title: AWS에 배포하기
subtitle: Amazon EC2 클러스터에 원클릭 배포
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

DbGate AWS 에디션은 Amazon Web Services(AWS) 환경에서의 데이터베이스 관리를 위해 특별히 설계된 협업형 다중 사용자 웹 플랫폼입니다. AWS 인프라를 활용하여 클라우드 환경에서 운영되는 조직의 팀 협업을 간소화합니다. 공유형 브라우저 기반 인터페이스는 AWS와 매끄럽게 통합되면서 협업, 데이터 접근 및 데이터베이스 관리를 단순하게 만들어 줍니다.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}AWS의 DbGate{{< /button >}}

## DbGate AWS 주요 기능
DbGate AWS는 DbGate Team Premium과 동일한 기능을 지원하지만, AWS에 최적화되어 있습니다

* AWS IAM 지원
* 사용자, 연결 및 역할 관리
* 데이터 탐색, 필터링 및 편집
* 데이터 가져오기 및 내보내기
* 시각적 쿼리 빌더

## 설치 과정
AWS에서의 설치는 매우 간단하며, 거의 원클릭 과정에 가깝습니다.

최상의 사용자 경험을 위해서는 t2.medium 인스턴스 유형을 권장하지만, 프리 티어에서 사용할 수 있는 t2.micro도 소수의 사용자에게는 충분합니다.

설치 후에는 관리자 비밀번호를 설정해야 하며, 그 다음 연결, 사용자, 역할을 관리하고 권한을 부여할 수 있습니다.

## 구독 및 라이선스
DbGate AWS는 AWS Marketplace를 통해 구독할 수 있으며, 가격은 선택한 인스턴스의 크기에 따라 결정됩니다. 인스턴스가 클수록 더 많은 동시 사용자를 지원합니다.

30일 무료 평가판을 통해 DbGate의 모든 기능을 사용할 수 있습니다. 평가 기간이 끝나면 선택한 인스턴스 크기에 따라 AWS의 요금제에 따라 청구됩니다. 모든 결제가 [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy) 구독을 통해 처리되므로 추가 라이선스는 필요하지 않습니다.

## DbGate AWS 업데이트
DbGate AWS는 전용 빌드를 사용하며 EC2의 가상 서버에서 직접 실행됩니다(docker와 같은 추가 가상화 계층이 없습니다). 자동 업그레이드 기능이 있어 시작 후 컨테이너가 최신 빌드를 요청하고, 발견되면 이전 버전을 교체합니다. 수동으로 업그레이드할 필요가 없습니다.

새 버전으로 EC2 컨테이너를 수동으로 새로 생성하면 새로운 데이터베이스를 갖게 되므로(내부 MySQL 데이터베이스는 컨테이너의 일부입니다), 연결과 사용자를 새 EC2 컨테이너로 옮기는 간단한 방법은 없습니다.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}AWS의 DbGate{{< /button >}}
