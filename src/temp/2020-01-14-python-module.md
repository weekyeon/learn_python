---
layout: post
title: "[Python] 모듈(Module)"
description: "python module"
feature-img: "assets/img/pexels/computer.webp"
author: weekyeon
excerpt_separator: <!--more-->
tags: [Python]
---

<p align="center" style="color:gray;">파이썬 모듈에 관해 알아보기</p>

* 모듈이 무엇인지
* 모듈은 어떨 때, 왜 사용하는지
* 파이썬에서 제공하는 모듈 적용하는 방법
* 내가 만든 모듈 적용하는 방법

<!--more-->

# 모듈(Module)

* 모듈은 함수나 변수, 또는 클래스를 모아 놓은 파일을 말함

* 대개 <span class="custom-markup-text">유사하거나 공통된 일을 하거나, 또는 관련된 일을 하는 함수나 변수</span>를 모아서 하나의 파일에 저장함

* Python 모듈의 확장자는 `.py`

* 모듈의 이름은 확장자를 제외한 파일 이름

  * **EX)** weekyeon.py
    * weekyeon이 모듈 이름

* 모듈 종류

  * `1` 표준 모듈
    * Python 패키지 안에 기본적으로 포함되어 제공되는 모듈
    * 프로그래밍을 할 때 어느 개발자가 됐든 **흔하게** 사용되는 **공통된** 기능들을 **편의를 위해** 파이썬에서 제공하는 것
  * `2` 사용자 정의 모듈
    * 개발자가 직접 정의하여 자신이 자주 사용하는 기능(함수)을 모아 만든 모듈
  * `3` 3rd party 모듈
    * 다른 업체나 개인이 만들어서 제공하는 모듈
    * 대표적인 모듈 : pandas, numpy, matplotlib 등

* 모듈의 사용 목적

  * `1` 코드의 재사용으로 인해 개발 및 유지보수 효율성 증가
  * `2` 프로그램 개발 시 전체 코드를 여러 모듈 단위로 분리하여 설계하면 작업 효율성 증가
  * `3` 별도의 이름 공간(Name space) 제공하여 **동일 이름**의 여러 함수나 변수를 각 모듈마다 독립적으로 정의해 사용 가능

  ---

  * 위의 내용이 정석적인 사용 목적이고 아래 내용부턴 사담에 가까우니, 위 내용이 잘 와닿지 않는다면 읽어도 좋고 너무나 잘 와닿는다면 흐린 눈으로 넘어가는 게 좋음
    * 모듈의 용도는 쉽게 말해서 회사에서 쓰는 공통 양식과 비슷하다.
    * 회사에서 기안문을 쓸 때 사내 양식을 가져와서 내용만 채우지, 기안문 양식부터 만드는 사람은 없다.
    * 왜? 양식부터 만들면 시간이 배로 드니까! 정작 써야 할 기안문은 바로 쓰지 못하니까!
    * 프로그래밍에서는 이와 비슷한 이유로 모듈을 사용한다.
    * 실제 개발을 하다보면 만들어야 하는 기능은 똑같은데 기능 안에 채워야 할 내용만 다른 경우가 생각보다 많다.
    * 이때, 작업의 효율성을 높이기 위해 개발자들은 모듈을 사용한다.
    * 비단 모듈 뿐 아니라 함수를 사용하는 이유도 이와 같다.
    * 프로그래밍을 할 때 항상 염두에 두어야 할 것은, `1` 같은 코드를 반복해서 쓰지 않음 `2` A 라는 기능을 만들기 위해 A 라는 함수를 만들었을 때, 이 A 함수에 언제나 A 기능만 담기는 것은 아님을 잊지 않기
    * 그래서 개발자들은 보통 A 함수에 A 라는 내용만 담을 수 있도록 설계하지 않고 A 함수에 A, B, C도 담을 수 있도록 설계함

<br>

# 모듈 사용하기

* ### 모듈 선언

```python
# 1.
import 모듈명

# ex) weekyeon.py 모듈을 사용하고 싶을 때
import weekyeon
```

```python
# 2.
import 모듈명 as 별칭

# ex) weekyeon.py 모듈을 사용하고 싶은데 이름이 너무 길거나 다른 모듈과 충돌이 일어날 것 같아
import weekyeon as wy
```

```python
# 3.
from 모듈명 import [함수명 또는 변수명]

# ex) weekyeon.py 모듈을 사용하고 싶은데 다 쓰고 싶진 않고 weekyeon.py 안에 있는 특정 기능(함수 또는 변수)만 사용하고 싶어
from weekyeon import func_date
```

```python
# 4.
from 모듈명 import *

# ex) weekyeon.py 모듈에 있는 public 접근제한 기능들만 가져올래
# __(언더바 2개) 붙은 건 안 가져올래
from weekyeon import *
```

```python
# 5.
from 모듈명 import * as 별칭

# ex) weekyeon.py 모듈을 wy라는 이름으로 사용하고 싶은데, wy라는 이름이 weekyeon.py에서 사용하고 있네?
from weekyeon import * as wy
```

<br>

* ### 모듈에 있는 함수 호출

```python
모듈명.함수(인수)
```

```python
# ex)
import weekyeon as wy

wy.func_date("인수로 던져줘야 할 데이터")
```

<br>

* ### 모듈을 사용할 수 있는



<br>

<br>

---

### Reference

* [link]()
* 박응용, 『Do it! 점프 투 파이썬』, 이지스퍼블리싱(2019)

<br>

<br>