# ⚾숫자 야구 게임(numericBaseball)

# 📄목차

[🛶개요](#개요)

[📅기간](#기간)

[📘기능](#기능)

[💻적용 알고리즘](#적용-알고리즘)

[📚사용기술](#사용기술)

---

# 🛶개요

1. 공책에 끄적거리면서 하던 놀이를 컴퓨터에서?
2. 숫자 야구 게임을 나 혼자서?
3. 숫자 야구 게임을 혼자서 컴퓨터로 할 수 있게 만들어 봤습니다.

# 📅기간

2024.06.07 ~ 2024.06.09(3일)

# 📘기능

## 메인 페이지

1. 움직이는 이모지들과 바뀌는 응원 메시지로 야구장을 표현
2. 투수와 타자 사이로 야구공이 움직이게 하여, 첫 페이지에서의 이목을 집중
3. ‘혼자하기‘ 버튼을 통해 게임을 위한 숫자 선택 페이지 이동
![메인페이지](https://github.com/KimBeomGi/numericBaseball/assets/128961042/e5d6a26f-d63f-440a-948e-a5909298591e)

## 숫자 선택 페이지

1. 야구 숫자게임을 위한 3개의 숫자를 중복되지 않게 선택 가능
2. 넘버 패드의 ‘C’ 클릭시 완전 삭제
3. 넘버패드의 ‘화살표’ 클릭시 마지막 입력 숫자 삭제
4. 숫자 3개 입력 시 숫자가 추가 되지 않음.
5. 선택한 숫자를  넘버패드에서 선택 숫자의 배경 바뀜 및 ‘선택한 숫자’에서 명시적으로 확인 가능
6. 게임 시작 버튼을 통해 게임 작동 페이지로 이동
![스크린샷 2024-06-09 010303](https://github.com/KimBeomGi/numericBaseball/assets/128961042/c9f46cfa-b17b-4aa7-974a-c505603fdf6e)
7. 숫자 3개를 미입력시 alert를 통해 알려주며, 페이지는 이동하지 않음
![스크린샷 2024-06-09 011029](https://github.com/KimBeomGi/numericBaseball/assets/128961042/117ca68e-814b-4b58-bafc-b65110fb9e53)

## 게임 페이지
1. ‘수 거름판’을 통해 상대방 번호에 대한 기록 가능
2. ‘내 현황판’을 통해 이번 게임에서 내가 지금까지 상대방에게 던진 숫자들을 확인 가능
3. ‘넘버패드’를 통해 중복되지 않는 숫자 3개를 입력하고, ‘입력’키로 상대방에게 숫자 3개를 던질 수 있음.
4. ‘넘버패드’상단의 입력한 숫자에서 내가 입력한 숫자를 확인 가능
5. ‘상대방 현황판’을 통해 상대방이 나에게 던진 숫자들을 확인 가능
![스크린샷 2024-06-09 011754](https://github.com/KimBeomGi/numericBaseball/assets/128961042/b00c6382-9815-4148-b1b2-8c8ca49c2c7a)
6. 컴퓨터에게 승리 시 ‘승리’표시와 함께 몇 회의 경기로 이겼음이 등장하고, 다시 하기 버튼이 생성됨
![스크린샷 2024-06-09 012114](https://github.com/KimBeomGi/numericBaseball/assets/128961042/c87b2885-120a-4768-a3a6-71be64d38af0)
7. 컴퓨터에게 패배도 가능. 이때는 ‘패배’표시와 함께 몇 회의 경기로 패배했음이 등장하고, 다시 하기 버튼이 생성됨.
![스크린샷 2024-06-09 011914](https://github.com/KimBeomGi/numericBaseball/assets/128961042/4d874f7f-1e1e-4bbc-9ec1-b90712ec7183)


# 💻적용 알고리즘

1. 컴퓨터에 다음과 같은 3가지 로직을 이용해 컴퓨터의 숫자 야구 게임 진행
    1. 랜덤 함수를 통해서 무작위 숫자 ３개를 추출.
    2. 컴퓨터가 나에게 던진 숫자 3개가 모두 들어있을 경우 (3strike 제외) enemyChecking 변수에 제외해야 할 숫자를 기입
        1. 3ball
        2. 2ball, 1strike
        3. 1ball, 2strike
    3. 다음 컴퓨터 회차에서 enemyChecking에 기입된 수를 제외한 3개의 숫자를 뽑아내서 나에게 던짐

# 📚사용기술
<div align=center>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 
	 <br>
   <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
   <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
	 <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 
   <br>
</div>
