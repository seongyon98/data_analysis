# Brazilian E-Commerce Public Dataset by Olist 데이터 분석

---
**목차**
- [Brazilian E-Commerce Public Dataset by Olist 데이터 분석](#brazilian-e-commerce-public-dataset-by-olist-데이터-분석)
  - [데이터 정보](#데이터-정보)
    - [데이터 출처](#데이터-출처)
    - [데이터 설명](#데이터-설명)
  - [데이터 전처리](#데이터-전처리)
    - [결측치 처리](#결측치-처리)
      - [결측치 발견 데이터](#결측치-발견-데이터)
    - [기타 전처리](#기타-전처리)
      - [전처리 방법](#전처리-방법)
      - [전처리 Flow Chart](#전처리-flow-chart)
  - [가설 및 검증](#가설-및-검증)
    - [EDA를 통해 세운 가설](#eda를-통해-세운-가설)
      - [가설](#가설)
    - [가설 검증을 위한 시도(통계적 기법, 시각화 등) 및 검증 결과](#가설-검증을-위한-시도통계적-기법-시각화-등-및-검증-결과)
      - [가설 검증 및 검증 결과](#가설-검증-및-검증-결과)
        - [가설 검증 시도](#가설-검증-시도)
      - [검증 결과](#검증-결과)
---

## 데이터 정보
### 데이터 출처
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download&select=product_category_name_translation.csv)
### 데이터 설명
각 데이터 파일의 컬럼 및 의미

**Olist Customers Dataset**
| customer_id | customer_unique_id | customer_zip_code_prefix | customer_city  | customer_state |
| ----------- | ------------------ | ------------------------ | -------------- | -------------- |
| 고객 아이디 | 고객 고유 아이디   | 고객 우편번호            | 고객 거주 도시 | 주             |

**Olist Geolocation Dataset**
| geolocation_zip_code_prefix | geolocation_lat | geolocation_lng | geolocation_city | geolocation_state |
| --------------------------- | --------------- | --------------- | ---------------- | ----------------- |
| 좌표 우편번호               | 위도            | 경도            | 좌표 도시        | 좌표 주           |

**Olist Order Items Dataset**
| order_id  | order_item_id | product_id  | seller_id     | shipping_limit_date | price | freight_value |
| --------- | ------------- | ----------- | ------------- | ------------------- | ----- | ------------- |
| 주문 번호 | 주문 수량     | 제품 아이디 | 판매자 아이디 | 배송 기한           | 가격  | 배송비        |

**Olist Order Payments Dataset**
| order_id  | payment_seqeuntial | payment_type | payment_installments | payment_value |
| --------- | ------------------ | ------------ | -------------------- | ------------- |
| 주문 번호 | 결제 순서          | 결제 방식    | 할부 개월            | 결제 금액     |

**Olist Order Reviews Dataset**
| review_id   | order_id  | review_score | review_comment_title | review_comment_message | review_creation_date | review_answer_timestamp |
| ----------- | --------- | ------------ | -------------------- | ---------------------- | -------------------- | ----------------------- |
| 리뷰 아이디 | 주문 번호 | 평점         | 리뷰 제목            | 리뷰 내용              | 리뷰 작성 날짜       | 판매자 리뷰 답변 날짜   |

**Olist Orders Dataset**
| order_id | customer_id | order_status | order_purchase_timestamp | order_approved_at | order_delivered_carrier_date | order_delivered_customer_date | order_estimated_delivery_date |
| -------- | ----------- | ------------ | ------------------------ | ----------------- | ---------------------------- | ----------------------------- | ----------------------------- |
| 주문번호 | 고객 아이디 | 발송 여부    | 주문 결제 날짜           | 결제 승인 날짜    | 운송업체 전달 날짜           | 배송 완료 날짜                | 배송 예정 날짜                |

**Olist Products Dataset**
| product_id  | product_category_name | product_name_lenght | product_description_lenght | product_photos_qty | product_weight_g | product_length_cm | product_height_cm | product_width_cm |
| ----------- | --------------------- | ------------------- | -------------------------- | ------------------ | ---------------- | ----------------- | ----------------- | ---------------- |
| 제품 아이디 | 제품 카테고리 이름    | 제품 이름 길이      | 제품 설명 길이             | 제품 사진 개수     | 제품 무게        | 제품 길이         | 제품 높이         | 제품 너비        |

**Olist Sellers Dataset**
| seller_id     | seller_zip_code_prefix | seller_city      | seller_state   |
| ------------- | ---------------------- | ---------------- | -------------- |
| 판매자 아이디 | 판매자 우편번호        | 판매자 거주 도시 | 판매자 거주 주 |

---
## 데이터 전처리
### 결측치 처리
#### 결측치 발견 데이터
1. **olist_products_dataset.csv**
  - 결측치 :
    - **product_category_name = Nan** 
  - 처리 기법
    - `dataframe.fillna('unknown')` 처리

2. **olist_orders.csv**
  - 결측치 : 
    - **order_approved_at**
    - **order_delivered_carrier_date**
    - **order_delivered_customer_dat**
  - 처리 기법 : 
    - `order_status`의 값이 `delivered`인 데이터 추출(isin 필터링); 결측치 수 대폭 감소
    - 데이터 추출 후 `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_dat` 결측치 소량 발생
    - df.dropna(inplace=True) 결측치 행 제거

3. `order_items_with_product_category.csv`
 - 결측치 : 
   - **product_category_name = unknown**
 - 처리 기법 :
   -  `dataframe.drop()` 처리 

4. `state_sports_df.csv`
  - 결측치 : 
    - **fashion_esporte_customers_state = Nan**
  - 처리 기법 : 
    - `dataframe.fillna(0)` 처리



### 기타 전처리
#### 전처리 방법
  - 데이터셋 병합 : `dataframe.merge()`
  - 컬럼 삭제 : `dataframe.drop()`
  - 열 매핑 : `dataframe.itertuples()`
  - 컬럼 생성 및 데이터 추가
#### 전처리 Flow Chart
  | Flow (1)                    |     | Flow (2)                    |     | Flow (3)                    |
  | --------------------------- | --- | --------------------------- | --- | --------------------------- |
  | ![image](images/flow_1.png) | →   | ![image](images/flow_2.png) | →   | ![image](images/flow_3.png) |
  - `olist_customer_dataset.csv`
    - 고객 고유 아이디("customer_unique_id")와 우편번호("customer_zip_code_prefix") 칼럼 삭제
    - 해안지역과 내륙지역으로 구분하기 위해 각각의 리스트를 생성한 후 'region' 칼럼 생성 및 데이터 추가
    - 지도 표시를 위해 주 이름 코드를 주 명칭으로 변경
  - `order_items_with_product_category.csv`
  - `olist_order_items_dataset.csv`
  - `olist_orders_dataset`
  - `olist_products_dataset`
  - `sorted_orders_dataset.csv`

---
## 가설 및 검증
### EDA를 통해 세운 가설
#### 가설
- 해안지역에 가까울수록 스포츠 용품 구매율이 높다.
  

### 가설 검증을 위한 시도(통계적 기법, 시각화 등) 및 검증 결과
#### 가설 검증 및 검증 결과
##### 가설 검증 시도
- **통계적 기법**
  - 해안/내륙(region) : 해안지역과 내륙지역 구분
  - 스포츠와 레저 카테고리 용품의 해안/내륙 구매자 수의 합(esporte_lazer_customers_region) : 해안지역과 내륙지역의 스포츠와 레저 카테고리 용품 구매량 비교
  - 스포츠 패션 카테고리 용품의 해안/내륙 구매자 수의 합(fashion_esporte_customers_region) : 해안지역과 내륙지역의 스포츠 패션 카테고리 용품 구매량 비교
  - 두 카테고리의 합(total) : 각 지역별 두 스포츠 카테고리 용품 구매량 총합 비교
  - 구매율(Purchase Rate) : 해안지역과 내륙지역 각각의 고객 수에 대비한 스포츠 용품 구매율 비교

- **시각화기법**
  - 브라질 전역의 상품 카테고리별 주문수량 비중을 **텍스트 마이닝** (wordcloud/PIL) 
    - 구매상품 카테고리를 지정하여 정리
    - 기술 통계 : 총 판매상품 수
    - ![텍스트마이닝](images/text_mining.png)
  - 브라질 지도에 구매율을 시각화한 **히트맵** (folium/heatmap) 
      - 지리적으로 어디에서 구매가 활발한지 직관적으로 보여줍니다.
      - 히트맵을 통해 특정 지역에서의 구매 활동을 시각적으로 분석하여 가설을 검증합니다.
      - ![heatmap](images/heatmap.png)
  - 해안 대 내륙 스포츠 용품 구매율 **파이 차트** (matplotlib)
    - 각 지역 상품 구매 고객 수 대비 스포츠 용품 구매 비율로 계산하여 시각화하였습니다.
    - 이를 통해 비율적인 차이를 명확히 시각화하여 가설을 검증합니다.
    - ![pie_chart](images/pie_chart.png)
  - 해안/내륙별 각 상위 5개 주 스포츠 용품 구매 비율 **막대그래프** (seaborn)
    - Top5 만 뽑았을 때도 확연하게 해안 쪽 고객 대비 수 스포츠 용품 구매율 높다는 것을 시각적으로 알 수 있다.
    - ![bar_plot](images/seaborn_barplot.png)

#### 검증 결과
- 해안지역에 가까울수록 스포츠 용품 구매율이 높다는 가설은 통계적 기법과 시각화 기법을 통해 검증되었습니다. 
- 해안지역의 스포츠 용품 구매율이 내륙지역보다 유의미하게 높았으며, 시각적 분석을 통해서도 이를 확인할 수 있었습니다. 
- 따라서, 해안지역이 내륙지역에 비해 스포츠 용품 구매에 더 활발하다는 결론을 내릴 수 있습니다.


## 회고
- 분석을 진행하면서 너무 간단한 가설을 설정하여 시각화가 단순하게 나올 것이 조금 걱정되기는 하였으나 지도를 활용하면서 더 풍부하고 구체적으로 시각화해볼 수 있어서 좋았다.
- 혼자서 진행하는 데이터 분석에 비해서 더 다양한 데이터셋들을 알아보고 활용해보면서 어떤 데이터를 활용할지 선택하고 결측치에 대해서도 어떻게 처리하는 게 가설 검증에 도움이 될지 많이 고민해보는 시간이 되었고, 어렵거나 고민이 되는 부분을 팀원들과 공유하여 해결하면서 더 좋은 결과값을 낼 수 있었다.
- 보고서 작성에서도 이미 내용에 대해 알고 있는 사람의 시선이 아닌 모르는 사람의 시선에서 어떤 부분에서 더 명확하고 구체적으로 내용을 전달하고 보완해야 하는지 배울 수 있었다.
- EDA 분석 과정을 거쳐서 더 체계적이고 분석적으로 가설을 세워보았다면 추후 분석 과정에서 더욱 도움이 되었을 것 같다는 생각이 들었고, 구체적인 기준과 명확한 목표를 통해서 시각화하는 방향으로 진행하였으면 텍스트 마이닝 작업에서도 더 좋은 결과가 나올 수 있었을텐데 그 부분도 약간 아쉬웠다.
- 사실 시각화 과정에서 해안과 내륙 지역 별로 구매량이 높은 카테고리 상품들을 추출한 막대 그래프를 만들었었는데, 스포츠 용품에 비해 다른 용품들의 구매비율이 훨씬 높았고, 그 부분은 상품 카테고리의 특성과 판매 상품 수의 차이로 추정하였으나 이 부분까지 분석을 진행하고 보고서에 추가하기에는 시간적 여유가 없어서 제외하였다.
- 각자 필요한 데이터셋에 대해서 전처리를 하는 과정에서 미리 그룹화를 하거나, 필요한 데이터셋을 활용하지 않아서 처음부터 다시 작업을 하는 등의 혼란이 있었는데, 서로 간의 소통이 더 자주 이뤄지고 일의 우선순위와 절차를 정리해서 공유한 후 프로젝트를 진행하였더라면 더 좋았을 것 같다.
- 다음에 이러한 프로젝트를 또 할 기회가 생겼을 때, 우선순위를 바탕으로 전체적인 계획과 세부 계획을 꼼꼼하게 세워 진행한다면 더 다양한 분석을 진행해보면서 다각도에서 가설을 검증할 수 있을 것으로 예상된다.