# Hipsa Home

이 문서는 Hipsa home의 구조에 관하여 다룹니다.

## Requirements
Docker  
Python  
Django  
pymysql  


## 간단 정리
- hipsa_home  

- group_meeting  
그룹 미팅시 사용할 회의록을 띄우는 기능을 합니다.  
NAS의 mariadb 5에 회의록 DB가 있으며, 회의록은 그 DB의 정보를 읽어와 페이지를 렌더링 합니다.
pymysql을 사용합니다.

- references  
읽은 논문 관리를 하기 위한 기능을 합니다.

- Blog(미구현)  
각종 Howto 문서들을 markdown으로 저장하고, 페이지로 렌더링 합니다.  
markdown renderer로 ~를 사용합니다.
---
## 자세한 구현
### Docker  
NAS의 docker를 사용합니다.  
>docker의 자세한 이용법은 곧 정리하여 올릴 예정입니다.  
올린다면, howto문서들과 같이 업로드 할 것이고, blog 파트 구현이 완료되면 blog폴더에 저장하고, renderer를 통하여 열람할 수 있을 것입니다.

컨테이너의 이름은 django_dev입니다. NAS의 폴더는 이 컨테이너의 폴더에 마운트 되어있습니다.  
컨테이너와의 자료 공유가 필요하다면 이 폴더를 사용할 수 있습니다.  
소스코드관리는 git을 사용하고 있습니다.
>현재 remote repository는 github의 제 개인 repo를 사용하지만, 추후 NAS의 git 서버로 옮길 예정입니다.

컨테이너를 실행한뒤, bash를 실행합니다.  
8080포트가 열려있으므로 다음 명령을 통하여 서버를 시작합니다.  
이 명령은 hipsa_home에서 실행되어야 합니다.
<pre><code>python manage.py runserver 0.0.0.0:8080</code></pre>


### Django
>django의 이용법 또한 정리하여 업로드 할 예정입니다.


hipsa_home은 3개의 폴더로 구성되어 있습니다.
1. hipsa_home
2. group_meeting
3. references
4. blog

서버의 url은  hipsa_home/urls.py을 통해 관리합니다.  
urls.py는 