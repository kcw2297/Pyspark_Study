

RDD 설명
Resilient Distributed Dataset, spark의 데이터 자료 구조입니다.
immutable한 분산 저장 객체이며 병렬처리가 가능합니다.
특징 1: immutable하기 때문에, 생성후 변경이 불가능합니다. 변경을 하려면 새로운 RDD 객체를 생성해야합니다.
특징 2: 클러스터 안의 여러 노드에 분산되어서 병렬처리가 가능합니다.
특징 3: 실패 복구가 가능합니다. 특정 노드의 task가 실패시, 잃어버린 RDD 데이터는 새실행으로 생성가능합니다.
특징 4: lazy evaluation, 데이터 처리 전, logical execution plan을 세운 후 action을 합니다.
특징 5: in-memory storage, RDD는 메모리에 캐시 가능합니다.
특징 6: 각 RDD 객체는 타입 지정이 가능합니다.