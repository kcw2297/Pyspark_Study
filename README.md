# RDD 설명

Resilient Distributed Dataset(RDD)는 Spark의 기본 데이터 구조입니다. RDD는 immutable한 분산 저장 객체로, 병렬 처리에 최적화되어 있습니다. 

## 주요 특징

1. **Immutable** : RDD는 immutable합니다. 즉, 한 번 생성된 후 변경이 불가능합니다. 변경을 원할 경우 새로운 RDD 객체를 생성해야 합니다.

2. **분산 처리** : RDD는 클러스터 안의 여러 노드에 분산되어 저장되기 때문에, 병렬 처리가 가능합니다.

3. **실패 복구** : 특정 노드의 task가 실패하더라도, 잃어버린 RDD 데이터는 새로운 실행을 통해 복구가 가능합니다.

4. **Lazy Evaluation** : RDD는 lazy evaluation 방식을 사용합니다. 즉, 실제 데이터 처리를 하기 전에 logical execution plan을 먼저 세운 후, action을 수행합니다.

5. **In-Memory Storage** : RDD는 메모리 내에 데이터를 캐시하는 것이 가능합니다. 이를 통해 반복 연산의 성능이 향상됩니다.

6. **타입 지정 가능** : 각 RDD 객체는 타입을 지정하여 생성이 가능합니다.

