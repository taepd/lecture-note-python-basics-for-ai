### google images download 설치하기
```console
foo@bar:~$ pip install --upgrade git+https://github.com/Joeclinton1/google-images-download.git
```

### google images download 실행하기

#### argument 설명
| name | description | optional |
|:------:|:-----|:-----:|
|keywords | 다운로드하고 싶은 키워드를 입력합니다. 여러 개의 키워드 검색이 가능합니다. 여러 단어를 검색할 경우 ','로 구분합니다. | False |
| limit | 검색 키워드 하나 당 다운로드하고 싶은 이미지의 최대 개수를 지정합니다.(default=100) | True |
| format | 다운로드 받을 이미지의 포맷을 지정합니다. | True |
| output_directory | 이미지가 다운로드되는 기본 디렉토리의 이름을 지정합니다. (default='downloads') | True |

### 예시
```console
foo@bar:~$ googleimagesdownload --keywords "블랙핑크 지수,블랙핑크 제니,블랙핑크 리사,블랙핑크 로제" --limit 20 --format png --output_directory data
```
- 검색할 키워드 : 블랙핑크 지수 / 블랙핑크 제니 / 블랙핑크 리사 / 블랙핑크 로제
- 다운로드 수 : 키워드 당 20 개 
- 이미지 파일 포맷 : png
- 다운로드 위치 : ./data/