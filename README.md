# tgd_css
트게더 custom CSS

# main.js 사용법
1. CSS를 만지고 싶은 페이지(트게더)에 들어가서 개발자 도구를 켠다.
1. 콘솔에서 `main.js` 파일의 내용을 복붙하여 실행시킨다.
1. 화면에 커다란 입력 창(textarea)과 실행버튼이 나온다.
1. 창에 css를 입력한 다음 버튼을 눌러 CSS가 적용되는지를 확인한다.

# main.py 사용법
1. `main.py`는 여러가지 기능이 있다.
    1. 색깔을 치환
        1. 밝기에 따라 색을 조절하기 위해 사용한다.
        1. `{{ 숫자 }}`로 사용, `0`에서 `100`사이의 값을 넣어서 사용한다.
    1. URL을 치환
        1. 이미지의 파일 이름을 넣으면 최종적으로 트게더에서 사용할 최종 URL로 치환해준다.
    1. minify
        1. 불필요한 공백과 줄바꿈을 줄여서 css를 압축시켜준다.  
1. `python main.py {input css file} {output css file}`로 사용한다.
1. `{input css file}`에 css를 작성한 후, 위 커맨드를 실행한다.
1. 그 이후에 `{output css file}`파일을 복사해서 앞의 textarea를 통해 사용한다.

# make.bat
- `make`를 해서 간편하게 실행
